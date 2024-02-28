import sys
from PyQt5 import QtWidgets, QtCore

# APPLICATION WINDOW:

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(800, 600)
widget.setWindowTitle("This is PyQt Widget example")
widget.show()
exit(app.exec_())