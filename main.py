from PyQt5 import QtCore, QtGui, QtWidgets
from login_window import Ui_Login_window
from consult_window import Ui_MainWindow

import tkinter as tk
from tkinter import END, filedialog

import sys

import pyodbc
import ast

import glob

from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, QualityForRecognition

from azure_faceAPI import PersonGroup

import requests

from PDF_gen import generarPDF

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
        
        self.cursor.execute("SELECT TOP (1000) [usuario],[contraseña]  FROM [dbo].[PN_admin]")
        row = self.cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = self.cursor.fetchone()

    def VerificarLogin(self,username, password):

        #cargar_ventana_consulta() #DEBUGING

        credenciales = self.RunQuery("SELECT * FROM [dbo].[PN_admin] WHERE usuario='" + username + "';")
        
        if(not credenciales):
            print("Credenciales invalidas")
            return

        if(len(credenciales)==2 and credenciales[1] == password):
            print("YEAH")
            cargar_ventana_consulta()
        else:
            print("Credenciales invalidas")

        while credenciales:
            print (str(credenciales[0]) + " " + str(credenciales[1]))
            credenciales = self.cursor.fetchone()


def login():
    print("boton clickeado")
    credenciales = ui0.getUsernamePassword()
    if(credenciales[0]=='' or credenciales[1] == ''):
        print("Credenciales no validas")
    else:
        conexion.VerificarLogin(credenciales[0], credenciales[1])

def cargar_ventana_consulta():
    DebugLogin = True

    if(DebugLogin):
        Login_window.close()
        Consult_window.show()
        return

def cargar_imagen():
    print("Cargar imagen!")

    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    print(file_path)

    ui1.cargar_foto1(file_path)

def hacer_consulta():
    if(ui1.Imagen1Cargada):
        print("Consultar!")
        foto = open(ui1.RutaFoto1,'r+b')
        personaIdentificada = azure_conn.psGroup.identifyPerson(foto)
        print(personaIdentificada)
        if(personaIdentificada):
            mostrarDatos(personaIdentificada)
    else:
        print("Debe cargar una imagen para consultar")

conseguirDatosDePersonaQuery = """SELECT [ID]
      ,[Nombres]
      ,[Apellidos]
      ,[Fecha de nacimiento]
      ,[Edad]
      ,[Genero]
      ,[Estatura]
      ,[Peso]
      ,[Piel]
      ,[Ojos]
      ,[Cabello]
      ,[Cicatrices]
      ,[Alias]
      ,[Padre]
      ,[Madre]
      ,[Direccion]
      ,[Delitos]
      ,[Casos asociados]
      ,[Tipo de instrumento usado]
      ,[imagenes]
      ,[face_ID]
  FROM [dbo].[PN_Individuos] WHERE [Nombres]='"""

campos = {'ID':0, 'Nombres':1, 'Apellidos':2, 'Fecha de nacimiento':3, 'Edad':4, 'Genero':5, 'Estatura':6, 'Peso':7,'Piel':8 ,'Ojos':9, 'Cabello':10 , 'Cicatrices':11 , 'Alias':12  , 'Padre':13 , 'Madre':14 , 'Direccion':15 , 'Delitos':16 , 'Casos asociados':17 , 'Tipo de instrumento usado':18, 'imagenes':19}

def mostrarDatos(personaIdentificada):

    nombre = personaIdentificada[0] + '\''
    datosPersona = conexion.RunQuery(conseguirDatosDePersonaQuery+nombre)

    ui1.NombreLabel.setText(datosPersona[campos['Nombres']])
    ui1.CedulaLabel.setText(datosPersona[campos['ID']])
    ui1.GeneroLabel.setText(datosPersona[campos['Genero']])
    ui1.EdadLabel.setText(datosPersona[campos['Edad']])

    Confianza = personaIdentificada[1]
    ui1.NumeroConfidencia.setProperty("value", Confianza*100) 

    imagenPersona = ast.literal_eval(datosPersona[campos['imagenes']])[0]
    imagen = requests.get(imagenPersona)

    azure_conn.ConsultaHecha = True
    ui1.cargar_foto2(imagen)

    print(datosPersona)
    azure_conn.datosPersona = datosPersona

def GenerarReporte():
    print("Generando reporte")
    if(azure_conn.datosPersona):
        generarPDF(azure_conn.datosPersona)
    else:
        print("Debe hacer una consulta para generar un reporte")
    pass

class Azure_conexion():
    def __init__(self, KEY,ENDPOINT):
        self.KEY = KEY
        self.ENDPOINT = ENDPOINT
        self.ConsultaHecha = False

        self.datosPersona = None

        file = open("trained_model_id.txt", "r")
        personGroup_ID = file.readlines()[0]

        self.faceclient = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))
        list_ps = self.faceclient.person_group.list()
        for ps in list_ps:
            print(ps)
        self.psGroup = PersonGroup(self.faceclient, name="Individuos", PERSON_GROUP_ID=personGroup_ID)
    

# This key will serve all examples in this document.
KEY = "f63e58d0115b4749bf79518134f3c85c"

# This endpoint will be used in all examples in this quickstart.
ENDPOINT = "https://proyecto-rec-escenas-prueba.cognitiveservices.azure.com/"

azure_conn = Azure_conexion(KEY=KEY, ENDPOINT=ENDPOINT)

conexion = Conexion()
app = QtWidgets.QApplication(sys.argv)

Login_window = QtWidgets.QMainWindow()
ui0 = Ui_Login_window()
ui0.setupUi(Login_window, funcion_button=login)

Consult_window = QtWidgets.QMainWindow()
ui1 = Ui_MainWindow()
ui1.setupUi(Consult_window, cargar_imagen_funcion=cargar_imagen, hacer_consulta_funcion=hacer_consulta,generar_reporte_funcion=GenerarReporte)    

if __name__ == "__main__":

    conexion.Cargar_credenciales_DB()
    conexion.Conectar_DB()

    Login_window.show()
    sys.exit(app.exec_())