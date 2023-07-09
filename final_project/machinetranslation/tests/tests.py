import unittest
from translator import englishToFrench, frenchToEnglish

class TestMymodule(unittest.TestCase):

    def test_englishToFrench(self):
        self.assertEqual(englishToFrench('Good morning'), 'Bonjour')


    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish('Merci'), 'Thank you')

if __name__ == '__main__':
    unittest.main()