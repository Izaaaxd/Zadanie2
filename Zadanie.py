s18112 = ["Andrzej", "Zalewski", "Siedlce"]
s21542 = ["Grażyna", "Staszewski", "Mińsk Mazowiecki"]
s81123 = ["Stefan", "Kolanowski", "Łuków"]
s91221 = ["Monika", "Kaszewska", "Siedlce"]

#TODO: Utwórz listę studentów z podanych numerów indeksów
#TODO: Stefan zmienił miejsce zamieszkania na Siedlce - nanieś zmiany w kodzie, nie w samej zmiennej
#TODO: W obu programach niżej, system ma pytań użytkownika, czy chce wyszukać lub dodać następną osobę
#TODO: Utwórz program, który analogicznie tworzy i dodaje studentów do listy - użyj input()
#TODO: Utwórz program, który w podanej liście studentów wyświetla dane studenta po podaniu mu numeru albumu
studenci = [s18112, s21542, s81123, s91221]
print (studenci)
for student in studenci:
    print(student[0])
    if student[0] =="Stefan":
        student[2]="Siedlce"
print (studenci)
while True:
    print ("Podaj imię")
    imie= input()
    print ("Podaj nazwisko")
    nazwisko= input()
    print ("Podaj miejscowość")
    miejscowosc= input()
    
    nowy_student=[imie, nazwisko, miejscowosc]
    
    studenci.append(nowy_student)
    print(studenci)
