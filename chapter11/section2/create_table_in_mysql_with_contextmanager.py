from contextlib import contextmanager

import MySQLdb as db


@contextmanager
def get_conn(**kwargs):
    conn = db.connect(host=kwargs.get('host', 'localhost'),
                        user=kwargs.get('user'),
                        passwd=kwargs.get('passwd'),
                        port=kwargs.get('port', 3306),
                        db=kwargs.get('db'))
    try:
        yield conn
    finally:
        if conn:
            conn.close()


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
    conn_args = dict(user='laimingxing', password='laimingxing', db='test')
    with get_conn(**conn_args) as conn:
        with conn as cur:
            cur.execute("select * from student")


if __name__ == '__main__':
    main()
