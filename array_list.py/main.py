num_of_days = int(input("How many day's temperature? "))
total = 0
temp = []
for i in range(num_of_days):
    next_day = int(input(f"Day {i}'s high temp: "))
    temp.append(next_day)
    total += temp[i]


avg = round(total/num_of_days, 2)
print(f"\nAverage = {avg}")

above = 0
for i in temp:
    if i > avg:
        above += 1
print(f"{above} day(s) above average")
