from check_kw import Scrapping as sc
import db
from models import Keyword
from data import export_results_to_excel

if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)

def keywords_como_lista_de_valores():
    keywords = [(key.keyword_,key.position) for key in Keyword.get_all()]
    return keywords

def cargar_keywords():
    file_k = open('keywords.txt','r')
    keyw = file_k.read()
    keyw = keyw.rstrip()
    keyw = keyw.split('\n')
    key_req = Keyword.get_all()
    key_to_compare = []
    for key in key_req:
        key_to_compare.append(key.keyword_)
    
    for key in keyw:
        if key not in key_to_compare:
            item = Keyword(key)
            item.save()
    file_k.close()
    return Keyword.get_all()
    


while True:
    keywords = Keyword.get_all()
    q = input('''
Welcome to Kwranking...
Export keywords to excel file insert 4
Search a keyword/s in google insert 3
View the keywords insert 2
Import keysword.txt insert 1
Exit insert 0
choice:  ''')

    if q == '1':
        cargar_keywords()

    elif q == '2':
        if len(keywords) < 1:
            print('File is not able')
        else:
            cont_2 = 0
            for key in keywords:
                print(key.keyword_ + ', position: ' + str(key.position))
                cont_2 += 1
                if cont_2 != 0 and cont_2 % 20 == 0:
                    input('press enter')

    elif q == '3':
        ls_kw = Keyword.get_all()
        for key in ls_kw:

            soup = sc('https://es.wikipedia.org/',key.keyword_)
            position = soup.check_keyword()
            if position >= 100:
                key.update_reg(None)
            else:
                key.update_reg(position)
    elif q == '4':
        keys = keywords_como_lista_de_valores()
        export_results_to_excel(keys)
        print('it\'s done')

    elif q == '0':
        print('thank you by participe, see you soon')
        break
    else:
        print('option is not valide')

            
        
