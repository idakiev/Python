exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time_min = exam_hour * 60 + exam_minutes
arrival_time_min = arrival_hour * 60 + arrival_minutes

diff_min = abs(exam_time_min - arrival_time_min)


if exam_time_min < arrival_time_min and 1 <= diff_min < 60:
    print("Late")
    print(f"{diff_min} minutes after the start")
elif exam_time_min < arrival_time_min and diff_min >= 60:
    diff_hour = diff_min // 60
    diff_min = diff_min % 60
    print("Late")
    print(f"{diff_hour}:{diff_min:02d} hours after the start")


if exam_time_min >= arrival_time_min and 0 <= diff_min <= 30:
    print("On time")
    if arrival_time_min < exam_time_min and diff_min <= 30:
        print(f"{diff_min} minutes before the start")
if exam_time_min > arrival_time_min and 30 < diff_min < 60:
    print("Early")
    print(f"{diff_min} minutes before the start")
elif exam_time_min > arrival_time_min and diff_min >= 60:
    diff_hour = diff_min // 60
    diff_min = diff_min % 60
    print("Early")
    print(f"{diff_hour}:{diff_min:02d} hours before the start")
