from PyQt5 import QtCore, QtGui, QtWidgets
from login_window import Ui_Login_window
from consult_window import Ui_MainWindow

import tkinter as tk
from tkinter import filedialog

import sys

import pyodbc
import ast

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

        cargar_ventana_consulta() #DEBUGING

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

conexion = Conexion()
app = QtWidgets.QApplication(sys.argv)

Login_window = QtWidgets.QMainWindow()
ui0 = Ui_Login_window()
ui0.setupUi(Login_window, funcion_button=login)

Consult_window = QtWidgets.QMainWindow()
ui1 = Ui_MainWindow()
ui1.setupUi(Consult_window, cargar_imagen_funcion=cargar_imagen)    

if __name__ == "__main__":

    conexion.Cargar_credenciales_DB()
    conexion.Conectar_DB()

    Login_window.show()
    sys.exit(app.exec_())