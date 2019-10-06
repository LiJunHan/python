with open('static/key.txt', 'a') as fp:
    for i in range(1000000):
        if i % 2 == 0:
            fp.write('1')
        else:
            fp.write('0')