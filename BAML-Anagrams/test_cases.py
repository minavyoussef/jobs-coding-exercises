import json
import random


# ------------------------------------------------------------------------------------------------------------------
# 1. Smoke Test Cases
# ------------------------------------------------------------------------------------------------------------------

class SmokeTestAnagrams:
    @classmethod
    def test_smoke(cls, tester, uut):
        tester.assertEqual(uut.get_anagrams(''), [])
        tester.assertEqual(uut.get_anagrams(None), [])
        tester.assertEqual(uut.get_anagrams('lasting'), ['lasting', 'salting'])
        tester.assertEqual(uut.get_anagrams('bestir'), ['bestir', 'biters', 'tribes'])
        tester.assertEqual(uut.get_anagrams('nest'), ['nest', 'nets', 'sent', 'tens'])
        tester.assertEqual(uut.get_anagrams('palest'), ['palest', 'pastel', 'petals', 'plates', 'staple'])
        tester.assertEqual(uut.get_anagrams('caret'), ['caret', 'cater', 'crate', 'react', 'recta', 'trace'])
        tester.assertEqual(uut.get_anagrams('pares'), ['pares', 'parse', 'pears', 'rapes', 'reaps', 'spare', 'spear'])


# ------------------------------------------------------------------------------------------------------------------
# 2. Functional Test Cases
# ------------------------------------------------------------------------------------------------------------------

class FunctionalTestAnagrams:
    @classmethod
    def test_two_anagrams(cls, tester, uut):
        tester.assertEqual(uut.get_anagrams('lasting'), ['lasting', 'salting'])
        tester.assertEqual(uut.get_anagrams('salting'), ['lasting', 'salting'])

    @classmethod
    def test_three_anagrams(cls, tester, uut):
        tester.assertEqual(uut.get_anagrams('bestir'), ['bestir', 'biters', 'tribes'])
        tester.assertEqual(uut.get_anagrams('biters'), ['bestir', 'biters', 'tribes'])
        tester.assertEqual(uut.get_anagrams('tribes'), ['bestir', 'biters', 'tribes'])

    @classmethod
    def test_four_anagrams(cls, tester, uut):
        tester.assertEqual(uut.get_anagrams('nest'), ['nest', 'nets', 'sent', 'tens'])
        tester.assertEqual(uut.get_anagrams('nets'), ['nest', 'nets', 'sent', 'tens'])
        tester.assertEqual(uut.get_anagrams('sent'), ['nest', 'nets', 'sent', 'tens'])
        tester.assertEqual(uut.get_anagrams('tens'), ['nest', 'nets', 'sent', 'tens'])

    @classmethod
    def test_five_anagrams(cls, tester, uut):
        tester.assertEqual(uut.get_anagrams('palest'), ['palest', 'pastel', 'petals', 'plates', 'staple'])
        tester.assertEqual(uut.get_anagrams('pastel'), ['palest', 'pastel', 'petals', 'plates', 'staple'])
        tester.assertEqual(uut.get_anagrams('petals'), ['palest', 'pastel', 'petals', 'plates', 'staple'])
        tester.assertEqual(uut.get_anagrams('plates'), ['palest', 'pastel', 'petals', 'plates', 'staple'])
        tester.assertEqual(uut.get_anagrams('staple'), ['palest', 'pastel', 'petals', 'plates', 'staple'])

    @classmethod
    def test_six_anagrams(cls, tester, uut):
        tester.assertEqual(uut.get_anagrams('caret'), ['caret', 'cater', 'crate', 'react', 'recta', 'trace'])
        tester.assertEqual(uut.get_anagrams('cater'), ['caret', 'cater', 'crate', 'react', 'recta', 'trace'])
        tester.assertEqual(uut.get_anagrams('crate'), ['caret', 'cater', 'crate', 'react', 'recta', 'trace'])
        tester.assertEqual(uut.get_anagrams('react'), ['caret', 'cater', 'crate', 'react', 'recta', 'trace'])
        tester.assertEqual(uut.get_anagrams('recta'), ['caret', 'cater', 'crate', 'react', 'recta', 'trace'])
        tester.assertEqual(uut.get_anagrams('trace'), ['caret', 'cater', 'crate', 'react', 'recta', 'trace'])

    @classmethod
    def test_seven_anagrams(cls, tester, uut):
        tester.assertEqual(uut.get_anagrams('pares'), ['pares', 'parse', 'pears', 'rapes', 'reaps', 'spare', 'spear'])
        tester.assertEqual(uut.get_anagrams('parse'), ['pares', 'parse', 'pears', 'rapes', 'reaps', 'spare', 'spear'])
        tester.assertEqual(uut.get_anagrams('pears'), ['pares', 'parse', 'pears', 'rapes', 'reaps', 'spare', 'spear'])
        tester.assertEqual(uut.get_anagrams('rapes'), ['pares', 'parse', 'pears', 'rapes', 'reaps', 'spare', 'spear'])
        tester.assertEqual(uut.get_anagrams('reaps'), ['pares', 'parse', 'pears', 'rapes', 'reaps', 'spare', 'spear'])
        tester.assertEqual(uut.get_anagrams('spare'), ['pares', 'parse', 'pears', 'rapes', 'reaps', 'spare', 'spear'])
        tester.assertEqual(uut.get_anagrams('spear'), ['pares', 'parse', 'pears', 'rapes', 'reaps', 'spare', 'spear'])


# ------------------------------------------------------------------------------------------------------------------
# 3. Non-Functional Test Cases
# ------------------------------------------------------------------------------------------------------------------

class NonFunctionalTestAnagrams:
    @classmethod
    def test_invalid_parameter_type(cls, tester, uut):
        tester.assertEqual(uut.get_anagrams(13), [])
        tester.assertEqual(uut.get_anagrams(13.5), [])
        tester.assertEqual(uut.get_anagrams({}), [])
        tester.assertEqual(uut.get_anagrams([]), [])
        tester.assertEqual(uut.get_anagrams(str), [])

    @classmethod
    def test_invalid_parameter_value(cls, tester, uut):
        tester.assertEqual(uut.get_anagrams(None), [])
        tester.assertEqual(uut.get_anagrams(''), [])
        tester.assertEqual(uut.get_anagrams('WordWithControl\02Character'), [])

    @classmethod
    def test_very_long_parameter_string(cls, tester, uut):
        tester.assertEqual(uut.get_anagrams("TheQuickBrownFoxJumpsOverTheLazyDogTheQuickBrownFoxJumpsOverTheLazyDog"),
                           [])


# ------------------------------------------------------------------------------------------------------------------
# 4. Stress Test Cases
# ------------------------------------------------------------------------------------------------------------------

class StressTestAnagrams:
    @classmethod
    def test_stress(cls, tester, uut, anagrams_json_file, sample):
        anagrams_lists = cls.get_all_anagrams(anagrams_json_file)
        sample_size = int(sample * len(anagrams_lists))

        while sample_size > 0:
            anagrams = cls.random_select(anagrams_lists)
            search_word = cls.random_select(anagrams)

            tester.assertEqual(uut.get_anagrams(search_word), anagrams)
            sample_size -= 1

    @classmethod
    def get_all_anagrams(cls, anagrams_json_file):
        with open(anagrams_json_file, 'r') as infile:
            anagrams = json.load(infile)
        return anagrams

    @classmethod
    def random_select(cls, general_list):
        return general_list[random.randint(0, len(general_list) - 1)]


# ------------------------------------------------------------------------------------------------------------------
# 5. Comparative Test Cases
# ------------------------------------------------------------------------------------------------------------------

class SolutionsComparativeTestAnagrams:
    @classmethod
    def test_compare(cls, tester, uut_one, uut_two):
        tester.assertEqual(uut_one.get_anagrams(''), uut_two.get_anagrams(''))
        tester.assertEqual(uut_one.get_anagrams(None), uut_two.get_anagrams(None))
        tester.assertEqual(uut_one.get_anagrams('lasting'), uut_two.get_anagrams('lasting'))
        tester.assertEqual(uut_one.get_anagrams('bestir'), uut_two.get_anagrams('bestir'))
        tester.assertEqual(uut_one.get_anagrams('nest'), uut_two.get_anagrams('nest'))
        tester.assertEqual(uut_one.get_anagrams('palest'), uut_two.get_anagrams('palest'))
        tester.assertEqual(uut_one.get_anagrams('caret'), uut_two.get_anagrams('caret'))
        tester.assertEqual(uut_one.get_anagrams('pares'), uut_two.get_anagrams('pares'))
