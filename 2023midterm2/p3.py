def process_number(number, hm):
    integer = int(number)
    output = ""
    if integer >= 10:
        if number[0] == "1":
            output += "十"
        else:
            output += f"{hm[number[0]]}十"
        if number[1] != "0":
            output += hm[number[1]]
        return output
    return hm[number]
            

data = input()
hm = {"0": "零",
       "1": "一",
       "2": "二",
       "3": "三",
       "4": "四",
       "5": "五",
       "6": "六",
       "7": "七",
       "8": "八",
       "9": "九"}
ans = ""
if "+" in data:
    data = data.split("+")
    left = data[0]
    right = data[1]
    up, down = right.split("/")[0], right.split("/")[1]
    ans = f"{process_number(left, hm)}又{process_number(down, hm)}分之{process_number(up, hm)}"
else:
    up, down = data.split("/")[0], data.split("/")[1]
    ans = f"{process_number(down, hm)}分之{process_number(up, hm)}"
print(ans)
