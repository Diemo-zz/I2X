import os
import pickle
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords


def get_keywords_and_values(words):
    """
    Takes in a list of words and calculates the weighted average of each one, two and three letter keyword in the list. 
    Keywords of size two are weighted to be three times as as good as keywords of size one, and keywords of size three
    are weighted to be five times as good as keywords of size one.

    :param words: list
        list of words to calculate keywords from

    :return: dict
        key: keyword
        value: weighted keyword value
    """

    d = {}
    triple_keyword_value = 5
    double_keyword_value = 3
    single_keyword_occurance_value = 1

    stop_words = set(stopwords.words("english"))

    for i in range(0, len(words) - 2):
        if words[i] not in stop_words and words[i].isalnum():
            d[words[i]] = d.get(words[i], 0.0) + single_keyword_occurance_value
            if words[i + 1] not in stop_words and words[i + 1].isalnum():
                d[words[i] + " " + words[i + 1]] = d.get(words[i] + " " + words[i + 1], 0.0) + double_keyword_value
                if words[i + 2] not in stop_words and words[i + 2].isalnum():
                    d[words[i] + " " + words[i + 1] + " " + words[i + 2]] = d.get(
                        words[i] + " " + words[i + 1] + " " + words[i + 2], 0.0) + triple_keyword_value

    if words[i + 1] not in stop_words and words[i + 1].isalnum():
        d[words[i + 1]] = d.get(words[i + 1], 0.0) + single_keyword_occurance_value
        if words[i + 2] not in stop_words and words[i + 2].isalnum():
            d[words[i + 1] + " " + words[i + 2]] = d.get(words[i + 1] + " " + words[i + 2], 0.0) + double_keyword_value
    if words[i + 2] not in stop_words and words[+2].isalnum():
        d[words[i + 2]] = d.get(words[i + 2], 0.0) + single_keyword_occurance_value
    return d


def get_lemitized_words_in_order(file_in):
    """

    :param file_in: str
        Path to the file to read in

    :return: list
        a list of all lemmitized words from the file
    """

    lemmitizer = WordNetLemmatizer()

    lexicon = []
    with open(file_in, 'r') as f:
        contents = f.readlines()
        for l in contents[:]:
            all_words = word_tokenize(l)
            for i in all_words:
                lexicon.append(i.lower())
    lexicon = [lemmitizer.lemmatize(i) for i in lexicon]
    return lexicon


def create_words_and_values(file_in):
    """

    :param file_in: str
        path to the file

    :return: dict
        key = word
        value = calculated keyword value for that file
    """

    # Read all the words into a list
    words_in_order = get_lemitized_words_in_order(file_in)

    # assign the values
    words_and_values = get_keywords_and_values(words_in_order)

    return words_and_values


def save_words_and_values(file_in, save_file):
    """


    :param file_in: str
        path to file to calculate words and values for
    :param save_file: str
        path to file to save the calculated word/value pairs

    :return: null
    """
    results = create_words_and_values(file_in)

    pickle.dump(results, open(save_file, 'wb'))


def evaluate_file(file_in):
    """
    A function that takes in a file, calculates the values, and saves the resulting dictionary to a .pickle file with 
    the same stem.
    :param file_in: str
        path to the file to evaluate
    :return: 
    """

    save_file = os.path.join(os.path.dirname(file_in), os.path.splitext(os.path.basename(file_in))[0] + ".pickle")
    print("Calculating values from", file_in, " and saving list to ", save_file)

    save_words_and_values(file_in, save_file)


def main():
    file_in = input("Please input the file to create the list from")
    evaluate_file(file_in)


if __name__ == "__main__":
    main()