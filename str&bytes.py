_str = 'str'
print(type(_str))
# 输出为 <class 'str'>

_bytes = b'bytes'
print(type(_bytes))
# 输出为<class 'bytes'>

_str = '快乐'
print(_str)
# 快乐

_bytes = '快乐'.encode()
print(_bytes)
# b'\xe4\xb8\xad\xe5\x9b\xbd'

_str = '快乐'
print(type(_str))  # <class 'str'>
print(_str)  # 快乐

_bytes = _str.encode()
print(type(_bytes))  # <class 'bytes'>
print(_bytes)  # b'\xe4\xb8\xad\xe5\x9b\xbd'

new_str = _bytes.decode()
print(type(new_str))  # <class 'str'>
print(new_str)  # 快乐




