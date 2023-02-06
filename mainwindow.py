import sys
import webbrowser
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QDockWidget
from PyQt6.QtGui import QPixmap, QPalette, QColor
from loginwidget import LoginWidget
from crnwindow import CrnWindow


class MainWindow(QMainWindow):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()
        self.initUI()
        self.show()
        sys.exit(self.app.exec())

    def initUI(self):
        self.changeWindowTitle("Minerva Course Bot")
        # Create the image label and set the image
        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap("images/mcgill_figure.png"))
        self.image_label.setScaledContents(True)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        # Create the buttons
        self.account_button = QPushButton("Enter account information here", self)
        self.webdriver_button = QPushButton("Run the webdriver bot", self)
        self.crn_button = QPushButton("Enter the CRNs", self)
        # connect buttons
        self.account_button.clicked.connect(self.account_button_clicked)
        self.crn_button.clicked.connect(self.crn_button_clicked)
        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.account_button)
        layout.addWidget(self.crn_button)
        layout.addWidget(self.webdriver_button)
        window = QWidget()
        window.setLayout(layout)
        self.setCentralWidget(window)

        # setup menubar
        self.addMenuBar()
        # setup statusbar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage("Add/Drop not active...")
        self.status_bar.setStyleSheet("background-color: FireBrick; border: 1px solid black;")

        #set up the palette
        palette = QPalette()
        red_color = QColor(255, 0, 0)
        palette.setColor(QPalette.ColorRole.Button, red_color)
        self.setPalette(palette)

        # set up the window properties
        self.setGeometry(300, 300, 300, 400)
    
    def addMenuBar(self):
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("File")
        aboutMenu = menuBar.addMenu("About")
        # Adding actions
        fileMenu.addAction("Exit", self.close)
        aboutMenu.addAction("About us", self.goToAboutUsPage)
    
    def goToAboutUsPage(self):
        # go to website
        webbrowser.open("www.google.com")

    def changeWindowTitle(self, pTitle):
        self.setWindowTitle(pTitle)

    def account_button_clicked(self):
        # open the login window
        self.login_window = LoginWidget()
        self.login_window.show()
    
    def crn_button_clicked(self):
        # open a new window
        self.crn_window = CrnWindow()
        self.crn_window.show()






