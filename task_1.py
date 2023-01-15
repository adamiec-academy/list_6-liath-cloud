from random import shuffle

def generate_assignments(previous_assignment, coders):
    coders_values = coders[:]
    new_assignment = {}
    check = 1

    while check != 0:
        random.shuffle(coders_values)
        check = 0

        for j in range(len(coders)):

            if coders_values[j] == coders[j] or coders_values[j] == coders[coders_values.index(coders[j])]:
                check += 1

            if coders[j] in previous_assignment.keys() and previous_assignment[coders[j]] == coders_values[j]:
                check += 1

    for j in range(len(coders)):
        new_assignment[coders[j]] = coders_values[j]

    return new_assignment
