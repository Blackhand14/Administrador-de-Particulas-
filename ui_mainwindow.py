# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(891, 596)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionMostrar_particulas = QAction(MainWindow)
        self.actionMostrar_particulas.setObjectName(u"actionMostrar_particulas")
        self.actionEjecutar_Algoritmo = QAction(MainWindow)
        self.actionEjecutar_Algoritmo.setObjectName(u"actionEjecutar_Algoritmo")
        self.actionProfundidad = QAction(MainWindow)
        self.actionProfundidad.setObjectName(u"actionProfundidad")
        self.actionAnchura = QAction(MainWindow)
        self.actionAnchura.setObjectName(u"actionAnchura")
        self.actionMostrar_Grafo_P = QAction(MainWindow)
        self.actionMostrar_Grafo_P.setObjectName(u"actionMostrar_Grafo_P")
        self.actionMostrar_Grafo_K = QAction(MainWindow)
        self.actionMostrar_Grafo_K.setObjectName(u"actionMostrar_Grafo_K")
        self.actionEjecutar_algoritmo_Prim = QAction(MainWindow)
        self.actionEjecutar_algoritmo_Prim.setObjectName(u"actionEjecutar_algoritmo_Prim")
        self.actionEjecutar_algoritmo_K = QAction(MainWindow)
        self.actionEjecutar_algoritmo_K.setObjectName(u"actionEjecutar_algoritmo_K")
        self.actionMostrar_Grafo_D = QAction(MainWindow)
        self.actionMostrar_Grafo_D.setObjectName(u"actionMostrar_Grafo_D")
        self.actionEjecutar_algoritmo_D = QAction(MainWindow)
        self.actionEjecutar_algoritmo_D.setObjectName(u"actionEjecutar_algoritmo_D")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_3 = QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Dibujar_pushButton = QPushButton(self.tab)
        self.Dibujar_pushButton.setObjectName(u"Dibujar_pushButton")

        self.gridLayout_3.addWidget(self.Dibujar_pushButton, 1, 0, 1, 1)

        self.graphicsView = QGraphicsView(self.tab)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_3.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.Limpiar_pushButton = QPushButton(self.tab)
        self.Limpiar_pushButton.setObjectName(u"Limpiar_pushButton")

        self.gridLayout_3.addWidget(self.Limpiar_pushButton, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.Tabla = QTableWidget(self.tab_2)
        self.Tabla.setObjectName(u"Tabla")

        self.gridLayout_4.addWidget(self.Tabla, 0, 0, 1, 3)

        self.id_lineEdit = QLineEdit(self.tab_2)
        self.id_lineEdit.setObjectName(u"id_lineEdit")

        self.gridLayout_4.addWidget(self.id_lineEdit, 1, 0, 1, 1)

        self.buscar_pushButton = QPushButton(self.tab_2)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout_4.addWidget(self.buscar_pushButton, 1, 1, 1, 1)

        self.Mostrar_tabla_pushButton = QPushButton(self.tab_2)
        self.Mostrar_tabla_pushButton.setObjectName(u"Mostrar_tabla_pushButton")

        self.gridLayout_4.addWidget(self.Mostrar_tabla_pushButton, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_5.addWidget(self.tabWidget, 0, 1, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_7 = QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.Salida = QPlainTextEdit(self.groupBox)
        self.Salida.setObjectName(u"Salida")

        self.gridLayout_7.addWidget(self.Salida, 6, 0, 1, 6)

        self.ord_id_pushButton = QPushButton(self.groupBox)
        self.ord_id_pushButton.setObjectName(u"ord_id_pushButton")

        self.gridLayout_7.addWidget(self.ord_id_pushButton, 7, 0, 1, 3)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 3, 1, 1)

        self.Green_spinBox = QSpinBox(self.groupBox_2)
        self.Green_spinBox.setObjectName(u"Green_spinBox")
        self.Green_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.Green_spinBox, 0, 4, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 5, 1, 1)

        self.Blue_spinBox = QSpinBox(self.groupBox_2)
        self.Blue_spinBox.setObjectName(u"Blue_spinBox")
        self.Blue_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.Blue_spinBox, 0, 6, 1, 1)

        self.Red_spinBox = QSpinBox(self.groupBox_2)
        self.Red_spinBox.setObjectName(u"Red_spinBox")
        self.Red_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.Red_spinBox, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_2, 3, 0, 1, 6)

        self.Agregar_Inicio_pushButton = QPushButton(self.groupBox)
        self.Agregar_Inicio_pushButton.setObjectName(u"Agregar_Inicio_pushButton")

        self.gridLayout_7.addWidget(self.Agregar_Inicio_pushButton, 5, 3, 1, 2)

        self.Agregar_Final_pushButton = QPushButton(self.groupBox)
        self.Agregar_Final_pushButton.setObjectName(u"Agregar_Final_pushButton")

        self.gridLayout_7.addWidget(self.Agregar_Final_pushButton, 5, 0, 1, 3)

        self.ord_dis_pushButton = QPushButton(self.groupBox)
        self.ord_dis_pushButton.setObjectName(u"ord_dis_pushButton")

        self.gridLayout_7.addWidget(self.ord_dis_pushButton, 7, 3, 1, 2)

        self.Mostrar_pushButton = QPushButton(self.groupBox)
        self.Mostrar_pushButton.setObjectName(u"Mostrar_pushButton")

        self.gridLayout_7.addWidget(self.Mostrar_pushButton, 5, 5, 1, 1)

        self.ord_vel_pushButton = QPushButton(self.groupBox)
        self.ord_vel_pushButton.setObjectName(u"ord_vel_pushButton")

        self.gridLayout_7.addWidget(self.ord_vel_pushButton, 7, 5, 1, 1)

        self.id_spinBox = QSpinBox(self.groupBox)
        self.id_spinBox.setObjectName(u"id_spinBox")
        self.id_spinBox.setMaximum(1000000000)

        self.gridLayout_7.addWidget(self.id_spinBox, 0, 1, 1, 5)

        self.Velocidad_spinBox = QSpinBox(self.groupBox)
        self.Velocidad_spinBox.setObjectName(u"Velocidad_spinBox")
        self.Velocidad_spinBox.setMaximum(1000000000)

        self.gridLayout_7.addWidget(self.Velocidad_spinBox, 4, 2, 1, 2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_7.addWidget(self.label_3, 4, 0, 1, 2)

        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.Destinox_spinBox = QSpinBox(self.groupBox_3)
        self.Destinox_spinBox.setObjectName(u"Destinox_spinBox")
        self.Destinox_spinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.Destinox_spinBox, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)

        self.Destinoy_spinBox = QSpinBox(self.groupBox_3)
        self.Destinoy_spinBox.setObjectName(u"Destinoy_spinBox")
        self.Destinoy_spinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.Destinoy_spinBox, 0, 3, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_3, 2, 0, 1, 6)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_7.addWidget(self.label_7, 0, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_6 = QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_6.addWidget(self.label_8, 0, 0, 1, 1)

        self.Origenx_spinBox = QSpinBox(self.groupBox_4)
        self.Origenx_spinBox.setObjectName(u"Origenx_spinBox")
        self.Origenx_spinBox.setMaximum(500)

        self.gridLayout_6.addWidget(self.Origenx_spinBox, 0, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_6.addWidget(self.label_9, 0, 2, 1, 1)

        self.Origeny_spinBox = QSpinBox(self.groupBox_4)
        self.Origeny_spinBox.setObjectName(u"Origeny_spinBox")
        self.Origeny_spinBox.setMaximum(500)

        self.gridLayout_6.addWidget(self.Origeny_spinBox, 0, 3, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_4, 1, 0, 1, 6)

        self.mostrar_grafo_pushButton = QPushButton(self.groupBox)
        self.mostrar_grafo_pushButton.setObjectName(u"mostrar_grafo_pushButton")

        self.gridLayout_7.addWidget(self.mostrar_grafo_pushButton, 4, 4, 1, 2)


        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 891, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuFuerza_Bruta = QMenu(self.menubar)
        self.menuFuerza_Bruta.setObjectName(u"menuFuerza_Bruta")
        self.menuRecorridos = QMenu(self.menubar)
        self.menuRecorridos.setObjectName(u"menuRecorridos")
        self.menuPrim = QMenu(self.menubar)
        self.menuPrim.setObjectName(u"menuPrim")
        self.menuKruskal = QMenu(self.menubar)
        self.menuKruskal.setObjectName(u"menuKruskal")
        self.menuDijkstra = QMenu(self.menubar)
        self.menuDijkstra.setObjectName(u"menuDijkstra")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuFuerza_Bruta.menuAction())
        self.menubar.addAction(self.menuRecorridos.menuAction())
        self.menubar.addAction(self.menuPrim.menuAction())
        self.menubar.addAction(self.menuKruskal.menuAction())
        self.menubar.addAction(self.menuDijkstra.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuFuerza_Bruta.addAction(self.actionMostrar_particulas)
        self.menuFuerza_Bruta.addAction(self.actionEjecutar_Algoritmo)
        self.menuRecorridos.addAction(self.actionProfundidad)
        self.menuRecorridos.addAction(self.actionAnchura)
        self.menuPrim.addAction(self.actionMostrar_Grafo_P)
        self.menuPrim.addAction(self.actionEjecutar_algoritmo_Prim)
        self.menuKruskal.addAction(self.actionMostrar_Grafo_K)
        self.menuKruskal.addAction(self.actionEjecutar_algoritmo_K)
        self.menuDijkstra.addAction(self.actionMostrar_Grafo_D)
        self.menuDijkstra.addAction(self.actionEjecutar_algoritmo_D)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionMostrar_particulas.setText(QCoreApplication.translate("MainWindow", u"Mostrar particulas", None))
        self.actionEjecutar_Algoritmo.setText(QCoreApplication.translate("MainWindow", u"Ejecutar Algoritmo", None))
        self.actionProfundidad.setText(QCoreApplication.translate("MainWindow", u"Profundidad", None))
        self.actionAnchura.setText(QCoreApplication.translate("MainWindow", u"Anchura", None))
        self.actionMostrar_Grafo_P.setText(QCoreApplication.translate("MainWindow", u"Mostrar Grafo", None))
        self.actionMostrar_Grafo_K.setText(QCoreApplication.translate("MainWindow", u"Mostrar Grafo", None))
        self.actionEjecutar_algoritmo_Prim.setText(QCoreApplication.translate("MainWindow", u"Ejecutar algoritmo", None))
        self.actionEjecutar_algoritmo_K.setText(QCoreApplication.translate("MainWindow", u"Ejecutar algoritmo", None))
        self.actionMostrar_Grafo_D.setText(QCoreApplication.translate("MainWindow", u"Mostrar Grafo", None))
        self.actionEjecutar_algoritmo_D.setText(QCoreApplication.translate("MainWindow", u"Ejecutar algoritmo", None))
        self.Dibujar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.Limpiar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Visualizador Gr\u00e1fico", None))
        self.id_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID de la Particula", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.Mostrar_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Part\u00edculas", None))
        self.ord_id_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar(ID)", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Color(R, G, B)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"G:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"R:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"B:", None))
        self.Agregar_Inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Inicio", None))
        self.Agregar_Final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
        self.ord_dis_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar(Distancia)", None))
        self.Mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.ord_vel_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar(Velocidad)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Destino", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u" X:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u" Y:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Origen", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u" X:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.mostrar_grafo_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar Grafo", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuFuerza_Bruta.setTitle(QCoreApplication.translate("MainWindow", u"Fuerza Bruta", None))
        self.menuRecorridos.setTitle(QCoreApplication.translate("MainWindow", u"Recorridos", None))
        self.menuPrim.setTitle(QCoreApplication.translate("MainWindow", u"Prim", None))
        self.menuKruskal.setTitle(QCoreApplication.translate("MainWindow", u"Kruskal", None))
        self.menuDijkstra.setTitle(QCoreApplication.translate("MainWindow", u"Dijkstra", None))
    # retranslateUi

