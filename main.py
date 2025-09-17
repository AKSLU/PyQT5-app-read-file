import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit, QFileDialog
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class TextFileReader(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Text Reader")
        self.setFixedSize(600, 400)

        self.setStyleSheet("""
            QWidget {
                background-color: SlateGrey;
                color: MistyRose;
            }
            QPushButton {
                background-color: Black;
                color: MistyRose;
                border: 1px solid #666;
                border-radius: 6px;
                padding: 6px;
            }
            QPushButton:hover {
                background-color: Grey;
            }
            QTextEdit {
                background-color: Black;
                color: MistyRose;
                border: 1px solid #444;
                padding: 8px;
                font-family: Consolas;
                font-size: 25px;
            }
        """)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)

        self.label = QLabel("Select .txt file")
        self.label.setFont(QFont("Consolas", 14))
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.button = QPushButton("Open file")
        self.button.setFont(QFont("Consolas", 12))
        self.button.clicked.connect(self.open_file)
        layout.addWidget(self.button)

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        layout.addWidget(self.text_edit)

        self.setLayout(layout)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open text file", "", "Text files (*.txt)"
        )
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.text_edit.setPlainText(content)
                self.label.setText(f"Файл: {file_path}")
            except Exception as e:
                self.text_edit.setPlainText(f"Error read file:\n{e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TextFileReader()
    window.show()
    sys.exit(app.exec_())

