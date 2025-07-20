def sort_stack(stack):
    output_stack = []
    while len(stack) > 0:
        value = stack.pop()
        while len(output_stack) > 0 and output_stack[-1] > value:
            stack.append(output_stack.pop())
        output_stack.append(value)
    return output_stack

if __name__ == "__main__":
    stack = [3,1,2]
    print(sort_stack(stack))