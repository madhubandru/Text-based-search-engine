# Text-based-search-engine

This project repository include below files/folders.

<b>1.file4.csv :</b> This is the data file, where we have cleaned data. It consist of 50 records with below fileds.<br>
    1. book_id<br>
    2. bookname<br>
    3.author_id<br>
    4. chapter<br>
    5. text

<b>2. templates folder :</b> This is the templates folder with UI screen designs both for search and results screens.

<b>3. static folder :</b> This folder consist of UI style/design CSS file and also background image used in UI.

<b>4. lib folder :</b> This folder is required for running the application.

<b>5. bin folder :</b> This folder is required for running the application.

<b>6. stemmer folder :</b> This folder consists of stemming related packages.

<b>7. tokenizers folder :</b> This folder consists of packages related to word tokenizer.

<b>8. app.py :</b> This file is the key driving file of the application. To launch the application locally this file need to be triggered.

<b>9. load_file.py :</b> Loading dataset(file4.csv) is done using thsi file.

<b>10. build_df.py :</b> This pyhton file is used to generate the dictionary with document frequency(DF) of the input file.

<b>11. cosine_similarity.py :</b> This pyhton file is used to process a input query provided by user and provide the results that matching the query.

<b>12. preprocess_data.py :</b> This python file is used to process both input data file and input provided by user query. Following functions are included in this file.<br>
    1.lower case conversion<br>
    2.stop words removal<br>
    3.removing punctuations<br>
    4.stemming<br>
    5.number to word conversion

<b>13. tf_idf.py :</b> This python file is used to calculate tf-idf scores.

<b>14. Procfile :</b> This file is required for hosting the application in web.

<b>15. pyvenv.cfg:</b> This is system generated file when application is created in flask.

<b>16. requirements.txt :</b> This file consist of all required python packages which will be auto installed when application is launched.
