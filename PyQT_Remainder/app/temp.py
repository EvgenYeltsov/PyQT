from PyQt5.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget, QScrollArea


app = QApplication([])

layout = QGridLayout()
for i in range(10):
    for j in range(5):
        button = QPushButton(f'{i}x{j}')
        layout.addWidget(button, i, j)

w = QWidget()
w.setLayout(layout)

mw = QScrollArea()
mw.setWidget(w)
mw.resize(200, 200)
mw.show()

app.exec()

