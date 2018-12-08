with open('day01-puzzle_input.txt') as f:
    puzzle_input = f.read().split()
f.close()

# puzzle_input = [+7, +7, -2, -7, -4 ]
# print (puzzle_input)

# Loop 139
# 488

summe = 0
freq = [None] * 200000
loop = 0
while True:
    loop = loop + 1
    print("Loop", loop)
    for i in puzzle_input:
        summe = summe + int(i)
        if freq[summe + 100001] == "found":
            print(summe)
            exit()
        else:
            freq[summe + 100001] = "found"
