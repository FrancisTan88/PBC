date_str = input()
sep = date_str.split("T")
year = sep[0]
time = ""
if len(sep) >= 2:
    time = sep[1]
ans = ""
hm1 = {"0": "零",
       "1": "一",
       "2": "二",
       "3": "三",
       "4": "四",
       "5": "五",
       "6": "六",
       "7": "七",
       "8": "八",
       "9": "九"}
hm2 = {"0": "零",
       "1": "一",
       "2": "兩",
       "3": "三",
       "4": "四",
       "5": "五",
       "6": "六",
       "7": "七",
       "8": "八",
       "9": "九"}
if year:
    sep_year = year.split("-")
    y, m, d = sep_year[0], sep_year[1], sep_year[2]
    y2c, m2c, d2c = "", "", ""
    for i in y:
        y2c += hm1[i]

    m2c += "十" if m[0] != "0" else ""
    m2c += hm1[m[1]] if m[1] != "0" else ""

    if d[0] != "0":
        d2c += "十" if d[0] == "1" else f"{hm1[d[0]]}十"
    d2c += hm1[d[1]] if d[1] != "0" else ""

    year = f"西元{y2c}年{m2c}月{d2c}日"
if time:
    sep_time = time.split(":")
    hr2c, min2c, sec2c = "", "", ""
    for i in range(len(sep_time)):
        if i == 0:
            hr_int = int(sep_time[i])
            hr2c += "下午" if hr_int >= 12 else "上午"
            if hr_int > 12:
                hr_int %= 12
            if hr_int < 10:
                hr2c += hm2[str(hr_int)]
            elif hr_int == 10:
                hr2c += "十"
            else:
                hr2c += f"十{hm1[str(hr_int)[1]]}"
            hr2c += "點"
        elif i == 1:
            min_int = int(sep_time[i])
            if min_int < 10:
                min2c += hm2[str(min_int)]
            elif min_int == 10:
                min2c += "十"
            elif min_int >= 11 and min_int <= 19:
                min2c += f"十{hm1[str(min_int)[1]]}"
            else:
                if str(min_int)[1] != "0":
                    min2c += f"{hm1[str(min_int)[0]]}十{hm1[str(min_int)[1]]}"
                else:
                    min2c += f"{hm1[str(min_int)[0]]}十"
            min2c += "分"
        else:
            sec_int = int(sep_time[i])
            if sec_int < 10:
                sec2c += hm2[str(sec_int)]
            elif sec_int == 10:
                sec2c += "十"
            elif sec_int >= 11 and sec_int <= 19:
                sec2c += f"十{hm1[str(sec_int)[1]]}"
            else:
                if str(sec_int)[1] != "0":
                    sec2c += f"{hm1[str(sec_int)[0]]}十{hm1[str(sec_int)[1]]}"
                else:
                    sec2c += f"{hm1[str(sec_int)[0]]}十"
            sec2c += "秒"
    time = hr2c + min2c + sec2c
print(year + time)
