from PyQt6 import QtCore, QtGui, QtWidgets
import pymysql
from config import host, user_name, password, db_name
import sk
import sys
import threading
import design  # Это наш конвертированный файл дизайна

def update(text):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user_name,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with connection.cursor() as cursor:
                cursor.execute(text)
                connection.commit()
                return 0

        finally:
            connection.close()
    except Exception as error:
        return f'*Ошибка с базой данных:* {error}. Не продолжайте!\n\nНажмите /start'
def create(text):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user_name,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with connection.cursor() as cursor:
                cursor.execute(text)
                connection.commit()
                return 0

        finally:
            connection.close()
    except Exception as error:
        return f'*Ошибка с базой данных:* {error}. Не продолжайте!\n\nНажмите /start'
def selone(text):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user_name,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with connection.cursor() as cursor:
                cursor.execute(text)
                return cursor.fetchone()

        finally:
            connection.close()
    except Exception as error:
        return f'*Ошибка с базой данных:* {error}. Не продолжайте!\n\nНажмите /start'
def selist(text):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user_name,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with connection.cursor() as cursor:
                cursor.execute(text)
                return cursor.fetchall()

        finally:
            connection.close()
    except Exception as error:
        return f'*Ошибка с базой данных:* {error}. Не продолжайте!\n\nНажмите /start'


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.init_plan()
        self.init_time()

    def init_plan(self):
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.scheduled_message)
        self.timer.start(10000)  # 60000 ms = 1 minute

    def init_time(self):
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.time_message)
        self.timer.start(1000)  # 60000 ms = 1 minute

    def scheduled_message(self):
        plan = str(self.plan_now())
        text_req = ("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\np, li { white-space: pre-wrap; }\n"
                    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                    "text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:100pt;\">" + plan + '</span></p></body></html>')
        self.label.setText(text_req)

    def time_message(self):
        times = str(sk.time_create())
        text_req = ("<html><head/><body><p align=\"center\"><font color=\"#fa8e47\" face=\"serif\">" + times + '</font></p></body></html>')
        self.label_3.setText(text_req)

    def plan_now(self):
        datenow = sk.date_create()
        daynow = datenow.split('.')[0]
        monthnow = datenow.split('.')[1]
        yearnow = datenow.split('.')[2]

        date_work = f'{daynow}.{monthnow}.{yearnow}'
        plan = selone(f"SELECT plan FROM work_plan WHERE date_work = '{date_work}'")['plan']

        return plan


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    threading.Thread(target=main())  # то запускаем функцию main()
