
import re 

def fix_text(text):
    text  = remove_escape_sequence(text)
    text = remove_punctuation(text)
    text = make_lowercase(text)
    return text

def remove_escape_sequence(text):
    escapes = '\b\n\r\t\\' 
    for c in escapes: 
        text = text.replace(c, '') 
    return text

def remove_punctuation(text):
    return re.sub(r'[^\w\s]', '', text)

def make_lowercase(text):
    return text.lower()

def dictionary_process(word): 
    if word not in word_dict.keys():
        word_dict[word] = 1
    else:
        word_dict[word] = word_dict[word]+1

    print(word,word_dict[word])


word_dict = {}

my_file = 'Text_file'
i = 0

with open(my_file, 'r') as f:
    lines = f.readlines()
    for line in lines:
        i += 1
        tmp = fix_text(line)
        tmp_words = tmp.split()
        for word in tmp_words:
            dictionary_process(word)






    