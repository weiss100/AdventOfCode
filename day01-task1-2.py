with open('day01-puzzle_input.txt') as f:
    puzzle_input = f.read().split()
f.close()

# puzzle_input = [+7, +7, -2, -7, -4 ]
# print (puzzle_input)

summe = 0
summe_items = []
loop = 0
while True:
    loop = loop + 1
    print("Loop", loop, summe)
    for i in puzzle_input:
        summe = summe + int(i)
        summe_items = summe_items + [summe]
        if summe in summe_items[:-1]:
            print(summe)
            exit()
