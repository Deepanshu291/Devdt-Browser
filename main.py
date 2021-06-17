__author__="Deepanshu Sharma"
import os

try:
    import sys
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *
    from PyQt5.QtWebEngineWidgets import *
except ImportError:
    print("Some Modules Are not Installed")
    os.system('python -m pip install -r requirements.txt')
    

class MainWindow(QMainWindow):

    def __init__(self):
        url = 'http://www.google.com'
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(url))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        # self.showFullScreen()

        #NavBar
        navbar = QToolBar()
        self.addToolBar(navbar)

        #back Btn
        back_btn = QAction('<', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        #forward Btn
        f_btn = QAction('>', self)
        f_btn.triggered.connect(self.browser.forward)
        navbar.addAction(f_btn)

        #Reload Btn
        r_btn = QAction('Reload',self)
        r_btn.triggered.connect(self.browser.reload)
        navbar.addAction((r_btn))

        # Home Btn
        h_btn = QAction('Home', self)
        h_btn.triggered.connect(self.Home)
        navbar.addAction((h_btn))

    def Home(self):
        url = 'http://www.google.com'
        self.browser.setUrl(QUrl(url))


app = QApplication(sys.argv)
QApplication.setApplicationName('DevDt Browser')
window = MainWindow()
app.exec_()