from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):

    def test_add_numbers(self):
        res = calc.add(3, 2)
        self.assertEqual(res, 5)
