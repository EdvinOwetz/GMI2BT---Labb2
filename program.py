from modules import read_file, input_not_empty
import json

# När programmet går igång startas listan 'persons' upp globalt.
# Denna fylls på med data ifrån antingen funktion 1 eller 6 i menyn.

persons = []

# Menyn har jag byggt på samma sätt som i labb 1.
# En While-loop med hårdkodade menyval ('menu_input').
# Detta medför en enkel men effektiv felhantering.

while True:
    print('\n--------Huvudmeny--------\n')
    print(' 1. Läs in originalfilen')
    print(' 2. Visa JSON-data')
    print(' 3. Lägg till person')
    print(' 4. Ta bort person')
    print(' 5. Spara fil')
    print(' 6. Läs in JSON-data')
    print(' 7. Avsluta programmet')
    print('\n-------------------------')
    
# Metoden nedan läser in originalfilen ('labb2-personer.csv') i listan 'persons'.
# Bra om man vill återgå till originaldatan. 
# Kompletteras av mitt tillagda menyval 6.
    
    menu_input = input('\nVälj en funktion: ')
    if menu_input == '1':
        persons = read_file()
        print('\n----------------------------')
        print(' Originalfilen har lästs in')
        print('----------------------------\n')

# Menyval för att visa JSON-data.
# .ljust används för att justera kolumnernas bredd.

    elif menu_input == '2':
        print() # Tom rad för formatering
        for row in persons:
            print(f'{row["Användarnamn"].ljust(10)} {row["Förnamn"].ljust(20)} {row["Efternamn"].ljust(25)} {row["E-mail"]}')

# Menyval för att lägga till en person i listan 'persons'.
# input_not_empty anropas från modules.py och finns beskriven där.

    elif menu_input == '3':
        user_name_input = input_not_empty('Ange användarnamn: ')
        firstname_input = input_not_empty('Ange förnamn: ')
        lastname_input = input_not_empty('Ange efternamn: ')
        email_input = input_not_empty('Ange e-mail: ')
        persons.append({'Användarnamn':user_name_input, 'Förnamn':firstname_input,'Efternamn':lastname_input,'E-mail':email_input})
        
# Menyval för att ta bort en person ur listan. 
# Listan visas med index konverterad till en string först, input från avändaren konverteras till en int.
# Felhantering sker i två steg, först med ValueError för att hantera de fall där något annat än ett heltal anges,
# sedan med IndexError om användaren anger ett index som inte finns i listan.        
           
    elif menu_input == '4':
        for index in range(len(persons)):
            row = persons[index]
            print(f'{str(index).ljust(3)} {row["Användarnamn"].ljust(10)} {row["Förnamn"].ljust(20)} {row["Efternamn"].ljust(25)} {row["E-mail"]}')
        while True:
            try:
                input_remove_user = int(input('\nFör att ta bort en användare, ange användarens index: '))
                persons.remove(persons[input_remove_user])
                break
            except ValueError:
                print('\nFelaktigt angivet index, försök igen. ')
            except IndexError:
                print('\nFelaktigt angivet index, försök igen. ')
        
# Menyval för att spara datan i programmets minne (listan 'persons') till JSON-filen ('labb2.json').
        
    elif menu_input == '5':
        with open('labb2.json', 'w', encoding='UTF-8-sig') as file_path:
            json.dump(persons, file_path, ensure_ascii=False, indent=4)
        print('\n------------------------')
        print(' JSONfilen har sparats')
        print('------------------------\n')

# Menyval 6 är ett val jag själv lagt till. 
# Detta då jag tyckte det borde finnas ett val för att i ett senare skede kunna återuppta arbetet med data som editerats i en tidigare körning.
# Allt som sker är att datan som finns sparad i json-filen ('labb2.json') läggs in i listan 'persons' så den kan arbetas med igen.
# Om listan blivit fylld av orignaldatan (menyval 1) skrivs den över av detta menyval. 
# Tyvärr tror jag detta även sker åt andra hållet, alltså om listan är fylld med denna data kan den skrivas över av menyval 1.
# Jag har inte kommit på en lösning på detta.

    elif menu_input == '6':
        try:
            f = open('labb2.json', 'r', encoding='UTF-8-sig').read()
            persons = json.loads(f)
            print('\n-------------------------')
            print(' JSON-datan har lästs in')
            print('-------------------------\n')
        except FileNotFoundError:
            print('JSON-filen existerar inte.')

# Avslutar programmet genom att bryta while-loopen.

    elif menu_input == '7':
        input('\nTryck på valfri tangent för att avsluta programmet')
        break

# Felhantering om något annat menyval än de specificerade anges.

    else:
        print('\nFelaktigt val, ange funktion utifrån huvudmenyns lista')