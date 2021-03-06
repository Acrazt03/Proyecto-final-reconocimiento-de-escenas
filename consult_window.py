# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consult_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, cargar_imagen_funcion, hacer_consulta_funcion,generar_reporte_funcion):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(685, 302)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(685, 302))
        MainWindow.setMaximumSize(QtCore.QSize(685, 302))
        MainWindow.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.GenerarReporteBtn = QtWidgets.QPushButton(self.centralwidget)
        self.GenerarReporteBtn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.GenerarReporteBtn.setObjectName("GenerarReporteBtn")

        self.GenerarReporteBtn.clicked.connect(generar_reporte_funcion)

        self.gridLayout.addWidget(self.GenerarReporteBtn, 1, 3, 1, 1)
        self.Foto2 = QtWidgets.QLabel(self.centralwidget)
        self.Foto2.setStyleSheet("background-image: url(download.png);")
        self.Foto2.setText("")
        self.Foto2.setPixmap(QtGui.QPixmap("download.png"))
        self.Foto2.setScaledContents(True)
        self.Foto2.setObjectName("Foto2")
        self.gridLayout.addWidget(self.Foto2, 0, 3, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Foto1 = QtWidgets.QLabel(self.centralwidget)
        self.Foto1.setStyleSheet("background-image: url(download.png);")
        self.Foto1.setText("")
        self.Foto1.setPixmap(QtGui.QPixmap("download.png"))
        self.Foto1.setScaledContents(True)
        self.Foto1.setObjectName("Foto1")

        self.Imagen1Cargada = False

        self.horizontalLayout.addWidget(self.Foto1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.HacerConsultaBtn = QtWidgets.QPushButton(self.centralwidget)
        self.HacerConsultaBtn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.HacerConsultaBtn.setObjectName("HacerConsultaBtn")
        
        self.HacerConsultaBtn.clicked.connect(hacer_consulta_funcion)

        self.gridLayout.addWidget(self.HacerConsultaBtn, 1, 2, 1, 1)
        self.CargarImagenBtn = QtWidgets.QPushButton(self.centralwidget)
        self.CargarImagenBtn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CargarImagenBtn.setObjectName("CargarImagenBtn")

        self.CargarImagenBtn.clicked.connect(cargar_imagen_funcion)

        self.gridLayout.addWidget(self.CargarImagenBtn, 1, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.NombreLabel = QtWidgets.QLabel(self.centralwidget)
        self.NombreLabel.setText("")
        self.NombreLabel.setObjectName("NombreLabel")
        self.horizontalLayout_5.addWidget(self.NombreLabel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.CedulaLabel = QtWidgets.QLabel(self.centralwidget)
        self.CedulaLabel.setText("")
        self.CedulaLabel.setObjectName("CedulaLabel")
        self.horizontalLayout_4.addWidget(self.CedulaLabel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.GeneroLabel = QtWidgets.QLabel(self.centralwidget)
        self.GeneroLabel.setText("")
        self.GeneroLabel.setObjectName("GeneroLabel")
        self.horizontalLayout_3.addWidget(self.GeneroLabel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.EdadLabel = QtWidgets.QLabel(self.centralwidget)
        self.EdadLabel.setText("")
        self.EdadLabel.setObjectName("EdadLabel")
        self.horizontalLayout_2.addWidget(self.EdadLabel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.NumeroConfidencia = QtWidgets.QLCDNumber(self.centralwidget)
        self.NumeroConfidencia.setMinimumSize(QtCore.QSize(40, 50))
        self.NumeroConfidencia.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.NumeroConfidencia.setSmallDecimalPoint(True)
        self.NumeroConfidencia.setDigitCount(2)
        self.NumeroConfidencia.setMode(QtWidgets.QLCDNumber.Dec)
        self.NumeroConfidencia.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.NumeroConfidencia.setProperty("value", 0.0)
        self.NumeroConfidencia.setProperty("intValue", 0)
        self.NumeroConfidencia.setObjectName("NumeroConfidencia")
        self.verticalLayout_3.addWidget(self.NumeroConfidencia)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Consulta"))
        self.GenerarReporteBtn.setText(_translate("MainWindow", "Generar reporte"))
        self.HacerConsultaBtn.setText(_translate("MainWindow", "Hacer consulta"))
        self.CargarImagenBtn.setText(_translate("MainWindow", "Cargar imagen"))
        self.label_3.setText(_translate("MainWindow", "Nombre:"))
        self.label_5.setText(_translate("MainWindow", "C??dula:"))
        self.label_8.setText(_translate("MainWindow", "G??nero:"))
        self.label_10.setText(_translate("MainWindow", "Edad:"))

    def cargar_foto1(self, image_path):
        self.Imagen1Cargada = True
        self.RutaFoto1 = image_path
        self.Foto1.setStyleSheet("background-image: url("+image_path+");")
        self.Foto1.setPixmap(QtGui.QPixmap(image_path))
    
    def cargar_foto2(self, imagen):
        self.Imagen2Cargada = True
        self.RutaFoto2 = "foto2.jpg"

        # 3. Open the response into a new file called instagram.ico
        open(self.RutaFoto2, "wb").write(imagen.content)

        self.Foto2.setStyleSheet("background-image: url("+self.RutaFoto2+");")
        self.Foto2.setPixmap(QtGui.QPixmap(self.RutaFoto2))
        
#import blank person image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
