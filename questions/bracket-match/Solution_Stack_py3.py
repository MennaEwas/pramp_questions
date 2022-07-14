def bracket_match(text):
    print(text)
    stack = []
    count = 0
    for i in range(len(text)):
        print(text[i])
        if text[i] == '(':
            stack.append(text[i])
        else:
            if not len(stack):
                count += 1
            else:
                stack.pop()

    # print(count, len(stack))
    return count + len(stack)
