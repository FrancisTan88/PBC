def cal_score(points, colors, colors_pool):
    def combination(pool, pick):
        if pool < pick:
            return 0
        if pool == pick:
            return 1
        mother = child = 1
        # tmp = pool - pick
        for _ in range(pick):
            mother *= pool
            child *= pick
            pool -= 1
            pick -= 1
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
        tmp = sorted(points)
        for i in range(4):
            if (tmp[i+1] != tmp[i] + 1) and \
                    (tmp[i+1] != tmp[i] + 9):
                return False
        return True

    def cal_e(points):
        for i in range(1, 14):
            if points.count(i) == 3:
                for j in range(1, 14):
                    if j != i and points.count(j) == 2:
                        return 80
                return 0
        return 0

    def cal_f(points):
        for i in range(1, 14):
            if points.count(i) == 5:
                return 500
            elif points.count(i) == 4:
                return 100
        return 0

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
    return total_score


def preprocess(curr_points):
    for i in range(len(curr_points)):
        if curr_points[i] == "A":
            curr_points[i] = 1
        elif curr_points[i] == "J":
            curr_points[i] = 11
        elif curr_points[i] == "Q":
            curr_points[i] = 12
        elif curr_points[i] == "K":
            curr_points[i] = 13
        else:
            curr_points[i] = int(curr_points[i])
    return curr_points


colors_pool = ["S", "H", "D", "C"]
max_score = -1
max_nums = []
people = int(input())
for j in range(people):
    curr_colors, curr_points = [], []
    for card in input().split(","):
        curr_colors.append(card[0])
        curr_points.append(card[1:])
    curr_points = preprocess(curr_points)
    score = cal_score(curr_points, curr_colors, colors_pool)
    if score > max_score:
        max_nums = [j+1]
        max_score = score
    elif score == max_score:
        max_nums.append(j+1)
print(",".join(list(map(str, max_nums))))
