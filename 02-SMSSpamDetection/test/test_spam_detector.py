import pickle
import pytest

from src.classes.SpamDetector import SpamDetector

spam_text = 'Sunshine Hols. To claim ur med holiday send a stamped self address envelope to Drinks on Us UK \n Wicklow \n  Eire. Quiz Starts Saturday! Unsub Stop'
ham_text = 'kasjfçskdjfçsakldfjçsakl asdfsadfsadfas'

# Instantiate class, not need repeat this proced.
@pytest.fixture
def spam_detector():
    return SpamDetector(pickle.load(open("./model/sms_model_v1.pkl", "rb")))

# ======================================================
# Tests with class when instantiate
# ======================================================
def test_instante_class_with_empty_parameter():
    with pytest.raises(TypeError):
        SpamDetector()

def test_instante_class_with_wrong_model_path():
    with pytest.raises(FileNotFoundError):
        SpamDetector(pickle.load(open("/sms_model_v1.pkl", "rb")))

def test_instante_class_with_wrong_type():
    with pytest.raises(TypeError):
        SpamDetector(1)

# ======================================================
# With a spam and ham mensage
# ======================================================
def test_is_spam_with_a_spam(spam_detector):
    assert spam_detector.is_spam(spam_text) == True

def test_is_spam_with_a_ham(spam_detector):
    assert spam_detector.is_spam(ham_text) == False

def test_prob_spam_with_a_spam(spam_detector):
    assert spam_detector.prob_spam(spam_text) >= 0.5

def test_prob_spam_with_a_ham(spam_detector):
    assert spam_detector.prob_spam(ham_text) <= 0.5    

# ======================================================
# With a number, type test
# ======================================================
def test_is_spam_with_a_number(spam_detector):
    with pytest.raises(AttributeError):
        spam_detector.is_spam(1)

def test_prob_spam_with_a_number(spam_detector):
    with pytest.raises(AttributeError):
        spam_detector.prob_spam(1)

# ======================================================
# With empty parameter
# ======================================================
def test_is_spam_with_a_number(spam_detector):
    with pytest.raises(TypeError):
        spam_detector.is_spam()

def test_prob_spam_with_a_number(spam_detector):
    with pytest.raises(TypeError):
        spam_detector.prob_spam()        