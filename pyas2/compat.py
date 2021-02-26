# -*- coding: utf-8 -*-
import email
import zlib
import six
import codecs
from six import ensure_text, ensure_binary, ensure_str

if six.PY2:
    unicode_type = unicode
    from cStringIO import StringIO
    from itertools import izip
    from email.generator import Generator
else:
    unicode_type = str
    izip = zip
    from io import BytesIO as StringIO
    from email.generator import BytesGenerator as Generator
    from six import string_types, ensure_str, ensure_binary


def hexify(value):
    return codecs.getencoder("hex")(value)[0]


def compress_hexify(value):
    if six.PY3:
        return zlib.compress(ensure_binary(value)).hex()
    return zlib.compress(value).encode("hex")


def email_msg_from_value(value):
    if six.PY3 and isinstance(value, (bytes, bytearray)):
        return email.message_from_bytes(value)
    return email.message_from_string(value)


def write_log(message):
    import csv
    with open('LOGS.csv', mode='a') as document:
        writer = csv.writer(document, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([message])
