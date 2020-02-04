from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

import re
import sys

from engine import di, da, morse2alpha, alpha2morse


class Game:
    def __init__(self):
        self.welcome()

    # @staticmethod
    def welcome(self):
        self.main_box = QWidget()
        print('this is welcome')
        self.main_box.setFixedSize(600, 600)
        self.main_box.setWindowTitle('摩尔斯电码小游戏')
        self.main_grid = QVBoxLayout()

        self.top = QHBoxLayout()
        # 计时器
        self.timer = QTimer()
        self.timer.setInterval(1000)

        # 题目
        self.quetion = QLabel()
        self.quetion.setFixedSize(400, 400)
        pic = QPixmap('res' + '\\tsl.jpg')
        self.quetion.setAlignment(Qt.AlignRight)  # 图片居中
        self.quetion.setPixmap(pic)

        # 倒计时
        self.num = QLCDNumber(2)
        self.num.setFixedSize(50, 100)
        self.num.setDigitCount(2)
        # self.num.display(self.updateTime())
        # self.num.connect(self.timer, SIGNAL('time'), self.updateTime)
        self.num.setSmallDecimalPoint(True)

        self.top.addWidget(self.quetion)
        self.top.addWidget(self.num)

        # 底部按钮
        self.buttom = QHBoxLayout()
        self.show_pic = QPushButton('打开速记图')
        self.start_game = QPushButton('开始游戏')
        self.ranks = QPushButton('排行榜')
        self.setting = QToolButton()

        self.show_pic.clicked.connect(self.show_picture)
        self.start_game.clicked.connect(self.start_new_game)

        self.buttom.addWidget(self.show_pic, )
        self.buttom.addWidget(self.start_game, )
        self.buttom.addWidget(self.setting, )

        self.main_grid.addLayout(self.top)
        self.main_grid.addLayout(self.buttom)

        self.main_box.setLayout(self.main_grid)
        # self.w.show()

    # def show(self):
    #     self.main_box.show()

    def show_picture(self):
        print('this is pic')
        picDialog = QDialog()
        # picDialog.setFixedSize(800, 900)
        picDialog.setWindowTitle('速记图')

        pic = QPixmap('res' + '\\morse.jpg')
        pic_label = QLabel()
        pic_label.setAlignment(Qt.AlignRight)     # 图片居中
        pic_label.setPixmap(pic)

        back_pic = QPushButton('关闭')            # 后退按钮
        back_pic.setFixedSize(50, 20)
        back_pic.clicked.connect(lambda x: picDialog.close())

        # 图片页组件
        pic_v = QVBoxLayout()
        pic_v.addWidget(pic_label)
        pic_v.addWidget(back_pic)

        picDialog.setLayout(pic_v)
        picDialog.show()

    @classmethod
    def start_new_game(self):
        print('this is a new game')

    def updateTime(self):
        curr_time = self.timer.remainingTime()

    def start1game(self):
        print('this a game')
        # self.timer.setInterval(1000)        # 计时器

    def show(self):
        self.main_box.show()


class Method:
    def __init__(self):
        # print('this is query')
        self.main()

    def main(self):
        self.main_box = QWidget()
        self.main_box.setFixedSize(630, 450)
        self.main_box.setWindowTitle('Translation Running Time')
        self.main_grid = QVBoxLayout()

        self.top_text = QLineEdit()#QPlainTextEdit()
        self.top_text.setFont(QFont("Decorative", 30))
        self.top_text.setFixedSize(600, 50)

        self.buttom_text = QTextEdit()#QLineEdit()#QPlainTextEdit()
        self.buttom_text.setFont(QFont("Decorative", 30))
        self.buttom_text.setFixedSize(600, 200)
        # self.buttom_text.setReadOnly(True)
        # self.buttom_text.moveCursor(QTextCursor.End)
        self.top_text.textEdited.connect(
            # self.buttom_text,
            lambda: self.showWhatYouWant(self.top_text, self.buttom_text, 0)
            # lambda: self.buttom_text.setText(self.top_text.text())
            # self.buttom_text.setPlainText(self.top_text.getPaintContext())
            # self.showWhatYouWant(self.top_text, self.buttom_text, 1)
        )

        self.buttom_text.cursorPositionChanged.connect(
            lambda: self.showWhatYouWant(self.buttom_text, self.top_text, 1)
        #     # lambda: self.top_text.setText(self.buttom_text.text())
        )
        # self.buttom_text.connect()
        # if self.top_text.textChanged():
        #     print('changes')
        self.copy = QPushButton('copy')
        self.copy_info = QLabel('')
        self.copy.setFixedSize(80, 50)
        self.copy.clicked.connect(lambda: self.copytoboard(self.buttom_text))

        self.copy_info.setAlignment(Qt.AlignRight)

        self.main_grid.addWidget(self.top_text)
        self.main_grid.addWidget(self.buttom_text)
        self.main_grid.addWidget(self.copy)
        self.main_grid.addWidget(self.copy_info)

        self.main_box.setLayout(self.main_grid)
        # self.main_box.show()

    def showWhatYouWant(self, output_obj, input_obj, type):
        """
        type:
        0: morse -> alpha
        1: alpha -> morse
        """
        res = ''
        self.copy_info.setText('')
        if type == 0:
            string_from = output_obj.text()
            # print(string_from)
            p = re.findall(r'\S+|\s', string_from)
            # print(p)
            for word in p:
                # print(word)
                if word[0] == ' ':
                    res += '/'
                    continue
                for char in word:
                    if char.isalpha():
                        try:
                            res += alpha2morse[char.upper()]
                        except KeyError:
                            res += '?'
                    else:
                        res += '?'
                    res += ' '
            print(res)
            input_obj.setText(res)
            input_obj.moveCursor(QTextCursor.End)
        if type == 1:
            string_from = output_obj.toPlainText()
            regex = '([{}|{}]+|/+)'.format(di, da)
            p = re.findall(regex, string_from)
            # print(p)
            down = False
            for tmp in p:
                if tmp == '/':
                    res += ' '
                    down = False
                    continue
                char = morse2alpha.search(tmp)
                if char:
                    if down:
                        char = char.lower()
                    res += char
                    down = True
                else:
                    res += '?'
            print(res)
            input_obj.setText(res)

    def copytoboard(self, lineedit):
        clip = QApplication.clipboard()
        string = lineedit.toPlainText()
        # print(string)
        clip.setText(string)
        self.copy_info.setText('done')

    def show(self):
        self.main_box.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    method_curr = Method()
    method_curr.show()
    sys.exit(app.exec_())

# pyinstaller -F game.py --noconsole
