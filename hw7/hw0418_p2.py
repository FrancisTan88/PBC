cns_uni_path = input()
cns_pho_path = input()
input_word = input()
cns2word, word2cns = {}, {}
cns2pho, pho2cns = {}, {}
with open(cns_uni_path, "r", encoding="utf-8") as f:
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
with open(cns_pho_path, "r", encoding="utf-8") as f2:
    for row in f2:
        c, pho = row.split()
        if c in cns2pho:
            if pho not in cns2pho[c]:
                cns2pho[c].append(pho)
        else:
            cns2pho[c] = [pho]
        if pho in pho2cns:
            if c not in pho2cns[pho]:
                pho2cns[pho].append(c)
        else:
            pho2cns[pho] = [c]
print(len(cns2pho))
if input_word not in word2cns:
    print("NO_CNS_DATA")
    exit()
idx_cns = sorted(word2cns[input_word])
ans = []
s = set()
for i in idx_cns:
    if i in cns2pho:
        for j in cns2pho[i]:
            if j not in s:
                ans.append(j)
                s.add(j)
if not ans:
    print("NO_PHONETIC_DATA")
else:
    for k in ans:
        print(k)
