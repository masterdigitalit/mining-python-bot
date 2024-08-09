# import asyncio
# import aiomysql
# from getpass import getpass
# from mysql.connector import connect, Error
#
# try:
#     with connect(
#         host="localhost",
#         user='root',
#         port='9000',
#
#         password="h}Bj#xlV9B*Y",
#     ) as connection:
#         print(connection)
# except Error as e:
#     print(e)

from datetime import datetime
import sqlite3
from datetime import datetime, timedelta
con = sqlite3.connect("mining.sqlite", detect_types=sqlite3.PARSE_DECLTYPES |
                             sqlite3.PARSE_COLNAMES, check_same_thread=False)
cursor = con.cursor()
def createTable():
    # создаем таблицу people
    cursor.execute("""CREATE TABLE Tasks (id INTEGER, uniqueCode TEXT, State TEXT, dateCreated TEXT, ConfirmationDate TEXT) """)

def changeUserLevel(id, level):
    cursor.execute("UPDATE Users SET level = ? WHERE id= ? ", [level, id])
    con.commit()
# changeUserLevel(1, 'admin')


def changeConfirmationState(uniqueCode, state):
    cursor.execute("UPDATE Tasks SET State = ? WHERE uniqueCode = ? ", [state, uniqueCode])
    con.commit()
def getTaskState(uniqueCode):
    req = cursor.execute("SELECT * FROM Tasks WHERE uniqueCode = ?", [uniqueCode]).fetchmany(10)
    return req[0][4]
# print(getTaskState('ejbfueuFBEUBUWufeuUWEIU'))

def getAllUsersId():
    result = cursor.execute("SELECT userId FROM Users")
    return result.fetchall()
def addUser(userId, Name, Surname):
    cursor.execute("INSERT INTO Users (userId, Name, Surname, registrationDate, Level) VALUES (?,?,?,?, ?)", [userId, Name, Surname, (datetime.now()).strftime('%d.%m.%Y %H:%M'), 'user'])
    con.commit()
def isUserExist(userId):
    result = cursor.execute("SELECT * FROM Users WHERE userId = ?", [userId])
    return result.fetchall()
def selectAllByTime(time):
    result = cursor.execute("SELECT * FROM Tasks WHERE NextSendDate = ?", [time])
    return result.fetchall()
def addTask(uniqueCode, name,type,state, UserId, nextSendTime):
    if(type == 'periodic'):
        req = cursor.execute("INSERT INTO  Tasks (uniqueCode, Name,Type,State,DateCreated,BlockTime, NextSendDate, UserId ) VALUES ( ?, ?, ?, ?,?,?,?, ?) ", [uniqueCode, name,type,state,datetime.now().strftime('%d.%m.%Y %H:%M') , (datetime.now() + timedelta(minutes=10)).strftime('%d.%m.%Y %H:%M'),  (datetime.now() + timedelta(minutes=nextSendTime)).strftime('%d.%m.%Y %H:%M'), UserId])
    else:
        req = cursor.execute(
            "INSERT INTO  Tasks (uniqueCode, Name,Type,State,DateCreated,BlockTime, NextSendDate, UserId ) VALUES ( ?, ?, ?, ?,?,?,?, ?) ",
            [uniqueCode, name, type, state, datetime.now().strftime('%d.%m.%Y %H:%M'),
             (datetime.now() + timedelta(minutes=10)).strftime('%d.%m.%Y %H:%M'),
             (datetime.now() + timedelta(minutes=20)).strftime('%d.%m.%Y %H:%M'),
             UserId])


    con.commit()
def deleteTable():
    cursor.execute('DROP TABLE Tasks')
def deleteNull():
    cursor.execute('DELETE FROM Tasks  ')
    con.commit()
# deleteNull()
# addTask('ejbfueuFBEUBUWufeuUWEIU', 'blum', 'daily', 'not-activated', '76374885385')

# print(selectAllByTime('07.08.2024 19:48'))


