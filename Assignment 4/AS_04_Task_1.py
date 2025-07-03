try:
    f = open('sample.txt', 'r')
    f1 = f.readlines()
    count: int = 0
    print('Reading file content:')
    for line in f1:
        count += 1
        print(f'Line {count}: {line}')
    f.close()
except FileNotFoundError:
    print('Error: The file', "'sample.txt'", 'was not found.')
