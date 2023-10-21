def orders(selector: str, materials: int):
    num_orders = 0
    if not selector:
        return 1
    if selector[0] == "0":
        return orders(selector[1:], materials)
    num_orders += orders(selector[1:], materials)
    if len(selector) >= 2 and int(selector[:2]) <= materials:
        num_orders += orders(selector[2:], materials)
    if len(selector) >= 3 and int(selector[:3]) <= materials:
        num_orders += orders(selector[3:], materials)
    return num_orders


if __name__ == "__main__":
    for _ in range(int(input())):
        m = int(input())
        s = input()
        print(orders(s, m))
