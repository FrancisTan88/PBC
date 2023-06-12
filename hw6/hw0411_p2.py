# chech if given string contains any key words
def find_keyword(string, kw):
    return any(k in string for k in kw)

# read the input content and build up the sets for the seperators and key words.
content = input()
string = '。，、；：「」『』（）─？！─…﹏《》〈〉．～　,.; !"' + "#$%&'()*+,-./:;<=>?@[\]^_`{¦}~"
key_word = {"大", "蛇", "丸"}
seperator = set()
for i in string:
    seperator.add(i)

# first, we find all positions of seperators in the content.
pos_sep = []
for i in range(len(content)):
    if content[i] in seperator:
        pos_sep.append(i)

# for each paragraph seperated by given seperators, if it contains any key words(i.e. "大", "蛇", "丸"),
# then insert the special sign("!") between each character of it before we concatenate the paragraph to the answer string,
# otherwise, just concatenate the original one. Keep repeating the steps above and we will get the required result.
ans = ""
first_para = content[:pos_sep[0]]
ans += first_para if not find_keyword(first_para, key_word) else "!".join(first_para)
for i in range(len(pos_sep)):
    ans += content[pos_sep[i]]
    if i < len(pos_sep) - 1:
        curr_para = content[pos_sep[i]+1:pos_sep[i+1]]
    else:
        curr_para = content[pos_sep[i]+1:len(content)]
    ans += curr_para if not find_keyword(curr_para, key_word) else "!".join(curr_para)
print(ans)