

def next_version(version: list):
    number_from_version = "".join(version)
    new_version = int(number_from_version) + 1
    final_version = []
    for i in range(len(str(new_version))):
        new_version_string = str(new_version)
        current_number = new_version_string[i]
        final_version.append(current_number)

    return final_version


current_version = input().split(".")

print(".".join(next_version(current_version)))
