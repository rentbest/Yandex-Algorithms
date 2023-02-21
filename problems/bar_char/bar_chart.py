def printchar(s):
    s = s.replace(" ", "").replace("\n", "")
    d = {}
    sorted_keys = sorted(set(s))
    for el in sorted_keys:
        d[el] = s.count(el)
    for step in range(max(d.values()), 0, -1):
        for key in sorted_keys:
            if d[key] >= step:
                print("#", end="")
            else:
                print(" ", end="")
        print()
    print("".join(sorted_keys))


with open("input.txt", encoding="utf-8") as f:
    printchar(f.read())
