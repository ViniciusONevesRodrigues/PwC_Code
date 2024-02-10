import unittest
from functions import *

class TestAddressFunctions(unittest.TestCase):

    def test_address_redirector_normal_address(self):
        result = address_redirector("Miritiba 339")
        self.assertEqual(result, '{"Miritiba", "339"}')

    def test_address_redirector_bigger_address(self):
        result = address_redirector('Quirino dos Santos 23 b')
        self.assertEqual(result, '{"Quirino dos Santos", "23 b"}')

    def test_address_redirector_foreigner_address_comma_and_number(self):
        result = address_redirector("4, Rue de la République")
        self.assertEqual(result, '{"Rue de la République", "4"}')

    def test_address_redirector_foreigner_address_number(self):
        result = address_redirector("100 Broadway Av")
        self.assertEqual(result, '{"Broadway Av", "100"}')

    def test_address_redirector_foreigner_address_comma(self):
        result = address_redirector("Calle Sagasta, 26")
        self.assertEqual(result, '{"Calle Sagasta", "26"}')

    def test_address_redirector_foreigner_address_No(self):
        result = address_redirector("Calle 44 No 1991")
        self.assertEqual(result, '{"Calle 44", "No 1991"}')

    def test_is_foreigner_address_comma(self):
        result = is_foreigner_address(["4,", "Rue", "de", "la", "République"])
        self.assertTrue(result)

    def test_is_foreigner_address_no(self):
        result = is_foreigner_address(["Calle", "44", "No", "1991"])
        self.assertTrue(result)

    def test_is_foreigner_address_number(self):
        result = is_foreigner_address(["100", "Broadway", "Av"])
        self.assertTrue(result)

    def test_has_number_with_number(self):
        result = has_number("123")
        self.assertTrue(result)

    def test_has_number_without_number(self):
        result = has_number("abc")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
