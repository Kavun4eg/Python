import unittest
from tests_functions import even_num_sum

class TestSumFunction(unittest.TestCase):
    def test_even_num_sum_1(self):
        actual_result = even_num_sum([1, 3, 5, 6, 8, 4])
        expected_result = 18
        self.assertEqual(actual_result, expected_result)

    def test_even_num_sum_2(self):
        actual_result = even_num_sum([2, 5, 7, 4])
        expected_result = 6
        self.assertEqual(actual_result, expected_result)

    def test_even_num_sum_3(self):
        actual_result = even_num_sum([3, 7, 9, 11])
        expected_result = 0
        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()

    from tests_functions import longest_word
    class TestWordFunction(unittest.TestCase):
        def test_longest_w_1(self):
            actual_result = longest_word(words=['Hello', 'how', 'are', 'you', 'feeling'])
            expected_result = 'feeling'
            self.assertEqual(actual_result, expected_result)

        def test_longest_w_2(self):
            actual_result = longest_word(words=['its', 'me', 'here'])
            expected_result = 'here'
            self.assertEqual(actual_result, expected_result)

        def test_longest_w_3(self):
            actual_result = longest_word(words=['nice', 'outside', 'now'])
            expected_result = 'outside'
            self.assertEqual(actual_result, expected_result)

        def test_longest_w_4(self):
            actual_result = longest_word(words=['maybe', 'tomorrow', 'we', 'meet'])
            expected_result = 'tomorrow'
            self.assertEqual(actual_result, expected_result)


    if __name__ == '__main__':
        unittest.main()
from tests_functions import only_str_list

class TestStrFunction(unittest.TestCase):
    def test_only_str_1(self):
        actual_result = only_str_list(lst1=['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'])
        expected_result = ['1', '2', 'False', '6', 'Python', 'Lorem Ipsum']
        self.assertEqual(actual_result, expected_result)

    def test_only_str_2(self):
        actual_result = only_str_list(lst1=[7, 8, 9, None])
        expected_result = []
        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()
