from __future__ import print_function
import sys
import os

from PIL import Image
from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS


def get_iamge_meta_info(filename):
    exif_data = {}
    with Image.open(filename) as img:
        data = img._getexif()
        for tag, value in data.iteritems():
            decoded = TAGS.get(tag)
            exif_data[decoded] = value

        if exif_data['GPSInfo']:
            gps_data = {}
            for tag, value in exif_data['GPSInfo'].iteritems():
                decoded = GPSTAGS.get(tag)
                gps_data[decoded] = value
            exif_data['GPSInfo'] = gps_data

    return exif_data


def main():
    sys.argv.append("")
    filename = sys.argv[1]
    if not os.path.exists(filename):
        raise SystemExit("{0} is not exists".format(filename))

    exif_data = get_iamge_meta_info(filename)

    for key, value in exif_data.iteritems():
        print(key, value, sep=':')


if __name__ == '__main__':
    main()
