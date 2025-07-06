try:
    f = open('sample.txt', 'r')
    f1 = f.readlines()
    count: int = 0
    print('Reading file content:')
    for line in f1:
        count += 1
        l=line.strip()
        print(f'Line {count}: {l}')

    f.close()
except FileNotFoundError:
    print('Error: The file', "'sample.txt'", 'was not found.')

