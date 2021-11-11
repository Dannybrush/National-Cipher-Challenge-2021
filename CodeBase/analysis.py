import json
from operator import itemgetter
from pprint import pprint
import matplotlib.pyplot as plt

def load(fn):
    # load the code
    filename = fn # "../Encrypted/Mission Intercept 5B_Transatlantic.md"
    with open(filename) as f:
        #lines = f.readlines()

        text = f.read()
        print(text)
        #line = f.readline()

    f = open(filename, 'r')
    contents = f.read()
    print(contents)
    length = len(contents)
    print(length)
    f.close()
    cleanse(contents)


def cleanse(contents):
    contents = contents.casefold()
    print(contents)
    cleansed = ''
    space = 0
    for i in range(len(contents)):
        if contents[i].isalnum():
            cleansed = cleansed+contents[i]
        elif contents[i] == ' ':
            space += 1
        else:
            continue
    print(len(cleansed))
    print(cleansed)
    print(space)
    print(space+len(cleansed))
    x ={}
    x = (freq_count(contents))
    pprint(x)
    print(type(x))

# NOTE ALL FREQ ANALYSIS DISCOUNTS NUMBERS AND punctuation

    #plot_dict(x)
    frq_perc(x)
    print("done")


def plot_dict(dict):
   # print(type(dict[0]))
    letters = []
    freq = []

    for l, f in dict.items():
        letters.append(l)
        freq.append(f)

    plt.bar(letters, freq)
    plt.show()
    plt.bar(range(len(dict)), freq, tick_label=letters)
    plt.show()

def freq_count(text):
    """
            Create a dictionary of letters A-Z and count the frequency
            of each in the supplied text.
            Lower case letters are converted to upper case.
            All other characters are ignored.
            The returned data structure is a list as we need to sort it by frequency.
            """

    frequencies = {}

    for asciicode in range(65, 91):
        frequencies[chr(asciicode)] = 0

    for letter in text:
        asciicode = ord(letter.upper())
        if asciicode >= 65 and asciicode <= 90:
            frequencies[chr(asciicode)] += 1

    #sorted_by_frequency = sorted(frequencies.items(), key=itemgetter(1), reverse=True)
    sorted_by_frequency = sorted(frequencies.items(), key=itemgetter(1), reverse=True)
    #return sorted_by_frequency
    return frequencies

def frq_perc(dict):
    letters = []
    freq = []

    for l, f in dict.items():
        letters.append(l)
        freq.append(f)
    total = sum(freq)
    print(total)
    freq2 = [((float(i)/total)*100) for i in freq]
    plt.bar(letters, freq2)
    plt.show()




def create_decryption_dictionary(plaintext_filepath, encrypted_filepath, dictionary_filepath):

    """
    Create an estimated mapping between encrypted letters and
    plaintext letters by comparing the frequencies in the
    plaintext and encrypted text.
    The dictionary is then saved as a JSON file.
    """

    sample_plaintext = _readfile(plaintext_filepath)
    encrypted_text = _readfile(encrypted_filepath)

    sample_plaintext_frequencies = freq_count(sample_plaintext)
    encrypted_text_frequencies = freq_count(encrypted_text)

    decryption_dict = {}
    for i in range(0, 26):
        decryption_dict[encrypted_text_frequencies[i][0]] = sample_plaintext_frequencies[i][0].lower()

    f = open(dictionary_filepath, "w")
    json.dump(decryption_dict, f)
    f.close()

def decrypt_file(encrypted_filepath, decrypted_filepath, dictionary_filepath):

    """
    Use the dictionary to decrypt the encrypted file
    and save the result.
    """

    encrypted_text = _readfile(encrypted_filepath)

    f = open(dictionary_filepath, "r")
    decryption_dict = json.load(f)
    f.close()

    decrypted_list = []

    for letter in encrypted_text:
        asciicode = ord(letter.upper())
        if asciicode >= 65 and asciicode <= 90:
            decrypted_list.append(decryption_dict[letter])

    decrypted_text = "".join(decrypted_list)

    f = open(decrypted_filepath, "w")
    f.write(decrypted_text)
    f.close()


def _readfile(path):

    f = open(path, "r")
    text = f.read()
    f.close()
    return text










# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    load("../Encrypted/Mission Intercept 5B_Transatlantic.md")
    load("../Encrypted/Mission Briefing 5A_ Derailed.md")