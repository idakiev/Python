budget = int(input())

costs = 0
command = ""

while command != "End":
    command = input()
    if command != "End":
        costs += int(command)
    if costs > budget:
        print("You went in overdraft!")
        break
    else:
        continue
if costs <= budget:
    print("You bought everything needed.")
