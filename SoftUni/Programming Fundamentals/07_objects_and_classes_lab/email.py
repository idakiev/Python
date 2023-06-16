
class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
command = input()

while command != "Stop":
    current_command = command.split(" ")
    current_sender = current_command[0]
    current_receiver = current_command[1]
    current_content = current_command[2]
    email = Email(current_sender, current_receiver, current_content)
    emails.append(email)
    command = input()


send_emails = list(map(lambda x: int(x), input(). split(", ")))

for y in send_emails:
    emails[y].send()

for email in emails:
    print(email.get_info())
