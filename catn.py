import sys
numberOfArgs = len(sys.argv)
if numberOfArgs < 2:
    sys.stderr.write("Usage: " + sys.argv[0] + " <filename>\n")
    sys.exit(1)
if numberOfArgs == 2:
    filename = sys.argv[1]
    try:
        fh = open(filename, "r")
    except FileNotFoundError:
        sys.stderr.write("File not found: " + filename + "\n")
        sys.exit(1)
    prev = ""
    for line in fh:
        if(line == prev):
            continue
        else:
            print(line, end="")
        prev = line
    fh.close()
elif numberOfArgs > 2:
    if(sys.argv[1]!= "-n"):
        sys.stderr.write("Usage: " + sys.argv[0] + " <filename> [-n]\n")
        sys.exit(1)
    else:
        filename = sys.argv[2]
        try:
            fh = open(filename, "r")
        except FileNotFoundError:
            sys.stderr.write("File not found: " + filename + "\n")
            sys.exit(1)
        prev = ""
        count = 1
        for line in fh:
            if(line == prev):
                continue
            else:
                print("\t"+str(count) + " " + line, end="")
                count += 1
            prev = line
else:
    sys.stderr.write("Usage: " + sys.argv[0] + " <filename> [-n]\n")
    sys.exit(1)
    