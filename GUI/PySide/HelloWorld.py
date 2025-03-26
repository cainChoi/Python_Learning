import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide 예제")
        self.setGeometry(100, 100, 300, 300)

        layout = QVBoxLayout()

        self.label = QLabel("Hello World!")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        self.button = QPushButton("클릭")
        self.button.clicked.connect(self.show_message)
        layout.addWidget(self.button)

        self.button2 = QPushButton("테스트")
        self.button2.clicked.connect(self.show_message)
        layout.addWidget(self.button2)

        self.setLayout(layout)

    def show_message(self):
        QMessageBox.information(self, "메세지", "버튼 클릭")

if(__name__ == "__main__"):
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

