import openapi
import sys
from PyQt5.QtWidgets import *

class get_daily_data():
    def __init__(self):
        self.api = openapi.Openapi()
        self.run()

    def run(self):
        data = self.api.get_total_data('005930', '20210118')
        print(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    get_daily_data()