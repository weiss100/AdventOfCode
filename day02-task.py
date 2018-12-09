import string

with open('day02-puzzle_input.txt') as f:
    puzzle_input = f.read().split()
f.close()

abc = list(string.ascii_lowercase)

counter_2 = 0
counter_3 = 0


for id_code in puzzle_input:
    check_2 = False
    check_3 = False

    for letter in abc:
        if not check_2 and id_code.count(letter) == 2:
            print(id_code, letter, id_code.count(letter))
            check_2 = True
            counter_2 += 1

        if not check_3 and id_code.count(letter) == 3:
            print (id_code, letter, id_code.count(letter))
            check_3 = True
            counter_3 += 1

        if check_2 and check_3:
            break

print ("\nI found {} time 2, and {} times 3.".format(counter_2, counter_3))
print ("Thus the checksum is " + repr(counter_2*counter_3))