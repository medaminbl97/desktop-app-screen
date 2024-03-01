
import sys
import threading
import asyncio
from PySide6.QtGui import QCloseEvent
import websockets
from PySide6.QtCore import QUrl, Qt,QObject, Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel,QSizePolicy,QLineEdit
from PySide6.QtGui import QFontMetrics





class TextArea(QLabel):
    def __init__(self,parent:QMainWindow=None):
        super().__init__()
        self.text = "haaa ich  bins"
        self.setText(self.text)
        self.setStyleSheet("QLineEdit{background : white; padding : 10px; font-family : monospace;}")
        self.setAlignment(Qt.AlignCenter)
        self.setGeometry(parent.geometry())
        self.setWordWrap(True)
        # self.setSizePolicy(
        #     QSizePolicy.Expanding, QSizePolicy.Expanding
        # )
    def transform_str(self,str):
        words = str.split()
        if len(words) <= 3:
            return str
        else:
            result = ''
            for i, word in enumerate(words):
                result += word
                if (i + 1) % 3 == 0:
                    result += '\n'
                else:
                    result += ' '
            return result.strip()

    def changeText(self,str):
        if str == "delete":
            self.setText("")
            self.text = ""
            self.fitTextToWidget()
        else:
            self.setText(self.transform_str(str))
            self.text = str
            self.fitTextToWidget()
            

    def fitTextToWidget(self):
        font = self.font()
        font.setPointSizeF(165)
        self.setFont(font)