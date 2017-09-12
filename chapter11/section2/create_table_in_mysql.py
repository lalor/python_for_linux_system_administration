import MySQLdb as db


def get_conn(**kwargs):
    return db.connect(host=kwargs.get('host', 'localhost'),
            user=kwargs.get('user'),
            passwd=kwargs.get('passwd'),
            port=kwargs.get('port', 3306),
            db=kwargs.get('db'))


def execute_sql(conn, sql):
    with conn as cur:
        cur.execute(sql)


def create_table(conn):
    sql_drop_table = "DROP TABLE IF EXISTS student"
    sql_create_table = """ CREATE TABLE `student` (
                           `sno` int(11) NOT NULL,
                           `sname` varchar(20) DEFAULT NULL,
                           `sage` int(11) DEFAULT NULL,
                           PRIMARY KEY (`sno`)
                           ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 """
    for sql in [sql_drop_table, sql_create_table]:
        execute_sql(conn, sql)


def insert_data(conn, sno, sname, sage):
    INSERT_FORMAT = "insert into student values({0}, '{1}', {2})"
    sql = INSERT_FORMAT.format(sno, sname, sage)
    execute_sql(conn, sql)

def main():
    conn = get_conn(user='laimingxing', password='laimingxing', db='test')
    try:
        create_table(conn)
        insert_data(conn, 1, 'zhangsan', 20)
        insert_data(conn, 2, 'lisi', 21)

        with conn as cur:
            cur.execute("select * from student")
            rows = cur.fetchall()
            for row in rows:
                print(row)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    main()
