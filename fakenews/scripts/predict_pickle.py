import pandas as pd
import pickle
import feature2

# FinalDataSet
# fake_or_real_news
def classify(title="NAN",text="NAN"):
    data = feature2.process(text)
    data = pd.DataFrame(data)
    data.columns = data.columns = ['text_wordCount', 'text_charCount', 'text_puncCount', 'text_upperCount',
                               'text_gunning_fog', 'text_automated_readability_index', 'text_linsear_write_formula',
                               'text_difficult_words', 'text_dale_chall_readability_score', 'txp1', 'txp2', 'txp3',
                               'txp4', 'txp5', 'txp6', 'txp7', 'txp8', 'txp9', 'txp10']
    data1 = feature2.process(title)
    data1 = pd.DataFrame(data1)
    data1.columns = ['title_wordCount', 'title_charCount', 'title_puncCount', 'title_upperCount', 'title_gunning_fog',
                     'title_automated_readability_index', 'title_linsear_write_formula', 'title_difficult_words',
                     'title_dale_chall_readability_score', 'tlp1', 'tlp2', 'tlp3', 'tlp4', 'tlp5', 'tlp6', 'tlp7', 'tlp8',
                     'tlp9', 'tlp10']
    result = pd.concat([data, data1], axis=1, join='inner')
    file_Name="trainedModel.sav"
    fileObject = open(file_Name,'rb')
    # load the object from the file into var b
    b = pickle.load(fileObject)
    a=b.predict(result)
    print(a)



classify()