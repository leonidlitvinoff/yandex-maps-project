from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QErrorMessage
from PyQt5.QtGui import QPixmap
from PIL.ImageQt import ImageQt
from PIL import Image
from io import BytesIO
import requests
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtCore import Qt

import sys

sys.path.append('data\\ui-py\\')

from mainWindow import Ui_Form


class Widget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.horizontalSlider.valueChanged.connect(self.changeZoom)
        self.pushButton.clicked.connect(self.query)
        self.pushButton_2.clicked.connect(self.editMoveMapMode)
        self.horizontalSlider.sliderReleased.connect(self.query)
        self.w = 0.0
        self.h = 0.0
        self.move_map_mode = False
        self.zoom = 0
        self.error_msg = QErrorMessage()
        self.zoom_map = {0: 18,
                         1: 24,
                         2: 18,
                         3: 13,
                         4: 9,
                         5: 1.3,
                         6: 0.9,
                         7: 0.5,
                         8: 0.1,
                         9: 0.068,
                         10: 0.03,
                         11: 0.009,
                         12: 0.005,
                         13: 0.001,
                         14: 0.0006,
                         15: 0.0002,
                         16: 0.00008,
                         17: 0.000046}

    def editMoveMapMode(self, value=False):
        self.lineEdit.setEnabled(value)
        self.lineEdit_2.setEnabled(value)
        self.horizontalSlider.setEnabled(value)
        self.pushButton.setEnabled(value)
        self.pushButton_2.setEnabled(value)
        self.move_map_mode = not value



    def changeZoom(self, z):
        self.zoom = z
        self.label_2.setText(f'Масштаб: {z}')

    def keyPressEvent(self, a0: QKeyEvent) -> None:
        if a0.key() == Qt.Key_PageUp:
            if self.zoom < 17:
                self.zoom += 1
                self.horizontalSlider.setValue(self.zoom)
                self.query()
        elif a0.key() == Qt.Key_PageDown:
            if self.zoom > 0:
                self.zoom -= 1
                self.horizontalSlider.setValue(self.zoom)
                self.query()
        elif a0.key() == Qt.Key_Escape:
            if self.move_map_mode:
                self.editMoveMapMode(True)
        else:
            if self.move_map_mode:
                if a0.key() == Qt.Key_Up:
                    self.h += self.zoom_map[self.zoom]
                    self.query()
                elif a0.key() == Qt.Key_Down:
                    self.h -= self.zoom_map[self.zoom]
                    self.query()
                elif a0.key() == Qt.Key_Left:
                    self.w -= self.zoom_map[self.zoom]
                    self.query()
                elif a0.key() == Qt.Key_Right:
                    self.w += self.zoom_map[self.zoom]
                    self.query()

    def query(self):
        map_request = {'l': 'map', 'z': str(self.zoom)}
        w, h = self.lineEdit.text(), self.lineEdit_2.text()
        if self.is_valid(w, h):
            map_request['ll'] = f'{float(w) + self.w},{float(h) + self.h}'
        else:
            return
        url = 'http://static-maps.yandex.ru/1.x/'
        request = requests.get(url, params=map_request)
        print(3)
        self.label_3.setPixmap(QPixmap.fromImage(ImageQt(Image.open(BytesIO(request.content)))))
        print(4)

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
