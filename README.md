# Projekt zaliczeniowy

### Projekt jest swego rodzaju prymitywną kopią discorda, użytkownicy mogą się logować, rejestrować, dołącząć do kanałów, pisać wiadomości, usuwać je itd.

## Opis instalacji
1. Aby uruchomić projekt, należy zainstalować Python. Można go pobrać z tego linku https://www.python.org/downloads/.
2. Następnie podczas instalaji, należy wybrać drugą opcję (Customize Installation), potem trzeba zaznaczyć każdą możliwą opcję. Kliknąć next, a następnie zaznaczyć "Add Python to environment variables".
3. Teraz trzeba otworzyć cmd i wejść w folder projektu.
4. Następnie należy napisać w cmd komendę "pip install django"
5. Potem należy napisać w cmd komendę "pip install djangorestframework"
6. Gdy już zainstalowaliśmy wszystkie pakiety, możemy uruchomić serwer komendą "python manage.py runserver".
7. Gdy uruchomienie serwera przebiegło pomyślnie, możemy wpisać w wyszukiwarkę adres IP, który powinienen wyświetlić się w cmd.
Jest to bodajże "127.0.0.1:8000".

## Użytkownicy i ich hasła

Aplikacja jest podzielona na super użytkowników i zwykłych użytkowników.
Obie te grupy mogą pisać wiadomości, tworzyć kanały itp.

Przykładowe hasło admina:  
Username: superuser  
Password: strong123

Przykładowe hasło użytkownika:  
Username: user  
Password: strong123  

Hasła są takie same, dlatego, aby łatwiej było je zapamiętać.

## Prezentacja aplikacji

Tak się prezentuje strona główna aplikacji.

Na środku strony widać wszytkie dostępne kanały. Można je filtrowac na podstawie tematu jaki się wybiera podczas tworzenia kanału za pomocą czerwonych przycisków oraz po nazwie kanału. 

![alt](imgs/1.png "1")

Jeżeli klikniemy na "Create Channel", albo "Join", to zostaniemy odesłani do formularza logowania.  

Formularz prezentuje się następująco.  
Możemy się zalogować, albo utworzyć nowe konto klikając "Sign Up".

![alt](imgs/2.png "2")


Po zalogowaniu mamy dostęp do wszytkich możliwości, które oferuje nam aplikacja.


![alt](imgs/3.png "3")

Po kliknięciu "Join", zostaniemy przeniesieni do wybranego kanału.


![alt](imgs/4.png "4")

Jak widać powyżej, użytkownicy mogą usuwać swoje wiadomości, natomiast nie mogą usuwać wiadomości napisanych przez inncyh użytkowników.  

Teraz spróbuje usunąć "testowa wiadomość".

![alt](imgs/5.png "5")

Wyświetli nam się taki komunikat, a po naciśnięciu "Confirm" wiadomość zostanie usunięta.


![alt](imgs/6.png "6")


Administratorzy mogą usuwać wszystkie wiadomości na każdym kanale.


![alt](imgs/7.png "7")

Jeżeli chcemy utworzyć nowy kanał, to musimy kliknąć "Create Channel" na głównej stronie lub wejść w ten link http://127.0.0.1:8000/create-channel/.

![alt](imgs/8.png "8")

W pierwszym inpucie wpisujemy nazwę kanału.  
W drugim wybieramy temat kanału, możemy go wybrać z listy lub wpisać swój własny. Jeżeli zastosujemy drugi sposób, to dodamy to co wpiszemy do bazy danych.  
W trzecim wpisujemy opis kanału.  

Następnie należy kliknąć 'Submit' i kanał będzie widoczny na stronie głównej.


![alt](imgs/9.png "9")


Jak widać kanał został dodany, a wraz z nim temat.


![alt](imgs/10.png "10")

Jeżeli dołączymy do tego kanału to możemy ten kanał usunąć lub zmodyfikować.  

Jeżeli klikniemy Edit otworzy nam się okno takie samo jak przy tworzeniu kanału i będziemy mogli zmienić dane kanału.

![alt](imgs/11.png "11")
