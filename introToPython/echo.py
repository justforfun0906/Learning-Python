import sys
while True:
    line = sys.stdin.readline()
    if line == '':
        break
    print(line)
    sys.stdout.write(line)
