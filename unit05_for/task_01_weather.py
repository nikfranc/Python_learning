currWeather = float(input())
days = 0
while currWeather < 22:
    days += 1
    currWeather = float(input())
print(days // 7)