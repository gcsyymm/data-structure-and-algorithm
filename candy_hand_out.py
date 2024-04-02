def candies(child_marks: list) -> list:
    if not child_marks:
        return 0
    left_asc = [1]*len(child_marks)
    right_asc = [1]*len(child_marks)
    for i in range(1, len(child_marks)):
        if child_marks[i] > child_marks[i-1]:
            left_asc[i] = left_asc[i] + 1
    res = left_asc[-1]
    for i in range(len(child_marks)-1, 0, -1):
        if child_marks[i-1] > child_marks[i]:
            right_asc[i-1] = right_asc[i] + 1
        res += max(right_asc[i-1], left_asc[i-1])
    return res


test = [1, 0, 2]
print(candies(test))
