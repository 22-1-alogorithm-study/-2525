hour, minute = map(int, input().split())
cooking_time = int(input())

min_result = cooking_time + minute
stack = 0
# while min_result >= 60:
stack = min_result // 60
min_result %= 60

hour_result = hour + int(stack)
if hour_result >= 24:
    hour_result -= 24
else:
    pass

print(hour_result, min_result)
