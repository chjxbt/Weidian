import os
database = "weidian"
host = "127.0.0.1"
port = "3306"
username = os.environ.get('DB_USER', 'root')
password = os.environ.get('DB_PWD', '')
charset = "utf8"
sqlenginename = 'mysql+pymysql'
