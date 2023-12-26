import sqlite3
import os
from settings import DB_PATH

class DBManager:
    def __init__ (self, db_path:str):
        self.db_path = db_path
        
    def check_database(self):
        return os.path.exists(self.bd_path)
    
    def connect_to_database(self):
        conn = sqlite3.connect(self.bd_path)
        cur = conn.cursor()
        return conn, cur
    
    def create_database(self, script_path:str):
        conn, cur = self.connect_to_database()
        try: 
            cur.executescript(open(script_path).read())
            conn.commit()
            conn.close()
        except Exception as err:
            print(err)
            os.remove(self.db_path)
            
            
    def execute(self, query: str, args=(), many: bool = True):
        conn, cur = self.connect_to_database
        try:
            res = cur.execute(query, args)
            result = res.fetchall() if many else res.fetchone()
            conn.commit()
            return {"code":200, "data":result}
        except sqlite3.Error as er:
            print(str(er))
            return{"code":500}
        finally:
            conn.close()
            
base_manager = DBManager(DB_PATH)