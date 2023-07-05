
path_file = input().split("\\")

file_location = list(path_file[-1])

file_name = file_location[:file_location.index(".")]
file_extension = file_location[file_location.index(".") + 1:]

print(f"File name: {''.join(file_name)}")
print(f"File extension: {''.join(file_extension)}")
