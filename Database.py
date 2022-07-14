import sqlite3


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add(self,tg_id ,time ,client_name,topic ,moment,phase,negative ,positive,dpk ,emotions,shsb ,tel ,shsb1,pk ,dpk1  ,shsb11 ,shsb12,pk1 ,dpk11,rate ,extra ,supervis,reflex,feelings,result ,makeBetter ,ans ):
        with self.connection:
            return self.cursor.execute("INSERT INTO users(tg_id ,time ,client_name,topic ,moment,phase,negative ,positive,dpk ,emotions,shsb ,tel ,shsb1,pk ,dpk1 ,shsb11 ,shsb12,pk1 ,dpk11,rate ,extra ,supervis,reflex,feelings,result ,makeBetter ,ans )"
                                       " VALUES (?, ?, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
                                       , (tg_id ,time ,client_name,topic ,moment,phase,negative ,positive,dpk ,emotions,shsb ,tel ,shsb1,pk ,dpk1 ,shsb11 ,shsb12,pk1 ,dpk11,rate ,extra ,supervis,reflex,feelings,result ,makeBetter ,ans, ))

    def getClient(self, tg_id):
        with self.connection:
            return self.cursor.execute("select client_name from users  where tg_id=?", (tg_id, )).fetchall()

    def getClientInfo(self, client_name):
        with self.connection:
            return self.cursor.execute("select * from users  where client_name=?", (client_name, )).fetchall()


if __name__ == '__main__':
    db = Database('db.db')
    print(db.getClientInfo("клиент"))
