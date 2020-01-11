import sys
import getopt
import random
import time
import matplotlib.pyplot as plt
from dir.PetitionersQueue import PetitionersQueue


def generateProblem(n):
    petitioners = list()

    for i in range(n):
        petitioners.append(random.randint(1, 4))

    return petitioners


if __name__ == "__main__":
    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, "h:m:n:k:s:r:")
    except getopt.GetoptError as err:
        print('main.py -m 1')
        print('main.py -m 2 -n <n_value>')
        print('main.py -m 3 -n <n_value> -k <number_of_steps> -s <value_of_step> -r <number of instances>')

        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('main.py -m 1')
            print('main.py -m 2 -n <n_value>')
            print('main.py -m 3 -n <n_value> -k <number_of_steps> -s <value_of_step> -r <number of instances>')

            sys.exit()

        elif opt == '-m':
            if arg == '1':
                n = int(input())
                inp = input()
                petitioners = [int(i) for i in inp.split()]
                qu = PetitionersQueue(n, petitioners)
                score = qu.solve()
                print(score)

            elif arg == '2':
                n = int(opts[1][1])
                petitioners = generateProblem(n)
                qu = PetitionersQueue(n, petitioners)

                score = qu.solve()

                print(score)

            elif arg == '3':
                n = int(opts[1][1])
                k = int(opts[2][1])
                step = int(opts[3][1])
                r = int(opts[4][1])
                timeMeasure = list()
                ns = list()

                for i in range(k):
                    size = n + i * step
                    ns.append(size)
                    timeList = list()

                    for j in range(r):
                        petitioners = generateProblem(size)
                        qu = PetitionersQueue(size, petitioners)
                        start = time.perf_counter()
                        qu.solve()
                        stop = time.perf_counter()

                        timeList.append(stop - start)

                    avg = 0
                    for value in timeList:
                        avg += value

                    avg /= r
                    timeMeasure.append(avg)

                plt.plot(ns, timeMeasure)
                plt.show()

                for i in range(k):
                    s = "n = " + str(n + i * step)
                    s += " time = " + str(timeMeasure[i])
                    s += " q = " + str(
                        (timeMeasure[i] * (n + (int(k / 2) * step))) / ((n + i * step) * timeMeasure[int(k / 2)]))
                    print(s)

            sys.exit()
