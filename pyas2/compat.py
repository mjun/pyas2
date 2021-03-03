# -*- coding: utf-8 -*-
import email
import inspect
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


def get_payload(email_msg):
    if six.PY3:
        return email_msg.as_bytes()
    return email_msg.get_payload()


def write_log(message):
    import csv
    with open('LOGS.csv', mode='a') as document:
        writer = csv.writer(document, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([message])


# class BinaryBytesGenerator(BytesGenerator):
#     """Override the bytes generator to better handle binary data."""
#
#     def _handle_text(self, msg):
#         """
#         Handle writing the binary messages to prevent default behaviour of
#         newline replacements.
#         """
#         if msg.get(
#             "Content-Transfer-Encoding"
#         ) == "binary" and msg.get_content_subtype() in [
#             "pkcs7-mime",
#             "pkcs7-signature",
#         ]:
#             payload = msg.get_payload(decode=True)
#             if payload is None:
#                 return
#             else:
#                 self._fp.write(payload)
#         else:
#             super()._handle_text(msg)
#
#     _writeBody = _handle_text


def raise_error(one, two):
    stack = inspect.stack()
    if not one == two:
        write_log('Value is NOT equal {}'.format(stack))
    else:
        write_log('Value IS equal {}'.format(stack))
