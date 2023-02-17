
key_number = int(input())
n = int(input())

decrypted_message = ""

for i in range(n):
    command = input()
    decrypted_message += chr(ord(command) + key_number)

print(decrypted_message)
