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

**Przykładowe hasło admina:**  
Username: superuser  
Password: strong123

**Przykładowe hasło użytkownika:**  
Username: user  
Password: strong123  

Hasła są takie same, aby łatwiej było je zapamiętać.

## Prezentacja aplikacji

Tak się prezentuje strona główna aplikacji.

Na środku strony widać wszytkie dostępne kanały. Można je filtrowac na podstawie tematu jaki się wybiera podczas tworzenia kanału za pomocą czerwonych przycisków oraz po nazwie kanału. 

![alt](https://github.com/dpjk00/python_discord/blob/main/imgs/1.PNG)

Jeżeli klikniemy na "Create Channel", albo "Join", to zostaniemy odesłani do formularza logowania.  

Formularz prezentuje się następująco.  
Możemy się zalogować, albo utworzyć nowe konto klikając "Sign Up".

![alt](https://github.com/dpjk00/python_discord/blob/main/imgs/2.PNG)


Po zalogowaniu mamy dostęp do wszytkich możliwości, które oferuje nam aplikacja.


![alt](https://github.com/dpjk00/python_discord/blob/main/imgs/3.PNG)

Po kliknięciu "Join", zostaniemy przeniesieni do wybranego kanału.


![alt](https://github.com/dpjk00/python_discord/blob/main/imgs/4.PNG)

Jak widać powyżej, użytkownicy mogą usuwać swoje wiadomości, natomiast nie mogą usuwać wiadomości napisanych przez inncyh użytkowników.  

Teraz spróbuje usunąć "testowa wiadomość".

![alt](https://github.com/dpjk00/python_discord/blob/main/imgs/5.PNG)

Wyświetli nam się taki komunikat, a po naciśnięciu "Confirm" wiadomość zostanie usunięta.


![alt](https://github.com/dpjk00/python_discord/blob/main/imgs/6.PNG)


Administratorzy mogą usuwać wszystkie wiadomości na każdym kanale.


![alt](https://github.com/dpjk00/python_discord/blob/main/imgs/7.PNG)

Jeżeli chcemy utworzyć nowy kanał, to musimy kliknąć "Create Channel" na głównej stronie lub wejść w ten link http://127.0.0.1:8000/create-channel/.

![alt](https://github.com/dpjk00/python_discord/blob/main/imgs/8.PNG)

W pierwszym inpucie wpisujemy nazwę kanału.  
W drugim wybieramy temat kanału, możemy go wybrać z listy lub wpisać swój własny. Jeżeli zastosujemy drugi sposób, to dodamy to co wpiszemy do bazy danych.  
W trzecim wpisujemy opis kanału.  

Następnie należy kliknąć 'Submit' i kanał będzie widoczny na stronie głównej.


![alt](https://github.com/dpjk00/python_discord/blob/main/imgs/9.PNG)


Jak widać kanał został dodany, a wraz z nim temat.


![alt](https://github.com/dpjk00/python_discord/blob/main/imgs/10.PNG)

Jeżeli dołączymy do tego kanału to możemy ten kanał usunąć lub zmodyfikować.  

Jeżeli klikniemy Edit otworzy nam się okno takie samo jak przy tworzeniu kanału i będziemy mogli zmienić dane kanału.

![alt](https://github.com/dpjk00/python_discord/blob/main/imgs/11.PNG)

![alt](https://github.com/dpjk00/python_discord/blob/main/imgs/12.PNG)

Aby usunąć kanał należy, być twórcą tego kanału i po wejściu na kanał kliknąć "Delete". Teraz usunę "Kanał dla fanów Lorem Ipsum".


![alt](https://github.com/dpjk00/python_discord/blob/main/imgs/13.PNG)

Po kliknięciu Delete zostaniemy przeniesieni do takiej strony i po naciśnięciu Confirm usuniemy kanał.



![alt](https://github.com/dpjk00/python_discord/blob/main/imgs/14.PNG)


### Rejestracja i logowanie poprzez API

Aby się zarejestrować poprzez API, należy wejść w ten link http://127.0.0.1:8000/api/registration.  

![alt](https://github.com/dpjk00/python_discord/blob/main/imgs/15.PNG)


Pole "Content" musimy uzupełnić kodem JSON np.

{
  "username": "markdown_user",
  "password": "markdown_password"
}


![alt](https://github.com/dpjk00/python_discord/blob/main/imgs/16.PNG)

Po kliknięciu POST, użytkownik zostanie dodany do bazy danych i będziemy mogli sie zalogować na jego konto.

![alt](https://github.com/dpjk00/python_discord/blob/main/imgs/17.PNG)


Aby zalogować się poprzez API, należy wejść na http://127.0.0.1:8000/api/login

![alt](https://github.com/dpjk00/python_discord/blob/main/imgs/18.PNG)

Następnie poprzez format JSON, należy podać username i password np.

{
  "username": "myszkamiki",
  "password": "strong123"
}


![alt](https://github.com/dpjk00/python_discord/blob/main/imgs/19.PNG)

Po kliknięciu POST, wyświetli nam sie komunikat "Login successful"


![alt](https://github.com/dpjk00/python_discord/blob/main/imgs/20.PNG)


Zostaniemy również zalogowani na konto podane w formacie JSON.


![alt](https://github.com/dpjk00/python_discord/blob/main/imgs/21.PNG)


Za pomocą API możemy też wyświetlić wszystkie istniejące kanały i użytkowników.

W tym celu musimy wejść na http://127.0.0.1:8000/api/channels/ lub http://127.0.0.1:8000/api/users/


![alt](https://github.com/dpjk00/python_discord/blob/main/imgs/22.PNG)
![alt](https://github.com/dpjk00/python_discord/blob/main/imgs/23.PNG)

### Testy

Aby zrobić test, należy w cmd wejśc w folder projektu i wpisać komendę:

python manage.py test


![alt](https://github.com/dpjk00/python_discord/blob/main/imgs/24.PNG)

