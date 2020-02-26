from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QErrorMessage
from PyQt5.QtGui import QPixmap
from PIL.ImageQt import ImageQt
from PyQt5.QtGui import QCursor
from PyQt5 import QtCore
from PyQt5 import QtGui
from PIL import Image
from io import BytesIO
import requests


import sys
sys.path.append('data\\ui-py\\')

from mainWindow import Ui_Form


class Widget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.horizontalSlider.valueChanged.connect(self.changeZ)
        self.pushButton.clicked.connect(self.query)

    def changeZ(self):
        self.label_2.setText(f'Масштаб: {str(self.horizontalSlider.value())}')

    def query(self):
        map_request = {
            'l': 'map',
            'z': str(self.horizontalSlider.value())
        }
        try:
            map_request['ll'] = f'{float(self.lineEdit.text())},{float(self.lineEdit_2.text())}'
            url = 'http://static-maps.yandex.ru/1.x/'
            request = requests.get(url, params=map_request)
            self.label_3.setPixmap(QPixmap.fromImage(ImageQt(Image.open(BytesIO(request.content)))))
        except Exception as e:
            self.exc = QErrorMessage()
            self.exc.showMessage(str(e).capitalize())
