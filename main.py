if __name__ == '__main__':
    file  = open("./text.txt")
    curr = 0
    max = 0
    l = []
    for x in file:
        a = x.strip()
        if a != "":
            curr += int(a)
        else:
            l.append(curr)
            curr = 0
            print("!")
    l.sort(reverse=True)
    print(l[0] + l[1] + l[2])
    file.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
