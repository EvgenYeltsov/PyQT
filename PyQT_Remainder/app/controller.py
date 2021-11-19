from functools import partial
from PyQt5 import QtCore

class RController:

    def __init__(self, view, model):
        self._view = view
        self._model = model

        self._add_new_task()

    def _add_new_task(self):
        print('ad')
        self._model.add_task()
        self._view.button1.clicked.connect(partial(self.show_task))
        self._view.button2.clicked.connect(partial(self._clear_task))
        self._view.button4.clicked.connect(partial(self._clear_all_tasks))



    def _clear_all_tasks(self):
        for i in reversed(range(self._view.task_area.count())):
            self._view.task_area.itemAt(i).widget().setParent(None)
        self._view.task_.setText("Good JoB")


    def _clear_task(self):
        for value in self._view.my_dict.values():
            if value.isChecked() ==True:
                value.setText("DONE")
                value.blockSignals(False)



    def show_task(self):
        if self._view.task_.text() == '':
            self._view.button1.blockSignals(False)
        else:
            self._view.new_editline()
            with open('reminder.txt', 'a') as file:
                textin = self._view.task_.text()
                file.write(f"task # {textin} + '\n'")
            self._view.task_.setText('')

