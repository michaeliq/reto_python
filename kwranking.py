def cargar_keywords():
    try:
        keys = []
        with open('keywords.txt','r') as f:
            for line in f:                                        keys.append(line)
            return keys
    except FileNotFoundError as err:
        print(err)
        return ''
keywords = ''
while True:
    q = input('''Welcome to Kwranking...
    if you need to view the keywords insert 2
    if you need to import keysword.txt insert 1
    if you wish exit insert 0:
    ''')

    if q == '1':
        keywords = cargar_keywords()
    elif q == '2':
        if len(keywords) < 1:
            print('File is not able')
        else:
            for key in range(len(keywords)):
                print(keywords[key])
                if key != 0 and key % 20 == 0:
                    input('press enter to see more')
    elif q == '0':
        print('thank you by participe, see you soon')
        break
    else:
        print('option is not valide')

            
        
