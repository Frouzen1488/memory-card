from PyQt6.QtWidgets import QApplication
from random import choice, shuffle
from time import sleep

app = QApplication([])
from main_window import *
from menu_window import *


class Question():
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.count_asked = 0
        self.count_right = 0

    def got_right(self):
        self.count_asked += 1
        self.count_right += 1

    def got_wrong(self):
        self.count_asked += 1


q1 = Question('Яблуко', 'apple', 'application', 'apply', 'answer')
q2 = Question('Двері', 'door', 'down', 'doom', 'dragon')
q3 = Question('Пайтон', 'python', 'piton', 'payton', 'pyiton')
q4 = Question('Машина', 'car', 'cur', 'bad', 'physics')
q5 = Question('Ліжко', 'bad', 'room', 'PK', 'tree')

questions = [q1, q2, q3, q4, q5]
radio_buttons = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]

cur_q = ''

def new_question():
    global cur_q
    cur_q = choice(questions)
    lb_question.setText(cur_q.question)
    lb_right_answer.setText(cur_q.answer)
    shuffle(radio_buttons)
    radio_buttons[0].setText(cur_q.answer)
    radio_buttons[1].setText(cur_q.wrong_answer1)
    radio_buttons[2].setText(cur_q.wrong_answer2)
    radio_buttons[3].setText(cur_q.wrong_answer3)


new_question()


def check_result():
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text() == lb_right_answer.text():
                lb_result.setText('Правильно')
                cur_q.got_right()
            else:
                lb_result.setText('Неправильно')
                cur_q.got_wrong()
            break

def clear():
    le_quest.clear()
    le_answer.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()

def add_question():
    new_q = Question(le_quest.text(), le_answer.text(), le_wrong_ans1.text(), le_wrong_ans2.text(), le_wrong_ans3.text())
    questions.append(new_q)
    clear()

def change_screen():
    if btn_next.text() == 'Відповісти':
        check_result()
        gb_question.hide()
        gb_answer.show()
        btn_next.setText('Наступне запитання')
    else:
        new_question()
        gb_answer.hide()
        gb_question.show()
        btn_next.setText('Відповісти')


def rest():
    window.hide()
    n = sp_rest.value() * 60
    sleep(n)
    window.show()


def menu():
    window.hide()
    lb_stats.setText(f'Статистика\nВсього відповіли:{cur_q.count_asked}\nПравильних відповідей: {cur_q.count_right}')
    menu_window.show()

def menu_back():
    menu_window.hide()
    window.show()

btn_clear.clicked.connect(clear)
btn_add.clicked.connect(add_question)
btn_back.clicked.connect(menu_back)
btn_rest.clicked.connect(rest)
btn_next.clicked.connect(change_screen)
btn_menu.clicked.connect(menu)

app.exec()
