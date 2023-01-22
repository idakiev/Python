steps_goal = 10000
steps_reached = 0

while True:
    current_steps = input()

    if current_steps != "Going home":
        steps_reached += int(current_steps)
        diff_steps = steps_reached - steps_goal
        if steps_reached >= steps_goal:
            print(f"Goal reached! Good job!\n" f"{diff_steps} steps over the goal!")
            break
        else:
            continue
    else:
        steps_to_home = int(input())
        steps_reached += steps_to_home

        if steps_reached >= steps_goal:
            diff_steps = steps_reached - steps_goal
            print(f"Goal reached! Good job!\n" f"{diff_steps} steps over the goal!")
        else:
            diff_steps = abs(steps_reached - steps_goal)
            print(f"{diff_steps} more steps to reach goal.")
    break
