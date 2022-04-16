import asyncio
import io
import glob
import os
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO
# To install this module, run:
# python -m pip install Pillow
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, QualityForRecognition

class PersonGroup:
  def __init__(self, face_client, name, detection_model="detection_03", recognition_model="recognition_04"):
    self.face_client = face_client
    self.name = name
    #self.PERSON_GROUP_ID = str(uuid.uuid4()) # assign a random ID (or name it anything)
    self.PERSON_GROUP_ID = "6129c084-32d8-4809-937f-e6bc66d2c99a"
    self.recognition_model = recognition_model
    self.detection_model = detection_model
    print('Person group:', self.PERSON_GROUP_ID)
    #self.face_client.person_group.create(person_group_id=self.PERSON_GROUP_ID, name=self.name, recognition_model=self.recognition_model)
    self.persons = []
  
  def addPersons(self, _persons): #persons es una lista de nombres
    for personName in _persons:
      new_person = self.face_client.person_group_person.create(self.PERSON_GROUP_ID, name=personName)
      self.persons.append([personName, new_person])

  def addFacesToPerson(self, personName, faces):
    
    personToModify = None
    
    for person in self.persons:
      if(person[0] == personName):
        print("Person found!")
        personToModify = person[1]
        break
    if(personToModify == None):
      print("Person not found!")
      return None

    for face in faces:
      img = open(face, 'r+b')
      print(face)
      self.face_client.person_group_person.add_face_from_stream(self.PERSON_GROUP_ID, personToModify.person_id, img)
  
  def train(self):
    '''
    Train PersonGroup
    '''
    print()
    print('Training the person group...')
    # Train the person group
    self.face_client.person_group.train(self.PERSON_GROUP_ID)
    
    while (True):
        training_status = self.face_client.person_group.get_training_status(self.PERSON_GROUP_ID)
        print("Training status: {}.".format(training_status.status))
        print()
        if (training_status.status is TrainingStatusType.succeeded):
            break
        elif (training_status.status is TrainingStatusType.failed):
            self.face_client.person_group.delete(person_group_id=self.PERSON_GROUP_ID)
            sys.exit('Training the person group has failed.')
        time.sleep(5)
  
  def identifyPerson(self, image):
    print('Pausing for 60 seconds to avoid triggering rate limit on free account...')
    time.sleep (10)

    # Detect faces
    self.face_ids = []
    # We use detection model 3 to get better performance, recognition model 4 to support quality for recognition attribute.
    faces = self.face_client.face.detect_with_stream(image, detection_model=self.detection_model, recognition_model=self.recognition_model, return_face_attributes=['qualityForRecognition'])
    for face in faces:
        # Only take the face if it is of sufficient quality.
        if face.face_attributes.quality_for_recognition == QualityForRecognition.high or face.face_attributes.quality_for_recognition == QualityForRecognition.medium:
            self.face_ids.append(face.face_id)

    # Identify faces
    self.results = self.face_client.face.identify(self.face_ids, self.PERSON_GROUP_ID)
    print('Identifying faces in {}'.format(os.path.basename(image.name)))
    if not self.results:
        print('No person identified in the person group for faces from {}.'.format(os.path.basename(image.name)))
    for person in self.results:
        if len(person.candidates) > 0:
            print("El de la imagen es: " + self.personToName(person.candidates[0].person_id))
            print('Person for face ID {} is identified in {} with a confidence of {}.'.format(person.face_id, os.path.basename(image.name), person.candidates[0].confidence)) # Get topmost confidence score
        else:
            print('No person identified for face ID {} in {}.'.format(person.face_id, os.path.basename(image.name)))
      
  def personToName(self, person):
    for saved_person in self.persons:
      if(saved_person[1].person_id == person):
        return saved_person[0]
    return None