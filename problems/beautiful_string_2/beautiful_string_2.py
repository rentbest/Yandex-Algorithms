def find_beauty(k, string):
    result = 0
    if k >= len(string):
        result = len(string)
    else:
        for c in "abcdefghijklmnopqrstuvwxyz":
            cur_beauty = 0
            left = 0
            cur_k = k
            for right in range(len(string)):
                if string[right] != c:
                    cur_k -= 1
                if cur_k >= 0 or string[right] == c:
                    cur_beauty += 1
                else:
                    if (cur_beauty > result):
                        result = cur_beauty
                    while (cur_k != 0 and cur_beauty >= 0):
                        if string[left] != c:
                            cur_k += 1
                        left += 1
                        cur_beauty -= 1
                    cur_beauty += 1
            if cur_beauty > result:
                result = cur_beauty
    return result


with open("input.txt", encoding="utf-8") as f:
    k = int(f.readline().strip())
    string = f.readline().strip()
    print(find_beauty(k, string))
