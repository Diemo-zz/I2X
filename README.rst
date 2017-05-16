Package Info
------------

To install diarmaidi2xpackage, clone this repository. Enter the I2X folder and run 'pip install .'. This will install
the diarmaidi2xpackage, together with it's requirements.

You can run tests by running 'python3 setup.py test' from inside the I2X folder.

To Use
------
Open a python terminal. Import the package using 'import diarmaidi2xpackage as dp'.  you can then call the package
commands by typing dp.<command>.

To create a keyword-value dictionary run 'dp.create_words_and_values(file_in)'. This will create a dictionary of
keywords and values.

You can save this dictionary by running 'dp.save_words_and_values(file_in, save_file)', where file_in is the path to
the file you want to analyse, and save_file is the path to the file you want to save the dictionary to.

To get the top keywords, use run 'dp.top_values(dict_in, n)', where dict_in is the output of create_words_and_values,
and n is the number of key-words to get. This will return a list of the top n keywords.

To compare a set of keywords to a file, run 'dp.compare_single_file(keywords_in, file_in), where key-words is the list
of words to compare and file_in is the path to the file to compare it with. This will return a sorted list of
(word,value) pairs.

To compare a pregenerated list to a list of files, call 'db.compare_file_list(words_in, files_in)', where words in is
the list of the top n keywords and files is a list of paths to the files to be compared. This will return a sorted list
of (word, value) pairs (holding the average value calculated over all files, and a dictionary holding the calculated
values for each file.

If the corpus is in a seperate directory, you can check the entire directory against a pregenerated list of keywords by
calling 'db.evaluate_corpus(save_file, n, directory_in), where save_file is the file that the dictionary of
keyword-values are saved to, n is the number of keywords to compare, and directory_in is a directory holding the corpus
to compare. This has the same output as 'db.compare_file_list()'.

Note that this will only compare against files ending in '.txt'.

If you want to compare the keywords generated from a particular file to a directory, you can do this by calling
'db.run(file_to_get_keywords, number_of_keywords, directory_to_compare)'. Here file_to_get_keywords is the path to the
file to use to create the keywords, and directory to compare is the directory holding the corpus. This has the same
output as 'db.compare_file_list()'.

Full list of commands
+++++++++++++++++++++
get_keywords_and_values,
get_lemitized_words_in_order, create_words_and_values,save_words_and_values, evaluate_file
get_all_txt_files_in_directory,compare_single_file,compare_file_list,get_sorted_key_words,get_top_values
get_overall_values_only, run

Requirements
------------
To install nltk manually, you can run
<sudo> pip install nltk

The requirements are the nltk datasets: "punkt", "stopwords", and "wordnet". If these fail to download them you can
install them manually by opening a python shell and running

>>>import nltk

>>>nltk.download(<dataset>)

>>>nltk.download("punkt")
