class PetitionersQueue:
    def __init__(self, n_value, petitioners_list):
        self.n = n_value
        self.petitioners = petitioners_list

    def solve(self):
        return self.__algorithm(self.n, self.petitioners)

    def __pretenders(self, n, petitioners, i, currentOfficial, pretendingOfficial):
        for j in range(i + 1, n):
            if petitioners[j] != currentOfficial[0] and petitioners[j] != currentOfficial[1] and (
                    petitioners[j] == pretendingOfficial[0] or petitioners[j] == pretendingOfficial[1]):
                currentOfficial = pretendingOfficial
                break

            elif petitioners[j] != pretendingOfficial[0] and petitioners[j] != pretendingOfficial[1] and (
                    petitioners[j] == currentOfficial[0] or petitioners[j] == currentOfficial[1]):
                break

            elif petitioners[j] != currentOfficial[0] and petitioners[j] != currentOfficial[1] and petitioners[j] != \
                    pretendingOfficial[0] and petitioners[j] != pretendingOfficial[1]:
                if j < n - 1 and (petitioners[j + 1] == currentOfficial[0] or petitioners[j + 1] == currentOfficial[1]) and (
                        petitioners[j + 1] == pretendingOfficial[0] or petitioners[j + 1] == pretendingOfficial[1]):
                    currentOfficial = self.__pretenders(n, petitioners, j, currentOfficial, pretendingOfficial)
                elif j < n - 1 and petitioners[j + 1] != currentOfficial[0] and petitioners[j + 1] != currentOfficial[1] and (
                        petitioners[j + 1] == pretendingOfficial[0] or petitioners[j + 1] == pretendingOfficial[1]):
                    currentOfficial = pretendingOfficial
                break
        return currentOfficial

    def __algorithm(self, n, petitioners):
        currentOfficial = (1, 2)

        score = 5 * n
        i = 0
        while i < n:
            if petitioners[i] != currentOfficial[0] and petitioners[i] != currentOfficial[1]: #jeżeli petet nie może zostać obsłużony
                score += 5

                if i + 1 < n:
                    if petitioners[i + 1] == currentOfficial[0] or petitioners[i + 1] == currentOfficial[1]:            # jeżeli następny petent może zostać obsłużony
                        if i + 2 < n and petitioners[i + 2] != currentOfficial[0] and petitioners[i + 2] != currentOfficial[1]: #jeżeli kolejny petent nie może zostać obsłużoby zmień
                            currentOfficial = (petitioners[i], petitioners[i + 1])
                        else:
                            pretendingOfficial = (petitioners[i], petitioners[i + 1])
                            currentOfficial = self.__pretenders(n, petitioners, i, currentOfficial, pretendingOfficial)

                    else:
                        currentOfficial = (petitioners[i], 0)   # jeżeli nie może dwóch pod rząd obsłużyć zmieniamy na nowego

                        for j in range(i + 1, n):
                            if currentOfficial[1] == 0 and petitioners[j] != currentOfficial[0]:
                                currentOfficial = (currentOfficial[0], petitioners[j])

                            if petitioners[j] != currentOfficial[0] and petitioners[j] != currentOfficial[1]:
                                i = j - 1
                                break
                            elif j == n - 1:
                                i = j
            i += 1

        return score
