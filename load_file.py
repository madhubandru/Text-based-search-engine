import pandas as pd

def load_file():
    books_data = pd.read_csv("file4.csv", encoding = 'utf-8')
    ###############
    #removing subset after pushing in flask successfully
    ###############
    books_data= books_data[:100]
    # return books_data.head()
    return books_data