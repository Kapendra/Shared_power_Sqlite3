import sqlite3
from sqlite3 import Error




def userinfo():
    db=sqlite3.connect("spower.db")
    c=db.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS userinfo (Fullname TEXT UNIQUE NOT NULL,"
              "Email TEXT,password VARCHAR(20),gender INTEGER(2),"
              "Country TEXT,phoneno INTEGER(10),AccountType TEXT)")
    db.commit()
    db.close()

def insertinfo():
    db=sqlite3.connect("spower.db")
    c=db.cursor()
    c.execute("INSERT INTO userinfo VALUES (?,?,?,?,?,?,?)"
)
    db.commit()
    db.close()

def fetchinfo():
    db=sqlite3.connect("spower.db")
    c=db.cursor()
    find=c.execute("SELECT * from userinfo")
    find=c.fetchall()
    db.commit()
    db.close()
    return 

def toolinfo():
    db=sqlite3.connect("spower.db")
    c=db.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS toolinfo(Toolname TEXT ,description TEXT,condition TEXT,Fulldayp INTEGER,halfdayp INTEGER,Date)")
    db.commit()
    db.close()

def inserttoolinfo():
    db=sqlite3.connect("spower.db")
    c=db.cursor()
    c.execute("INSERT into toolinfo VALUES (?,?,?,?,?,?)")
    db.commit()
    db.close()

def login():
    db=sqlite3.connect("spower.db")
    c=db.cursor()
    c.execute("SELECT * from userinfo")
    info=c.fetchall()
    db.commit()
    db.close()
    return  info



def fetchtoolinfo():
    db=sqlite3.connect("spower.db")
    c=db.cursor()
    tool=c.execute("SELECt * from toolinfo")
    tool.fetchall()
    db.commit()
    db.close()
    return tool

insertinfo()
