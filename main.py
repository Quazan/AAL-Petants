import sys
import getopt


def firstAlg(n, petants):

    matrix = [[0 for x in range(n)] for y in range(6)]
    officials = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

    for i in range(6):
        inc = 0
        for j in range(n-1, -1, -1):
            if petants[j] == officials[i][0] or petants[j] == officials[i][1]:
                inc += 1
                matrix[i][j] = inc
            else:
                inc = 0

    score = n * 5
    currentOfficial = 0

    for i in range(n):
        if matrix[currentOfficial][i] == 0:
            score += 5
            if i+1 < n and currentOfficial != findMaxOfficial(i+1, matrix):
                currentOfficial = findMaxOfficial(i, matrix)

    print(score)


def findMaxOfficial(column, matrix):
    maxOfficial = 0
    max = -1
    for i in range(6):
        if matrix[i][column] > max:
            max = matrix[i][column]
            maxOfficial = i

    return maxOfficial

def secondAlg(n, petants):

    currentOfficial = (1, 2)

    score = 5 * n
    i = 0
    while i < n:
        if petants[i] != currentOfficial[0] and petants[i] != currentOfficial[1]:
            score += 5
            if i + 1 < n:
                if petants[i+1] == currentOfficial[0] or petants[i+1] == currentOfficial[1]:    #sytuacja w  której mogę obsłużyć i+1 osobę
                    if i + 2 < n and petants[i+2] != currentOfficial[0] and petants[i+2] != currentOfficial[1]:
                        currentOfficial = (petants[i], petants[i+1])
                        print(str(currentOfficial) + " " + str(i) + " tutaj")
                    else:               # 1 2 3 1 1 1 1 3 3 3 3   / 1 2 3 1 1 1 1 2 2 2 2
                        pretendingOfficial = (petants[i], petants[i+1])
                        for j in range(i+1, n):
                            if petants[j] != currentOfficial[0] and petants[j] != currentOfficial[1] and (petants[j] == pretendingOfficial[0] or petants[j] == pretendingOfficial[1]):
                                currentOfficial = pretendingOfficial
                                i = j
                                break
                            elif petants[j] != pretendingOfficial[0] and petants[j] != pretendingOfficial[1] and (petants[j] == currentOfficial[0] or petants[j] == currentOfficial[1]):
                                i = j
                                break
                            elif petants[j] != currentOfficial[0] and petants[j] != currentOfficial[1] and petants[j] != pretendingOfficial[0] and petants[j] != pretendingOfficial[1]:
                                i = j-1
                                break
                            elif j == n - 1:
                                i = j
                else:
                    """nie mogę dwóch pod rząd więc lecę ze zmnienionym urzędnikiem"""
                    currentOfficial = (petants[i], 0)
                    print(str(currentOfficial) + " " + str(i))
                    for j in range(i+1, n):
                        if currentOfficial[1] == 0 and petants[j] != currentOfficial[0]:
                            currentOfficial = (currentOfficial[0], petants[j])

                        if petants[j] != currentOfficial[0] and petants[j] != currentOfficial[1]:
                            i = j - 1
                            break
                        elif j == n - 1:
                            i = j
                    print(str(currentOfficial) + " " + str(i))
        i += 1

    print(score)


def findTwoElements(table, index, limit):
    lista = list()
    for i in range(index, limit):
        if table[i] not in lista:
            lista.append(table[i])
            if len(lista) == 2:
                return (lista[0], lista[1])

    return (lista[0], lista[0] % 4 + 1)


if __name__ == "__main__":
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "h:m:n:k:step:r")
    except getopt.GetoptError as err:
        print('test.py -m 1')
        print('test.py -m 2 -n <n_value>')
        print('test.py -m 3 -n <n_value> -k <number_of_steps> -step <value_of_step> -r <number of instances>')
        sys.exit(2)

    for opt, arg in opts:
        print(arg)
        if opt == '-h':
            print('test.py -m 1')
            print('test.py -m 2 -n <n_value>')
            print('test.py -m 3 -n <n_value> -k <number_of_steps> -step <value_of_step> -r <number of instances>')
            sys.exit()
        elif opt == '-m':
            if arg == '1':
                n = int(input())
                str = input()
                petants = [int(i) for i in str.split()]
                secondAlg(n, petants)

            elif arg == '2':
                print(2)
            elif arg == '3':
                print(3)

