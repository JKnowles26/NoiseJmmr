import sqlite3

class DBManager:
    def __init__(self, fileName):
        path = fileName + ".db"
        self.conn = sqlite3.connect(path)
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS tracks (
                            track_id TEXT,
                            mfcc TEXT,
                            divisor INT,
                            PRIMARY KEY (track_id))''')

    def insert_values(self, track):
        self.c.execute("INSERT OR REPLACE INTO tracks(track_id, mfcc, divisor) VALUES (?,?,?)", track)

    def close_db(self):
        self.conn.commit()
        self.conn.close()
