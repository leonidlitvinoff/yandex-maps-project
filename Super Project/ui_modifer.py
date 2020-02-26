from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QErrorMessage
from PyQt5.QtGui import QPixmap
from PIL.ImageQt import ImageQt
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
        self.horizontalSlider.valueChanged.connect(self.changeZoom)
        self.pushButton.clicked.connect(self.query)
        self.horizontalSlider.sliderReleased.connect(self.query)

        self.zoom = 0
        self.error_msg = QErrorMessage()

    def changeZoom(self, z):
        self.zoom = z
        self.label_2.setText(f'Масштаб: {z}')

    def query(self):
        map_request = {'l': 'map', 'z': str(self.zoom)}
        w, h = self.lineEdit.text(), self.lineEdit_2.text()
        print(1)
        if self.is_valid(w, h):
            map_request['ll'] = f'{w},{h}'
        else:
            return
        print(2)
        url = 'http://static-maps.yandex.ru/1.x/'
        request = requests.get(url, params=map_request)
        self.label_3.setPixmap(QPixmap.fromImage(ImageQt(Image.open(BytesIO(request.content)))))

    def is_valid(self, w, h, show_error=True, debag=False):
        if debag:
            print('перевод долготы в float')
        try:
            w = float(self.lineEdit.text())
        except Exception:
            self.error('Неверная долгота (выражается вещественным числом, через точку)')
            return

        if debag:
            print('проверка ограничения долготы (-180 - 180)')
        if w >= 180 or w <= -180:
            self.error('Неверная долгота (от -180 до 180)')
            return

        if debag:
            print('перевод широта в float')
        try:
            h = float(self.lineEdit.text())
        except Exception:
            self.error('Неверная широта (выражается вещественным числом, через точку)')
            return

        if debag:
            print('проверка ограничения долготы (-90 - 90)')
        if h >= 90 or h <= -90:
            self.error('Неверная широта (от -90 до 90)')
            return

        return str(w), str(h)

    def error(self, msg):
        self.error_msg.showMessage(msg)
