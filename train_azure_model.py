import sys

import pyodbc
import ast

import glob

from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, QualityForRecognition

from azure_faceAPI import PersonGroup

GetPersonDataQuery = "SELECT [Nombres],[imagenes] FROM [dbo].[PN_Individuos]"

class Conexion():
    def __init__(self):
        self.credentials_quantity = 5
        self.credentials_filename = "credentials.txt"        

    def Cargar_credenciales_DB(self):
        file = open(self.credentials_filename, "r")
        lines = file.readlines()
        
        if(len(lines)==self.credentials_quantity):
            self.server = ast.literal_eval(lines[0])[0]
            self.database = ast.literal_eval(lines[1])[0]
            self.username = ast.literal_eval(lines[2])[0]
            self.password = ast.literal_eval(lines[3])[0]
            self.driver = ast.literal_eval(lines[4])[0]

            print(self.server,self.password)
        else:
            print("Credenciales no validas")

    def RunQuery(self, Query):
        
        self.cursor.execute(Query)
        row = self.cursor.fetchone()
        
        return row

    def Conectar_DB(self):

        self.conn = pyodbc.connect('DRIVER='+self.driver+';SERVER=tcp:'+self.server+';PORT=1433;DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
        self.cursor = self.conn.cursor()

conexion = Conexion()
conexion.Cargar_credenciales_DB()
conexion.Conectar_DB()

row = conexion.RunQuery(GetPersonDataQuery)

Personas = []

while row:
    rutasImagenes = ast.literal_eval(row[1])
    Personas.append([str(row[0]), rutasImagenes])

    print (str(row[0]) + " " + str(row[1]))
    row = conexion.cursor.fetchone()

print(Personas[2])
print()
# This key will serve all examples in this document.
#KEY = "97631f19ea6f4925aa4ecc9f28e049e7"
KEY = "f63e58d0115b4749bf79518134f3c85c"
# This endpoint will be used in all examples in this quickstart.
#ENDPOINT = "https://itla-rec-cog-serv.cognitiveservices.azure.com/"
ENDPOINT = "https://proyecto-rec-escenas-prueba.cognitiveservices.azure.com/"
# Create an authenticated FaceClient.
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

psGroup = PersonGroup(face_client, name="Individuos")

psGroup.addPersons([Nombre[0] for Nombre in Personas])

for Persona in Personas:
    nombre = Persona[0]
    url_imgenes = Persona[1]
    psGroup.addFacesToPerson(nombre, url_imgenes)

psGroup.train()

psGroup.save()
