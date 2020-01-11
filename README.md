# AAL-Petitioners
##### Grzegorz Aleksiuk

#### Treść zadania

AAL-3-LS urząd spraw czworakich

Urząd spraw czworakich przyjmuje petentów w czterech różnych sprawach.
Obsługa każdego petenta zajmuje 5 minut i jest wykonywana przez urzędnika specjalizującego się w danej sprawie.
Urząd zatrudnia sześciu urzędników, każdy specjalizuje się w dwóch różnych sprawach.
W urzędzie znajduje sięjedno okienko przy którym na początku dnia siedzi urzędnik specjalizujący się 
w pierwszej i drugiej sprawie. Do okienka ustawia się kolejka osób z różnymi sprawami. Gdy do okienka podchodzi osoba ze sprawą inną niż ta,
w której specjalizuje się urzędnik, może zostać obsłużona na dwa sposoby:
1) urzędnik przy okienku dzwoni do urzędnika specjalizującego się w tej sprawie i załatwia
tą konkretną sprawę telefonicznie, przez co obsługa wydłuża się o dodatkowe 5 minut,
2) urzędnik wychodzi i woła na swoje miejsce (na trwałe) urzędnika specjalizującego się w tej sprawie,
co także zajmuje dodatkowe 5 minut.

Należy znaleźć sposób obsługi petentów minimalizujący całkowity czas obsługi.
Porządek ludzi w kolejce jest znany od początku i się nie zmienia.

####Tryby wykonania
    1) main.py -m 1
    2) main.py -m 2 -n <n_value>
    3) main.py -m 3 -n <n_value> -k <number_of_steps> -s <value_of_step> -r <number of instances>
    
1) Zywkłe uruchomienie programu
2) Wylosowanie problemu o wielkości n
3) Proces tesotwania algorytmu z pomiarem czasu dla rosnącego n i porównanie ze złożonością teoretyczną

####Konwencje danych
Na wejściu podawana jest liczba n (1 <= n <= 10^6), następnie w nowej linii podawanych jest n wartości p oddzielonych spacją
z zakresu (1 <= p <= 4).

Na wyjściu liczba oznaczjąca ilość minut potrzebną na obsłużenie danej ilości osób

In:  
6  
1 2 3 4 2 4

Out:  
40

####Metoda rozwiązania

Przejście po kolei po kolejce petentów i sprawdzanie czy aktualny urzędnik jest w stanie obsłużyć tę osobę, jeśli tak 
robi to, jeśli nie to sprawdzane jest czy następną osobę może obsłużyć jeśli tak to istnieje duże prawdopodobieństwo że lepiej
jest zadzwonić do tej osoby niż zmieniać urzędnika, jednocześnie sprawdzane jest czy urzędnik który potrafiłby obsłużyć następnych dwóch
petenów nie jest lepszy od aktualnego, jeśli jest to zmieniamy aktualnego na kandydującego. W momencie jeżeli urzędnik nie może 
obsłużyć dwóch petentów pod rząd jest on zmieniany, na takiego który potrafi ich obsłużyć.


Struktury danych:
- listy
- PetitionersQueue

####Dekompozycja programu na pliki źródłowe
W folderze dir znajduje się plik PetitionersQueue.py, znajduje się w nim klasa odpowiadająca
za przechowanie danych i rozwiązanie danego problemu.
Plik main.py zawiera implementację interfejsu i moduły testujące rozwiązanie.
 



