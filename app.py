# change directory to env and execute below command
# source bin/activate

from flask import Flask, render_template, url_for, request
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from collections import Counter
from num2words import num2words

import nltk
import os
import string
import numpy as np
import copy
import pandas as pd
import pickle
import re
import math

from load_file import load_file
from preprocess_data import process_data
from build_df import build_DF
from tf_idf import tf_idf
from cosine_similarity import cosine_similarity

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('search.html')

@app.route('/search/results', methods=['GET', 'POST'])

def search_request():
    # print(request.form["input"])
    search_term = request.form.get("input")
    # search_term = flask.request.args.get('name')
    Q = cosine_similarity(books_data = books_data,DF = DF, tf_idf = tf_idf,total_vocab = total_vocab, total_vocab_size = total_vocab_size, k = 10, query = search_term)
    print(Q)
    return render_template('results.html', res=Q )

# def index():
#     return render_template('index.html', variable = Q)

if __name__ == "__main__":
    load_data = False
    if not load_data:
        books_data = load_file()
        N = books_data.shape[0]
        processed_bookname, processed_text = process_data(books_data)
        DF, total_vocab_size, total_vocab = build_DF(N,processed_text,processed_bookname)
        tf_idf, df = tf_idf(N,processed_text,processed_bookname)
    # Q = cosine_similarity(books_data = books_data,DF = DF, tf_idf = tf_idf,total_vocab = total_vocab, total_vocab_size = total_vocab_size, k = 10, query = "The evening of the day on which Mr Gibson had been to see the squire")
    app.run(debug=True)
