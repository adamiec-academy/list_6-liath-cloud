def get_seats(seats_number, votes_data):
    new_votes_data = votes_data.copy()
    votes = []

    for key, value in votes_data.items():
        new_value = [value]
        votes.append(value)

        for i in range(2, seats_number + 1):
            new_value.append(value/(i))
            votes.append(value/i)

        votes_data[key] = new_value
        new_votes_data[key] = 0

    votes.sort(reverse=True)

    for key, value in votes_data.items():
        common = set(value) & set(votes[:seats_number])
        new_votes_data[key] = len(common)

    return new_votes_data
