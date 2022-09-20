from unittest import TestCase, main
from hw import moveZerosToEnd

class moveZerosToEnd(TestCase):
    def test_1_front(self):
        self.assertEqual(moveZerosToEnd[0,0,0,4,5,6,7],[1,2,3,4,0,0])

    def test_2_zeros_between(self):
        self.assertEqual(moveZerosToEnd[1,2,0,0,5,6,7][1,2,5,6,7,0,0])

    def test_3_no_zeros(self):
        self.assetEqual(moveZerosToEnd[1,2,3,4,5,6][1,2,3,4,5,6])