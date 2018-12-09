with open('day02-puzzle_input.txt') as f:
    puzzle_input = f.read().split()
f.close()

# Lauf durch das gesamte File, Zeile fuer Zeile
for line_counter in range(len(puzzle_input)):
    # Schneide in der Referenzzeile jeweils einen Buchstaben raus und ...
    for position in range(len(puzzle_input[line_counter])):
        # Hol die den aktuellen Code
        test_code_ref = puzzle_input[line_counter]
        # Schneid an der position einen Buchstaben raus
        test_code_ref = test_code_ref[:position] + test_code_ref[(position+1):]

        # ... vergleiche den gekuerzten Code mit allen restlichen Zeilen
        for test_code in puzzle_input[line_counter+1:]:
            # Hol die den aktuellen Verlgeichs-Code
            test_code_comp = test_code
            # Schneid an der position einen Buchstaben raus
            test_code_comp = test_code_comp[:position] + test_code_comp[(position + 1):]
            # Vergleich Referenz mit aktueller Zeile
            if test_code_ref == test_code_comp:
                print (test_code_ref)

exit()
