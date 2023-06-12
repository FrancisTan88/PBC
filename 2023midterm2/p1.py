text = input()
name = "陳林黃張李王吳劉蔡楊許鄭謝郭洪曾邱廖賴周徐蘇葉莊呂江何蕭羅高簡朱鍾施游詹沈彭胡余盧潘顏梁趙柯翁魏方孫戴范宋鄧杜侯曹薛傅丁溫紀蔣歐藍連唐馬董石卓程姚康馮古姜湯汪白田涂鄒巫尤鐘龔嚴韓黎阮袁童陸金錢邵"
# after_name = "先生,小姐,姓"
n = len(text)
hm = {}
for i in name:
    hm[i] = 0
for i in range(n):
    if text[i] in hm:
        if i+1 <= n-1:
            if text[i+1] == "姓":
                hm[text[i]] += 1
        if i+2 <= n-1:
            if text[i+1:i+3] == "先生" or text[i+1:i+3] == "小姐":
                hm[text[i]] += 1
        if i-1 >= 0:
            if text[i-1] == "姓":
                hm[text[i]] += 1
ans = []
for k, v in hm.items():
    if v != 0:
        ans.append([k, v])
ans.sort(key=lambda x: x[1], reverse=True)
for name, times in ans:
    print(f"{name}:{str(times)}")
