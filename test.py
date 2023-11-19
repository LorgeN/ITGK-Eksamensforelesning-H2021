def respons(fil, r, c):
    try:
        with open(fil) as f:
            line = f.readlines()[r].split(";")
            if c == 0:
                return line[3].strip()[int(line[c])]
    except:
        return ("error")

print(respons("fil.txt", 3, 0))
