if __name__ == "__main__":
    for _ in range(int(input())):
        steps = 0
        start_cell = 0
        for __ in range(int(input().split(" ")[0])):
            level = [int(c) for c in input().split(" ")]
            level.sort()
            des_start = level[0]
            des_stop = level[-1]
            if des_start < start_cell:
                steps += start_cell - des_start
                if des_stop <= start_cell:
                    start_cell = des_start
                else:
                    steps += des_stop - des_start
                    start_cell = des_stop
            else:
                steps += des_stop - start_cell
                start_cell = des_stop
        print(steps)
