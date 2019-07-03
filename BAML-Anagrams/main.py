# Given a words.txt file containing a newline-delimited list of dictionary
# words, please implement the Anagrams class so that the get_anagrams() method
# returns all anagrams from words.txt for a given word.
#
# Bonus requirements:
#   - Optimise the code for fast retrieval
#   - Write more tests
#   - Thread safe implementation

import unittest

from solutions import FastRetrievalIndexer, FastRetrievalFinder, AnagramsExecutionTemplate
from solutions import FastRetrievalIndexerThreadSafe, FastRetrievalFinderThreadSafe
from solutions import SimpleFinder, SimpleIndexer
#
# Define words list file name (assumption: file should be in same directory as solution).
#
from test_cases import SmokeTestAnagrams, FunctionalTestAnagrams, NonFunctionalTestAnagrams, \
    SolutionsComparativeTestAnagrams, StressTestAnagrams

# ------------------------------------------------------------------------------------------------------------------
# Configurations
# ------------------------------------------------------------------------------------------------------------------

WORDS_FILE = 'words.txt'

#
# Define all anagrams file name (assumption: file should be in same directory as solution).
#
ALL_ANAGRAMS_FILE = 'all_anagrams.json'


#
# Define Different configuration setup and act as dependency injection
#
def get_simple_solution_config():
    return SimpleIndexer(), SimpleFinder()


def get_fast_retrieval_solution_config():
    return FastRetrievalIndexer(), FastRetrievalFinder()


def get_fast_retrieval_thread_safe_solution_config():
    return FastRetrievalIndexerThreadSafe(), FastRetrievalFinderThreadSafe()


# ------------------------------------------------------------------------------------------------------------------
# Main
# ------------------------------------------------------------------------------------------------------------------

class Anagrams:
    def __init__(self, config_func):
        # Using with to ensure file is close after.
        with open(WORDS_FILE, 'r') as file_words:
            self.words = [word.strip() for word in file_words.readlines()]

        # Create Template executor solver instance.
        self.solver = AnagramsExecutionTemplate()

        # Create and configure the actual solver as Strategy Design Pattern.
        indexer, finder = config_func()
        self.solver.set_config(indexer, finder)
        self.solver.initialize(self.words)

    def get_anagrams(self, word):
        return self.solver.find_anagram(word)


class TestAnagrams(unittest.TestCase):
    """
    Class TestAnagrams provide unit testing for the following solutions:
        - Simple Solution
        - Fast Retrieval Solution
        - Fast Retrieval Solution (Thread Safe)
    """

    @classmethod
    def get_all_solution_configs(cls):
        return [get_simple_solution_config,
                get_fast_retrieval_solution_config,
                get_fast_retrieval_thread_safe_solution_config]

    def test_smoke(self):
        """
        In SmokeTestAnagrams we test basic functional/non-functional features, one sample of every anagram size
        and part of invalid params

        :return:
        :rtype:
        """
        for solution_config in self.get_all_solution_configs():
            anagrams = Anagrams(solution_config)
            SmokeTestAnagrams.test_smoke(tester=self, uut=anagrams)

    def test_functional(self):
        """
        In FunctionTestAnagrams we test the correct functional behavior for 2, 3, 4, 5, 6 and 7 anagram counts (i.e. all differencet
        sizes of anagrams results from words.txt)

        And doing testing all possible words that would result in a given anagrams set.

        :return: None
        :rtype: None
        """
        for solution_config in self.get_all_solution_configs():
            anagrams = Anagrams(solution_config)
            FunctionalTestAnagrams.test_two_anagrams(tester=self, uut=anagrams)
            FunctionalTestAnagrams.test_three_anagrams(tester=self, uut=anagrams)
            FunctionalTestAnagrams.test_four_anagrams(tester=self, uut=anagrams)
            FunctionalTestAnagrams.test_five_anagrams(tester=self, uut=anagrams)
            FunctionalTestAnagrams.test_six_anagrams(tester=self, uut=anagrams)
            FunctionalTestAnagrams.test_seven_anagrams(tester=self, uut=anagrams)

    def test_non_functional(self):
        """
        In NonFunctionTestAnagrams we test for invalid parameters/miss-use of the API, and in this case I followed returning
        empty list []

        Invalid parameters could be:
            - None
            - Empty string literal
            - Different data type
            - very long string

        :return: None
        :rtype: None
        """

        for solution_config in self.get_all_solution_configs():
            anagrams = Anagrams(solution_config)
            NonFunctionalTestAnagrams.test_invalid_parameter_type(tester=self, uut=anagrams)
            NonFunctionalTestAnagrams.test_invalid_parameter_value(tester=self, uut=anagrams)
            NonFunctionalTestAnagrams.test_very_long_parameter_string(tester=self, uut=anagrams)

    def test_stress(self):
        """
        In StressTestAnagrams we stress test the solution given sample size between ]0, 1] (default is 0.1) 10% of all anagrams,
        Where we load all anagrams, randomly select a sample and then randomly select search word.

        :return: None
        :rtype: None
        """
        for solution_config in self.get_all_solution_configs():
            anagrams = Anagrams(solution_config)
            StressTestAnagrams.test_stress(tester=self, uut=anagrams, anagrams_json_file=ALL_ANAGRAMS_FILE, sample=0.01)

    def test_comparative(self):
        """
        In SolutionsComparativeTestAnagrams we compare the results of the three approaches against each other.

        :return: None
        :rtype: None
        """

        anagrams_solver_simple = Anagrams(get_simple_solution_config)
        anagrams_solver_fast = Anagrams(get_fast_retrieval_solution_config)
        anagrams_solver_fast_thread_safe = Anagrams(get_fast_retrieval_thread_safe_solution_config)

        SolutionsComparativeTestAnagrams.test_compare(tester=self,
                                                      uut_one=anagrams_solver_simple,
                                                      uut_two=anagrams_solver_fast)
        SolutionsComparativeTestAnagrams.test_compare(tester=self,
                                                      uut_one=anagrams_solver_simple,
                                                      uut_two=anagrams_solver_fast_thread_safe)
        SolutionsComparativeTestAnagrams.test_compare(tester=self,
                                                      uut_one=anagrams_solver_fast,
                                                      uut_two=anagrams_solver_fast_thread_safe)


if __name__ == '__main__':
    unittest.main()
