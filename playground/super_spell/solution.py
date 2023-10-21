def get_lexicographically_smallest(s, c):
    i = 0
    while i < len(s):
        if super_spell[i] > c:
            s = s[:i] + c + s[i:]
            return s
        i = i + 1
    s = s + c
    return s


if __name__ == "__main__":
    for _ in range(int(input())):
        super_spell = ""
        for __ in range(int(input())):
            chars = list(input())
            chars.sort()
            super_spell = get_lexicographically_smallest(super_spell, chars[0])

        print(super_spell)
