#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import print_function
from collections import namedtuple

Disk = namedtuple('Disk', 'major_number minor_number device_name'
                          ' read_count read_merged_count read_sections'
                          ' time_spent_reading write_count write_merged_count'
                          ' write_sections time_spent_write io_requests'
                          ' time_spent_doing_io weighted_time_spent_doing_io')


def get_disk_info(device):
    """
    从/proc/diskstats中读取磁盘的IO信息
    $ cat /proc/diskstats
     254 32 vdc 614 0 22180 408 51203 2822 1857922 1051716 0 40792 1052064
    """
    with open("/proc/diskstats") as f:
        for line in f:
            if line.split()[2] == device:
                return Disk(*(line.split()))
    raise RuntimeError("device ({0}) not found !".format(device))


def main():
    disk_info = get_disk_info('vdc')

    print(disk_info)

    print("磁盘写次数：{0}".format(disk_info.write_count))
    print("磁盘写字节数：{0}".format(long(disk_info.write_sections) * 512))
    print("磁盘写延时：{0}".format(disk_info.time_spent_write))


if __name__ == '__main__':
    main()
