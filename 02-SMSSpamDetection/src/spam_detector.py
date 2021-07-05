import os
import pickle
import argparse
import pandas as pd

from classes.SpamDetector import SpamDetector
from classes.TreaterMensage import TreaterMensage

# Upload model
sms_model = pickle.load(open("../model/sms_model_v1.pkl", "rb"))

# Set inputs in CLI
parser = argparse.ArgumentParser(description="The SpamDetector")
parser.add_argument('-fp',help='Path where the mensage file located, can just .csv or .txt files.')

# Recive inputs and store variable
args = parser.parse_args()

# Trate exeption if not pass inputs in CLI
try:
    # If file is a csv file, so is a treate to convert a dataframe and iterate for get each mensage properties
    treated_mensagem, type_mensage = TreaterMensage(args.fp).get_mensage()

    # Instatiate class
    spam_detect = SpamDetector(sms_model)

    # If a dataframe mensages iterate each mensage and show how many is spams and hams.
    if type_mensage == 'csv':     
        prob_spam_array = list(map(lambda x: spam_detect.prob_spam(x), treated_mensagem['mensages'].values))
        is_pram_array = list(map(lambda x: spam_detect.is_spam(x), treated_mensagem['mensages'].values))

        qt_ham, qt_spam = pd.DataFrame(list(map(int,is_pram_array))).value_counts().values
        
        print(f'This list have {qt_spam} spams and {qt_ham} hams!')

    # If a simple txt file then return if is spam or ham and your probabilitie
    else:
        if_spam = 'Spam' if spam_detect.is_spam(treated_mensagem) else 'Ham'
        prob_spam = spam_detect.prob_spam(treated_mensagem) 
        a_prob_spam = prob_spam if if_spam == 'Spam' else  round(1 -prob_spam, 3)
        print(f'This mensage is {if_spam} with {a_prob_spam*100}% certainty!')

# If user just execute code and not pass a path file        
except AttributeError:
    print("\nPlease, read the help descriptions below>>")
    os.system('python spam_detector.py -h')
