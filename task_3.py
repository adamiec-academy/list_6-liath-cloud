def play(starting_board, turns):

    # Creating variable to store changed map
    updated_board = [['' for s in range(len(starting_board[0]))] for z in range(len(starting_board))]

    for i in range(turns):

        for n in range(len(starting_board[0])):
            for m in range(len(starting_board)):

                n_max = len(starting_board[1]) - 1
                m_max = len(starting_board) - 1

                neighbours = []

                # Sprawdzenie czy komrka jest żywa i jej sonsiadow
                if  n == 0:
                    if m == 0:
                        neighbours.append(starting_board[1][0])
                        neighbours.append(starting_board[0][1])
                        neighbours.append(starting_board[1][1])

                    elif m == m_max:
                        neighbours.append(starting_board[m_max - 1][0])
                        neighbours.append(starting_board[m_max][1])
                        neighbours.append(starting_board[m_max - 1][1])

                    else:
                        neighbours.append(starting_board[m - 1][0])
                        neighbours.append(starting_board[m + 1][0])
                        neighbours.append(starting_board[m - 1][1])
                        neighbours.append(starting_board[m][1])
                        neighbours.append(starting_board[m + 1][1])

                elif  n == n_max:
                    if m == 0:
                        neighbours.append(starting_board[0][n_max])
                        neighbours.append(starting_board[1][n_max])
                        neighbours.append(starting_board[0][n_max - 1])

                    elif m == m_max:
                        neighbours.append(starting_board[m_max - 1][n_max])
                        neighbours.append(starting_board[m_max][n_max - 1])
                        neighbours.append(starting_board[m_max - 1][n_max - 1])

                    else:
                        neighbours.append(starting_board[m - 1][n_max])
                        neighbours.append(starting_board[m + 1][n_max])
                        neighbours.append(starting_board[m - 1][n_max - 1])
                        neighbours.append(starting_board[m][n_max - 1])
                        neighbours.append(starting_board[m + 1][n_max - 1])

                elif  m == 0:
                    neighbours.append(starting_board[0][n - 1])
                    neighbours.append(starting_board[0][n + 1])
                    neighbours.append(starting_board[1][n - 1])
                    neighbours.append(starting_board[1][n])
                    neighbours.append(starting_board[1][n + 1])

                elif  m == m_max:
                    neighbours.append(starting_board[m_max][n - 1])
                    neighbours.append(starting_board[m_max][n + 1])
                    neighbours.append(starting_board[m_max - 1][n - 1])
                    neighbours.append(starting_board[m_max - 1][n])
                    neighbours.append(starting_board[m_max - 1][n + 1])

                else:
                    neighbours.append(starting_board[m - 1][n - 1])
                    neighbours.append(starting_board[m - 1][n])
                    neighbours.append(starting_board[m - 1][n + 1])
                    neighbours.append(starting_board[m][n - 1])
                    neighbours.append(starting_board[m][n + 1])
                    neighbours.append(starting_board[m + 1][n - 1])
                    neighbours.append(starting_board[m + 1][n])
                    neighbours.append(starting_board[m + 1][n + 1])

                neighbour_count = neighbours.count('X')

                if neighbour_count == 3 and starting_board[m][n] == ".":
                    updated_board[m][n] = "X"

                elif starting_board[m][n] == "X":
                    if neighbour_count == 3:
                        updated_board[m][n] = "X"

                    elif neighbour_count == 2:
                        updated_board[m][n] = "X"

                    else:
                        updated_board[m][n] = "."

                else:
                    updated_board[m][n] = starting_board[m][n]

        starting_board = updated_board[:][:]
        updated_board = [['' for s in range(len(starting_board[0]))] for z in range(len(starting_board))]


    return starting_board
