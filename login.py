import PyQt5
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# Conn
app = QApplication(sys.argv)

# Frame
w = QWidget()
w.resize(400,200)
w.move(100,100)
w.setWindowTitle("LogIn page")

# Frame Layout
flo = QFormLayout()
w.setLayout(flo)

################################################

# Edit Text - Email
em = QLineEdit()
flo.addRow("Email ID : " ,em)

# Edit Text - Password
ps = QLineEdit()
flo.addRow("Password : " ,ps)

# button - login
b1 = QPushButton("Login")
b1.clicked.connect(lambda:btn_click(b1))
flo.addRow(b1)

def btn_click(x):
    '''
    e = em.displayText()
    iate = e.find("@")
    idot = e.find(".")
    print(iate,idot)
    '''
    
    print("Email id :",em.displayText())
    


        







################################################
w.show()
sys.exit(app.exec_())
