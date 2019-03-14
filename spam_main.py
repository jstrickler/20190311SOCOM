#!/usr/bin/env python

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_spam import Ui_Spam


class spamMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_Spam()
        self.ui.setupUi(self)

        # Connect up menu actions
        # self.ui.actionExit.triggered.connect(self.close)

        # Connect up buttons.
        # self.ui.BUTTON_NAME.clicked.connect(self._pushed)

    def handle_push(self):
        pass

    def handle_dont(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = spamMain()
    main.show()
    sys.exit(app.exec_())


