import base64

_bytes = b'test bytes'

b64 = base64.b64encode(_bytes)
print(b64)  # b'dGVzdCBieXRlcw=='

new_bytes = base64.b64decode(b64)
print(new_bytes)  # b'test bytes'


import base64

_bytes = b'\xfd\xcf\xbe'
b64 = base64.b64encode(_bytes)
print(b64)  # b'/c++'

us_b64 = base64.urlsafe_b64encode(_bytes)
print(us_b64)  # b'_c--'

new_bytes = base64.urlsafe_b64decode(us_b64)
print(new_bytes)  # b'\xfd\xcf\xbe'
