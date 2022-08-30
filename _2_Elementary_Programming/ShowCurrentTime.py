import time

currentTime = time.time()

totalSeconds = int(currentTime)
print(totalSeconds)

totalMinutes = totalSeconds // 60
print(totalMinutes)

totalHours = totalMinutes // 60
print(totalHours)

remainingMinutes = totalMinutes % 60
print(remainingMinutes)

remainingSeconds = remainingMinutes % 60
print(remainingSeconds)