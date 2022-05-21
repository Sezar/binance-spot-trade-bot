import sqlite3

coinName="BTC"

db = sqlite3.connect("cyriptoDB.db")
dbcursor = db.cursor()
dbcursor.execute("CREATE TABLE IF NOT EXISTS Cyripto (name TEXT,miktar DOUBLE,sonAlis DOUBLE,alisOrtalama DOUBLE,satmadanAlis DOUBLE,alisToplamPara DOUBLE,alis INT,satis INT,komisyon DOUBLE) ")
dbcursor.execute("INSERT INTO Cyripto VALUES ('"+coinName+"USDT',0,0,0,0,0,0,0,0)")
db.commit()
