from unittest import TestCase, mock

from anagrams.__main__ import anagrams

word_list_empty = []
word_list_1 = [
    "Chitina\n",
    "Chianti\n",
    "Chaitin\n",
    "supers\n",
    "purses\n",
    "pusser\n",
    "sprues\n",
    "chaitin\n",
    "a\n",
    "B\n",
]

module_path = "anagrams.__main__"


class AnagramsTest(TestCase):
    @mock.patch(f"{module_path}.load_words", return_value=word_list_empty)
    def test_it_should_pass_if_return_empty_list(self, loader):
        self.assertEqual(anagrams(), [])

    @mock.patch(f"{module_path}.load_words", return_value=word_list_1)
    def test_it_should_pass_if_input_is_valid_case_sensitive(self, loader):
        actual = anagrams(case_sensitive=True)
        self.assertCountEqual(actual[0], ["Chitina", "Chaitin", "Chianti"])
        self.assertCountEqual(actual[1], ["sprues", "purses", "pusser", "supers"])

    @mock.patch(f"{module_path}.load_words", return_value=word_list_1)
    def test_it_should_pass_if_input_is_valid_case_insensitive(self, loader):
        actual = anagrams(case_sensitive=False)
        self.assertCountEqual(actual[0], ["chaitin", "chianti", "chitina"])
        self.assertCountEqual(actual[1], ["sprues", "purses", "pusser", "supers"])

    @mock.patch(f"{module_path}.load_words", return_value=word_list_1)
    def test_it_should_pass_if_each_list_has_more_than_one_item(self, loader):
        actual = anagrams()
        for arr in actual:
            self.assertGreater(len(arr), 1)

    @mock.patch(f"{module_path}.load_words", return_value=word_list_1)
    def test_it_should_pass_if_anagram_lists_item_not_duplicated(self, loader):
        actual = anagrams(True)
        for arr in actual:
            duplicates = [x for x in arr if arr.count(x) >= 2]
            self.assertLess(len(duplicates), 2)

    @mock.patch(f"{module_path}.load_words", return_value=word_list_1)
    def test_it_should_pass_if_words_not_contain_escape_characters(self, loader):
        actual = anagrams()
        for arr in actual:
            for item in arr:
                self.assertNotIn("\n", item)

    @mock.patch(f"{module_path}.load_words", return_value=word_list_1)
    def test_it_should_pass_if_ignore_one_char_words(self, loader):
        actual = anagrams()
        for arr in actual:
            for item in arr:
                self.assertGreater(len(item), 1)
