import threading


# ------------------------------------------------------------------------------------------------------------------
# Execution Controller
# ------------------------------------------------------------------------------------------------------------------

class AnagramsExecutionTemplate:
    """
    Class AnagramsExecutionTemplate act as both Facade and Template methods class
    [https://en.wikipedia.org/wiki/Facade_pattern and https://en.wikipedia.org/wiki/Template_method_pattern]

    With main components:
        - Indexer: Used to perform indexing on list of words
        - Finder: Use to search for anagrams
    """

    def __init__(self):
        self.indexer = None
        self.finder = None

    def set_config(self, indexer, finder):
        self.indexer = indexer
        self.finder = finder

    def validate(self, word):
        if self.indexer is None:
            raise Exception('Data Indexer is not set')
        if self.finder is None:
            raise Exception('Data Finder is not set')

        return self.validate_param(word)

    @classmethod
    def validate_param(cls, word):
        return word is not None and \
               isinstance(word, str) and \
               word != '' and \
               not cls.has_control_char(word)

    @classmethod
    def has_control_char(cls, word):
        for c in word:
            if 0 <= ord(c) <= 31:
                return True
        return False

    def initialize(self, words_list):
        indexed_data = self.indexer.perform_indexing(words_list)
        self.finder.set_data(indexed_data)

    def find_anagram(self, word):
        """
        Find all possible anagrams using finder component.

        :param word: Word to search against
        :type word: str
        :return: list of anagrams
        :rtype: list of strings
        """

        if not self.validate(word):
            return []
        return self.finder.find_anagram(word)


# ------------------------------------------------------------------------------------------------------------------
# Approach #1 - Simple Solution
# ------------------------------------------------------------------------------------------------------------------

class SimpleFinder:
    """
    SimpleFinder provides simple approach implementation for anagrams finder.
    """

    def __init__(self):
        self.words_list = None

    def set_data(self, words_list):
        """
        Set words list.

        :param words_list: list of words to be searched
        :type words_list: list
        :return: None
        :rtype: None
        """

        self.words_list = words_list

    def validate(self):
        """
        Validate the state of instance before performing searching.

        :return: True is valid, False otherwise.
        :rtype: bool
        """

        if self.words_list is None:
            raise Exception('Words list is not set')

    def find_anagram(self, word):
        """
        Find list of anagrams given a words, if any
        Complexity O(n)

        :param word: word to be used as a search reference.
        :type word: str
        :return: list of anagrams
        :rtype: list
        """

        self.validate()

        anagrams = []
        word_freq_table = calculate_frequency_table(word)
        for iter_word in self.words_list:
            iter_word_freq_table = calculate_frequency_table(iter_word)
            if word_freq_table == iter_word_freq_table:
                anagrams.append(iter_word)

        return anagrams


class SimpleIndexer:
    """
    SimpleIndexer provides simple approach implementation for anagrams indexers.
    """

    def perform_indexing(self, words_list):
        """
        Simple solution approach does not require any kind of indexing therefore return the the same world list,
        SimpleIndexer [implements a Null Object Design Pattern (https://en.wikipedia.org/wiki/Null_object_pattern)]
        to be used by the Template Executor AnagramsExecutionTemplate [implements a Template Method
        Design Pattern https://en.wikipedia.org/wiki/Template_method_pattern]

        @param words_list: loaded words list
        @type words_list: list()
        @return: unmodified loaded words list
        @rtype: list()
        """
        return words_list


# ------------------------------------------------------------------------------------------------------------------
# Approach #2 - Fast Retrieval Solution
# ------------------------------------------------------------------------------------------------------------------

class FastRetrievalFinder:
    """
    FastRetrievalFinder provides fast retrieval approach implementation for anagrams finder.
    """

    def __init__(self):
        self.indexer_table = None

    def set_data(self, indexer_table):
        """
        Set indexer table to be used in anagram finder.

        :param indexer_table: list of words to be searched
        :type indexer_table: dictionary of dictionary of anagrams
            indexer_table[<hash_value>][<frequency_table>] = [<Anagrams list>]
        :return: None
        :rtype: None
        """

        self.indexer_table = indexer_table

    def validate(self):
        """
        Validate the state of instance before performing searching.

        :return: True is valid, False otherwise.
        :rtype: bool
        """

        if self.indexer_table is None:
            raise Exception('Indexed words table is not set')

    def find_anagram(self, word):
        """
        Find list of anagrams given a words, if any
        Complexity O(1)

        :param word: word to be used as a search reference.
        :type word: str
        :return: list of anagrams
        :rtype: list
        """

        self.validate()

        hash_value = FastRetrievalIndexer.calculate_weighted_hash(word)
        freq_table = calculate_frequency_table(word)

        if hash_value not in self.indexer_table:
            return []
        if as_set(freq_table) not in self.indexer_table[hash_value]:
            return []
        return self.indexer_table[hash_value][as_set(freq_table)]


class FastRetrievalIndexer:
    """
    FastRetrievalIndexer provides fast retrieval approach implementation for anagrams indexers.
    """

    # Alphabets hashing with the following conditions to minimize hash table hit collision:
    #   - Hash values are primes
    #   - Delta between two consecutive numbers are unique
    alpha_lookup = {
        'a': 2,
        'b': 3,
        'c': 5,
        'd': 11,
        'e': 19,
        'f': 23,
        'g': 37,
        'h': 47,
        'i': 59,
        'j': 79,
        'k': 97,
        'l': 113,
        'm': 137,
        'n': 163,
        'o': 191,
        'p': 223,
        'q': 257,
        'r': 293,
        's': 331,
        't': 353,
        'u': 383,
        'v': 431,
        'w': 487,
        'x': 541,
        'y': 587,
        'z': 631,
        '-': 673,
        '\'': 733,
        '2': 773,
        '3': 823
    }

    def perform_indexing(self, words_list):
        """
        Perform and return indexed data structure given list of words.

        :param words_list: loaded words list
        :type words_list: list()
        :return indexer_table: list of words to be searched
        :rtype indexer_table: dictionary of dictionary of anagrams
            indexer_table[<hash_value>][<frequency_table>] = [<Anagrams list>]
        """

        indexer_table = {}

        for word in words_list:
            hash_value = self.calculate_weighted_hash(word)
            freq_table = calculate_frequency_table(word)

            if hash_value not in indexer_table:
                indexer_table[hash_value] = {}
                indexer_table[hash_value][as_set(freq_table)] = [word]
            else:
                if as_set(freq_table) not in indexer_table[hash_value]:
                    indexer_table[hash_value][as_set(freq_table)] = [word]
                else:
                    indexer_table[hash_value][as_set(freq_table)].append(word)

        return indexer_table

    @classmethod
    def calculate_weighted_hash(cls, word):
        """
        Calculate hash value of given word.

        :param word: Word to calculate hash value of.
        :type word: str
        :return: Hashed value of given word.
        :rtype: int
        """

        hash_value = 0
        for char in word:
            hash_value += cls.alpha_lookup[char.lower()]
        return hash_value


# ------------------------------------------------------------------------------------------------------------------
# Bonus - ThreadSafe Solution
# ------------------------------------------------------------------------------------------------------------------

class FastRetrievalFinderThreadSafe:
    """
    FastRetrievalFinderThreadSafe provides thread safe fast retrieval approach implementation for anagrams finder.
    By wrapping FastRetrievalFinder as proxy class [implementing Proxy Design Pattern https://en.wikipedia.org/wiki/Proxy_pattern]
    """

    def __init__(self):
        self.finder = FastRetrievalFinder()
        self.lock = threading.RLock()  # Using RLock for same-thread non-blocking

    def set_data(self, indexer_table):
        with self.lock:
            self.finder.indexer_table = indexer_table

    def validate(self):
        with self.lock:
            if self.finder.indexer_table is None:
                raise Exception('Indexed words table is not set')

    def find_anagram(self, word):
        with self.lock:
            return self.finder.find_anagram(word)


class FastRetrievalIndexerThreadSafe:
    """
    FastRetrievalIndexerThreadSafe provides thread safe fast retrieval approach implementation for anagrams indexer.
    By wrapping FastRetrievalIndexer as proxy class [implementing Proxy Design Pattern https://en.wikipedia.org/wiki/Proxy_pattern]
    """

    def __init__(self):
        self.indexer = FastRetrievalIndexer()
        self.lock = threading.RLock()  # Using RLock for same-thread non-blocking

    def perform_indexing(self, words_list):
        with self.lock:
            return self.indexer.perform_indexing(words_list)


# ------------------------------------------------------------------------------------------------------------------
# Utilities
# ------------------------------------------------------------------------------------------------------------------


def as_set(dict_inst):
    """
    [Helper] Get dictionary as frozenset instance.

    :param dict_inst: Dictionary to be returned as frozenset.
    :type dict_inst: Dictionary.
    :return: Equivalent frozenset.
    :rtype: frozenset.
    """

    return frozenset(dict_inst.items()) if isinstance(dict_inst, dict) else None


def calculate_frequency_table(word):
    """
    Calculate frequency table of a given string.

    :param word: String to be calculated frequency table of.
    :type word: String.
    :return: Dictionary of frequency of occurrence of each character of.
    :rtype: Dictionary
    """

    frequency_table = {}
    if word is None:
        return frequency_table

    for char in word:
        if char not in frequency_table.keys():
            frequency_table[char] = 1
        else:
            frequency_table[char] += 1

    return frequency_table
