import MySQLdb as db
conn = db.connect(host="localhost", db="test", user='lmx', passwd='my_passwd', unix_socket='/tmp/mysql.sock')
cur = conn.cursor()
sql = "select 1"
cur.execute(sql)
rows =  cur.fetchall()
print rows
