for _ in range(int(input())):
    steps = 0
    current_cell = 0
    for __ in range(int(input().split(" ")[0])):
        level = [int(c) for c in input().split(" ")]
        level.sort()
        des_start = level[0]
        des_stop = level[-1]
        if des_start < current_cell:
            steps += current_cell - des_start
            current_cell = des_start
        if des_stop > current_cell:
            steps += des_stop - current_cell
            current_cell = des_stop
    print(steps)
