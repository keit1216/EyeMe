# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\python\Nov4.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import time, pyodbc
from playsound import playsound
from gtts import gTTS
from pygame import mixer
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def getValue(self, btn):
        try:
            btn.clicked.disconnect()
        except:
            pass
        listA = [['', '', '', '', '', '', ''],
                 ['', 'ㄅ', 'ㄆ', 'ㄇ', 'ㄈ', 'ㄉ', 'ㄊ'],
                 ['', 'ㄋ', 'ㄌ', 'ㄍ', 'ㄎ', 'ㄏ', 'ㄐ'],
                 ['', 'ㄑ', 'ㄒ', 'ㄓ', 'ㄔ', 'ㄕ', 'ㄖ'],
                 ['', 'ㄗ', 'ㄘ', 'ㄙ', 'ㄧ', 'ㄨ', 'ㄩ'],
                 ['', 'ㄚ', 'ㄛ', 'ㄜ', 'ㄝ', 'ㄞ', 'ㄟ'],
                 ['', 'ㄠ', 'ㄡ', 'ㄢ', 'ㄣ', 'ㄤ', 'ㄥ']]

        if self.label_left.text() != 'ㄦ':
            a = int(self.label_left.text())
            b = int(self.label_middle.text())

        if self.label_single2.text() == '進入單音視窗' and self.label_left.text() == 'ㄦ':
            ''' 按下ㄦ後'''
            self.label_up2_2.setText('ㄦ')

            self.pushButton_one_2.show()
            self.pushButton_two_2.show()
            self.pushButton_three_2.show()
            self.pushButton_four_2.show()
            self.pushButton_five_2.show()
            self.pushButton_sure_5.show()
            self.label_choose_sound.show()
            self.label_choose1.hide()
            self.label_choose2.hide()

            self.frame.hide()
            self.frame_3.show()
            self.pushButton_sure_5.hide()
            self.pushButton_cancel_7.hide()

            self.openOne()

        elif self.label_single2.text() == '進入單音視窗':

            self.label_up2_2.setText(listA[a][b])

            self.pushButton_one_2.show()
            self.pushButton_two_2.show()
            self.pushButton_three_2.show()
            self.pushButton_four_2.show()
            self.pushButton_five_2.show()
            self.pushButton_sure_5.show()
            self.label_choose_sound.show()
            self.label_choose1.hide()
            self.label_choose2.hide()

            self.frame.hide()
            self.frame_3.show()
            self.pushButton_sure_5.hide()
            self.pushButton_cancel_7.hide()

            self.check()

        elif self.label_single2.text() == '進入雙音視窗' and self.label_right.text() == '':

            self.label_right.setText(listA[a][b])
            self.label_up_2.setText(listA[a][b])

            self.label_left.setText('')
            self.label_middle.setText('')

            self.label_double_1.hide()
            self.label_triple_2.show()

            self.pushButton_4.show()
            self.pushButton_5.show()
            self.pushButton_6.show()
            self.label_choose2.hide()
            self.label_choose1.show()

            self.pushButton_sure.hide()
            self.pushButton_cancel.hide()  # insert

            self.openTwo()

        elif self.label_single2.text() == '進入雙音視窗' and self.label_right.text() != '':

            self.label_up2_2.setText(listA[a][b])

            self.pushButton_one_2.show()
            self.pushButton_two_2.show()
            self.pushButton_three_2.show()
            self.pushButton_four_2.show()
            self.pushButton_five_2.show()
            self.pushButton_sure_5.show()
            self.label_choose_sound.show()
            self.label_choose1.hide()
            self.label_choose2.hide()
            self.frame.hide()
            self.frame_3.show()
            self.pushButton_sure_5.hide()
            self.pushButton_cancel_7.hide()
            self.check()

            self.openTwo()


        elif self.label_single2.text() == '進入三音視窗' and self.label_right.text() == '':

            self.label_right.setText(listA[a][b])
            self.label_up_2.setText(listA[a][b])

            self.label_left.setText('')
            self.label_middle.setText('')

            self.pushButton_1.hide()
            self.pushButton_2.hide()
            self.pushButton_3.hide()
            self.pushButton_5.hide()
            self.pushButton_6.hide()

            self.pushButton_4.show()

            self.pushButton_sure.hide()
            self.pushButton_cancel.hide()

            self.label_triple_1.hide()
            self.label_triple_2.show()
            self.label_choose2.hide()
            self.label_choose1.show()

            self.openThree()



        elif self.label_single2.text() == '進入三音視窗' and self.label_right_2.text() == '':

            self.label_right_2.setText(listA[a][b])
            self.label_up2_2.setText(listA[a][b])

            self.pushButton_1.hide()
            self.pushButton_2.hide()
            self.pushButton_3.hide()
            self.pushButton_4.hide()

            self.pushButton_5.show()
            self.pushButton_6.show()

            self.pushButton_sure.hide()
            self.pushButton_cancel.hide()
            self.label_choose2.hide()
            self.label_choose1.show()
            self.label_left.setText('')
            self.label_middle.setText('')
            self.openThree()


        elif self.label_single2.text() == '進入三音視窗' and self.label_right_2.text() != '':

            self.label_up3_2.setText(listA[a][b])

            self.pushButton_one_2.show()
            self.pushButton_two_2.show()
            self.pushButton_three_2.show()
            self.pushButton_four_2.show()
            self.pushButton_five_2.show()
            self.pushButton_sure_5.show()
            self.label_choose_sound.show()
            self.label_choose1.hide()
            self.label_choose2.hide()

            self.frame.hide()
            self.frame_3.show()
            self.pushButton_sure_5.hide()
            self.pushButton_cancel_7.hide()
            self.openThree()
            self.check()

    def warning(self):
        msgBox = QMessageBox(QMessageBox.NoIcon, '警告', '輸入錯誤請重新選擇!')
        msgBox.exec()

    def check(self):

        server = 'DESKTOP-9G62UKP'
        database = 'master'
        username = 'sa'
        password = '123'
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = cnxn.cursor()
        row = []
        ConvertedRow = []
        if self.label_single2.text() == '進入單音視窗':
            VoiceOne = self.label_up2_2.text()
            cursor.execute("select singlewordid from singleword where singlewordname='" + VoiceOne + "'")
            ChineseWordData = cursor.fetchone()
            row = list(ChineseWordData)
            ConvertedRow.append(row[0].rstrip())
            x = 0
            try:
                Voice = ConvertedRow[0] + '00001'
                mixer.init()
                mixer.music.load('D:\\music\\' + Voice + '.mp3')
            except:
                x = x + 1
            try:
                Voice = ConvertedRow[0] + '00002'
                mixer.init()
                mixer.music.load('D:\\music\\' + Voice + '.mp3')
            except:
                x = x + 1
            try:
                Voice = ConvertedRow[0] + '00003'
                mixer.init()
                mixer.music.load('D:\\music\\' + Voice + '.mp3')
            except:
                x = x + 1
            try:
                Voice = ConvertedRow[0] + '00004'
                mixer.init()
                mixer.music.load('D:\\music\\' + Voice + '.mp3')
            except:
                x = x + 1
            try:
                Voice = ConvertedRow[0] + '00000'
                mixer.init()
                mixer.music.load('D:\\music\\' + Voice + '.mp3')
            except:
                x = x + 1
            if x == 5:
                self.warning()
                self.keep()
                self.openOneUi()

        elif self.label_single2.text() == '進入雙音視窗':
            VoiceTwo = [self.label_up_2.text(), self.label_up2_2.text()]
            for cont in range(0, 2):
                cursor.execute("select singlewordid from singleword where singlewordname='" + VoiceTwo[cont] + "'")
                ChineseWordData = cursor.fetchone()
                row = list(ChineseWordData)
                ConvertedRow.append(row[0].rstrip())
            x = 0
            try:
                Voice = ConvertedRow[0] + ConvertedRow[1] + '001'
                mixer.init()
                mixer.music.load('D:\\music\\' + Voice + '.mp3')
            except:
                x = x + 1
            try:
                Voice = ConvertedRow[0] + ConvertedRow[1] + '002'
                mixer.init()
                mixer.music.load('D:\\music\\' + Voice + '.mp3')
            except:
                x = x + 1
            try:
                Voice = ConvertedRow[0] + ConvertedRow[1] + '003'
                mixer.init()
                mixer.music.load('D:\\music\\' + Voice + '.mp3')
            except:
                x = x + 1
            try:
                Voice = ConvertedRow[0] + ConvertedRow[1] + '004'
                mixer.init()
                mixer.music.load('D:\\music\\' + Voice + '.mp3')
            except:
                x = x + 1
            try:
                Voice = ConvertedRow[0] + ConvertedRow[1] + '000'
                mixer.init()
                mixer.music.load('D:\\music\\' + Voice + '.mp3')
            except:
                x = x + 1
            if x == 5:
                self.warning()
                self.keep()
                self.openTwoUi()
        elif self.label_single2.text() == '進入三音視窗':
            VoiceThree = [self.label_up_2.text(), self.label_up2_2.text(), self.label_up3_2.text()]
            for cont in range(0, 3):
                cursor.execute("select singlewordid from singleword where singlewordname='" + VoiceThree[cont] + "'")
                ChineseWordData = cursor.fetchone()
                row = list(ChineseWordData)
                ConvertedRow.append(row[0].rstrip())
            x = 0
            try:
                Voice = ConvertedRow[0] + ConvertedRow[1] + ConvertedRow[2] + '1'
                mixer.init()
                mixer.music.load('D:\\music\\' + Voice + '.mp3')
            except:
                x = x + 1
            try:
                Voice = ConvertedRow[0] + ConvertedRow[1] + ConvertedRow[2] + '2'
                mixer.init()
                mixer.music.load('D:\\music\\' + Voice + '.mp3')
            except:
                x = x + 1
            try:
                Voice = ConvertedRow[0] + ConvertedRow[1] + ConvertedRow[2] + '3'
                mixer.init()
                mixer.music.load('D:\\music\\' + Voice + '.mp3')
            except:
                x = x + 1
            try:
                Voice = ConvertedRow[0] + ConvertedRow[1] + ConvertedRow[2] + '4'
                mixer.init()
                mixer.music.load('D:\\music\\' + Voice + '.mp3')
            except:
                x = x + 1
            try:
                Voice = ConvertedRow[0] + ConvertedRow[1] + ConvertedRow[2] + '0'
                mixer.init()
                mixer.music.load('D:\\music\\' + Voice + '.mp3')
            except:
                x = x + 1
            if x == 5:
                self.warning()
                self.keep()
                self.openThreeUi()

    def voice(self, btn):
        import pyodbc

        try:
            btn.clicked.disconnect()
        except:
            pass
        self.pushButton_one_2.hide()
        self.pushButton_two_2.hide()
        self.pushButton_three_2.hide()
        self.pushButton_four_2.hide()
        self.pushButton_five_2.hide()
        self.pushButton_sure_5.hide()
        self.pushButton_cancel_7.hide()

        self.frame_4.show()
        self.label_choose_end.show()
        self.label_choose_sound.hide()
        self.label_choose2.hide()

        # connect資料庫
        server = 'DESKTOP-9G62UKP'
        database = 'master'
        username = 'sa'
        password = '123'
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = cnxn.cursor()
        row = []
        ConvertedRow = []

        TextOne = self.label_up_2.text()
        TextTwo = self.label_up2_2.text()
        TextThree = self.label_up3_2.text()
        TextFour = self.label_sound_2.text()

        if btn.text() == '確認':
            if TextOne == '' and TextThree == '':

                cont = 0
                VoiceOne = [TextTwo, TextFour]
                for cont in range(0, 2):
                    cursor.execute("select singlewordid from singleword where singlewordname='" + VoiceOne[cont] + "'")
                    ChineseWordData = cursor.fetchone()
                    row = list(ChineseWordData)
                    ConvertedRow.append(row[0].rstrip())

                Voice = ConvertedRow[0] + '0000' + ConvertedRow[1]
                '''
                if self.label_x.text() == '':
                    self.label_x.setText(Voice )
                elif self.label_x.text() != '':
                    self.label_x.setText(self.label_x.text() +','+ Voice)
                '''

            elif TextThree == '':
                cont = 0
                VoiceTwo = [TextOne, TextTwo, TextFour]
                for cont in range(0, 3):
                    cursor.execute("select singlewordid from singleword where singlewordname='" + VoiceTwo[cont] + "'")
                    ChineseWordData = cursor.fetchone()
                    row = list(ChineseWordData)
                    ConvertedRow.append(row[0].rstrip())

                Voice = ConvertedRow[0] + ConvertedRow[1] + '00' + ConvertedRow[2]
                '''
                if self.label_x.text() == '':
                    self.label_x.setText(Voice)
                elif self.label_x.text() != '':
                    self.label_x.setText(self.label_x.text() +','+ Voice)
                '''
            elif TextOne != '' and TextTwo != '' and TextThree != '' and TextFour != '':
                cont = 0
                VoiceThree = [TextOne, TextTwo, TextThree, TextFour]
                for cont in range(0, 4):
                    cursor.execute(
                        "select singlewordid from singleword where singlewordname='" + VoiceThree[cont] + "'")
                    ChineseWordData = cursor.fetchone()
                    row = list(ChineseWordData)
                    ConvertedRow.append(row[0].rstrip())
                Voice = ConvertedRow[0] + ConvertedRow[1] + ConvertedRow[2] + ConvertedRow[3]
                '''
                if self.label_x.text() == '':
                    self.label_x.setText(Voice )
                elif self.label_x.text() != '':
                    self.label_x.setText(self.label_x.text() +','+ Voice)
                '''

            try:
                playsound('D:\\music\\' + Voice + '.mp3')
                if self.label_x.text() == '':
                    self.label_x.setText(Voice)
                elif self.label_x.text() != '':
                    self.label_x.setText(self.label_x.text() + ',' + Voice)
            except Exception:
                self.warning()
                if self.label_single2.text() == '進入單音視窗':
                    self.frame_3.show()
                    self.label_choose_sound.hide()
                    self.label_choose_end.hide()
                    self.frame_4.hide()
                    self.cancel7()
                    self.openOne()
                elif self.label_single2.text() == '進入雙音視窗':
                    self.frame_3.show()
                    self.label_choose_end.hide()
                    self.frame_4.hide()
                    self.cancel7()
                    self.openTwo()
                elif self.label_single2.text() == '進入三音視窗':
                    self.frame_3.show()
                    self.label_choose_end.hide()
                    self.frame_4.hide()
                    self.cancel7()
                    self.openThree()

        elif btn.text() == '重播':
            VoiceArr = self.label_x.text()
            VoiceArray = []
            VoiceArray = VoiceArr.split(",")
            a = 0
            for a in range(0, len(VoiceArray)):
                mixer.init()
                mixer.music.load('D:\\music\\' + VoiceArray[a] + '.mp3')
                mixer.music.play()
                time.sleep(0.6)
                print(VoiceArray[a])
                print(VoiceArray)
        elif btn.text() == '整句播放':
            VoiceArr = self.label_x.text()
            VoiceArray = []
            VoiceArray = VoiceArr.split(",")
            a = 0
            for a in range(0, len(VoiceArray)):
                mixer.init()
                mixer.music.load('D:\\music\\' + VoiceArray[a] + '.mp3')
                mixer.music.play()
                time.sleep(0.6)
                print(VoiceArray[a])
                print(VoiceArray)
            self.label_x.setText('')
        self.pushButton_replay.clicked.connect(lambda: self.voice(self.pushButton_replay))

    def cancel7(self):
        self.label_sound_2.setText('')
        self.pushButton_one_2.show()
        self.pushButton_two_2.show()
        self.pushButton_three_2.show()
        self.pushButton_four_2.show()
        self.pushButton_five_2.show()
        self.label_choose_sound.show()
        self.label_choose2.hide()

        self.pushButton_sure_5.hide()
        self.pushButton_cancel_7.hide()

    def cancel(self):
        self.label_left.setText('')
        self.label_middle.setText('')

        self.pushButton_sure.hide()
        self.pushButton_cancel.hide()
        self.label_choose1.show()
        self.label_choose2.hide()

        if self.label_single2.text() == '進入單音視窗' and self.label_left.text() == 'ㄦ':
            self.pushButton_3.show()
            self.pushButton_4.show()
            self.pushButton_5.show()
            self.pushButton_6.show()
            self.pushButton_37.show()



        elif self.label_single2.text() == '進入單音視窗':
            self.pushButton_3.show()
            self.pushButton_4.show()
            self.pushButton_5.show()
            self.pushButton_6.show()
            self.pushButton_37.show()


        elif self.label_single2.text() == '進入雙音視窗' and self.label_right.text() == '':
            self.pushButton_1.show()
            self.pushButton_2.show()
            self.pushButton_3.show()
            self.pushButton_4.show()
            self.pushButton_5.hide()
            self.pushButton_6.hide()

        elif self.label_single2.text() == '進入雙音視窗' and self.label_right.text() != '':
            self.pushButton_1.hide()
            self.pushButton_2.hide()
            self.pushButton_3.hide()
            self.pushButton_4.show()
            self.pushButton_5.show()
            self.pushButton_6.show()

        elif self.label_single2.text() == '進入三音視窗' and self.label_right.text() == '':
            self.pushButton_1.show()
            self.pushButton_2.show()
            self.pushButton_3.show()
            self.pushButton_4.show()
            self.pushButton_5.hide()
            self.pushButton_6.hide()

        elif self.label_single2.text() == '進入三音視窗' and self.label_right_2.text() == '':
            self.pushButton_4.show()
            self.pushButton_5.hide()
            self.pushButton_6.hide()

        elif self.label_single2.text() == '進入三音視窗' and self.label_right_2.text() != '':
            self.pushButton_5.show()
            self.pushButton_6.show()
            self.pushButton_1.hide()
            self.pushButton_2.hide()
            self.pushButton_3.hide()
            self.pushButton_4.hide()

    def keep(self):
        try:
            self.pushButton_keep.clicked.disconnect()
        except:
            pass

        self.frame_2.show()
        self.frame_3.hide()
        self.frame_4.hide()
        self.label_choose_end.hide()
        self.label_choose_sound.hide()

        self.label_single.hide()
        self.label_double_1.hide()
        self.label_double_2.hide()
        self.label_triple_1.hide()
        self.label_triple_2.hide()

        self.label_left.setText('')
        self.label_middle.setText('')
        self.label_up2_2.setText('')
        self.label_sound_2.setText('')
        self.label_single2.setText('')

        self.pushButton_1.show()
        self.pushButton_2.show()
        self.pushButton_3.show()
        self.pushButton_4.show()
        self.pushButton_5.show()
        self.pushButton_6.show()
        self.pushButton_37.show()

    def one(self):
        self.label_sound_2.setText('一聲')
        self.pushButton_one_2.hide()
        self.pushButton_two_2.hide()
        self.pushButton_three_2.hide()
        self.pushButton_four_2.hide()
        self.pushButton_five_2.hide()
        self.label_choose_sound.hide()
        self.label_choose2.show()

    def two(self):
        self.label_sound_2.setText('二聲')
        self.pushButton_one_2.hide()
        self.pushButton_two_2.hide()
        self.pushButton_three_2.hide()
        self.pushButton_four_2.hide()
        self.pushButton_five_2.hide()
        self.label_choose_sound.hide()
        self.label_choose2.show()

    def three(self):
        self.label_sound_2.setText('三聲')
        self.pushButton_one_2.hide()
        self.pushButton_two_2.hide()
        self.pushButton_three_2.hide()
        self.pushButton_four_2.hide()
        self.pushButton_five_2.hide()
        self.label_choose_sound.hide()
        self.label_choose2.show()

    def four(self):
        self.label_sound_2.setText('四聲')
        self.pushButton_one_2.hide()
        self.pushButton_two_2.hide()
        self.pushButton_three_2.hide()
        self.pushButton_four_2.hide()
        self.pushButton_five_2.hide()
        self.label_choose_sound.hide()
        self.label_choose2.show()

    def five(self):
        self.label_sound_2.setText('輕聲')
        self.pushButton_one_2.hide()
        self.pushButton_two_2.hide()
        self.pushButton_three_2.hide()
        self.pushButton_four_2.hide()
        self.pushButton_five_2.hide()
        self.label_choose_sound.hide()
        self.label_choose2.show()

    def OneTextSet(self, btn):
        try:
            btn.clicked.disconnect()
        except:
            pass
        print(btn.text())
        x = btn.text()

        if self.label_single2.text() == '進入單音視窗':

            self.pushButton_1.show()
            self.pushButton_2.show()

            if self.label_left.text() == '':
                self.label_left.setText(x)

            elif self.label_left.text() != '':
                self.label_middle.setText(x)
                self.pushButton_sure.show()
                self.pushButton_cancel.show()
                self.pushButton_1.hide()
                self.pushButton_2.hide()
                self.pushButton_3.hide()
                self.pushButton_4.hide()
                self.pushButton_5.hide()
                self.pushButton_6.hide()
                self.pushButton_37.hide()
                self.label_choose1.hide()
                self.label_choose2.show()

            if self.label_left.text() == 'ㄦ':
                self.label_middle.setText(x)
                self.pushButton_sure.show()
                self.pushButton_cancel.show()
                self.pushButton_1.hide()
                self.pushButton_2.hide()
                self.pushButton_3.hide()
                self.pushButton_4.hide()
                self.pushButton_5.hide()
                self.pushButton_6.hide()
                self.pushButton_37.hide()
                self.label_choose1.hide()
                self.label_choose2.show()

            self.openOne()

        elif self.label_single2.text() == '進入雙音視窗':

            self.pushButton_1.show()
            self.pushButton_2.show()
            self.pushButton_3.show()
            self.pushButton_5.show()
            self.pushButton_6.show()

            if self.label_left.text() == '':
                self.label_left.setText(x)


            elif self.label_left.text() != '':
                self.label_middle.setText(x)
                self.label_choose2.show()
                self.label_choose1.hide()
                self.pushButton_sure.show()
                self.pushButton_cancel.show()
                self.pushButton_1.hide()
                self.pushButton_2.hide()
                self.pushButton_3.hide()
                self.pushButton_4.hide()
                self.pushButton_5.hide()
                self.pushButton_6.hide()

            self.openTwo()

        elif self.label_single2.text() == '進入三音視窗':

            self.pushButton_5.show()
            self.pushButton_6.show()

            if self.label_left.text() == '' and self.label_right_2.text() != '':
                self.label_left.setText(x)
                self.pushButton_1.show()
                self.pushButton_2.show()
                self.pushButton_3.show()
                self.pushButton_4.show()


            elif self.label_left.text() == '':
                self.label_left.setText(x)

            elif self.label_left.text() != '' and self.label_middle.text() == '':
                self.label_middle.setText(x)
                self.label_choose2.show()
                self.label_choose1.hide()
                self.pushButton_sure.show()
                self.pushButton_cancel.show()
                self.pushButton_1.hide()
                self.pushButton_2.hide()
                self.pushButton_3.hide()
                self.pushButton_4.hide()
                self.pushButton_5.hide()
                self.pushButton_6.hide()



            elif self.label_middle.text() != '' and self.label_right_2.text() != '':
                self.pushButton_1.hide()
                self.pushButton_2.hide()
                self.pushButton_3.hide()
                self.pushButton_4.hide()
                self.label_choose2.show()

            self.openThree()

    # button connect相關
    def openOne(self):
        MainWindow.setStyleSheet("#MainWindow{background-image:url(D:/secondPIC.png);}")  # 修改
        self.pushButton_1.clicked.connect(lambda: self.OneTextSet(self.pushButton_1))
        self.pushButton_2.clicked.connect(lambda: self.OneTextSet(self.pushButton_2))
        self.pushButton_3.clicked.connect(lambda: self.OneTextSet(self.pushButton_3))
        self.pushButton_4.clicked.connect(lambda: self.OneTextSet(self.pushButton_4))
        self.pushButton_5.clicked.connect(lambda: self.OneTextSet(self.pushButton_5))
        self.pushButton_6.clicked.connect(lambda: self.OneTextSet(self.pushButton_6))
        self.pushButton_37.clicked.connect(lambda: self.OneTextSet(self.pushButton_37))
        self.pushButton_sure.clicked.connect(lambda: self.getValue(self.pushButton_sure))
        self.pushButton_replay.clicked.connect(lambda: self.voice(self.pushButton_replay))
        self.pushButton_allplay.clicked.connect(lambda: self.voice(self.pushButton_allplay))
        self.pushButton_one_2.clicked.connect(self.one)
        self.pushButton_two_2.clicked.connect(self.two)
        self.pushButton_three_2.clicked.connect(self.three)
        self.pushButton_four_2.clicked.connect(self.four)
        self.pushButton_five_2.clicked.connect(self.five)

        self.pushButton_one_2.clicked.connect(self.pushButton_sure_5.show)
        self.pushButton_two_2.clicked.connect(self.pushButton_sure_5.show)
        self.pushButton_three_2.clicked.connect(self.pushButton_sure_5.show)
        self.pushButton_four_2.clicked.connect(self.pushButton_sure_5.show)
        self.pushButton_five_2.clicked.connect(self.pushButton_sure_5.show)

        self.pushButton_one_2.clicked.connect(self.pushButton_cancel_7.show)
        self.pushButton_two_2.clicked.connect(self.pushButton_cancel_7.show)
        self.pushButton_three_2.clicked.connect(self.pushButton_cancel_7.show)
        self.pushButton_four_2.clicked.connect(self.pushButton_cancel_7.show)
        self.pushButton_five_2.clicked.connect(self.pushButton_cancel_7.show)

        self.pushButton_sure_5.clicked.connect(lambda: self.voice(self.pushButton_sure_5))
        self.pushButton_cancel_7.clicked.connect(self.cancel7)
        self.pushButton_keep.clicked.connect(self.keep)
        self.pushButton_cancel.clicked.connect(self.cancel)

    # hide show enable相關
    def openOneUi(self):
        self.label_gender2.hide()
        self.pushButton_sure.hide()
        self.pushButton_cancel.hide()
        self.pushButton_37.show()
        self.frame_2.hide()
        self.frame.show()
        self.label_single.show()
        self.label_left.setText('')
        self.label_middle.setText('')
        self.label_right.setText('')
        self.label_right_2.setText('')
        self.label_choose1.show()

        self.label_up_2.setText('')
        self.label_up2_2.setText('')
        self.label_up3_2.setText('')
        self.pushButton_1.hide()
        self.pushButton_2.hide()
        self.label_single2.setText('進入單音視窗')
        self.openOne()

    # button connect相關
    def openTwo(self):
        MainWindow.setStyleSheet("#MainWindow{background-image:url(D:/secondPIC.png);}")  # 修改
        self.pushButton_1.clicked.connect(lambda: self.OneTextSet(self.pushButton_1))
        self.pushButton_2.clicked.connect(lambda: self.OneTextSet(self.pushButton_2))
        self.pushButton_3.clicked.connect(lambda: self.OneTextSet(self.pushButton_3))
        self.pushButton_4.clicked.connect(lambda: self.OneTextSet(self.pushButton_4))
        self.pushButton_5.clicked.connect(lambda: self.OneTextSet(self.pushButton_5))
        self.pushButton_6.clicked.connect(lambda: self.OneTextSet(self.pushButton_6))
        self.pushButton_replay.clicked.connect(lambda: self.voice(self.pushButton_replay))
        self.pushButton_sure.clicked.connect(lambda: self.getValue(self.pushButton_sure))

        self.pushButton_one_2.clicked.connect(self.one)
        self.pushButton_two_2.clicked.connect(self.two)
        self.pushButton_three_2.clicked.connect(self.three)
        self.pushButton_four_2.clicked.connect(self.four)
        self.pushButton_five_2.clicked.connect(self.five)

        self.pushButton_one_2.clicked.connect(self.pushButton_sure_5.show)
        self.pushButton_two_2.clicked.connect(self.pushButton_sure_5.show)
        self.pushButton_three_2.clicked.connect(self.pushButton_sure_5.show)
        self.pushButton_four_2.clicked.connect(self.pushButton_sure_5.show)
        self.pushButton_five_2.clicked.connect(self.pushButton_sure_5.show)

        self.pushButton_one_2.clicked.connect(self.pushButton_cancel_7.show)
        self.pushButton_two_2.clicked.connect(self.pushButton_cancel_7.show)
        self.pushButton_three_2.clicked.connect(self.pushButton_cancel_7.show)
        self.pushButton_four_2.clicked.connect(self.pushButton_cancel_7.show)
        self.pushButton_five_2.clicked.connect(self.pushButton_cancel_7.show)

        self.pushButton_sure_5.clicked.connect(lambda: self.voice(self.pushButton_sure_5))
        self.pushButton_allplay.clicked.connect(lambda: self.voice(self.pushButton_allplay))

        self.pushButton_cancel_7.clicked.connect(self.cancel7)
        self.pushButton_cancel.clicked.connect(self.cancel)
        self.pushButton_keep.clicked.connect(self.keep)

    def opensexual(self):
        MainWindow.setStyleSheet("#MainWindow{background-image:url(D:/secondPIC.png);}")  # 修改
        self.frame_5.show()
        self.label_eye.hide()
        self.label_title.hide()
        self.pushButton_start.hide()

    def openchoosepage(self):
        MainWindow.setStyleSheet("#MainWindow{background-image:url(D:/secondPIC.png);}")  # 修改
        self.frame_5.hide()
        self.frame_2.show()
        self.label_gender2.show()

    # hide show enable相關
    def openTwoUi(self):
        self.label_gender2.hide()
        self.pushButton_37.hide()
        self.pushButton_sure.hide()
        self.pushButton_cancel.hide()
        self.frame_2.hide()
        self.frame.show()
        self.label_double_1.show()
        self.label_left.setText('')
        self.label_middle.setText('')
        self.label_right.setText('')
        self.label_right_2.setText('')
        self.label_choose1.show()

        self.label_up_2.setText('')
        self.label_up2_2.setText('')
        self.label_up3_2.setText('')
        self.pushButton_5.hide()
        self.pushButton_6.hide()
        self.label_single2.setText('進入雙音視窗')
        self.openTwo()

    def openThree(self):
        MainWindow.setStyleSheet("#MainWindow{background-image:url(D:/secondPIC.png);}")  # 修改
        self.label_gender2.hide()
        self.pushButton_1.clicked.connect(lambda: self.OneTextSet(self.pushButton_1))
        self.pushButton_2.clicked.connect(lambda: self.OneTextSet(self.pushButton_2))
        self.pushButton_3.clicked.connect(lambda: self.OneTextSet(self.pushButton_3))
        self.pushButton_4.clicked.connect(lambda: self.OneTextSet(self.pushButton_4))
        self.pushButton_5.clicked.connect(lambda: self.OneTextSet(self.pushButton_5))
        self.pushButton_6.clicked.connect(lambda: self.OneTextSet(self.pushButton_6))

        self.pushButton_sure.clicked.connect(lambda: self.getValue(self.pushButton_sure))
        self.pushButton_replay.clicked.connect(lambda: self.voice(self.pushButton_replay))

        self.pushButton_one_2.clicked.connect(self.one)
        self.pushButton_two_2.clicked.connect(self.two)
        self.pushButton_three_2.clicked.connect(self.three)
        self.pushButton_four_2.clicked.connect(self.four)
        self.pushButton_five_2.clicked.connect(self.five)

        self.pushButton_one_2.clicked.connect(self.pushButton_sure_5.show)
        self.pushButton_two_2.clicked.connect(self.pushButton_sure_5.show)
        self.pushButton_three_2.clicked.connect(self.pushButton_sure_5.show)
        self.pushButton_four_2.clicked.connect(self.pushButton_sure_5.show)
        self.pushButton_five_2.clicked.connect(self.pushButton_sure_5.show)

        self.pushButton_one_2.clicked.connect(self.pushButton_cancel_7.show)
        self.pushButton_two_2.clicked.connect(self.pushButton_cancel_7.show)
        self.pushButton_three_2.clicked.connect(self.pushButton_cancel_7.show)
        self.pushButton_four_2.clicked.connect(self.pushButton_cancel_7.show)
        self.pushButton_five_2.clicked.connect(self.pushButton_cancel_7.show)

        self.pushButton_sure_5.clicked.connect(lambda: self.voice(self.pushButton_sure_5))
        self.pushButton_allplay.clicked.connect(lambda: self.voice(self.pushButton_allplay))

        self.pushButton_cancel_7.clicked.connect(self.cancel7)
        self.pushButton_cancel.clicked.connect(self.cancel)
        self.pushButton_keep.clicked.connect(self.keep)

    def openThreeUi(self):
        self.pushButton_37.hide()
        self.pushButton_sure.hide()
        self.pushButton_cancel.hide()
        self.frame_2.hide()
        self.frame.show()
        self.label_triple_1.show()
        self.label_left.setText('')
        self.label_middle.setText('')
        self.label_right.setText('')
        self.label_right_2.setText('')
        self.label_choose1.show()

        self.label_up_2.setText('')
        self.label_up2_2.setText('')
        self.label_up3_2.setText('')
        self.pushButton_5.hide()
        self.pushButton_6.hide()

        self.label_single2.setText('進入三音視窗')
        self.openThree()

    def setupUi(self, MainWindow):
        MainWindow.setStyleSheet("#MainWindow{background-image:url(D:/firstPIC.png);}")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1414, 810)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_single2 = QtWidgets.QLabel(self.centralwidget)
        self.label_single2.setGeometry(QtCore.QRect(30, 40, 581, 81))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_single2.setFont(font)
        self.label_single2.setObjectName("label_single2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(850, 120, 431, 501))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.left1 = QtWidgets.QLabel(self.frame)
        self.left1.setGeometry(QtCore.QRect(20, 290, 31, 71))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.left1.setFont(font)
        self.left1.setObjectName("left1")
        self.left2 = QtWidgets.QLabel(self.frame)
        self.left2.setGeometry(QtCore.QRect(170, 290, 31, 71))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.left2.setFont(font)
        self.left2.setObjectName("left2")
        self.pushButton_37 = QtWidgets.QPushButton(self.frame)
        self.pushButton_37.setGeometry(QtCore.QRect(20, 210, 91, 81))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_37.setFont(font)
        self.pushButton_37.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    color : #000000;\n"
                                         "    background-color : #F9F7F3;\n"
                                         "    border-radius: 45px;\n"
                                         "    border: 3px solid #FFD700;\n"
                                         "    border-bottom: 4px solid #AAAAAA;\n"
                                         "    border-right:4px solid #AAAAAA;\n"
                                         "}\n"
                                         "QPushButton:focus \n"
                                         "{\n"
                                         "    color : #315659;\n"
                                         "    border-width: 3px; border-style: solid; border-radius: 45px;\n"
                                         "    background-color: #F6E27F; \n"
                                         "}")
        self.pushButton_37.setAutoDefault(True)
        self.pushButton_37.setObjectName("pushButton_37")
        self.right1 = QtWidgets.QLabel(self.frame)
        self.right1.setGeometry(QtCore.QRect(90, 290, 31, 71))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.right1.setFont(font)
        self.right1.setObjectName("right1")
        self.label_left = QtWidgets.QLabel(self.frame)
        self.label_left.setGeometry(QtCore.QRect(50, 300, 31, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_left.setFont(font)
        self.label_left.setText("")
        self.label_left.setObjectName("label_left")
        self.pushButton_sure = QtWidgets.QPushButton(self.frame)
        self.pushButton_sure.setGeometry(QtCore.QRect(170, 200, 91, 81))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_sure.setFont(font)
        self.pushButton_sure.setStyleSheet("QPushButton\n"
                                           "{\n"
                                           "    color : #000000;\n"
                                           "    background-color : #F9F7F3;\n"
                                           "    border-radius: 45px;\n"
                                           "    border: 3px solid #FFD700;\n"
                                           "    border-right: 4px solid #AAAAAA;\n"
                                           "    border-bottom: 4px solid #AAAAAA;\n"
                                           "}\n"
                                           "QPushButton:focus \n"
                                           "{\n"
                                           "    color : #315659;\n"
                                           "    border-width: 3px; border-style: solid; border-radius: 45px;\n"
                                           "    background-color: #F6E27F; \n"
                                           "}")
        self.pushButton_sure.setAutoDefault(True)
        self.pushButton_sure.setObjectName("pushButton_sure")
        self.right2 = QtWidgets.QLabel(self.frame)
        self.right2.setGeometry(QtCore.QRect(240, 290, 31, 71))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.right2.setFont(font)
        self.right2.setObjectName("right2")
        self.label_middle = QtWidgets.QLabel(self.frame)
        self.label_middle.setGeometry(QtCore.QRect(200, 300, 31, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_middle.setFont(font)
        self.label_middle.setText("")
        self.label_middle.setObjectName("label_middle")
        self.pushButton_cancel = QtWidgets.QPushButton(self.frame)
        self.pushButton_cancel.setGeometry(QtCore.QRect(320, 200, 91, 81))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setStyleSheet("QPushButton\n"
                                             "{\n"
                                             "    color : #000000;\n"
                                             "    background-color : #F9F7F3;\n"
                                             "    border-radius: 45px;\n"
                                             "    border: 3px solid #FFD700;\n"
                                             "    border-right: 4px solid #AAAAAA;\n"
                                             "    border-bottom: 4px solid #AAAAAA;\n"
                                             "}\n"
                                             "QPushButton:focus \n"
                                             "{\n"
                                             "    color : #315659;\n"
                                             "    border-width: 3px; border-style: solid; border-radius: 45px;\n"
                                             "    background-color: #F6E27F; \n"
                                             "}")
        self.pushButton_cancel.setAutoDefault(True)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 110, 91, 81))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "    color : #000000;\n"
                                        "    background-color : #F9F7F3;\n"
                                        "    border-radius: 45px;\n"
                                        "    border: 3px solid #FFD700;\n"
                                        "    border-right: 4px solid #AAAAAA;\n"
                                        "    border-bottom: 4px solid #AAAAAA;\n"
                                        "}\n"
                                        "QPushButton:focus \n"
                                        "{\n"
                                        "    color : #315659;\n"
                                        "    border-width: 3px; border-style: solid; border-radius: 45px;\n"
                                        "    background-color: #F6E27F; \n"
                                        "}")
        self.pushButton_4.setAutoDefault(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(170, 110, 91, 81))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "    color : #000000;\n"
                                        "    background-color : #F9F7F3;\n"
                                        "    border-radius: 45px;\n"
                                        "    border: 3px solid #FFD700;\n"
                                        "    border-right: 4px solid #AAAAAA;\n"
                                        "    border-bottom: 4px solid #AAAAAA;\n"
                                        "}\n"
                                        "QPushButton:focus \n"
                                        "{\n"
                                        "    color : #315659;\n"
                                        "    border-width: 3px; border-style: solid; border-radius: 45px;\n"
                                        "    background-color: #F6E27F; \n"
                                        "}")
        self.pushButton_5.setAutoDefault(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 10, 91, 81))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "    color : #000000;\n"
                                        "    background-color : #F9F7F3;\n"
                                        "    border-radius: 45px;\n"
                                        "    border: 3px solid #FFD700;\n"
                                        "    border-bottom: 4px solid #AAAAAA;\n"
                                        "    border-right: 4px solid #AAAAAA;\n"
                                        "}\n"
                                        "QPushButton:focus \n"
                                        "{\n"
                                        "    color : #315659;\n"
                                        "    border-width: 3px; border-style: solid; border-radius: 45px;\n"
                                        "    background-color: #F6E27F; \n"
                                        "}")
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 10, 91, 81))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "    color : #000000;\n"
                                        "    background-color : #F9F7F3;\n"
                                        "    border-radius: 45px;\n"
                                        "    border: 3px solid #FFD700;\n"
                                        "    border-bottom: 4px solid #AAAAAA;\n"
                                        "    border-right: 4px solid #AAAAAA;\n"
                                        "}\n"
                                        "QPushButton:focus \n"
                                        "{\n"
                                        "    color : #315659;\n"
                                        "    border-width: 3px; border-style: solid; border-radius: 45px;\n"
                                        "    background-color: #F6E27F; \n"
                                        "}")
        self.pushButton_3.setAutoDefault(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(320, 110, 91, 81))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "    color : #000000;\n"
                                        "    background-color : #F9F7F3;\n"
                                        "    border-radius: 45px;\n"
                                        "    border: 3px solid #FFD700;\n"
                                        "    border-right: 4px solid #AAAAAA;\n"
                                        "    border-bottom: 4px solid #AAAAAA;\n"
                                        "}\n"
                                        "QPushButton:focus \n"
                                        "{\n"
                                        "    color : #315659;\n"
                                        "    border-width: 3px; border-style: solid; border-radius: 45px;\n"
                                        "    background-color: #F6E27F; \n"
                                        "}")
        self.pushButton_6.setAutoDefault(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_1 = QtWidgets.QPushButton(self.frame)
        self.pushButton_1.setGeometry(QtCore.QRect(20, 10, 91, 81))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "    color : #000000;\n"
                                        "    background-color : #F9F7F3;\n"
                                        "    border-radius: 45px;\n"
                                        "    border: 3px solid #FFD700;\n"
                                        "    border-bottom: 4px solid #AAAAAA;\n"
                                        "    border-right: 4px solid #AAAAAA;\n"
                                        "}\n"
                                        "QPushButton:focus \n"
                                        "{\n"
                                        "    color : #315659;\n"
                                        "    border-width: 3px; border-style: solid; border-radius: 45px;\n"
                                        "    background-color: #F6E27F; \n"
                                        "}")
        self.pushButton_1.setAutoDefault(True)
        self.pushButton_1.setObjectName("pushButton_1")
        self.left3 = QtWidgets.QLabel(self.frame)
        self.left3.setGeometry(QtCore.QRect(20, 400, 31, 71))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.left3.setFont(font)
        self.left3.setObjectName("left3")
        self.label_right = QtWidgets.QLabel(self.frame)
        self.label_right.setGeometry(QtCore.QRect(40, 410, 51, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_right.setFont(font)
        self.label_right.setObjectName("label_right")
        self.right3 = QtWidgets.QLabel(self.frame)
        self.right3.setGeometry(QtCore.QRect(90, 400, 31, 71))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.right3.setFont(font)
        self.right3.setObjectName("right3")
        self.left4 = QtWidgets.QLabel(self.frame)
        self.left4.setGeometry(QtCore.QRect(170, 400, 31, 71))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.left4.setFont(font)
        self.left4.setObjectName("left4")
        self.right4 = QtWidgets.QLabel(self.frame)
        self.right4.setGeometry(QtCore.QRect(240, 400, 31, 71))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.right4.setFont(font)
        self.right4.setObjectName("right4")
        self.label_right_2 = QtWidgets.QLabel(self.frame)
        self.label_right_2.setGeometry(QtCore.QRect(190, 410, 51, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_right_2.setFont(font)
        self.label_right_2.setObjectName("label_right_2")
        self.label_single = QtWidgets.QLabel(self.centralwidget)
        self.label_single.setGeometry(QtCore.QRect(30, 140, 731, 498))
        self.label_single.setMinimumSize(QtCore.QSize(711, 371))
        self.label_single.setMaximumSize(QtCore.QSize(841, 501))
        self.label_single.setObjectName("label_single")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(830, 440, 531, 171))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pushButton_allplay = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_allplay.setGeometry(QtCore.QRect(30, 90, 401, 71))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_allplay.setFont(font)
        self.pushButton_allplay.setStyleSheet("QPushButton\n"
                                              "{\n"
                                              "    color : #000000;\n"
                                              "    background-color : #F9F7F3;\n"
                                              "    border-radius: 45px;\n"
                                              "    border: 3px solid #FFD700;\n"
                                              "    border-right: 4px solid #AAAAAA;\n"
                                              "    border-bottom: 4px solid #AAAAAA;\n"
                                              "}\n"
                                              "QPushButton:focus \n"
                                              "{\n"
                                              "    color : #315659;\n"
                                              "    border-width: 3px; border-style: solid; border-radius: 45px;\n"
                                              "    background-color: #F6E27F; \n"
                                              "}")
        self.pushButton_allplay.setAutoDefault(True)
        self.pushButton_allplay.setObjectName("pushButton_allplay")
        self.pushButton_replay = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_replay.setGeometry(QtCore.QRect(250, 10, 181, 71))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_replay.setFont(font)
        self.pushButton_replay.setStyleSheet("QPushButton\n"
                                             "{\n"
                                             "    color : #000000;\n"
                                             "    background-color : #F9F7F3;\n"
                                             "    border-radius: 45px;\n"
                                             "    border: 3px solid #FFD700;\n"
                                             "    border-right: 4px solid #AAAAAA;\n"
                                             "    border-bottom: 4px solid #AAAAAA;\n"
                                             "}\n"
                                             "QPushButton:focus \n"
                                             "{\n"
                                             "    color : #315659;\n"
                                             "    border-width: 3px; border-style: solid; border-radius: 45px;\n"
                                             "    background-color: #F6E27F; \n"
                                             "}")
        self.pushButton_replay.setAutoDefault(True)
        self.pushButton_replay.setObjectName("pushButton_replay")
        self.pushButton_keep = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_keep.setGeometry(QtCore.QRect(30, 10, 191, 71))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_keep.setFont(font)
        self.pushButton_keep.setStyleSheet("QPushButton\n"
                                           "{\n"
                                           "    color : #000000;\n"
                                           "    background-color : #F9F7F3;\n"
                                           "    border-radius: 45px;\n"
                                           "    border: 3px solid #FFD700;\n"
                                           "    border-right: 4px solid #AAAAAA;\n"
                                           "    border-bottom: 4px solid #AAAAAA;\n"
                                           "}\n"
                                           "QPushButton:focus \n"
                                           "{\n"
                                           "    color : #315659;\n"
                                           "    border-width: 3px; border-style: solid; border-radius: 45px;\n"
                                           "    background-color: #F6E27F; \n"
                                           "}")
        self.pushButton_keep.setAutoDefault(True)
        self.pushButton_keep.setObjectName("pushButton_keep")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(780, -40, 581, 551))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_five_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_five_2.setGeometry(QtCore.QRect(30, 390, 261, 71))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_five_2.setFont(font)
        self.pushButton_five_2.setStyleSheet("QPushButton\n"
                                             "{\n"
                                             "    color : #000000;\n"
                                             "    background-color : #F9F7F3;\n"
                                             "    border-radius: 45px;\n"
                                             "    border: 3px solid #FFD700;\n"
                                             "    border-right: 4px solid #AAAAAA;\n"
                                             "    border-bottom: 4px solid #AAAAAA;\n"
                                             "}\n"
                                             "QPushButton:focus \n"
                                             "{\n"
                                             "    color : #315659;\n"
                                             "    border-width: 3px; border-style: solid; border-radius: 45px;\n"
                                             "    background-color: #F6E27F; \n"
                                             "}")
        self.pushButton_five_2.setAutoDefault(True)
        self.pushButton_five_2.setObjectName("pushButton_five_2")
        self.pushButton_three_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_three_2.setGeometry(QtCore.QRect(30, 310, 111, 71))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_three_2.setFont(font)
        self.pushButton_three_2.setStyleSheet("QPushButton\n"
                                              "{\n"
                                              "    color : #000000;\n"
                                              "    background-color : #F9F7F3;\n"
                                              "    border-radius: 45px;\n"
                                              "    border: 2px solid #FFD700;\n"
                                              "    border-bottom: 4px solid #AAAAAA;\n"
                                              "    border-right: 4px solid #AAAAAA;\n"
                                              "}\n"
                                              "QPushButton:focus \n"
                                              "{\n"
                                              "    color : #315659;\n"
                                              "    border-width: 3px; border-style: solid; border-radius: 45px;\n"
                                              "    background-color: #F6E27F; \n"
                                              "}")
        self.pushButton_three_2.setAutoDefault(True)
        self.pushButton_three_2.setObjectName("pushButton_three_2")
        self.pushButton_two_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_two_2.setGeometry(QtCore.QRect(180, 220, 111, 71))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_two_2.setFont(font)
        self.pushButton_two_2.setStyleSheet("QPushButton\n"
                                            "{\n"
                                            "    color : #000000;\n"
                                            "    background-color : #F9F7F3;\n"
                                            "    border-radius: 45px;\n"
                                            "    border: 3px solid #FFD700;\n"
                                            "    border-right: 4px solid #AAAAAA;\n"
                                            "    border-bottom: 4px solid #AAAAAA;\n"
                                            "}\n"
                                            "QPushButton:focus \n"
                                            "{\n"
                                            "    color : #315659;\n"
                                            "    border-width: 3px; border-style: solid; border-radius: 45px;\n"
                                            "    background-color: #F6E27F; \n"
                                            "}")
        self.pushButton_two_2.setAutoDefault(True)
        self.pushButton_two_2.setObjectName("pushButton_two_2")
        self.pushButton_four_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_four_2.setGeometry(QtCore.QRect(180, 310, 111, 71))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_four_2.setFont(font)
        self.pushButton_four_2.setStyleSheet("QPushButton\n"
                                             "{\n"
                                             "    color : #000000;\n"
                                             "    background-color : #F9F7F3;\n"
                                             "    border-radius: 45px;\n"
                                             "    border: 3px solid #FFD700;\n"
                                             "    border-right: 4px solid #AAAAAA;\n"
                                             "    border-bottom: 4px solid #AAAAAA;\n"
                                             "}\n"
                                             "QPushButton:focus \n"
                                             "{\n"
                                             "    color : #315659;\n"
                                             "    border-width: 3px; border-style: solid; border-radius: 45px;\n"
                                             "    background-color: #F6E27F; \n"
                                             "}")
        self.pushButton_four_2.setAutoDefault(True)
        self.pushButton_four_2.setObjectName("pushButton_four_2")
        self.pushButton_one_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_one_2.setGeometry(QtCore.QRect(30, 220, 111, 71))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_one_2.setFont(font)
        self.pushButton_one_2.setStyleSheet("QPushButton\n"
                                            "{\n"
                                            "    color : #000000;\n"
                                            "    background-color : #F9F7F3;\n"
                                            "    border-radius: 45px;\n"
                                            "    border: 3px solid #FFD700;\n"
                                            "    border-right: 4px solid #AAAAAA;\n"
                                            "    border-bottom: 4px solid #AAAAAA;\n"
                                            "}\n"
                                            "QPushButton:focus \n"
                                            "{\n"
                                            "    color : #315659;\n"
                                            "    border-width: 3px; border-style: solid; border-radius: 45px;\n"
                                            "    background-color: #F6E27F; \n"
                                            "}")
        self.pushButton_one_2.setAutoDefault(True)
        self.pushButton_one_2.setObjectName("pushButton_one_2")
        self.left1_6 = QtWidgets.QLabel(self.frame_3)
        self.left1_6.setGeometry(QtCore.QRect(330, 210, 31, 71))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.left1_6.setFont(font)
        self.left1_6.setObjectName("left1_6")
        self.right1_6 = QtWidgets.QLabel(self.frame_3)
        self.right1_6.setGeometry(QtCore.QRect(400, 210, 31, 71))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.right1_6.setFont(font)
        self.right1_6.setObjectName("right1_6")
        self.label_up_2 = QtWidgets.QLabel(self.frame_3)
        self.label_up_2.setGeometry(QtCore.QRect(350, 220, 51, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_up_2.setFont(font)
        self.label_up_2.setObjectName("label_up_2")
        self.left1_7 = QtWidgets.QLabel(self.frame_3)
        self.left1_7.setGeometry(QtCore.QRect(330, 290, 31, 71))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.left1_7.setFont(font)
        self.left1_7.setObjectName("left1_7")
        self.right1_7 = QtWidgets.QLabel(self.frame_3)
        self.right1_7.setGeometry(QtCore.QRect(400, 290, 31, 71))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.right1_7.setFont(font)
        self.right1_7.setObjectName("right1_7")
        self.label_up2_2 = QtWidgets.QLabel(self.frame_3)
        self.label_up2_2.setGeometry(QtCore.QRect(350, 300, 51, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_up2_2.setFont(font)
        self.label_up2_2.setObjectName("label_up2_2")
        self.label_up3_2 = QtWidgets.QLabel(self.frame_3)
        self.label_up3_2.setGeometry(QtCore.QRect(350, 380, 51, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_up3_2.setFont(font)
        self.label_up3_2.setObjectName("label_up3_2")
        self.right1_8 = QtWidgets.QLabel(self.frame_3)
        self.right1_8.setGeometry(QtCore.QRect(400, 370, 31, 71))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.right1_8.setFont(font)
        self.right1_8.setObjectName("right1_8")
        self.left1_8 = QtWidgets.QLabel(self.frame_3)
        self.left1_8.setGeometry(QtCore.QRect(330, 370, 31, 71))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.left1_8.setFont(font)
        self.left1_8.setObjectName("left1_8")
        self.label_sound_2 = QtWidgets.QLabel(self.frame_3)
        self.label_sound_2.setGeometry(QtCore.QRect(450, 300, 71, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_sound_2.setFont(font)
        self.label_sound_2.setObjectName("label_sound_2")
        self.left1_9 = QtWidgets.QLabel(self.frame_3)
        self.left1_9.setGeometry(QtCore.QRect(430, 290, 31, 71))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.left1_9.setFont(font)
        self.left1_9.setObjectName("left1_9")
        self.right1_9 = QtWidgets.QLabel(self.frame_3)
        self.right1_9.setGeometry(QtCore.QRect(520, 290, 31, 71))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.right1_9.setFont(font)
        self.right1_9.setObjectName("right1_9")
        self.pushButton_sure_5 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_sure_5.setGeometry(QtCore.QRect(440, 380, 91, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_sure_5.setFont(font)
        self.pushButton_sure_5.setStyleSheet("QPushButton\n"
                                             "{\n"
                                             "    color : #000000;\n"
                                             "    background-color : #F9F7F3;\n"
                                             "    border-radius: 45px;\n"
                                             "    border: 3px solid #FFD700;\n"
                                             "    border-right: 4px solid #AAAAAA;\n"
                                             "    border-bottom: 4px solid #AAAAAA;\n"
                                             "}\n"
                                             "QPushButton:focus \n"
                                             "{\n"
                                             "    color : #315659;\n"
                                             "    border-width: 3px; border-style: solid; border-radius: 45px;\n"
                                             "    background-color: #F6E27F; \n"
                                             "}")
        self.pushButton_sure_5.setAutoDefault(True)
        self.pushButton_sure_5.setObjectName("pushButton_sure_5")
        self.pushButton_cancel_7 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_cancel_7.setGeometry(QtCore.QRect(440, 460, 91, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_cancel_7.setFont(font)
        self.pushButton_cancel_7.setStyleSheet("QPushButton\n"
                                               "{\n"
                                               "    color : #000000;\n"
                                               "    background-color : #F9F7F3;\n"
                                               "    border-radius: 45px;\n"
                                               "    border: 3px solid #FFD700;\n"
                                               "    border-right: 4px solid #AAAAAA;\n"
                                               "    border-bottom: 4px solid #AAAAAA;\n"
                                               "}\n"
                                               "QPushButton:focus \n"
                                               "{\n"
                                               "    color : #315659;\n"
                                               "    border-width: 3px; border-style: solid; border-radius: 45px;\n"
                                               "    background-color: #F6E27F; \n"
                                               "}")
        self.pushButton_cancel_7.setAutoDefault(True)
        self.pushButton_cancel_7.setObjectName("pushButton_cancel_7")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(300, 160, 741, 441))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(60, 30, 141, 351))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton\n"
                                      "{\n"
                                      "    color : #000000;\n"
                                      "    background-color : #F9F7F3;\n"
                                      "    border-radius: 45px;\n"
                                      "    border: 3px solid #FFD700;\n"
                                      "    border-right: 4px solid #AAAAAA;\n"
                                      "    border-bottom: 4px solid #AAAAAA;\n"
                                      "}\n"
                                      "QPushButton:focus \n"
                                      "{\n"
                                      "    color : #315659;\n"
                                      "    border-width: 5px; border-style: solid; border-radius: 50px;\n"
                                      "    background-color: #F6E27F; \n"
                                      "}")
        self.pushButton.setAutoDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_7.setGeometry(QtCore.QRect(300, 30, 141, 351))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "    color : #000000;\n"
                                        "    background-color : #F9F7F3;\n"
                                        "    border: 3px solid #FFD700;\n"
                                        "    border-radius:50px;\n"
                                        "    border-right: 4px solid #AAAAAA;\n"
                                        "    border-bottom: 4px solid #AAAAAA;\n"
                                        "}\n"
                                        "QPushButton:focus \n"
                                        "{\n"
                                        "    color : #315659;\n"
                                        "    border-width: 5px; border-style: solid; border-radius: 50px;\n"
                                        "    background-color: #F6E27F; \n"
                                        "}")
        self.pushButton_7.setAutoDefault(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_8.setGeometry(QtCore.QRect(540, 30, 141, 351))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "    color : #000000;\n"
                                        "    background-color : #F9F7F3;\n"
                                        "    border-radius: 55px;\n"
                                        "    border: 3px solid #FFD700;\n"
                                        "    border-bottom: 4px solid #AAAAAA;\n"
                                        "    border-right:4px solid #AAAAAA;\n"
                                        "}\n"
                                        "QPushButton:focus \n"
                                        "{\n"
                                        "    color : #315659;\n"
                                        "    border-width: 5px; border-style: solid; border-radius: 50px;\n"
                                        "    background-color: #F6E27F; \n"
                                        "}")
        self.pushButton_8.setAutoDefault(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton.raise_()
        self.label_x = QtWidgets.QLabel(self.centralwidget)
        self.label_x.setGeometry(QtCore.QRect(30, 680, 731, 61))
        self.label_x.setText("")
        self.label_x.setObjectName("label_x")
        self.label_x.hide()
        self.label_double_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_double_1.setGeometry(QtCore.QRect(30, 140, 731, 498))
        self.label_double_1.setMinimumSize(QtCore.QSize(711, 371))
        self.label_double_1.setMaximumSize(QtCore.QSize(841, 501))
        self.label_double_1.setObjectName("label_double_1")
        self.label_double_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_double_2.setGeometry(QtCore.QRect(30, 150, 731, 498))
        self.label_double_2.setMinimumSize(QtCore.QSize(711, 371))
        self.label_double_2.setMaximumSize(QtCore.QSize(841, 501))
        self.label_double_2.setObjectName("label_double_2")
        self.label_triple_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_triple_1.setGeometry(QtCore.QRect(40, 140, 731, 498))
        self.label_triple_1.setMinimumSize(QtCore.QSize(711, 371))
        self.label_triple_1.setMaximumSize(QtCore.QSize(841, 501))
        self.label_triple_1.setObjectName("label_triple_1")
        self.label_triple_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_triple_2.setGeometry(QtCore.QRect(30, 140, 731, 498))
        self.label_triple_2.setMinimumSize(QtCore.QSize(711, 371))
        self.label_triple_2.setMaximumSize(QtCore.QSize(841, 501))
        self.label_triple_2.setObjectName("label_triple_2")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(380, 80, 721, 671))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_gender = QtWidgets.QLabel(self.frame_5)
        self.label_gender.setGeometry(QtCore.QRect(-30, 30, 681, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_gender.setFont(font)
        self.label_gender.setObjectName("label_gender")
        self.pushButton_Boy = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_Boy.setGeometry(QtCore.QRect(80, 120, 201, 91))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Boy.setFont(font)
        self.pushButton_Boy.setAutoDefault(True)
        self.pushButton_Boy.setObjectName("pushButton_Boy")
        self.pushButton_Boy.setStyleSheet("QPushButton\n"
                                          "{\n"
                                          "    color : #000000;\n"
                                          "    background-color : #F9F7F3;\n"
                                          "    border-radius: 50px;\n"
                                          "    border: 3px solid #FFD700;\n"
                                          "    border-bottom: 4px solid #AAAAAA;\n"
                                          "    border-right:4px solid #AAAAAA;\n"
                                          "}\n"
                                          "QPushButton:focus \n"
                                          "{\n"
                                          "    color : #315659;\n"
                                          "    border-width: 5px; border-style: solid; border-radius: 50px;\n"
                                          "    background-color: #F6E27F; \n"
                                          "}")
        self.pushButton_Girl = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_Girl.setGeometry(QtCore.QRect(340, 120, 201, 91))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Girl.setFont(font)
        self.pushButton_Girl.setAutoDefault(True)
        self.pushButton_Girl.setObjectName("pushButton_Girl")
        self.pushButton_Girl.setStyleSheet("QPushButton\n"
                                           "{\n"
                                           "    color : #000000;\n"
                                           "    background-color : #F9F7F3;\n"
                                           "    border-radius: 50px;\n"
                                           "    border: 3px solid #FFD700;\n"
                                           "    border-bottom: 4px solid #AAAAAA;\n"
                                           "    border-right:4px solid #AAAAAA;\n"
                                           "}\n"
                                           "QPushButton:focus \n"
                                           "{\n"
                                           "    color : #315659;\n"
                                           "    border-width: 5px; border-style: solid; border-radius: 50px;\n"
                                           "    background-color: #F6E27F; \n"
                                           "}")
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(590, 260, 201, 91))
        self.pushButton_start.setAutoDefault(True)
        self.pushButton_start.setStyleSheet("QPushButton\n"
                                            "{\n"
                                            "    color : #000000;\n"
                                            "    background-color : #F9F7F3;\n"
                                            "    border-radius: 50px;\n"
                                            "    border: 3px solid #FFD700;\n"
                                            "    border-bottom: 4px solid #AAAAAA;\n"
                                            "    border-right:4px solid #AAAAAA;\n"
                                            "}\n"
                                            "QPushButton:focus \n"
                                            "{\n"
                                            "    color : #315659;\n"
                                            "    border-width: 5px; border-style: solid; border-radius: 50px;\n"
                                            "    background-color: #F6E27F; \n"
                                            "}")
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")
        self.label_eye = QtWidgets.QLabel(self.centralwidget)
        self.label_eye.setGeometry(QtCore.QRect(376, 175, 681, 41))
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(462, 40, 681, 100))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_eye.setFont(font)
        self.label_eye.setObjectName("label_eye")
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.label_gender2 = QtWidgets.QLabel(self.centralwidget)
        self.label_gender2.setGeometry(QtCore.QRect(550, 80, 681, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_gender2.setFont(font)
        self.label_gender2.setObjectName("label_gender2")
        self.label_choose1 = QtWidgets.QLabel(self.centralwidget)
        self.label_choose1.setGeometry(QtCore.QRect(35, 120, 681, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_choose1.setFont(font)
        self.label_choose1.setObjectName("label_choose1")
        self.label_choose2 = QtWidgets.QLabel(self.centralwidget)
        self.label_choose2.setGeometry(QtCore.QRect(760, 130, 681, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_choose2.setFont(font)
        self.label_choose2.setObjectName("label_choose2")
        self.label_choose_sound = QtWidgets.QLabel(self.centralwidget)
        self.label_choose_sound.setGeometry(QtCore.QRect(40, 120, 681, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_choose_sound.setFont(font)
        self.label_choose_sound.setObjectName("label_choose_sound")
        self.label_choose_end = QtWidgets.QLabel(self.centralwidget)
        self.label_choose_end.setGeometry(QtCore.QRect(325, 55, 991, 101))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_choose_end.setFont(font)
        self.label_choose_end.setObjectName("label_choose_end")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1414, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.label_single.hide()
        self.label_double_1.hide()
        self.label_double_2.hide()
        self.label_triple_1.hide()
        self.label_triple_2.hide()
        self.frame.hide()
        self.frame_2.hide()
        self.frame_3.hide()
        self.frame_4.hide()
        self.frame_5.hide()
        self.label_gender2.hide()
        self.label_choose1.hide()
        self.label_choose2.hide()
        self.label_choose_sound.hide()
        self.label_choose_end.hide()

        self.pushButton_sure.hide()
        self.pushButton_cancel.hide()

        self.pushButton.clicked.connect(self.openOneUi)
        self.pushButton_7.clicked.connect(self.openTwoUi)
        self.pushButton_8.clicked.connect(self.openThreeUi)
        self.pushButton_start.clicked.connect(self.opensexual)
        self.pushButton_Boy.clicked.connect(self.openchoosepage)
        self.pushButton_Girl.clicked.connect(self.openchoosepage)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_7)
        MainWindow.setTabOrder(self.pushButton_7, self.pushButton_8)
        MainWindow.setTabOrder(self.pushButton_8, self.pushButton_1)
        MainWindow.setTabOrder(self.pushButton_1, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.pushButton_4)
        MainWindow.setTabOrder(self.pushButton_4, self.pushButton_5)
        MainWindow.setTabOrder(self.pushButton_5, self.pushButton_6)
        MainWindow.setTabOrder(self.pushButton_6, self.pushButton_37)
        MainWindow.setTabOrder(self.pushButton_37, self.pushButton_sure)
        MainWindow.setTabOrder(self.pushButton_sure, self.pushButton_cancel)
        MainWindow.setTabOrder(self.pushButton_cancel, self.pushButton_one_2)
        MainWindow.setTabOrder(self.pushButton_one_2, self.pushButton_two_2)
        MainWindow.setTabOrder(self.pushButton_two_2, self.pushButton_three_2)
        MainWindow.setTabOrder(self.pushButton_three_2, self.pushButton_four_2)
        MainWindow.setTabOrder(self.pushButton_four_2, self.pushButton_five_2)
        MainWindow.setTabOrder(self.pushButton_five_2, self.pushButton_sure_5)
        MainWindow.setTabOrder(self.pushButton_sure_5, self.pushButton_cancel_7)
        MainWindow.setTabOrder(self.pushButton_cancel_7, self.pushButton_keep)
        MainWindow.setTabOrder(self.pushButton_keep, self.pushButton_replay)
        MainWindow.setTabOrder(self.pushButton_replay, self.pushButton_allplay)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_single2.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.left1.setText(_translate("MainWindow", "["))
        self.left2.setText(_translate("MainWindow", "["))
        self.pushButton_37.setText(_translate("MainWindow", "ㄦ"))
        self.right1.setText(_translate("MainWindow", "]"))
        self.pushButton_sure.setText(_translate("MainWindow", "確認"))
        self.right2.setText(_translate("MainWindow", "]"))
        self.pushButton_cancel.setText(_translate("MainWindow", "取消"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.left3.setText(_translate("MainWindow", "["))
        self.label_right.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.right3.setText(_translate("MainWindow", "]"))
        self.left4.setText(_translate("MainWindow", "["))
        self.right4.setText(_translate("MainWindow", "]"))
        self.label_right_2.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_single.setText(_translate("MainWindow",
                                             "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                             "p, li { white-space: pre-wrap; }\n"
                                             "</style></head><body style=\" font-family:\'PMingLiU\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/open/single.png\" /></p></body></html>"))
        self.pushButton_allplay.setText(_translate("MainWindow", "整句播放"))
        self.pushButton_replay.setText(_translate("MainWindow", "重播"))
        self.pushButton_keep.setText(_translate("MainWindow", "繼續"))
        self.pushButton_five_2.setText(_translate("MainWindow", "輕聲"))
        self.pushButton_three_2.setText(_translate("MainWindow", "三聲"))
        self.pushButton_two_2.setText(_translate("MainWindow", "二聲"))
        self.pushButton_four_2.setText(_translate("MainWindow", "四聲"))
        self.pushButton_one_2.setText(_translate("MainWindow", "一聲"))
        self.left1_6.setText(_translate("MainWindow", "["))
        self.right1_6.setText(_translate("MainWindow", "]"))
        self.label_up_2.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.left1_7.setText(_translate("MainWindow", "["))
        self.right1_7.setText(_translate("MainWindow", "]"))
        self.label_up2_2.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_up3_2.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.right1_8.setText(_translate("MainWindow", "]"))
        self.left1_8.setText(_translate("MainWindow", "["))
        self.label_sound_2.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.left1_9.setText(_translate("MainWindow", "["))
        self.right1_9.setText(_translate("MainWindow", "]"))
        self.pushButton_sure_5.setText(_translate("MainWindow", "確認"))
        self.pushButton_cancel_7.setText(_translate("MainWindow", "取消"))
        self.pushButton.setText(_translate("MainWindow", "單\n"
                                                         "音\n"
                                                         "\n"
                                                         "ㄨ\n"
                                                         ""))
        self.pushButton_7.setText(_translate("MainWindow", "雙\n"
                                                           "音\n"
                                                           "ㄉ\n"
                                                           "ㄨ\n"
                                                           ""))
        self.pushButton_8.setText(_translate("MainWindow", "三\n"
                                                           "音\n"
                                                           "ㄉ\n"
                                                           "ㄨ\n"
                                                           "ㄛ"))
        self.label_double_1.setText(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'PMingLiU\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/open/double-1.png\" /></p></body></html>"))
        self.label_double_2.setText(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'PMingLiU\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/open/double-2.png\" /></p></body></html>"))
        self.label_triple_1.setText(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'PMingLiU\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/open/triple-1.png\" /></p></body></html>"))
        self.label_triple_2.setText(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'PMingLiU\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/open/triple-2.png\" /></p></body></html>"))
        self.label_gender.setText(_translate("MainWindow",
                                             "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">請選擇性別</p></body></html>"))
        self.pushButton_Boy.setText(_translate("MainWindow", "男性"))
        self.pushButton_Girl.setText(_translate("MainWindow", "女性"))
        self.pushButton_start.setText(_translate("MainWindow", "開始"))
        self.label_eye.setText(_translate("MainWindow",
                                          "<html><head/><body><p><span style=\" font-size:28pt;\">即將選取瞳孔資訊，請注視鏡頭三秒鐘</span></p><p><br/></p><p><br/></p></body></html>"))
        self.label_title.setText(_translate("MainWindow",
                                            "<html><head/><body><p><span style=\" font-size:72pt;\">用EYE發音</span></p><p><br/></p><p><br/></p></body></html>"))
        self.label_gender2.setText(
            _translate("MainWindow", "<html><head/><body><span style=\" font-size:28pt;\">請選擇注音組合</p></body></html>"))
        self.label_choose1.setText(_translate("MainWindow",
                                              "<html><head/><body><p><span style=\" font-size:22pt;\">請依據左方圖示，輸入注音符號下方之對應編號</span></p></body></html>"))
        self.label_choose2.setText(_translate("MainWindow", "輸入完畢請選確認，欲重新選擇請選取消"))
        self.label_choose_sound.setText(_translate("MainWindow", "請依據欲輸入字，選擇聲調"))
        self.label_choose_end.setText(_translate("MainWindow",
                                                 "<html><head/><body><p>輸入完成，請選繼續，輸入下一個字。</p><p>若想重聽一次請選重播。若整句話已輸入完畢，可選整句播放。</p></body></html>"))


import openone

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())

