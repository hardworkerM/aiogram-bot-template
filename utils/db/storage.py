import sqlite3 as lite


class DatabaseManager(object):

    def __init__(self, path):
        self.conn = lite.connect(path)
        self.conn.execute('pragma foreign_keys = on')
        self.conn.commit()
        self.cur = self.conn.cursor()

    def create_tables(self):
        self.query('CREATE TABLE IF NOT EXISTS Users (id int, u_name text)')
        self.query("""CREATE TABLE IF NOT EXISTS Data (user_id int, word text,
                                                        tries int,
                                                        correct int,
                                                        combo int,
                                                        ans_time text,
                                                        percents int
                                                        )""")
        self.query('CREATE TABLE IF NOT EXISTS Weights (user_id int, word text, y int)')
        self.query('CREATE TABLE IF NOT EXISTS Dictionary (user_id int, word text, translate text)')
        self.query('CREATE TABLE IF NOT EXISTS Sad (user_id int, about text)')


    def query(self, arg, values=None):
        if values == None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        self.conn.commit()

    def fetchone(self, arg, values=None):
        if values == None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        return self.cur.fetchone()

    def fetchall(self, arg, values=None):
        if values == None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        return self.cur.fetchall()

    def __del__(self):
        self.conn.close()


'''

products: idx text, title text, body text, photo blob, price int, tag text

orders: cid int, usr_name text, usr_address text, products text

cart: cid int, idx text, quantity int ==> product_idx

categories: idx text, title text

wallet: cid int, balance real

questions: cid int, question text

users: user text

'''
