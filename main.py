import sys
import getopt
import random
import time
import matplotlib.pyplot as plt
from dir.PetantsQueue import PetantsQueue


def generateProblem(n):
    petants = list()

    for i in range(n):
        petants.append(random.randint(1, 4))

    return petants


if __name__ == "__main__":
    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, "h:m:n:k:s:r:")
    except getopt.GetoptError as err:
        print('test.py -m 1')
        print('test.py -m 2 -n <n_value>')
        print('test.py -m 3 -n <n_value> -k <number_of_steps> -s <value_of_step> -r <number of instances>')

        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('test.py -m 1')
            print('test.py -m 2 -n <n_value>')
            print('test.py -m 3 -n <n_value> -k <number_of_steps> -s <value_of_step> -r <number of instances>')

            sys.exit()

        elif opt == '-m':
            if arg == '1':
                n = int(input())
                inp = input()
                petants = [int(i) for i in inp.split()]
                qu = PetantsQueue(n, petants)
                score = qu.solve()
                print(score)

            elif arg == '2':
                n = int(opts[1][1])
                petants = generateProblem(n)
                qu = PetantsQueue(n, petants)

                score = qu.solve()

                print(score)

            elif arg == '3':
                n = int(opts[1][1])
                k = int(opts[2][1])
                step = int(opts[3][1])
                r = int(opts[4][1])
                timeMeasue = list()
                ns = list()

                for i in range(k):
                    size = n + i * step
                    ns.append(size)
                    timeList = list()

                    for j in range(r):
                        petants = generateProblem(size)
                        qu = PetantsQueue(size, petants)
                        start = time.clock()
                        qu.solve()
                        stop = time.clock()

                        timeList.append(stop - start)

                    avg = 0
                    for value in timeList:
                        avg += value

                    avg /= r
                    timeMeasue.append(avg)

                plt.plot(ns, timeMeasue)
                plt.show()

                for i in range(k):
                    s = "n = " + str(n + i * step)
                    s += " time = " + str(timeMeasue[i])
                    s += " q = " + str(
                        (timeMeasue[i] * (n + (int(k / 2) * step))) / ((n + i * step) * timeMeasue[int(k / 2)]))
                    print(s)

            sys.exit()
