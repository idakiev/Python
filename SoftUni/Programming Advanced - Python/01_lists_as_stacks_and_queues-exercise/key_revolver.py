
from collections import deque

bullet_price = int(input())

gun_barrel_size = int(input())

bullets = list(map(int, input().split(" ")))

locks = deque(map(int, input().split(" ")))

intelligence_value = int(input())

bullets_used = 0

while bullets:
    fired_bullets = gun_barrel_size
    for i in range(gun_barrel_size):

        if bullets and locks:
            current_bullet = bullets.pop()
            bullets_used += 1
            current_lock = locks[0]

            if current_bullet <= current_lock:
                print(f"Bang!")
                locks.popleft()
                fired_bullets -= 1

            else:
                print(f"Ping!")
                fired_bullets -= 1

    if bullets and fired_bullets == 0:
        print(f"Reloading!")
    if not locks:
        break

diff_money = intelligence_value - (bullets_used * bullet_price)
if not locks:
    print(f"{len(bullets)} bullets left. Earned ${diff_money}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
