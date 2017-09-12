#!/usr/bin/python
#-*- coding: UTF-8 -*-
from __future__ import print_function
import argparse
import json
from collections import defaultdict
from contextlib import contextmanager

import pymysql


def to_json(in_dict):
    return json.dumps(in_dict, sort_keys=True, indent=2)


@contextmanager
def get_conn(**kwargs):
    conn = pymysql.connect(**kwargs)
    try:
        yield conn
    finally:
        conn.close()


def parse_args():
    parser = argparse.ArgumentParser(description='OpenStack Inventory Module')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--list', action='store_true', help='List active servers')
    group.add_argument('--host', help='List details about the specific host')

    return parser.parse_args()


def list_all_hosts(conn):
    hosts = defaultdict(list)

    with conn as cur:
        cur.execute('select * from hosts')
        rows = cur.fetchall()
        for row in rows:
            no, host, group, user, port = row
            hosts[group].append(host)

    return hosts


def get_host_detail(conn, host):
    details = {}
    with conn as cur:
        cur.execute("select * from hosts where host='{0}'".format(host))
        rows = cur.fetchall()
        if rows:
            no, host, group, user, port = rows[0]
            details.update(ansible_user=user, ansible_port=port)
    return details


def main():
    parser = parse_args()
    with get_conn(host='127.0.0.1', user='laimingxing', passwd='laimingxing', db='test') as conn:
        if parser.list:
            hosts = list_all_hosts(conn)
            print(to_json(hosts))
        else:
            details = get_host_detail(conn, parser.host)
            print(to_json(details))


if __name__ == '__main__':
    main()
