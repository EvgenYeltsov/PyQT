import sys

from PyQt5.QtWidgets import QApplication

from app.view import ReminderView
from app.controller import RController
from app.model import RemModel


def main():
    app = QApplication(sys.argv)

    view = ReminderView()
    model = RemModel()
    RController(view=view, model=model)
    view.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
