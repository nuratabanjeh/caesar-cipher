import nltk 
import re
nltk.download('words', quiet=True)
nltk.download('names', quiet=True)
from nltk.corpus import words, names
word_list = words.words()
name_list = names.words()
upperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_list = list(upperCase)
lower_list = list(lowerCase)
def encrypt(plain_text, key):
    encrypted = ''
    for character in plain_text:
        if character not in upper_list and character not in lower_list:
            char = re.sub(r'[^A-Za-z]+', '', character)
            encrypted += char
        elif character in upper_list:
            char = (upper_list.index(character) + key) % 26
            encrypted += upper_list[char]
        else:
            char = (lower_list.index(character) + key) % 26
            encrypted += lower_list[char] 
    return encrypted

def decrypt(en_text, key):
    return encrypt(en_text, -key)

def count_words(text):
    candidate_words = text.split()
    word_count = 0
    for candidate in candidate_words:        
        word = re.sub(r'[^A-Za-z]+','', candidate)        
        if word.lower() in word_list or word in name_list:           
             word_count += 1        
        # else:            
        #     pass
    return word_count

def crack(en_text):
    emptyS=""
    for key in range(26):
        word = decrypt(en_text, key)
        persentage = int(count_words(word)) / len(word.split()) * 100
        if persentage > 50:
            emptyS = word
   
        return word
            

        





if __name__ == "__main__":
    # print(encrypt('***', 1))
    # print(encrypt('My name is solve the problem ', 26))
    # print(encrypt('ABC', 1))
    # print(decrypt('BCD', 1))
    example = encrypt('652//**  --',2)
    print(example)
    # example2=decrypt(example,2)
    # crack(example2)
    # print(encrypt('"Where\'s Papa going with that ax?" said Fern to her mother as they were setting the table for breakfast.'))
    # print(crack(example2))