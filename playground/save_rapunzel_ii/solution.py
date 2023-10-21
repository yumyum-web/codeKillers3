def search_leader(leaderspace, soldier):
    if not leaderspace:
        return None

    limit = soldier * 2
    if len(leaderspace) == 1:
        if leaderspace[0] <= limit:
            return leaderspace[0]
        else:
            return None

    middle = len(leaderspace) // 2

    if leaderspace[middle] == limit:
        return limit
    elif leaderspace[middle] < limit:
        right_result = search_leader(
            leaderspace[(middle + 1):], limit  # fmt: skip
        )
        if right_result is not None:
            return right_result
        else:
            return leaderspace[middle]
    else:
        return search_leader(leaderspace[:middle], limit)


if __name__ == "__main__":
    for _ in range(int(input())):
        input()
        leaders = []
        soldiers = [int(s) for s in input().split(" ")]
        sorted_soldiers = soldiers[:]
        sorted_soldiers.sort()
        for s in soldiers:
            s_leaderspace = sorted_soldiers[:]
            s_leaderspace.remove(s)
            leader = search_leader(s_leaderspace, s) or -1
            leaders.append(leader)
        print(*leaders)
