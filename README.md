
# Nuveo Challenge
    The challenge folders are organized in this way:

```
project
│   README.md
│   .gitignore
│   requiriments.txt
└───01-WheresWally
│   └───data
|   │   └───ReferenceData
|   |   |   | wally.jpg
|   |   |   | wheres_wally_train.csv
|   │   └───removed
|   │   |   │  ....json
|   │   |   │  ....jpg
|   │   └───TestSet
|   │   |   │  ....jpg
│   └───TrainingSet
|   |    └───images
|   │    |   │  ....jpg
|   |    └───json
|   │    |   │  ....json
│   └───src
│   |    │   wally_detector.ipynb   
└───02-SMSSpamDetection
|    └───data
|    |    └───examples
|    |    |     list_1_mensages.csv
|    |    |     ....
|    |    |     only_mensage_1
|    |    |     ....
|    |    └───TestSet
|    |    |     sms-hamspam-test.csv
|    |    └───TrainingSet
|    |    |     sms-hamspam-train.csv
|    |    |     sms-hamspam-val.csv
|    └───model
│    │   sms_model_v1.pkl
|    └───src
|    |    └───classes
|    |    |    __init__.py
|    |    |    SpamDetector.py
|    |    |    TreaterMensage.py
|    |   model_analysis.ipynb
│    │   spam_detector.py
|    └───test
│    │   test_spam_detector.py

```

# Envoriment packages need

- Utilize the ```requiriments.txt``` file with pip:
    
    ```pip install -r requiriments.txt```

- WheresWally problem was made in colab notebooks
- SMSSpamDetectin problem was made terminal utilizing argeparse package

# 01 - WheresWally
Just execute the notebook in colab workspace

# 02 - SMSSpamDetection
- You can run two type file in this program: csv or txt file, some file are in ```02-SMSSpamDetection\data\examples``` folder. After instaling package needed go to ``` src ``` folder and run this way:

``` python spam_detector.py -fp [path_file]```

example:

``` python spam_detector.py -fp ../data/example/only_mensage_1.txt```

and then, the expected output is:
    ```This mensage is Ham with 93.0% certainty!```

other example:

``` python spam_detector.py -fp ../data/example/only_mensage_1.csv```

and then, the expected output is:
    ```This list have 112 spams and 735 hams!```    

- CSV files, must have just messages, one column with messages for tests.
- For run test with ```pytest``` you need in ````02-SMSSpamDetection\```` and execute ```pytest``` in your terminal.
- In ````02-SMSSpamDetection\src```` have ````model_analysis.ipynb```` file that have some tests into provided model, the intention is to evaluate the model consistency.



**All codes are documented.**