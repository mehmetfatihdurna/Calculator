import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QToolTip,QLabel,QLineEdit,QPushButton
from PyQt5.QtGui import QIcon

class Calculator(QMainWindow):

    security_of_eval = "123456789/*-+."

    def __init__(self):
        super(Calculator, self).__init__()

        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("robotic.png"))
        self.setToolTip("MFD")
        self.setGeometry(200,200,300,300)
        self.setFixedSize(300,300)
        self.initUI()
    
    def initUI(self):

        self.content = ""

        #text_area
        self.text_line = QLineEdit(self)
        self.text_line.move(40,30)
        self.text_line.resize(220,30)

        #button1
        self.button_1 = QPushButton(self)
        self.button_1.setText("1")
        self.button_1.move(40,70)
        self.button_1.resize(46,46)
        self.button_1.clicked.connect(lambda: self.clicked(self.button_1))

        #button2
        self.button_2 = QPushButton(self)
        self.button_2.setText("2")
        self.button_2.move(98,70)
        self.button_2.resize(46,46)
        self.button_2.clicked.connect(lambda: self.clicked(self.button_2))

        #button3
        self.button_3 = QPushButton(self)
        self.button_3.setText("3")
        self.button_3.move(156,70)
        self.button_3.resize(46,46)
        self.button_3.clicked.connect(lambda: self.clicked(self.button_3))

        #button_plus
        self.button_plus = QPushButton(self)
        self.button_plus.setText("+")
        self.button_plus.move(214,70)
        self.button_plus.resize(46,46)
        self.button_plus.clicked.connect(lambda: self.clicked(self.button_plus))

        #button4
        self.button_4 = QPushButton(self)
        self.button_4.setText("4")
        self.button_4.move(40,128)
        self.button_4.resize(46,46)
        self.button_4.clicked.connect(lambda: self.clicked(self.button_4))

        #button5
        self.button_5 = QPushButton(self)
        self.button_5.setText("5")
        self.button_5.move(98,128)
        self.button_5.resize(46,46)
        self.button_5.clicked.connect(lambda: self.clicked(self.button_5))

        #button6
        self.button_6 = QPushButton(self)
        self.button_6.setText("6")
        self.button_6.move(156,128)
        self.button_6.resize(46,46)
        self.button_6.clicked.connect(lambda: self.clicked(self.button_6))

        #button_ eksi
        self.button_eksi = QPushButton(self)
        self.button_eksi.setText("-")
        self.button_eksi.move(214,128)
        self.button_eksi.resize(46,46)
        self.button_eksi.clicked.connect(lambda : self.clicked(self.button_eksi))

        #button7
        self.button_7 = QPushButton(self)
        self.button_7.setText("7")
        self.button_7.move(40,186)
        self.button_7.resize(46,46)
        self.button_7.clicked.connect(lambda: self.clicked(self.button_7))

        #button8
        self.button_8 = QPushButton(self)
        self.button_8.setText("8")
        self.button_8.move(98,186)
        self.button_8.resize(46,46)
        self.button_8.clicked.connect(lambda: self.clicked(self.button_8))

        #button9
        self.button_9 = QPushButton(self)
        self.button_9.setText("9")
        self.button_9.move(156,186)
        self.button_9.resize(46,46)
        self.button_9.clicked.connect(lambda: self.clicked(self.button_9))

        #button_carp
        self.button_carp = QPushButton(self)
        self.button_carp.setText("*")
        self.button_carp.move(214,186)
        self.button_carp.resize(46,46)
        self.button_carp.clicked.connect(lambda: self.clicked(self.button_carp))

        #button0
        self.button_0 = QPushButton(self)
        self.button_0.setText("0")
        self.button_0.move(40,244)
        self.button_0.resize(104,46)
        self.button_0.clicked.connect(lambda: self.clicked(self.button_0))

        #button/
        self.button_divide = QPushButton(self)
        self.button_divide.setText("/")
        self.button_divide.move(156,244)
        self.button_divide.resize(46,46)
        self.button_divide.clicked.connect(lambda: self.clicked(self.button_divide))

        #button_=
        self.button_equal = QPushButton(self)
        self.button_equal.setText("=")
        self.button_equal.move(214,244)
        self.button_equal.resize(46,46)
        self.button_equal.clicked.connect(self.equal)
    
    def clicked(self,a):
        self.content = self.content + a.text()
        self.text_line.setText(self.content)

    def equal(self):
        
        try:
            text = self.text_line.text()
            for i in text:
                if i in self.security_of_eval:
                    continue
                else:
                    raise NameError
            total = eval(text)
            self.text_line.setText(str(total))

        except ZeroDivisionError:
            self.text_line.setText("HATA")
        
        except NameError:
            self.text_line.setText("HATA")
        
        finally:
            self.content = ""
        

    


def window():
    app = QApplication(sys.argv)
    win = Calculator()

    win.show()

    sys.exit(app.exec_())

window()


