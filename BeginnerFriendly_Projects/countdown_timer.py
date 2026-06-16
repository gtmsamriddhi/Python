from time import sleep
count = 10
while count > 0:
    print(count)
    sleep(1)
    count -= 1
print("Done")

import time

hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

total_seconds = hours * 3600 + minutes * 60 + seconds

while total_seconds > 0:
    hrs = total_seconds // 3600
    mins = (total_seconds % 3600) // 60
    secs = total_seconds % 60

    print(f"\r{hrs:02d}:{mins:02d}:{secs:02d}", end="")
    time.sleep(1)
    total_seconds -= 1

print("\r00:00:00")
print("Time's up!")