import glob

from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, QualityForRecognition

from azure_faceAPI import PersonGroup

# This key will serve all examples in this document.
#KEY = "97631f19ea6f4925aa4ecc9f28e049e7"
KEY = "f63e58d0115b4749bf79518134f3c85c"
# This endpoint will be used in all examples in this quickstart.
#ENDPOINT = "https://itla-rec-cog-serv.cognitiveservices.azure.com/"
ENDPOINT = "https://proyecto-rec-escenas-prueba.cognitiveservices.azure.com/"
# Create an authenticated FaceClient.
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

psGroup = PersonGroup(face_client, name="Amigos 2")

psGroup.addPersons(["Arturo", "Wilson"])

print(psGroup.persons)

Arturo_images = [file for file in glob.glob('*.jpg') if file.startswith("arturo")]
psGroup.addFacesToPerson("Arturo", Arturo_images)

Wilson_images = [file for file in glob.glob('*.jpg') if file.startswith("wilson")]
psGroup.addFacesToPerson("Wilson", Wilson_images)

#psGroup.train()

test_image_path = "Test_arturo.jpg"
image = open(test_image_path, 'r+b')

print(psGroup.identifyPerson(image))

test_image_path = "Test_wilson.jpg"
image = open(test_image_path, 'r+b')

print(psGroup.identifyPerson(image))