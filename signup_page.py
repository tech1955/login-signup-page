import PyQt5
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# Conn
app = QApplication(sys.argv)

# Frame
w = QWidget()
w.resize(400,400)
w.move(100,100)
w.setWindowTitle("Signup page")

# Frame Layout
flo = QFormLayout()
w.setLayout(flo)

################################################

# Edit Text - First Name
fn = QLineEdit()
flo.addRow("First Name : " ,fn)

# Edit Text - Last Name
ln = QLineEdit()
flo.addRow("Last Name : " ,ln)

# Edit Text - DoB
dob = QLineEdit()
flo.addRow("DOB : " ,dob)

# Edit Text - phone
ph = QLineEdit()
flo.addRow("phone : " ,ph)

# Edit Text - Email
em = QLineEdit()
flo.addRow("Email ID : " ,em)

# Edit Text - Password
ps = QLineEdit()
flo.addRow("Password : " ,ps)

# Edit Text - Re-enter Password
ps1 = QLineEdit()
flo.addRow("Re-enter password : " ,ps1)

# button - Signup
b1 = QPushButton("Signup")
b1.clicked.connect(lambda:btn_click(b1))
flo.addRow(b1)

def btn_click(x):

    if ps.displayText() != ps1.displayText() :
        print("Password m jhol hhh......!")
    else:
        print("Name :",fn.displayText(),ln.displayText())
        print("DOB :",dob.displayText())
        print("phone :",ph.displayText())
        print("Email id :",em.displayText())
        print("password :",ps.displayText())
        

    
    
    
    


        







################################################
w.show()
sys.exit(app.exec_())
