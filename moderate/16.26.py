def calculator(expr: str) -> int:
    # Remove spaces
    expr = expr.replace(' ', '')
    nums = []
    ops = []
    i = 0
    while i < len(expr):
        if expr[i].isdigit() or (expr[i] == '-' and (i == 0 or not expr[i-1].isdigit())):
            # Num or unary -
            sign = -1 if expr[i] == '-' else 1
            if expr[i] == '-':
                i += 1
            num = 0
            while i < len(expr) and expr[i].isdigit():
                num = num * 10 + int(expr[i])
                i += 1
            nums.append(sign * num)
            continue
        # Op
        while ops and (expr[i] in '+-' and ops[-1] in '*/' or expr[i] == ops[-1]):
            b, a = nums.pop(), nums.pop()
            op = ops.pop()
            if op == '+': nums.append(a + b)
            elif op == '-': nums.append(a - b)
            elif op == '*': nums.append(a * b)
            elif op == '/': nums.append(a // b)  # Integer div
        ops.append(expr[i])
        i += 1
    while ops:
        b, a = nums.pop(), nums.pop()
        op = ops.pop()
        if op == '+': nums.append(a + b)
        elif op == '-': nums.append(a - b)
        elif op == '*': nums.append(a * b)
        elif op == '/': nums.append(a // b)
    return nums[0]