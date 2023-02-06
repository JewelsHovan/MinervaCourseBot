import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMainWindow
from PyQt6.QtGui import QIntValidator
from cryptography.fernet import Fernet
import json

from time import sleep

class LoginWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle("Account Login")

    def initUI(self):
        title_label = QLabel("Enter your Minerva Account information here", self)
        title_label.setStyleSheet("border: 1px solid black")
        # Create the Email label and textbox
        email_label = QLabel("Email:", self)
        self.email_textbox = QLineEdit(self)
        self.email_textbox.setPlaceholderText("Enter your email")
        # Create the Password label and textbox
        password_label = QLabel("Password:", self)
        self.password_textbox = QLineEdit(self)
        self.password_textbox.setEchoMode(QLineEdit.EchoMode.Password)  # Hide the characters typed in the textbox
        self.password_textbox.setPlaceholderText("Enter your password")
        # Create the Submit button
        submit_button = QPushButton("Submit", self)
        submit_button.setStyleSheet("border: 1px solid black")
        submit_button.clicked.connect(self.validate)

        # Set up the layout
        vbox = QVBoxLayout()
        vbox.addWidget(title_label)
        vbox.addWidget(email_label)
        vbox.addWidget(self.email_textbox)
        vbox.addWidget(password_label)
        vbox.addWidget(self.password_textbox)
        vbox.addWidget(submit_button)
        self.setLayout(vbox)

    
    def encrypt_string(self, string, key):
        cipher = Fernet(key)
        encrypted = cipher.encrypt(string.encode())
        return encrypted 
    
    def decrypt_string(self, string, key):
        cipher = Fernet(key)
        decrypted = cipher.decrypt(string)
        return decrypted.decode()

    def validate(self):
        email = self.email_textbox.text()
        password = self.password_textbox.text()
        # encrypt the email and password and save to json file
        key = Fernet.generate_key() # generate key and save to file
        key_data = {'key': key.decode()}
        with open('key.json', 'w') as f:
            json.dump(key_data, f)

        data = {'email': self.encrypt_string(email, key).decode(), 'password': self.encrypt_string(password, key).decode()}
        with open('account_information.txt', 'w') as wf:
            json.dump(data, wf)

        sleep(0.5)
        self.close()
        



