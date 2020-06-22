import openpyxl
import os.path

def export_results_to_excel(keywords):
    book = openpyxl.Workbook()
    leaf = book.create_sheet('keys')
    leaf.append(('Keywords','Position'))
    for keyw in keywords:
        leaf.append(keyw)
    num = 1
    name = "Keyw_book_N"
    while True:
        if os.path.isfile(name+str(num)+".xlsx"):
            num += 1
        else:
            break

    book.save(name+str(num)+".xlsx")



