# -*- coding: utf-8 -*-

# PYTHON_APP_TIME_COUNTER V0.1

# Herramienta para el control del tiempo que tenemos una aplicación específica activa.
# Solo necesita copiar la dirección del ejecutable de la aplicación en cuestión, y al
# cerrarla, podrá ver en pantalla, el tiempo que la ha tenido en funcionamiento.

# Por hacer:
# -Explorador de archivos para buscar visualmente el ejecutable.
# -Registrar histórico de ejecución, por aplicación utilizada a través de la herramienta.
# -Mejorar aspecto visual.
# -Optimizar código.
# -Escribir "Ayuda". (Si es que lo necesita)
# -¿Conectar registros con base de datos?.

# -Cualquier otra posible incorporación.

# Por: Juan Antonio
# https://sirvaseusted.es


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import time

i = 0
f = 0
s = 0

class Ui_ContadordeTiempo(object):
	def setupUi(self, ContadordeTiempo):
		ContadordeTiempo.setObjectName("ContadordeTiempo")
		ContadordeTiempo.resize(434, 122)
		
		self.input = QtWidgets.QLineEdit(ContadordeTiempo)
		self.input.setGeometry(QtCore.QRect(4, 80, 230, 26))
		self.input.setObjectName("input")
		
		self.iniciar = QtWidgets.QPushButton(ContadordeTiempo)
		self.iniciar.setGeometry(QtCore.QRect(250, 80, 80, 26))
		self.iniciar.setObjectName("iniciar")
		
		self.cerrar = QtWidgets.QPushButton(ContadordeTiempo)
		self.cerrar.setGeometry(QtCore.QRect(350, 80, 80, 26))
		self.cerrar.setObjectName("cerrar")
		
		self.etiqueta = QtWidgets.QLabel(ContadordeTiempo)
		self.etiqueta.setGeometry(QtCore.QRect(10, 60, 250, 18))
		self.etiqueta.setObjectName("etiqueta")
		
		self.label1 = QtWidgets.QLabel(ContadordeTiempo)
		self.label1.setGeometry(QtCore.QRect(50, 10, 58, 18))
		self.label1.setObjectName("label1")
		
		self.label0 = QtWidgets.QLabel(ContadordeTiempo)
		self.label0.setGeometry(QtCore.QRect(50, 30, 58, 18))
		self.label0.setObjectName("label0")
		
		self.label2 = QtWidgets.QLabel(ContadordeTiempo)
		self.label2.setGeometry(QtCore.QRect(280, 10, 131, 18))
		self.label2.setObjectName("label2")
		
		self.cuenta = QtWidgets.QLabel(ContadordeTiempo)
		self.cuenta.setGeometry(QtCore.QRect(310, 40, 58, 18))
		font = QtGui.QFont()
		font.setPointSize(16)
		self.cuenta.setFont(font)
		self.cuenta.setTextFormat(QtCore.Qt.AutoText)
		self.cuenta.setObjectName("cuenta")
		self.tinicial = QtWidgets.QLabel(ContadordeTiempo)
		self.tinicial.setGeometry(QtCore.QRect(110, 10, 120, 18))
		self.tinicial.setObjectName("tinicial")
		self.tfinal = QtWidgets.QLabel(ContadordeTiempo)
		self.tfinal.setGeometry(QtCore.QRect(110, 30, 120, 18))
		self.tfinal.setObjectName("tfinal")
		self.retranslateUi(ContadordeTiempo)
		self.cerrar.clicked.connect(ContadordeTiempo.reject)
		self.iniciar.clicked.connect(self.Iniciar)
		QtCore.QMetaObject.connectSlotsByName(ContadordeTiempo)
	def retranslateUi(self, ContadordeTiempo):
		_translate = QtCore.QCoreApplication.translate
		ContadordeTiempo.setWindowTitle(_translate("ContadordeTiempo", "Contador de Tiempo"))
		self.iniciar.setText(_translate("ContadordeTiempo", "Iniciar"))
		self.cerrar.setText(_translate("ContadordeTiempo", "Cerrar"))
		self.etiqueta.setText(_translate("ContadordeTiempo", "Inserte dirección del ejecutable:"))
		self.label1.setText(_translate("ContadordeTiempo", "Inicio:"))
		self.label0.setText(_translate("ContadordeTiempo", "Fin:"))
		self.label2.setText(_translate("ContadordeTiempo", "Tiempo de Trabajo:"))
		self.cuenta.setText(_translate("ContadordeTiempo", "00:00"))
		self.tinicial.setText(_translate("ContadordeTiempo", "00:00"))
		self.tfinal.setText(_translate("ContadordeTiempo", "00:00"))

	def Iniciar(self):
		global i
		i = round(time.time(), 2)
		self.tinicial.setText(str(i))
		p = self.input.text()
		x = os.system("'"+ p +"'")
		f = round(time.time(), 2)
		self.tfinal.setText(str(f))
		s = round(float(f) - float(i), 2)
		self.cuenta.setText(str(s))
		print(f)
		print(i)
		print(s)



if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	ContadordeTiempo = QtWidgets.QDialog()
	ui = Ui_ContadordeTiempo()
	ui.setupUi(ContadordeTiempo)
	ContadordeTiempo.show()
	sys.exit(app.exec_())

