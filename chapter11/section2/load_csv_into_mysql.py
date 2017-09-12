import csv
from collections import namedtuple
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


def get_data(file_name):
    with open(file_name) as f:
        f_csv = csv.reader(f)
        headings = next(f_csv)
        Row = namedtuple('Row', headings)
        for r in f_csv:
            yield Row(*r)


def execute_sql(conn, sql):
    with conn as cur:
        cur.execute(sql)


def main():
    conn_args = dict(user='laimingxing', password='laimingxing', db='test')
    with get_conn(**conn_args) as conn:
        SQL_FORMAT = """insert into student values({0}, '{1}', {2})"""
        for t in get_data('data.csv'):
            sql = SQL_FORMAT.format(t.sno, t.sname, t.sage)
            execute_sql(conn, sql)


if __name__ == '__main__':
    main()
