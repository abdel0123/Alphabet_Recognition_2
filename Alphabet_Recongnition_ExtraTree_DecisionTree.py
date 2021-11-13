import time

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog
import numpy as np
from skimage.io import imread
from skimage.color import rgb2grey
from skimage.filters import threshold_mean
from sklearn import tree

# DEFINITION DE LA FONCTION QUI CHARGE LES IMAGES D'APPRENTISSAGE
def pretraitement():
# la base de donnees D'apprentissage contient les images suivants:
# 5a-3b-3c-2d-3e-3f-2g-3h-4i-3j-2k-2l-2m-3n-3o-3p-2q-2r-3s-2t-3u-2v-2w-2x-2y-2z
    y = np.array(
        [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 9, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13,
         14, 14,
         15, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26])
    images = []
    for i in range(1, 63):
        img = "C:/Users/HP/Desktop/circuit/MST_s2/images/apprentissage/".__add__(i.__str__()).__add__(".png")
        imageRGB = imread(img)
        image = rgb2grey(imageRGB)
        thresh = threshold_mean(image)
        binary = image > thresh
        binary = binary * 1
        images.append(np.ravel(binary))
    return images, y

# DEFINITION DE LA FONCTION QUI CHARGE LES IMAGES DE TEST
def image_test():
    y = np.array([1,1,2,2,3,3,4,4,5,5,6,6,6,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,
                      18,19,19,20,21,21,22,23,24,25,26])
    images = []
    for i in range(1, 45):
        img = "C:/Users/HP/Desktop/circuit/MST_s2/images/TEST/".__add__(i.__str__()).__add__(".png")
        imageRGB = imread(img)
        #ON FAIT LE TRAITEMENT SUR LES IMAGES POUR QU'ILS ETRE DES IMAGES BINAIRE
        image = rgb2grey(imageRGB)
        thresh = threshold_mean(image)
        binary = image > thresh
        binary = binary * 1
        images.append(np.ravel(binary))
    return images, y
#LE CODE QUI PERMET D'AFFICHER L'INTERFACE GRAPHIQUE
class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(786, 468)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(290, 50, 50, 50))
        self.image.setText("")
        self.image.setObjectName("image")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(34, 20, 731, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(34, 80, 731, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(34, 120, 731, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(34, 160, 731, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
       
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(24, 30, 20, 141))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(144, 30, 20, 141))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(314, 30, 20, 141))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(754, 30, 20, 141))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(534, 30, 20, 141))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(64, 50, 51, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(54, 100, 81, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(44, 140, 91, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(54, 180, 81, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(164, 50, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.TG = QtWidgets.QLabel(self.centralwidget)
        self.TG.setGeometry(QtCore.QRect(164, 100, 151, 20))
        self.TG.setText("")
        self.TG.setObjectName("TG")
        self.TM = QtWidgets.QLabel(self.centralwidget)
        self.TM.setGeometry(QtCore.QRect(164, 140, 151, 20))
        self.TM.setText("")
        self.TM.setObjectName("TM")
        self.TB = QtWidgets.QLabel(self.centralwidget)
        self.TB.setGeometry(QtCore.QRect(164, 180, 151, 20))
        self.TB.setText("")
        self.TB.setObjectName("TB")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(344, 50, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.PG = QtWidgets.QLabel(self.centralwidget)
        self.PG.setGeometry(QtCore.QRect(344, 100, 171, 20))
        self.PG.setText("")
        self.PG.setObjectName("PG")
        self.PM = QtWidgets.QLabel(self.centralwidget)
        self.PM.setGeometry(QtCore.QRect(340, 140, 181, 20))
        self.PM.setText("")
        self.PM.setObjectName("PM")
        self.PB = QtWidgets.QLabel(self.centralwidget)
        self.PB.setGeometry(QtCore.QRect(340, 180, 181, 20))
        self.PB.setText("")
        self.PB.setObjectName("PB")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(594, 30, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.CG = QtWidgets.QLabel(self.centralwidget)
        self.CG.setGeometry(QtCore.QRect(510, 100, 131, 20))
        self.CG.setText("")
        self.CG.setObjectName("CG")
        self.CM = QtWidgets.QLabel(self.centralwidget)
        self.CM.setGeometry(QtCore.QRect(510, 140, 131, 20))
        self.CM.setText("")
        self.CM.setObjectName("CM")
        self.CB = QtWidgets.QLabel(self.centralwidget)
        self.CB.setGeometry(QtCore.QRect(510, 180, 131, 20))
        self.CB.setText("")
        self.CB.setObjectName("CB")
        self.ouvrir = QtWidgets.QPushButton(self.centralwidget)
        self.ouvrir.setGeometry(QtCore.QRect(50, 410, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ouvrir.setFont(font)
        self.ouvrir.setObjectName("ouvrir")
        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageLabel.setGeometry(QtCore.QRect(50, 240, 171, 171))
        self.imageLabel.setText("")
        self.imageLabel.setObjectName("imageLabel")
        self.PTG = QtWidgets.QLabel(self.centralwidget)
        self.PTG.setGeometry(QtCore.QRect(550, 100, 201, 20))
        self.PTG.setText("")
        self.PTG.setObjectName("PTG")
        self.PTM = QtWidgets.QLabel(self.centralwidget)
        self.PTM.setGeometry(QtCore.QRect(550, 140, 201, 20))
        self.PTM.setText("")
        self.PTM.setObjectName("PTM")
        self.PTB = QtWidgets.QLabel(self.centralwidget)
        self.PTB.setGeometry(QtCore.QRect(550, 180, 201, 20))
        self.PTB.setText("")
        self.PTB.setObjectName("PTB")
        self.ETC = QtWidgets.QPushButton(self.centralwidget)
        self.ETC.setGeometry(QtCore.QRect(220, 240, 290, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ETC.setFont(font)
        self.ETC.setObjectName("gaussian")
        
        self.DTC = QtWidgets.QPushButton(self.centralwidget)
        self.DTC.setGeometry(QtCore.QRect(220, 360, 290, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DTC.setFont(font)
        self.DTC.setObjectName("bernouli")
        self.resultat = QtWidgets.QLabel(self.centralwidget)
        self.resultat.setGeometry(QtCore.QRect(220, 290, 500, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.resultat.setFont(font)
        self.resultat.setText("")
        self.resultat.setObjectName("resultat")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Classifier"))
        self.label_2.setText(_translate("MainWindow", "DecisionTree"))
        self.label_3.setText(_translate("MainWindow", "ExtraTree"))
     
        self.label_5.setText(_translate("MainWindow", "Temps d\'execution"))
        self.label_9.setText(_translate("MainWindow", "Phase d\'apprentissage"))
        self.label_13.setText(_translate("MainWindow", "phase de test"))
        # INSERTION DU DONNEES
        self.TG.setText(str(t11-t1))
        self.TM.setText(str(t22-t2))
        
        self.PG.setText(str(dtc.score(x1,y1)*100))
        self.PM.setText(str(etc.score(x1,y1)*100))
        
        self.PTG.setText(str(dtc.score(x2,y2)*100))
        self.PTM.setText(str(etc.score(x2,y2)*100))
        
        self.ouvrir.setText(_translate("MainWindow", "parcourir"))
        self.DTC.setText(_translate("MainWindow", "DecisionTreeClassifier"))
        self.ETC.setText(_translate("MainWindow", "ExtraTreeClassifier"))
        
        self.ouvrir.clicked.connect(self.openFile)
        self.DTC.clicked.connect(self.DecisionTreeClassifier)
        self.ETC.clicked.connect(self.ExtraTreeClassifier)


    # CETTE FONCTION PERMET DE OUVRIR UNE FENETRE POUR CHOISIR UNE IMAGE POUR LE TEST
    def openFile(self):
        alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                    "T", "U", "V", "W", "X", "Y", "Z"]
        nom_fichier = QFileDialog.getOpenFileName(self, 'Open file',"C:/Users/HP/Desktop/circuit/MST_s2/images/TEST/")
        self.path = nom_fichier[0]
        pathx = self.path
        pixmap = QtGui.QPixmap(pathx)
        pixmap4 = pixmap.scaled(151, 301, QtCore.Qt.KeepAspectRatio)
        self.imageLabel.setPixmap(QtGui.QPixmap(pixmap4))
        imageTestRGB = imread(self.path)
        imageTest = rgb2grey(imageTestRGB)
        thresh = threshold_mean(imageTest)
        binaryTest = imageTest > thresh
        binaryTest = binaryTest * 1
        self.imageTest = np.ravel(binaryTest)
        
    def DecisionTreeClassifier(self):
        y_predg = dtc.predict([self.imageTest])
        y_predg = np.int(y_predg[0])
        self.resultat.setText("Resultat Decision Tree Classifier : " + alphabet[y_predg - 1])

    # LA PREDICTION DE LA METHODE Extra Tree Classifier
    def ExtraTreeClassifier(self):
        y_predb = etc.predict([self.imageTest])
        y_predb = np.int(y_predb[0])
        self.resultat.setText("Resultat Extra Tree Classifier : " + alphabet[y_predb - 1])



if __name__ == "__main__":
    import sys
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]
    x1, y1 = pretraitement()
    x2, y2 = image_test()
   

    t1 = time.perf_counter()
    etc = tree.ExtraTreeClassifier(random_state=0,criterion='entropy')
    etc.fit(x1, y1)
    t11 = time.perf_counter()
    
    
    
    t2 = time.perf_counter()
    dtc = tree.DecisionTreeClassifier(criterion='entropy',max_leaf_nodes=300)
    dtc.fit(x1, y1)
    t22 = time.perf_counter()
    
    
    
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

