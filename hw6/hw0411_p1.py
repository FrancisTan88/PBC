# string matching
def string_match(string, content, pos):
    if pos + len(string) - 1 >= len(content):
        return False

    for i in range(len(string)):
        if string[i] != content[pos + i]:
            return False

    return True


# read the input data
string1 = input()
string2 = input()
distance = int(input())
content = input()
# check the correctness of input data
if (len(string1) < 1 or len(string1) > 10000) or (len(string2) < 1 or len(string2) > 10000) or \
        (len(content) < 1 or len(content) > 10000) or (distance < 0 or distance > 1000):
    print("ILLEGAL_INPUT")
else:
    ans = []
    # we scan all the characters, if there is a match with one of the two strings, we scan the continuing characters
    # and check if there is one another match with the other string within the valid range(i.e. must meet the distance constraint).
    for i in range(len(content)):
        if string_match(string1, content, i):
            for j in range(i+len(string1), i+len(string1)+distance):
                if string_match(string2, content, j):
                    ans.append(content[i:j+len(string2)])
        elif string_match(string2, content, i):
            for j in range(i+len(string1), i+len(string1)+distance):
                if string_match(string1, content, j):
                    ans.append(content[i:j+len(string1)])
    # if "ans" is empty, it means that there is no substring that meets our requirement.
    if not ans:
        print("^^NOT_FOUND^^")
    else:
        for substr in ans:
            print(substr)
