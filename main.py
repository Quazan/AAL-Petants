import sys
import getopt
import random

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
            if i+1 < n and currentOfficial != findMaxOfficial(i+1, matrix, currentOfficial):
                currentOfficial = findMaxOfficial(i, matrix, currentOfficial)

    return score


def findMaxOfficial(column, matrix, currentOfficial):
    maxOfficial = 0
    max = -1

    for i in range(6):
        if matrix[i][column] > max:
            max = matrix[i][column]
            maxOfficial = i

        if matrix[i][column] == max and i == currentOfficial:
            maxOfficial = i

    return maxOfficial

def pretenders(petants, n, i, currentOfficial, pretendingOfficial, score):

    for j in range(i + 1, n):
        if petants[j] != currentOfficial[0] and petants[j] != currentOfficial[1] and (petants[j] == pretendingOfficial[0] or petants[j] == pretendingOfficial[1]):
            currentOfficial = pretendingOfficial
            break

        elif petants[j] != pretendingOfficial[0] and petants[j] != pretendingOfficial[1] and (petants[j] == currentOfficial[0] or petants[j] == currentOfficial[1]):
            break

        elif petants[j] != currentOfficial[0] and petants[j] != currentOfficial[1] and petants[j] != pretendingOfficial[0] and petants[j] != pretendingOfficial[1]:
            if j < n-1 and (petants[j+1] == currentOfficial[0] or petants[j+1] == currentOfficial[1]) and (petants[j+1] == pretendingOfficial[0] or petants[j+1] == pretendingOfficial[1]):
                currentOfficial, score = pretenders(petants, n, j, currentOfficial, pretendingOfficial, score)
            elif j < n-1 and  petants[j+1] != currentOfficial[0] and petants[j+1] != currentOfficial[1] and (petants[j+1] == pretendingOfficial[0] or petants[j+1] == pretendingOfficial[1]):
                currentOfficial = pretendingOfficial
            break
    return currentOfficial, score

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

                    else:
                        pretendingOfficial = (petants[i], petants[i+1])
                        currentOfficial, score = pretenders(petants, n, i, currentOfficial, pretendingOfficial, score)

                else:
                    currentOfficial = (petants[i], 0)

                    for j in range(i+1, n):
                        if currentOfficial[1] == 0 and petants[j] != currentOfficial[0]:
                            currentOfficial = (currentOfficial[0], petants[j])

                        if petants[j] != currentOfficial[0] and petants[j] != currentOfficial[1]:
                            i = j - 1
                            break
                        elif j == n - 1:
                            i = j

        i += 1

    return score


def findTwoElements(table, index, limit):
    lista = list()

    for i in range(index, limit):
        if table[i] not in lista:
            lista.append(table[i])

            if len(lista) == 2:
                return lista[0], lista[1]

    return lista[0], lista[0] % 4 + 1

def generateProblem(n):
    petants = list()

    for i in range(0, n):
        petants.append(random.randint(1, 4))
        #print(petants)

    return petants


if __name__ == "__main__":
    argv = sys.argv[1:]

    n = 100000
    a = 1
    b = 1
    #petants = [3, 1, 1, 4, 3, 1]
    #print(firstAlg(n, petants))
    #print(secondAlg(n, petants))

    while a == b:
        petants = generateProblem(n)
        a = secondAlg(n, petants)
        b = firstAlg(n, petants)

    print(a)
    print(b)
    print(petants)

    try:
        opts, args = getopt.getopt(argv, "h:m:n:k:step:r")
    except getopt.GetoptError as err:
        print('test.py -m 1')
        print('test.py -m 2 -n <n_value>')
        print('test.py -m 3 -n <n_value> -k <number_of_steps> -step <value_of_step> -r <number of instances>')

        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('test.py -m 1')
            print('test.py -m 2 -n <n_value>')
            print('test.py -m 3 -n <n_value> -k <number_of_steps> -step <value_of_step> -r <number of instances>')

            sys.exit()

        elif opt == '-m':
            if arg == '1':
                n = int(input())
                inp = input()
                petants = [int(i) for i in inp.split()]
                secondAlg(n, petants)

            elif arg == '2':
                n = int(opts[1][1])
                a = 1
                b = 0
                while a != b:
                    petants = generateProblem(n)
                    a = secondAlg(n, petants)
                    b = firstAlg(n ,petants)
                    print(a + " " + b)

                print(petants)

            elif arg == '3':
                print(3)

            sys.exit()

