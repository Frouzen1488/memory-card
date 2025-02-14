from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget, QLabel, QPushButton,
    QRadioButton, QHBoxLayout, QVBoxLayout,
    QGroupBox, QButtonGroup, QSpinBox
)
window = QWidget()
window.setWindowTitle('Memory card')
window.resize(600, 500)

btn_menu = QPushButton('Меню')
btn_rest = QPushButton('Відпочити')
btn_next = QPushButton('Відповісти')
sp_rest = QSpinBox()
sp_rest.setValue(30)

lb_question = QLabel('Запитання')
lb_rest = QLabel('хвилин')
lb_result = QLabel('Правильно')
lb_right_answer = QLabel('текст правильної відповіді')

rb_ans1 = QRadioButton('перший варіант')
rb_ans2 = QRadioButton('другий варіант')
rb_ans3 = QRadioButton('третій варіант')
rb_ans4 = QRadioButton('четвертий варіант')
RadioGroup = QButtonGroup()
RadioGroup.addButton(rb_ans1)
RadioGroup.addButton(rb_ans2)
RadioGroup.addButton(rb_ans3)
RadioGroup.addButton(rb_ans4)

gb_question = QGroupBox('Варіанти відповідей')
rb_h1 = QHBoxLayout()
rb_v1 = QVBoxLayout()
rb_v2 = QVBoxLayout()
rb_v1.addWidget(rb_ans1)
rb_v1.addWidget(rb_ans2)
rb_v2.addWidget(rb_ans3)
rb_v2.addWidget(rb_ans4)
rb_h1.addLayout(rb_v1)
rb_h1.addLayout(rb_v2)
gb_question.setLayout(rb_h1)

gb_answer = QGroupBox('Результат відповіді')
v1 = QVBoxLayout()
v1.addWidget(lb_result)
v1.addWidget(lb_right_answer)
gb_answer.setLayout(v1)

v1_main = QVBoxLayout()
h1_main = QHBoxLayout()
h2_main = QHBoxLayout()
h3_main = QHBoxLayout()
h4_main = QHBoxLayout()

h1_main.addWidget(btn_menu)
h1_main.addStretch(1)
h1_main.addWidget(btn_rest)
h1_main.addWidget(sp_rest)
h1_main.addWidget(lb_rest)

h2_main.addWidget(lb_question, alignment=Qt.AlignmentFlag.AlignHCenter)

h3_main.addWidget(gb_answer)
h3_main.addWidget(gb_question)
gb_answer.hide()

h4_main.addStretch(1)
h4_main.addWidget(btn_next, stretch=2)
h4_main.addStretch(1)

v1_main.addLayout(h1_main, stretch=1)
v1_main.addLayout(h2_main, stretch=2)
v1_main.addLayout(h3_main, stretch=7)
v1_main.addLayout(h4_main)
v1_main.setSpacing(10)
window.setLayout(v1_main)
window.show()