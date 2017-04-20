# wywolywana gdy system = 10 czyli podawana liczba jest w systemie dziesietnym i chcemy ja zamienic na binarny
def decimalTObinary(decimal_number):
    if decimal_number != 0:
        binary=[]
        while decimal_number != 0:  #dzielimy liczbe przez 2 tak dlugo az wynik jest rozny od 0
            binary.append(decimal_number % 2)   # do listy dodajemy reszt (o lub 1)
            if (decimal_number % 2) != 0:
                decimal_number = int((decimal_number/2)-0.5)    #jesli liczba jest podzielna przez 2 to ja dzielimy i dalej dzialamy w petli
            elif (decimal_number % 2) == 0:                     #jesli liczba nie jest podzielna przez 2 to ja dzielimy i odejmujemy 0.5 aby dalej dzialac w petli
                decimal_number = int(decimal_number / 2)
        return binary[::-1]                                 #petle zapisujemy od konca
        print(binary)
    else:
        return [0]
         



# wywolywana gdy system = 2 czyli podawana liczba jest w systemie binarnym i chcemy zamienic ja na dziesietna
def count(number_binary):    #liczymy ilosc cyfr
   
    digits = 1

    while number_binary % (10**digits) != number_binary:   #tyle razy ile wykona sie petla to tyle mamy cyfr w liczbie (+1)
        digits += 1

    return digits

def binarylist(number_binary):  #wrzuca nasza liczbe w liste
    binary_list = []
    digits = count(number_binary) #pobieramy ilosc cyfr w liczbie z count().

    for x in range(0, digits):  #tworzymy liste, wyliczamy wartosc (0,1) dla kolejnych miejsc listy
        binary_list.append(int(((number_binary % (10**(digits-x))) - (number_binary % (10**(digits-x-1)))) / (10**(digits-x-1))))

    return binary_list

def binaryTOdecimal(number_binary):
    list = binarylist(number_binary) #pobieramy liste z wczesniejszej funkcji
    number_decimal = 0  #poczatkowa wartosc liczby przed uruchomieniem petli

    for x in range(0,len(list)): #dla el.listy = 0 nie musimy wykonywac petli bo i tak wartosc rownania bedzie 0, dlatego ten if
        if list[x] is 1:
            number_decimal += 2**(len(list)-x-1)

    return number_decimal

    print(number_decimal)



number, system=map(str, input().split()) 

try:
    number=int(number)
    system=int(system)
    if (number or system) < 0:
       print('You must enter a positive number and "2" or "10" !') 
    if system == 10:
        decimal_number = number
        print(''.join(map(str, decimalTObinary(decimal_number))), '2')

    if system == 2:

        number_binary = number
        print(binaryTOdecimal(number_binary), '10')
    if (system != 2 and system != 10):
        print("Second number has to be 10 or 2")


except ValueError:
    print('You must enter a positive number and "2" or "10" !') 