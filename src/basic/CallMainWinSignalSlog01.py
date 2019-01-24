# !user/bin/env python
# -*- coding:utf-8 -*-
"""
@author: Jeremy
@file: CallMainWinSignalSlog01.py.py
@time: 2019/01/24
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWinSignalSlog01 import Ui_Form

class MyMainWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywin = MyMainWindow()
    mywin.show()
    sys.exit(app.exec_())

