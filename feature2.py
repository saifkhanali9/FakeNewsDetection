# sentence length(# of char)
# sentence length(# of words)
# # of punctuations
# # of illegal punctuations
import string
import numpy as np
import nltk
from textstat.textstat import textstat


def extract_adjective(sentences):
    adj_sentences = list()
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        adj_tags = nltk.pos_tag(words)
        one_adj_sentence = ""
        for index, tag in enumerate(adj_tags, start=0):
            one_tag = tag[1]
            if one_tag in ['JJ', 'JJR', 'JJS']:
                one_adj_sentence += words[index]
                one_adj_sentence += " "
        adj_sentences.append(one_adj_sentence)
        # print(one_adj_sentence)
    return adj_sentences


def removePunc(input):
    '''
    :param input: string
    :return: string, without the punctuations
    '''
    return input.translate(bytes.maketrans(b"", ""), string.punctuation)


count = lambda l1, l2: len(list(filter(lambda c: c in l2, l1)))


def numOfWords(input):
    '''
    :param input: string
    :return: number of words, number of continuous space
    '''
    splitted = input.split(" ")
    res = 0
    for i in splitted:
        if len(i) > 0:
            res += 1
    return res


def numOfChar(input):
    '''
    :param input: string
    :return: number of char
    '''
    return len(input)


def numOfPunc(input):
    '''
    :param input: string
    :return: number of punctuations
    '''
    return len(input) - len(removePunc(input))


def numOfContPunc(input):
    res = 0
    state = False
    for i in range(1, len(input)):
        if input[i] in string.punctuation:
            if input[i - 1] in string.punctuation:
                if state:
                    pass
                else:
                    state = True
                    res += 1
            else:
                state = False
                pass
        else:
            state = False
    return res


def numOfContUpperCase(input):
    res = 0
    state = False
    for i in range(1, len(input)):
        if input[i].isupper():
            if input[i - 1].isupper():
                if state:
                    pass
                else:
                    state = True
                    res += 1
            else:
                state = False
                pass
        else:
            state = False
    return res
    pass



def process(data):
    res = np.array([])
    cleaned = data.lower().strip()
    original = data.strip()
    fea1 = numOfWords(cleaned)
    # fea1 = fea1 / 10
    fea2 = numOfChar(cleaned)
    # fea2 = fea2 / 100
    fea3 = count(cleaned, string.punctuation)
    fea5 = numOfContUpperCase(original)
    fea4 = textstat.gunning_fog(data)
    fea6 = textstat.automated_readability_index(data)
    fea7 = textstat.linsear_write_formula(data)
    fea8 = textstat.difficult_words(data)
    fea9 = textstat.dale_chall_readability_score(data)
    fea10 = data.count("\'") + data.count(".") + data.count("\"") + data.count(",") + data.count(
        "’") + data.count("‘") + data.count("”") + data.count("“")
    fea10 = (fea10 / len(data)) * 1000
    fea11 = data.count("1") + data.count("2") + data.count("3") + data.count("4") + data.count(
        "5") + data.count("6") + data.count("7") + data.count("8") + data.count("9") + data.count("0")
    fea12 = data.count("?") + data.count("!") + data.count("@") + data.count("#") + data.count(
        "$") + data.count("%") + data.count("&")
    fea13 = data.count(":") + data.count(";")
    fea14 = data.count("—") + data.count("-") + data.count("_")
    fea15 = (fea10 / len(data)) * 100
    fea16 = data.count("(") + data.count(")") + data.count("[") + data.count("]") + data.count(
        "{") + data.count("}")

    fea17 = data.count("*") + data.count("/")
    fea18 = data.count("?")
    fea19 = fea10 + fea11 + fea12 + fea13 + fea14 + fea15 + fea16 + fea17 + fea18
    res = np.array([[fea1, fea2, fea3, fea5, fea4, fea6, fea7, fea8, fea9, fea10, fea11, fea12, fea13, fea14,
                     fea15, fea16, fea17, fea18, fea19]])


    return res
