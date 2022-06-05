try:
    test_file = open('test.txt', 'r')
except Exception:
    print('broad error')

except IOError:
    print('IO Error')

# Problem is first exception is too broad and will trip every time. This will lead to less specific error reporting to users.
