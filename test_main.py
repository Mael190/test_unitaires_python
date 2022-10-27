import unittest
import main
from datetime import datetime


class TestMain(unittest.TestCase):
    def test_hello_morning(self):
        date = datetime.now().replace(hour=11)
        self.assertEqual(main.hello(date), 'C\'est l\'heure du café')

    def test_hello_moon(self):
        date = datetime.now().replace(hour=12)
        self.assertEqual(main.hello(date), 'Il va falloir penser à aller manger')

    def test_hello_afternoon(self):
        date = datetime.now().replace(hour=16)
        self.assertEqual(main.hello(date), 'Bonne journée')

    def test_goodbye_morning(self):
        date = datetime.now().replace(hour=11)
        self.assertEqual(main.goodbye(date), 'Bonne fin de matinée')

    def test_goodbye_moon(self):
        date = datetime.now().replace(hour=12)
        self.assertEqual(main.goodbye(date), 'Bon apétit')

    def test_goodbye_afternoon(self):
        date = datetime.now().replace(hour=16)
        self.assertEqual(main.goodbye(date), 'La journée est bientôt finit')

    def test_mirror_true(self):
        self.assertEqual(main.miror('thomas'), 'samoht')

    def test_mirror_true(self):
        self.assertNotEqual(main.miror('thomas'), 'izefuhi')

    def test_palindrome_true(self):
        self.assertTrue(main.isPalindrome('kayak'))

    def test_palindrome_false(self):
        self.assertFalse(main.isPalindrome('thomas'))


if __name__ == '__main__':
    unittest.main()
