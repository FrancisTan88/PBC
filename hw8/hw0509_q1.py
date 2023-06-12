def combination(pool, pick):
    if pool < pick:
        return 0
    mother = child = 1
    tmp = pool - pick
    for _ in range(tmp):
        mother *= pool
        child *= tmp
        pool -= 1
        tmp -= 1
    return mother // child


def cal_a(points):
    return 5 * points.count(1)


def cal_b(points):
    score = 0
    for i in range(1, 14):
        score += 10 * combination(points.count(i), 2)
    return score


def cal_c(colors, colors_pool) -> bool:
    for color in colors_pool:
        if colors.count(color) == 5:
            return True
    return False


def cal_d(points) -> bool:
    points.sort()
    for i in range(4):
        if (points[i+1] != points[i] + 1) and (points[i+1] != points[i] + 9):
            return False
    return True


def cal_e(points):
    three = 0
    for i in range(1, 14):
        if points.count(i) == 3:
            three = i
    for j in range(1, 14):
        if three and j != three and \
                points.count(j) == 2:
            return 80
    return 0


def cal_f(points):
    for i in range(1, 14):
        if points.count(i) == 5:
            return 500
    for i in range(1, 14):
        if points.count(i) == 4:
            return 100
    return 0


colors = [i for i in input().split(",")]
points = [i for i in input().split(",")]
colors_pool = ["S", "H", "D", "C"]
for i in range(len(points)):
    if points[i] == "A":
        points[i] = 1
    elif points[i] == "J":
        points[i] = 11
    elif points[i] == "Q":
        points[i] = 12
    elif points[i] == "K":
        points[i] = 13
    else:
        points[i] = int(points[i])

total_score = 0
total_score += cal_a(points)
total_score += cal_b(points)
is_same_color = cal_c(colors, colors_pool)
total_score += is_same_color * 30
is_continuous = cal_d(points)
total_score += is_continuous * 50
total_score += 300 * (is_same_color and is_continuous)
total_score += cal_e(points)
total_score += cal_f(points)
print(total_score)
