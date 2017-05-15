import os
import pickle
from collections import Counter
from operator import itemgetter
from pprint import pprint as pp

from diarmaidi2xpackage import create_words_and_values, save_words_and_values


def get_all_txt_files_in_directory(directoryIn):
    """
    Get all of the files in the directory which end in .txt

    :param directoryIn: str
        Path to the directory to evaluate
    :return: list
        list of all files in the directory
    """

    fileshan = []
    for root, dirs, files in os.walk(directoryIn):
        for file in files:
            if file.endswith(".txt"):
                l = os.path.join(root, file)
                fileshan.append(l)

    return fileshan


def compare_single_file(words_in, file_in):
    """
    Takes as input a list of words and compares it to all words in a file.
    Ranks each word as by frequency of the words occurrence in the file.

    :param words_in: list
        A list of words in string format to be compared to the words in file_in
    :param file_in: str
        The file path for the text to be compared

    :return: collections.Counter()
        key: str, word
        value: real ,weighted_average
    """
    results = create_words_and_values(file_in)

    s = sum(results.values())

    overall_value = {}
    for word in words_in:
        # Get the weighted percentage of the keyword
        weighted_average = 100 * results.get(word, 0.0) / s
        overall_value[word] = weighted_average
    return Counter(overall_value)


def compare_file_list(words_in, files_in):
    """

    Compare a list of words with the words in each file in files_in.
    Return a list of word values for each file and an overall value

    :param words_in: list
        A list of words in string format
    :param files_in: list
        A list of file paths

    :return: list, dict
        sorted_values: list
            a list of tuples, with each tuple holding the word/value pair
        file_values: dict
            key: file_name
            value: collections.Counter
                key: word
                Value: Holds the calculated weighted average for each word for each file. 
    """
    overall_value = Counter({})
    file_values = {}

    for file_in in files_in:
        values_out = compare_single_file(words_in, file_in)
        overall_value += values_out
        file_values[file_in] = sorted(values_out.items(), key=itemgetter(1), reverse=True)

    for word in words_in:
        overall_value[word] = overall_value.get(word, 0.0) / len(files_in)

    sorted_values = sorted(overall_value.items(), key=itemgetter(1), reverse=True)
    return sorted_values, file_values


def get_sorted_key_words(file_in):
    """
    Simple subroutine to read in the data
    :param file_in: str
        Path of the file to read the kew-words from

    :return: list
        A list of the the sorted keywords 

    """
    x = pickle.load(open(file_in, 'rb'))
    sorted_x = sorted(x.items(), key=itemgetter(1), reverse=True)

    sorted_words = list(map(itemgetter(0), sorted_x))
    return sorted_words


def get_top_n_values(dict_in, n):
    """
    Sort the dictionary created in create_keywords_and_values
    
    :param dict_in: dict
        Dictionary you want to sort
    :param n: integer
        number of elements to return
    :return: list
        Sorted values
    """
    sorted_x = sorted(dict_in.items(), key=itemgetter(1), reverse=True)

    sorted_words = list(map(itemgetter(0), sorted_x))
    return sorted_words[0:n]

def get_top_values(file_in, n):
    """
    Get the top n keywords to use
    :param file_in: str
        path of the file to read the keywords from
    :param n: integer
        number of keywords to get

    :return: sorted_words: list
        A list of the top n keywords
    """

    sorted_words = get_sorted_key_words(file_in)

    return sorted_words[0:n]


def evaluate_corpus(word_file_in, number_of_words_in, directory_in):
    """
    Evaluate all of the files in a directory with the file ending '.txt.   Return the overall weighted average of the words, and the weighted average of the words for each file.

    :param word_file_in: str
        Path to the file holding the dictionary of keywords to use
    :param number_of_words_in: integer
        Number of words to compare
    :param directory_in: str
        Path to the directory to check

    :return:
     val: list
        Overall weighted average for all files.   Each element in the list is a word/value pair. The list is sorted, with higher values first.
     file_val: dict
        Holds the values for each file
            key: filename
            Value: list
                Weighted average for each word

    """

    values = get_top_values(word_file_in, number_of_words_in)

    files = get_all_txt_files_in_directory(directory_in)

    val, file_val = compare_file_list(values, files)
    return val, file_val


def get_overall_values_only(word_file_in, number_of_words_in, directory_in):
    """
    Evaluate all of the files in a directory with the file ending '.txt.   Return the overall weighted average of the words.

    :param word_file_in: str
        Path to the file holding the dictionary of keywords to use
    :param number_of_words_in: integer
        Number of words to compare
    :param directory_in: str
        Path to the directory to check

    :return:
     val: list
        Overall weighted average for all files.   Each element in the list is a word/value pair. The list is sorted, with higher values first.

    """
    val, file_val = evaluate_corpus(word_file_in, number_of_words_in, directory_in)
    return val

def run(file_in, number_of_words_in, directory_in):
    """
    
    :param file_in: str
        path of the file to get keywords from
    :param number_of_words_in: integer
        number of keywords to use
    :param directory_in: str
        path to directory to use. It will compare the keywords to each '.txt' file in the directory
    :return: 
    val: list
        Overall weighted average for all files.   Each element in the list is a word/value pair. The list is sorted, with higher values first.
    file_val: dict
        Holds the values for each file
        key: filename
        Value: list
            Weighted average for each word
    
    """
    savefile = file_in+".pickle"
    save_words_and_values(file_in, savefile)

    overall_val, file_val = evaluate_corpus(savefile, number_of_words_in,directory_in)

    return overall_val, file_val


def main():
    file_in = input("Please input the file to load the dataset from")
    number = eval(input("Please input the number of words to use"))

    directory_in = input("Please input the directory holding the corpus of information")
    pp(get_overall_values_only(file_in, number, directory_in))



if __name__ == "__main__":
    main()
