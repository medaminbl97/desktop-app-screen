import sys
import threading
import asyncio
from PySide6.QtGui import QCloseEvent
import websockets
from PySide6.QtCore import QUrl, Qt,QObject, Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView

from browser import Browser
from textArea import TextArea
from websocket_server import WebSocketServer

class MainWindow(QMainWindow):
    closing = Signal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window Example")
        self.current = "prayer"
        self.setGeometry(100, 100, 1280, 920)
        self.setContentsMargins(0, 0, 0, 0)
        # Window Components
        self.browser = Browser(self)
        self.text = TextArea(self)
        self.web_socket = WebSocketServer()
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout(central_widget)  # Set layout on central widget
        self.layout.addWidget(self.browser)
        self.websocket_thread = threading.Thread(target=self.web_socket.start)

        self.bind()
        self.run()

    def change_screen(self, cmd):
        
        # print("change screen to:", cmd)
        # if cmd != self.current:
        #     if self.current in ["prayer", "izr", "app"]:  # Widgets to remove
        #         self.layout.removeWidget(self.browser)
        #         print("removed browser widget")
        #     elif self.current == "text":
        #         self.layout.removeWidget(self.text)

        #     self.current = cmd  # Update current screen

        #     if cmd in ["prayer", "izr","app"]:  # Widgets to add
        #         self.layout.addWidget(self.browser)
        #     elif cmd == "text":
        #         print("adding browser widget")
        #         self.layout.addWidget(self.text)
        # self.setLayout(self.layout)
        return
    def closeEvent(self, event: QCloseEvent) -> None:
        print("this is form close event")
        self.web_socket
        self.web_socket.stop()
        self.websocket_thread.join()
        return super().closeEvent(event)
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.text.fitTextToWidget()
        self.text.setGeometry(0, 0, self.geometry().width(), self.geometry().height())

    def bind(self):
        self.web_socket.change_screen.connect(self.change_screen)
        self.web_socket.change_text.connect(self.text.changeText)
        self.web_socket.change_url.connect(self.browser.change_url)
        self.closing.connect(self.web_socket.stop)

    def run(self):
        self.websocket_thread.start()

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    # browser = Browser()
    # my_server = WebSocketServer()
    # my_server.change_url.connect(browser.change_url)
    # my_server.connected.connect(browser.connected)
    # browser.closing.connect(my_server.stop)
    # # Start the WebSocket server on a separate thread
    # websocket_thread = threading.Thread(target=my_server.start)

    # websocket_thread.start()

    # browser.show()
    sys.exit(app.exec())
