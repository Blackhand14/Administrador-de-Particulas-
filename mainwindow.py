from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtCore import Slot
from PySide2.QtGui import QPen, QColor, QTransform
from grafo import Grafo
from particulas.algoritmos import puntos_mas_cercanos
from ui_mainwindow import Ui_MainWindow 
from particulas.particulas import Particulas
from particulas.particula import Particula
from random import randint
from nodo import Nodo
from pprint import pformat

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.particulas = Particulas()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.puntos = []

        self.ui.Agregar_Final_pushButton.clicked.connect(self.click_agregar_final)
        self.ui.Agregar_Inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.Mostrar_pushButton.clicked.connect(self.click_mostrar) 
        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)

        self.ui.Mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)

        self.ui.Dibujar_pushButton.clicked.connect(self.dibujar)
        self.ui.Limpiar_pushButton.clicked.connect(self.limpiar)
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

        self.ui.ord_id_pushButton.clicked.connect(self.ordenar_id)
        self.ui.ord_dis_pushButton.clicked.connect(self.ordenar_dist)
        self.ui.ord_vel_pushButton.clicked.connect(self.ordenar_velocidad)

        self.ui.actionMostrar_particulas.triggered.connect(self.mostrar_particulas)
        self.ui.actionEjecutar_Algoritmo.triggered.connect(self.puntos_mas_cercanos)

        self.ui.mostrar_grafo_pushButton.clicked.connect(self.mostrar_grafo) 

        self.ui.actionProfundidad.triggered.connect(self.recorrido_profundidad)
        self.ui.actionAnchura.triggered.connect(self.recorrido_anchura)

        self.ui.actionEjecutar_algoritmo_Prim.triggered.connect(self.prim)
        self.ui.actionMostrar_Grafo_P.triggered.connect(self.mostrar_P)

        self.ui.actionEjecutar_algoritmo_K.triggered.connect(self.kruskal)
        self.ui.actionMostrar_Grafo_K.triggered.connect(self.mostrar_K)

        self.ui.actionMostrar_Grafo_D.triggered.connect(self.mostrar_D)
        self.ui.actionEjecutar_algoritmo_D.triggered.connect(self.dijkstra)

    @Slot()
    def dijkstra(self):
        if len(self.particulas) == 0:
            QMessageBox.critical(
                self,
                "No se pudo llevar a cabo el algoritmo",
                "Verifica si hay un Grafo existente"
            )
        else:
            origen_x = int(self.ui.Origenx_spinBox.text())
            origen_y = int(self.ui.Origeny_spinBox.text())
            origen = (origen_x, origen_y)
            destino_x = int(self.ui.Destinox_spinBox.text())
            destino_y = int(self.ui.Destinoy_spinBox.text())
            destino = (destino_x, destino_y)
            if Nodo(origen) not in self.particulas.lista() or Nodo(destino) not in self.particulas.lista():
                QMessageBox.critical(
                    self,
                    "Nose puede ejecutar el algoritmo",
                    "Verifica los datos de origen y destino"
                )
            else:
                distancias, camino = self.particulas.dijkstra(origen) 
                self.particulas.mostrar_Dijkstra(distancias)
                self.particulas.mostrar_Dijkstra(camino)
                self.ui.tabWidget.setCurrentIndex(2)
                self.scene.clear()
                pen = QPen()
                pen.setColor(QColor(255, 30, 180))
                dimension = 5
                pen.setWidth(dimension)

                siguiente = Nodo(destino)

                while siguiente != Nodo(origen): 
                    actual = camino[siguiente]
                    self.scene.addLine(actual.get_x()+3, actual.get_y()+3, siguiente.get_x()+3, siguiente.get_y()+3, pen)
                    siguiente = camino[siguiente] 

    @Slot()
    def mostrar_D(self):
        self.ui.Salida.clear()
        self.particulas.crear_grafo()
        grafo = self.particulas.lista()
        mostrar = self.particulas.mostrar_grafo(grafo)
        self.ui.Salida.insertPlainText(mostrar)
        print(mostrar)
        self.dibujar()

    @Slot()
    def kruskal(self):
        grafo = self.particulas.crear_grafo2()
        if len(self.particulas) == 0:
            QMessageBox.critical(
                self,
                "No se pudo llevar a cabo el recorrido",
                "Verifica si hay un Grafo existente"
            )
        else:
            self.ui.Salida.clear()
            kruskal = self.particulas.kruskal(grafo)
            mostrar = self.particulas.mostrar_grafo(kruskal[1])
            print("Kruskal: ")
            print(mostrar)
            self.ui.Salida.insertPlainText("Kruskal: " + "\n")
            self.ui.Salida.insertPlainText(mostrar)
            self.dibujar()
            pen = QPen()
            pen.setWidth(2)
            color = QColor(255, 30, 180)
            pen.setColor(color)
            for nodo in kruskal[0]:
                origen = nodo[1]
                destino = nodo[2]
                self.scene.addLine(origen.get_x()+3, origen.get_y()+3, destino.get_x()+3, destino.get_y()+3, pen)

    @Slot()
    def mostrar_K(self):
        self.ui.Salida.clear()
        self.particulas.crear_grafo2()
        grafo = self.particulas.lista()
        mostrar = self.particulas.mostrar_grafo(grafo)
        self.ui.Salida.insertPlainText(mostrar)
        print(mostrar)
        self.dibujar()

    @Slot()
    def prim(self):
        if len(self.particulas) == 0:
            QMessageBox.critical(
                self,
                "No se pudo llevar a cabo el recorrido",
                "Verifica si hay un Grafo existente"
            )
        else:
            origen_x = int(self.ui.Origenx_spinBox.text())
            origen_y = int(self.ui.Origeny_spinBox.text())
            origen = (origen_x, origen_y)
            self.particulas.crear_grafo()
            if Nodo(origen) not in self.particulas.lista():
                QMessageBox.critical(
                    self,
                    "No se pudo llevar a cabo el recorrido",
                    "Verifica el origen del recorrido"
                )
            else:
                self.ui.Salida.clear()
                prim = self.particulas.prim(origen)
                mostrar = self.particulas.mostrar_grafo(prim[0])
                self.ui.Salida.insertPlainText("Origen: " + str(origen) + "\n")
                self.ui.Salida.insertPlainText("Prim: " + "\n")
                self.ui.Salida.insertPlainText(mostrar)
                self.dibujar()
                print("Origen: " + str(origen))
                print("Prim: ")
                print(mostrar)
                pen = QPen()
                pen.setWidth(2)
                color = QColor(255, 30, 180)
                pen.setColor(color)
                for arista in prim[1]:
                    inicio = arista[1]
                    destino = arista[2]
                    self.scene.addLine(inicio.get_x()+3, inicio.get_y()+3, destino.get_x()+3, destino.get_y()+3, pen)
    
    @Slot()
    def mostrar_P(self):
        self.ui.Salida.clear()
        self.particulas.crear_grafo()
        grafo = self.particulas.lista()
        mostrar = self.particulas.mostrar_grafo(grafo)
        self.ui.Salida.insertPlainText(mostrar)
        print(mostrar)
        self.dibujar()

    @Slot()
    def recorrido_anchura(self):
        if len(self.particulas) == 0:
            QMessageBox.critical(
                self,
                "No se pudo llevar a cabo el recorrido",
                "Verifica si hay un Grafo existente"
            )
        else:
            origen_x = self.ui.Origenx_spinBox.value()
            origen_y = self.ui.Origeny_spinBox.value()
            origen = (origen_x, origen_y)
            self.particulas.crear_grafo()
            if Nodo(origen) not in self.particulas.lista():
                QMessageBox.critical(
                    self,
                    "No se pudo llevar a cabo el recorrido",
                    "Verifica el origen del recorrido"
                )
            else:
                anchura = self.particulas.recorrido_anchura(origen)
                recorrido = self.particulas.recorrido_toString(anchura)
                print("Origen: " + str(origen))
                print("Anchura: ")                
                print(recorrido)
                self.ui.Salida.clear()
                self.ui.Salida.insertPlainText("Origen: " + str(origen) + "\n")
                self.ui.Salida.insertPlainText("Anchura: \n")
                self.ui.Salida.insertPlainText(recorrido)

    @Slot()
    def recorrido_profundidad(self):
        if len(self.particulas) == 0:
            QMessageBox.critical(
                self,
                "No se pudo llevar a cabo el recorrido",
                "Verifica si hay un Grafo existente"
            )
        else:
            origen_x = self.ui.Origenx_spinBox.value()
            origen_y = self.ui.Origeny_spinBox.value()
            origen = (origen_x, origen_y)
            self.particulas.crear_grafo()
            if Nodo(origen) not in self.particulas.lista():
                QMessageBox.critical(
                    self,
                    "No se pudo llevar a cabo el recorrido",
                    "Verifica el origen del recorrido"
                )
            else:
                profundidad = self.particulas.recorrido_profundidad(origen)
                recorrido = self.particulas.recorrido_toString(profundidad)
                print("Origen: " + str(origen))
                print("Profundidad: ")                
                print(recorrido)
                self.ui.Salida.clear()
                self.ui.Salida.insertPlainText("Origen: " + str(origen) + "\n")
                self.ui.Salida.insertPlainText("Profundidad: \n")
                self.ui.Salida.insertPlainText(recorrido)

    @Slot() 
    def mostrar_grafo(self):
        self.ui.Salida.clear()
        self.particulas.crear_grafo()
        grafo = self.particulas.lista()
        mostrar = self.particulas.mostrar_grafo_lista(grafo)
        self.ui.Salida.insertPlainText(mostrar)
        print(mostrar)
        self.dibujar()
  
    @Slot()
    def puntos_mas_cercanos(self):
        resultado = puntos_mas_cercanos(self.puntos)
        #print(resultado)
        pen = QPen()
        pen.setWidth(2)
        for punto1, punto2 in resultado:
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            color = QColor(r, g, b)
            pen.setColor(color)

            x1 = punto1[0]
            y1 = punto1[1]
            x2 = punto2[0]
            y2 = punto2[1]
            self.scene.addLine(x1+3, y1+3, x2+3, y2+3, pen)

    @Slot()
    def mostrar_particulas(self):
        self.limpiar()
        self.puntos = []
        pen = QPen()
        pen.setWidth(2)
        for particula in self.particulas:
            x1 = particula.origen_x
            x2 = particula.origen_y
            punto = (x1, x2)
            self.puntos.append(punto)
            y1 = particula.destino_x
            y2 = particula.destino_y
            punto = (y1, y2)
            self.puntos.append(punto)
        for punto in self.puntos:
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)

            x1 = punto[0]
            x2 = punto[1]
            y1 = punto[0]
            y2 = punto[1] 
            color = QColor(r, g, b)
            pen.setColor(color)
            self.scene.addRect(x1, x2, 6, 6, pen)
            self.scene.addRect(y1, y2, 6, 6, pen)


    @Slot()
    def ordenar_id(self):
        self.particulas.ordenar_ID()
        self.click_mostrar()

    @Slot()
    def ordenar_dist(self):
        self.particulas.ordenar_Distancia()
        self.click_mostrar()

    @Slot()
    def ordenar_velocidad(self):
        self.particulas.ordenar_Velocidad()
        self.click_mostrar()


    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8) 


    @Slot()
    def dibujar(self):
        pen = QPen()
        pen.setWidth(2)
        for particula in self.particulas:
            r = particula.red
            g = particula.green
            b = particula.blue

            color = QColor(r, g, b)
            pen.setColor(color)

            x_origen = particula.origen_x
            y_origen = particula.origen_y
            x_destino = particula.destino_x
            y_destino = particula.destino_y

            self.scene.addEllipse(x_origen, y_origen, 6, 6, pen)
            self.scene.addEllipse(x_destino, y_destino, 6, 6, pen)
            self.scene.addLine(x_origen+3, y_origen+3, x_destino+3, y_destino+3, pen)

                
    @Slot()
    def limpiar(self):
        self.scene.clear()
        self.ui.graphicsView.setTransform(QTransform())


    @Slot()
    def buscar_id(self):
        id = self.ui.id_lineEdit.text()
        encontrado = False
        for particula in self.particulas:
            #print(particula)
            if id == str(particula.id):
                self.ui.Tabla.clear()
                self.ui.Tabla.setColumnCount(10)
                headers = ["ID", "Origen x", "Origen y", "Destino x", "Destino y",
                            "Velocidad", "Red", "Green", "Blue", "Distancia"]
                self.ui.Tabla.setHorizontalHeaderLabels(headers)
                self.ui.Tabla.setRowCount(len(self.particulas))
                self.ui.Tabla.setRowCount(1)
                id_widget = QTableWidgetItem(str(particula.id))
                origen_x_widget = QTableWidgetItem(str(particula.origen_x))
                origen_y_widget = QTableWidgetItem(str(particula.origen_y))
                destino_x_widget = QTableWidgetItem(str(particula.destino_x))
                destino_y_widget = QTableWidgetItem(str(particula.destino_y))
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                red_widget = QTableWidgetItem(str(particula.red))
                green_widget = QTableWidgetItem(str(particula.green))
                blue_widget = QTableWidgetItem(str(particula.blue))
                distancia_widget = QTableWidgetItem(str(particula.distancia))
                #print(particula.id)
                self.ui.Tabla.setItem(0, 0, id_widget)
                self.ui.Tabla.setItem(0, 1, origen_x_widget)
                self.ui.Tabla.setItem(0, 2, origen_y_widget)
                self.ui.Tabla.setItem(0, 3, destino_x_widget)
                self.ui.Tabla.setItem(0, 4, destino_y_widget)
                self.ui.Tabla.setItem(0, 5, velocidad_widget)
                self.ui.Tabla.setItem(0, 6, red_widget)
                self.ui.Tabla.setItem(0, 7, green_widget)
                self.ui.Tabla.setItem(0, 8, blue_widget)
                self.ui.Tabla.setItem(0, 9, distancia_widget)
                encontrado = True
                return
        if not encontrado:
            QMessageBox.warning(
                self,
                "Atencion",
                f'La particula con el ID "{id}" no fue encontrada'
            )


    @Slot()
    def mostrar_tabla(self):
        self.ui.Tabla.setColumnCount(10)
        headers = ["ID", "Origen x", "Origen y", "Destino x", "Destino y",
                    "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.Tabla.setHorizontalHeaderLabels(headers)
        self.ui.Tabla.setRowCount(len(self.particulas))
        row = 0
        for particula in self.particulas:
            id_widget = QTableWidgetItem(str(particula.id))
            origen_x_widget = QTableWidgetItem(str(particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(particula.origen_y))
            destino_x_widget = QTableWidgetItem(str(particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(particula.destino_y))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))
            #print(particula.id)
            self.ui.Tabla.setItem(row, 0, id_widget)
            self.ui.Tabla.setItem(row, 1, origen_x_widget)
            self.ui.Tabla.setItem(row, 2, origen_y_widget)
            self.ui.Tabla.setItem(row, 3, destino_x_widget)
            self.ui.Tabla.setItem(row, 4, destino_y_widget)
            self.ui.Tabla.setItem(row, 5, velocidad_widget)
            self.ui.Tabla.setItem(row, 6, red_widget)
            self.ui.Tabla.setItem(row, 7, green_widget)
            self.ui.Tabla.setItem(row, 8, blue_widget)
            self.ui.Tabla.setItem(row, 9, distancia_widget)
            row += 1


    @Slot()
    def click_mostrar(self):
        #self.particulas.mostrar()
        self.ui.Salida.clear()
        self.ui.Salida.insertPlainText(str(self.particulas)) 
    
    @Slot()
    def click_agregar_final(self):
        Id = self.ui.id_spinBox.value()
        Origen_x = self.ui.Origenx_spinBox.value()
        Origen_y = self.ui.Origeny_spinBox.value()
        Destino_x = self.ui.Destinox_spinBox.value()
        Destino_y = self.ui.Destinoy_spinBox.value()
        Velocidad = self.ui.Velocidad_spinBox.value()
        Red = self.ui.Red_spinBox.value()
        Green = self.ui.Green_spinBox.value()
        Blue = self.ui.Blue_spinBox.value() 

        particula = Particula(Id, Origen_x, Origen_y, Destino_x, Destino_y, Velocidad, Red, Green, Blue)
        self.particulas.agregarFinal(particula)

    @Slot()
    def click_agregar_inicio(self):
        Id = self.ui.id_spinBox.value()
        Origen_x = self.ui.Origenx_spinBox.value()
        Origen_y = self.ui.Origeny_spinBox.value()
        Destino_x = self.ui.Destinox_spinBox.value()
        Destino_y = self.ui.Destinoy_spinBox.value()
        Velocidad = self.ui.Velocidad_spinBox.value()
        Red = self.ui.Red_spinBox.value()
        Green = self.ui.Green_spinBox.value()
        Blue = self.ui.Blue_spinBox.value() 

        particula = Particula(Id, Origen_x, Origen_y, Destino_x, Destino_y, Velocidad, Red, Green, Blue)
        self.particulas.agregarInicio(particula) 

    @Slot()
    def action_abrir_archivo(self):
        #print('Abrir archivo')
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.particulas.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se recupero el archvio: " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Error al recuperar el archivo: " + ubicacion
            )


    @Slot()
    def action_guardar_archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        #print(ubicacion)
        if self.particulas.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se pudo crear el archivo: " + ubicacion
            )
        else: 
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo crear el archivo: " + ubicacion
            )
