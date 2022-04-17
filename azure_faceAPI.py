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
  def __init__(self, face_client, name, detection_model="detection_03", recognition_model="recognition_04",PERSON_GROUP_ID=None):
    
    self.face_client = face_client
    self.name = name
    self.recognition_model = recognition_model
    self.detection_model = detection_model

    if(PERSON_GROUP_ID): #PARA INFERENCIA
      self.PERSON_GROUP_ID = PERSON_GROUP_ID
      #self.face_client.person_group.create(person_group_id=self.PERSON_GROUP_ID, name=self.name, recognition_model=self.recognition_model)
      #self.face_client.person_group.get(self.PERSON_GROUP_ID)
      #print(self.face_client.person_group)
    else: #PARA ENTRENAMIENTO
      self.PERSON_GROUP_ID = str(uuid.uuid4()) # assign a random ID (or name it anything)
      self.face_client.person_group.create(person_group_id=self.PERSON_GROUP_ID, name=self.name, recognition_model=self.recognition_model)

    #print('Person group:', self.PERSON_GROUP_ID)
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
      try:
        self.face_client.person_group_person.add_face_from_url(self.PERSON_GROUP_ID, personToModify.person_id, face)
      except:
        print("La imagen no posee una cara reconocible, será ignorada")

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
    #print('Pausing for 60 seconds to avoid triggering rate limit on free account...')
    #time.sleep (10)
    #print("tiempo paso")
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
    #print('Identifying faces in {}'.format(os.path.basename(image.name)))
    #if not self.results:
        #print('No person identified in the person group for faces from {}.'.format(os.path.basename(image.name)))
    for personaIdentificada in self.results:
      #print("El de la imagen es: " + self.personToName(person.candidates[0].person_id))
      #print('Person for face ID {} is identified in {} with a confidence of {}.'.format(personaIdentificada.face_id, os.path.basename(image.name), personaIdentificada.candidates[0].confidence)) # Get topmost confidence score
      if len(personaIdentificada.candidates) <= 0:
        print('No person identified for face ID {} in {}.'.format(personaIdentificada.face_id, os.path.basename(image.name)))
    
    persons = self.face_client.person_group_person.list(self.PERSON_GROUP_ID)
    
    for personaIdentificada in self.results:
        if len(personaIdentificada.candidates) > 0:
          for person in persons:
            person_id = person.person_id
            try:
              result = self.face_client.face.verify_face_to_person(face_id=personaIdentificada.face_id,person_id=person_id,person_group_id=self.PERSON_GROUP_ID)
              if(result.is_identical):
                return [person.name, result.confidence]
            except:
              print(person.name + " no es el de la imagen")
    
    return None
  
  def personToName(self, person):
    for saved_person in self.persons:
      if(saved_person[1].person_id == person):
        return saved_person[0]
    return None

  def save(self):
    file = open("trained_model_id.txt", "w+")
    file.write(self.PERSON_GROUP_ID)