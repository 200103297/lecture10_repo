import unittest

from django.test import TestCase
class YourTestClass(TestCase):

    def setUp(self):
        print("setUp")
        pass

    def test_false(self):
        print("False method")
        self.assertFalse(False)

    def test_two_times_two(self):
        print("multiplication method")
        self.assertEqual(2*2, 4)

    def test_is_bigger(self):
        num = 33
        self.assertTrue(num>32)

    def test_is_lower(self):
        num2 = 1
        self.assertTrue(num2<5)