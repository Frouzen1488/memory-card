from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget, QLabel, QPushButton,
    QRadioButton, QHBoxLayout, QVBoxLayout,
    QLineEdit
)

menu_window= QWidget()
menu_window.resize(400,400)

lb_quest= QLabel("Введіть запитання: ")
lb_answer= QLabel("Введіть вірну відповідь: ")
lb_wrong_ans1= QLabel("Введіть першу хибну відповідь: ")
lb_wrong_ans2= QLabel("Введіть другу хибну відповідь: ")
lb_wrong_ans3= QLabel("Введіть третю хибну відповідь: ")
lb_stats= QLabel("Статистика")

le_quest= QLineEdit()
le_answer= QLineEdit()
le_wrong_ans1= QLineEdit()
le_wrong_ans3= QLineEdit()
le_wrong_ans2= QLineEdit()

btn_add= QPushButton("Додати запитання")
btn_clear= QPushButton("Очистити")
btn_back= QPushButton("Назад")

h1_quest= QHBoxLayout()
h2_btn= QHBoxLayout()
v1= QVBoxLayout()
v2= QVBoxLayout()
main_v= QVBoxLayout()

v1.addWidget(lb_quest)
v1.addWidget(lb_answer)
v1.addWidget(lb_wrong_ans1)
v1.addWidget(lb_wrong_ans2)
v1.addWidget(lb_wrong_ans3)

v2.addWidget(le_quest)
v2.addWidget(le_answer)
v2.addWidget(le_wrong_ans1)
v2.addWidget(le_wrong_ans2)
v2.addWidget(le_wrong_ans3)

h1_quest.addLayout(v1)
h1_quest.addLayout(v2)

h2_btn.addWidget(btn_add)
h2_btn.addWidget(btn_clear)

main_v.addLayout(h1_quest)
main_v.addLayout(h2_btn)
main_v.addWidget(lb_stats)
main_v.addWidget(btn_back)
menu_window.setLayout(main_v)