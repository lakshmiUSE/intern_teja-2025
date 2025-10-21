from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
import sys

def on_click():
    QMessageBox.information(window, "Message", "Hello, PyQt5!")

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("My First PyQt5 App")
window.setGeometry(400, 200, 300, 200)

button = QPushButton("Click Me!", window)
button.setGeometry(100, 80, 100, 40)
button.clicked.connect(on_click)

window.show()
sys.exit(app.exec_())


