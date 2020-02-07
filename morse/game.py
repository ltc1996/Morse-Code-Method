from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

import re
import os
import sys
import configparser

from __init__ import __version__
from convert import *


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
        self.setting_filename = 'setting.ini'
        self.initsetting()
        self.main()

    def main(self):
        self.main_box = QWidget()
        logo_svg = QIcon(r'./res/Logo.svg')     # logo: ./res/Logo.svg
        self.main_box.setWindowIcon(logo_svg)
        # self.main_box.setFixedSize(630, 450)
        title = 'Translation Running Time {}'.format(__version__)
        self.main_box.setWindowTitle(title)
        self.main_grid = QVBoxLayout()

        self.top_text = QLineEdit()#QPlainTextEdit()
        # self.top_text.setTab
        self.top_text.setFont(QFont("Decorative", 30))
        # self.top_text.setFixedSize(600, 50)

        self.buttom_text = QTextEdit()#QLineEdit()#QPlainTextEdit()
        self.buttom_text.setFont(QFont("Decorative", 30))
        self.buttom_text.setTabStopWidth(1)
        # self.buttom_text.setTextColor(QColor(255, 80, 0, 160))
        # self.buttom_text.setTextBackgroundColor(QColor(0, 0, 0))
        # self.buttom_text.setFixedSize(600, 200)
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
        )

        # setting button
        self.setting_btn = QPushButton()
        icon_svg = QIcon('./res/Setting.svg')
        self.setting_btn.setIcon(icon_svg)
        self.setting_btn.setFixedSize(80, 50)
        self.setting_btn.clicked.connect(lambda: self.setting_dialog())

        self.copy = QPushButton('copy')
        self.copy_info = QLabel('')
        self.copy.setFixedSize(80, 50)
        self.copy.clicked.connect(lambda: self.copytoboard(self.buttom_text))
        self.copy_info.setAlignment(Qt.AlignRight)

        # lineEdit and textEdit
        self.main_grid.addWidget(self.top_text)
        self.main_grid.addWidget(self.buttom_text)

        # button h box
        self.button_h = QHBoxLayout()
        self.button_h.addWidget(self.setting_btn)
        self.button_h.addWidget(self.copy)
        self.button_h.addWidget(self.copy_info)

        self.main_grid.addLayout(self.button_h)

        self.main_box.setLayout(self.main_grid)
        # self.main_box.show()

    def showWhatYouWant(self, output_obj, input_obj, type):
        """
        type:
        0: morse -> alpha
        1: reversed
        """
        res = ''
        self.copy_info.setText('')
        if type == 0:
            string_from = output_obj.text()
            res = alpha_morse(string_from)
            print(res)
            input_obj.setText(res)
            input_obj.moveCursor(QTextCursor.End)
        if type == 1:
            string_from = output_obj.toPlainText()
            res = morse_alpha(string_from)
            print(res)
            input_obj.setText(res)

        # return

    def setting_dialog(self):
        print('setting')
        self.setting_d = QDialog(None, Qt.WindowCloseButtonHint)
        self.setting_d.setWindowTitle('Setting Options')
        self.setting_d.setFixedSize(400, 200)
        logo_svg = QIcon(r'./res/Logo.svg')  # logo: ./res/Logo.svg
        self.setting_d.setWindowIcon(logo_svg)
        self.setting_d.show()

        # assign your own bi-nary Morse code
        intro = QLabel('Some setting options will be there soon')
        color = QPushButton('Change Font')
        color.clicked.connect(lambda: self.changeColor_Dialog())
        this_di = ''
        this_da = ''

        file = QPushButton('Choose from file')
        file.clicked.connect(lambda: self.convertFile('1'))

        main_v = QVBoxLayout()
        main_v.addWidget(intro)
        main_v.addWidget(color)
        main_v.addWidget(file)
        main_v.addWidget(QLabel(''))
        main_v.addWidget(QLabel(''))

        self.setting_d.setLayout(main_v)

    def copytoboard(self, lineedit):
        clip = QApplication.clipboard()
        string = lineedit.toPlainText()
        # print(string)
        clip.setText(string)
        self.copy_info.setText('\nCopied to clipboard')
        self.copy_info.setFont(QFont("Decorative", 10))

    def changeColor_Dialog(self,):
        print('change color')
        color_d = QFontDialog(self.setting_d)
        logo_svg = QIcon(r'./res/Logo.svg')  # logo: ./res/Logo.svg
        color_d.setWindowIcon(logo_svg)
        color_d.setWindowTitle('Changing...')
        # color_d.open()
        (ok, font) = color_d.getFont()
        if ok:
            # print(font)
            self.top_text.setFont(font)
        else:
            print('cancel')

    def convertFile(self, mode):
        print('convert file in mode {}'.format(mode))
        file_name = self.chooseFile_Dialog()
        print(file_name)

    def chooseFile_Dialog(self):
        print('choose file')
        file_d = QFileDialog()
        logo_svg = QIcon(r'./res/Logo.svg')  # logo: ./res/Logo.svg
        file_d.setWindowIcon(logo_svg)
        file_d.setWindowTitle('Choosing...')
        file_d.setFileMode(QFileDialog.ExistingFile)        # choose from existing files
        file_d.setAcceptMode(QFileDialog.AcceptOpen)
        # if file_d.exec():
        file_name = file_d.getOpenFileName()
        return file_name

    def saveFile_Dialog(self, filename):
        print('Saving...')
        pass



    def save(self):
        try:
            self.config.write(open(self.setting_filename, 'w'))
            return True
        except:
            return False

    def setting(self, pro, value) -> None:
        if not isinstance(value, str):
            raise TypeError('wrong args')
        self.config.set('setting', pro, value)
        self.save()

    def initsetting(self):
        exist = os.path.exists(self.setting_filename)
        if not exist:
            with open(self.setting_filename, 'w') as f:
                print('init setting file..')

        self.config = configparser.ConfigParser()
        self.config.read(self.setting_filename)
        sections = self.config.sections()
        if 'setting' not in sections:
            print('setting')
            self.config.add_section('setting')
        self.config.write(open(self.setting_filename, 'w'))

    def readsetting(self, pro) -> bool:
        return self.config.get('setting', pro)

    def show(self):
        self.main_box.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    method_curr = Method()
    method_curr.show()
    # method_curr.setting('alpha', '123')
    # print(method_curr.readsetting('alpha'))
    sys.exit(app.exec_())

# pyinstaller -F game.py --noconsole
