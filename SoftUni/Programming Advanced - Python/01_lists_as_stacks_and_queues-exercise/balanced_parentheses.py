
data = input()

open_parentheses = "{[("

open_symbol_stack = []

for i in range(len(data)):
    symbol = data[i]
    if symbol in open_parentheses:
        open_symbol_stack.append(symbol)
    else:
        if open_symbol_stack:
            if symbol == "}":
                if open_symbol_stack[-1] == "{":
                    open_symbol_stack.pop()
                else:
                    print("NO")
                    raise SystemExit
            elif symbol == "]":
                if open_symbol_stack[-1] == "[":
                    open_symbol_stack.pop()
                else:
                    print("NO")
                    raise SystemExit
            elif symbol == ")":
                if open_symbol_stack[-1] == "(":
                    open_symbol_stack.pop()
                else:
                    print("NO")
                    raise SystemExit
        else:
            print("NO")
            raise SystemExit

print("YES")
