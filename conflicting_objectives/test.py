from unittest import TestCase
from unittest.mock import patch, mock_open

from conflicting_objectives.__main__ import conflicting_objectives

word_list = "emigrationists\npearlites\npeascods\npeaklike\nrewear\n" \
            "re\nwear\na\nEmigrationists\nrewear\nRewear\nRe\npear\nlites\ncodlik\n"


class ConflictingObjectivesTest(TestCase):
    @patch("builtins.open", mock_open(read_data=word_list))
    def test_it_should_pass_if_result_not_contain_escape_characters(self):
        actual = conflicting_objectives()
        for case in actual:
            for item in case:
                self.assertNotIn("\n", item)

    @patch("builtins.open", mock_open(read_data=word_list))
    def test_it_should_pass_if_result_word_length_greater_than_one(self):
        actual = conflicting_objectives()
        for case in actual:
            for item in case:
                self.assertGreater(len(item), 1)

    @patch("builtins.open", mock_open(read_data=word_list))
    def test_it_should_pass_if_result_word_length_less_or_equal_word_length_limit(self):
        word_length_limit = 6
        actual = conflicting_objectives(word_length_limit)
        for case in actual:
            for item in case:
                self.assertLessEqual(len(item), word_length_limit)

    @patch("builtins.open", mock_open(read_data=word_list))
    def test_it_should_pass_if_result_not_duplicated(self):
        word_length_limit = 6
        actual = conflicting_objectives(word_length_limit=word_length_limit)

        duplicates = [x for x in actual if actual.count(x[0])]
        self.assertLess(len(duplicates), 2)

    @patch("builtins.open", mock_open(read_data=word_list))
    def test_it_should_pass_if_result_is_correct_when_case_sensitive(self):
        actual = conflicting_objectives(case_sensitive=True)
        self.assertCountEqual(
            actual, [["rewear", "re", "wear"], ["Rewear", "Re", "wear"]]
        )

    @patch("builtins.open", mock_open(read_data=word_list))
    def test_it_should_pass_if_result_is_correct_when_case_insensitive(self):
        actual = conflicting_objectives(case_sensitive=False)
        self.assertCountEqual(actual, [["rewear", "re", "wear"]])
