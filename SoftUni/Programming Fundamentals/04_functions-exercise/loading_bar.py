progress_percent = int(input())


def loading_bar(number):
    current_progress = "[..........]"
    progress = current_progress.replace(".", "%", int(number/10))

    if number == 100:
        print("100% Complete!")
        print(progress)
    else:
        print(f"{number}% {progress}")
        print("Still loading...")


loading_bar(progress_percent)
