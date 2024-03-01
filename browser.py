
from PySide6.QtGui import QCloseEvent
from PySide6.QtCore import QUrl, Qt,Signal
from PySide6.QtWidgets import QVBoxLayout, QWidget, QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView





class Browser(QMainWindow):
    def __init__(self,parent:QMainWindow=None):
        super().__init__()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.central_widget.setLayout(self.layout)

        self.browser = QWebEngineView()
        self.layout.addWidget(self.browser)

        # Load an initial URL
        self.browser.setUrl(QUrl("http://www.izr-verwaltung.de"))
        # self.browser.page().settings().setAttribute(Qt.WebEngineSettings.WebAttribute.ShowScrollBars, False)

    def change_url(self, url):
        print("Changing url: " + url)
        if url == "izr":
            self.browser.setUrl(QUrl("https://iz-regensburg.de"))
        elif url == "prayer":
            self.browser.setUrl(QUrl("http://www.izr-verwaltung.de"))
        elif url == "app":
            self.browser.setUrl(QUrl("https://www.izr-services.de/#/appflyer"))
        else:
            None
    def connected(self, adress):
        print(adress)
   
    def keyPressEvent(self, event):
        # Handle key press events
        if event.key() == Qt.Key_Escape:
            # For example, close the application when the Escape key is pressed
            print("closing")
            self.close()
            
        elif event.key() == Qt.Key_R:
            # Reload the web page when F5 is pressed
            self.browser.reload()
            print("reload ")
        elif event.key() == Qt.Key_I:
            # Reload the web page when F5 is pressed
            self.change_url("https://iz-regensburg.de")
            print("changing to iz-regensburg ")
        else:
            # Call the base class implementation to handle other key events
            super().keyPressEvent(event)

