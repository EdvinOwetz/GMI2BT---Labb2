import csv, json

# Metoden nedan läser in originalfilen (labb2-personer.csv) i programmet. 
# I program.py matas den returnerade 'file_list' in i listan 'persons' vilket tillåter oss att jobba med datan däri.
# Rad 15 och 16 tar bort den översta raden i CSV-filen (rubrikerna)(tack Thomas!).

def read_file(csv_file='labb2-personer.csv', csv_path='./'):
    file_list = []
    csv_path+=csv_file
    
    try:
        with open(csv_path, 'r', encoding='utf-8-sig') as csv_file:
            first_line = True
            for line in csv_file:
                if first_line:
                    first_line = False
                elif len(line) > 0:
                    rf_line = line.rstrip('\n').split(';')
                    file_list.append({'Användarnamn':rf_line[0], 'Förnamn':rf_line[1],'Efternamn':rf_line[2],'E-mail':rf_line[3]})
            return file_list
    except FileNotFoundError:
        print('Originalfilen existerar inte.')    

# Metoden nedan dubbelkollar att användaren faktiskt skriver något vid en begärt input.

def input_not_empty(text):
    while True:
        input_str = input(text)
        if len(input_str.strip()) > 0:
            return input_str