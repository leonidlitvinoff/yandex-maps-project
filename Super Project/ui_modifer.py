from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QErrorMessage
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtGui import QPixmap
from PIL.ImageQt import ImageQt
from PyQt5.QtCore import Qt
from PIL import Image
from requests import get
import sys

sys.path.append('data\\ui-py\\')

from mainWindow2 import Ui_FormMap


class Widget(QWidget, Ui_FormMap):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.zoom.valueChanged.connect(self.changeScale)
        self.adress.textChanged.connect(self.changeTypeQuery)
        self.Button_Search.clicked.connect(self.reset_and_query)
        self.Button_SettingMap.clicked.connect(self.editMoveMapMode)
        self.zoom.sliderReleased.connect(self.query)
        self.TypeMap.currentIndexChanged.connect(self.query)

        self.editMoveMapMode(True)

        self.shift_w = self.shift_h = 0
        self.move_map_mode = False
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

        self.type_map = {0: 'map',
                         1: 'sat',
                         2: 'sat,skl'}

    def changeTypeQuery(self):
        if self.adress.text():
            state = True
        else:
            state = False

        self.latitude.setReadOnly(state)
        self.longitude.setReadOnly(state)

    def editMoveMapMode(self, value=False):
        self.latitude.setEnabled(value)
        self.longitude.setEnabled(value)
        self.adress.setEnabled(value)
        self.zoom.setEnabled(value)
        self.Button_Search.setEnabled(value)
        self.Button_SettingMap.setEnabled(value)
        self.TypeMap.setEnabled(value)
        self.Button_SettingMap_label.setVisible(not value)
        self.move_map_mode = not value

    def changeScale(self, scale):
        self.zoom_label.setText(f'Масштаб: {scale}')

    def keyPressEvent(self, a0: QKeyEvent) -> None:
        if a0.key() == Qt.Key_PageUp and self.zoom.value() < 17:
            self.zoom.setValue(self.zoom.value() + 1)
        elif a0.key() == Qt.Key_PageDown and self.zoom.value() > 0:
            self.zoom.setValue(self.zoom.value() - 1)
        elif self.move_map_mode:  # Режим редактирования
            step = self.zoom_map[self.zoom.value()]
            if a0.key() == Qt.Key_Escape:
                self.editMoveMapMode(True)
                return
            elif a0.key() == Qt.Key_Up and self.latitude.value() + self.shift_w + step <= 90:
                self.shift_w += step
            elif a0.key() == Qt.Key_Down and self.latitude.value() + self.shift_w - step >= -90:
                self.shift_w -= step
            elif a0.key() == Qt.Key_Left and self.longitude.value() + self.shift_h - step >= -180:
                self.shift_h -= step
            elif a0.key() == Qt.Key_Right and self.longitude.value() + self.shift_h + step <= 180:
                self.shift_h += step
        else:
            return
        self.query()

    def reset_and_query(self):
        self.shift_w = self.shift_h = 0
        self.query()

    def query(self):
        # Если В запросе указан адресс, сначало находим его широту и долготу
        if self.adress.text():
            geocoder_params = {
                "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
                "geocode": self.adress.text(),
                "format": "json"}

            response = get("http://geocode-maps.yandex.ru/1.x/", params=geocoder_params)

            if not response:
                self.error('Ошибка подключения, проверьте интернет')
                return False

            json_response = response.json()

            toponym = json_response["response"]["GeoObjectCollection"]["featureMember"]
            if not toponym:
                self.error('Не удалось найти обьект (Введите другой адрес)')
                return False

            toponym_coodrinates = toponym[0]["GeoObject"]["Point"]["pos"]
            toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

            self.longitude.setValue(float(toponym_longitude))
            self.latitude.setValue(float(toponym_lattitude))

        map_params = {
            "ll": f"{self.longitude.value() + self.shift_h},{self.latitude.value() + self.shift_w}",
            "l": self.type_map[self.TypeMap.currentIndex()],
            "z": self.zoom.value(),
        }

        if self.adress.text():
            map_params['pt'] = f"{self.longitude.value()},{self.latitude.value()}" + ',vkbkm'

        url = 'http://static-maps.yandex.ru/1.x/'
        request = get(url, params=map_params, stream=True).raw

        if not request:
            self.error('Ошибка подключения, проверьте интернет')
            return False

        self.Map.setPixmap(QPixmap.fromImage(ImageQt(Image.open(request).convert('RGBA'))))

    def error(self, msg):
        self.error_msg.showMessage(msg)