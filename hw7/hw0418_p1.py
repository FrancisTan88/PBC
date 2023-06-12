file_path = input()
types, content = input().split(":")
cns2word = {}
word2cns = {}
with open(file_path, "r") as f:
    for row in f:
        cns, unicode = row.split()
        word = chr(int(f"0x{unicode}", 16))
        if cns in cns2word and word != cns2word[cns]:
            print("MAPPING_TABLE_ERROR")
            exit()
        else:
            cns2word[cns] = word
        if word in word2cns:
            if cns not in word2cns[word]:
                word2cns[word].append(cns)
        else:
            word2cns[word] = [cns]
print(len(cns2word))
if types == "CNS":
    if content not in cns2word:
        print("NO_DATA_FOUND")
    else:
        print(cns2word[content])
else:
    if content not in word2cns:
        print("NO_DATA_FOUND")
    else:
        for i in sorted(word2cns[content]):
            print(i)
