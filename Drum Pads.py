import sys
import threading
from PyQt5 import QtWidgets
import design.untitled as design
from playsound import playsound
class ExamleApp(QtWidgets.QMainWindow,design.Ui_MainWindow):
    def __init__ (self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.click0)
        self.pushButton_2.clicked.connect(self.click1)
        self.pushButton_4.clicked.connect(self.click2)
        self.pushButton_5.clicked.connect(self.click3)
        self.pushButton_7.clicked.connect(self.click4)

    def click0(self):
        threading.Thread(target=self.sound0, args=()).start()

    def sound0(self):
        playsound('Sounds/Sound_04669.mp3')

    def click1(self):
        threading.Thread(target=self.sound1, args=()).start()

    def sound1(self):
        playsound('Sounds/Sound_04685.mp3')

    def click2(self):
        threading.Thread(target=self.sound2, args=()).start()

    def sound2(self):
        playsound('Sounds/Sound_17211.mp3')

    def click3(self):
        threading.Thread(target=self.sound3, args=()).start()

    def sound3(self):
        playsound('Sounds/Sound_17947.mp3')

    def click4(self):
        threading.Thread(target=self.sound4, args=()).start()

    def sound4(self):
        playsound('Sounds/Sound_20955.mp3')




app=QtWidgets.QApplication(sys.argv)
window=ExamleApp()
window.show()
app.exec_()