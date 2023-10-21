def get_rank(char):
    return "abcdefghijklmopqrstuvwxyz".index(char)


def get_char(rank):
    return "abcdefghijklmopqrstuvwxyz"[rank]


for _ in range(int(input())):
    super_spell = ""
    for __ in range(int(input())):
        super_spell += get_char(min([get_rank(c) for c in input()]))
    print(super_spell)
