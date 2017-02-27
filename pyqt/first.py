from PyQt5 import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowtitle("Первая программа на PyQt")
window.resize(300,70)
label = QtGui.QLabel("<center>hello world!</center>")
btnQuit = QtGui.QPushButton("&Закрыть окно")
vbox = QtGui.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(btnQuit)
window.setLayout(vbox)
QtCore.QObject.connect(btnQuit, QtCore.SIGNAL("clicked()"), QtGui.qApp, QtCore.SLOT("quit()"))
window.show()
sys.exit(app.exec_())
