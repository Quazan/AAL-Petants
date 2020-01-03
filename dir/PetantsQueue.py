class PetantsQueue:
    def __init__(self, n_value, petants_list):
        self.n = n_value
        self.petants = petants_list

    def solve(self):
        return self.__algorithm(self.n, self.petants)

    def __pretenders(self, n, petants, i, currentOfficial, pretendingOfficial):
        for j in range(i + 1, n):
            if petants[j] != currentOfficial[0] and petants[j] != currentOfficial[1] and (
                    petants[j] == pretendingOfficial[0] or petants[j] == pretendingOfficial[1]):
                currentOfficial = pretendingOfficial
                break

            elif petants[j] != pretendingOfficial[0] and petants[j] != pretendingOfficial[1] and (
                    petants[j] == currentOfficial[0] or petants[j] == currentOfficial[1]):
                break

            elif petants[j] != currentOfficial[0] and petants[j] != currentOfficial[1] and petants[j] != \
                    pretendingOfficial[0] and petants[j] != pretendingOfficial[1]:
                if j < n - 1 and (petants[j + 1] == currentOfficial[0] or petants[j + 1] == currentOfficial[1]) and (
                        petants[j + 1] == pretendingOfficial[0] or petants[j + 1] == pretendingOfficial[1]):
                    currentOfficial = self.__pretenders(n, petants, j, currentOfficial, pretendingOfficial)
                elif j < n - 1 and petants[j + 1] != currentOfficial[0] and petants[j + 1] != currentOfficial[1] and (
                        petants[j + 1] == pretendingOfficial[0] or petants[j + 1] == pretendingOfficial[1]):
                    currentOfficial = pretendingOfficial
                break
        return currentOfficial

    def __algorithm(self, n, petants):
        currentOfficial = (1, 2)

        score = 5 * n
        i = 0
        while i < n:
            if petants[i] != currentOfficial[0] and petants[i] != currentOfficial[1]:
                score += 5

                if i + 1 < n:
                    if petants[i + 1] == currentOfficial[0] or petants[i + 1] == currentOfficial[1]:
                        if i + 2 < n and petants[i + 2] != currentOfficial[0] and petants[i + 2] != currentOfficial[1]:
                            currentOfficial = (petants[i], petants[i + 1])

                        else:
                            pretendingOfficial = (petants[i], petants[i + 1])
                            currentOfficial = self.__pretenders(n, petants, i, currentOfficial, pretendingOfficial)

                    else:
                        currentOfficial = (petants[i], 0)

                        for j in range(i + 1, n):
                            if currentOfficial[1] == 0 and petants[j] != currentOfficial[0]:
                                currentOfficial = (currentOfficial[0], petants[j])

                            if petants[j] != currentOfficial[0] and petants[j] != currentOfficial[1]:
                                i = j - 1
                                break
                            elif j == n - 1:
                                i = j
            i += 1

        return score
