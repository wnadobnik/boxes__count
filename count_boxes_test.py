import unittest
from count_boxes import count_boxes

class TextBoxes(unittest.TestCase):

    def test_boxes(self):
        result = count_boxes(1)
        self.assertEqual(result['small'], 1)
        self.assertEqual(result['medium'], 0)
        self.assertEqual(result['large'], 0)
        result = count_boxes(3)
        self.assertEqual(result['small'], 1)
        self.assertEqual(result['medium'], 0)
        self.assertEqual(result['large'], 0)
        result = count_boxes(4)
        self.assertEqual(result['small'], 0)
        self.assertEqual(result['medium'], 1)
        self.assertEqual(result['large'], 0)
        result = count_boxes(6)
        self.assertEqual(result['small'], 0)
        self.assertEqual(result['medium'], 1)
        self.assertEqual(result['large'], 0)
        result = count_boxes(7)
        self.assertEqual(result['small'], 0)
        self.assertEqual(result['medium'], 0)
        self.assertEqual(result['large'], 1)
        result = count_boxes(9)
        self.assertEqual(result['small'], 0)
        self.assertEqual(result['medium'], 0)
        self.assertEqual(result['large'], 1)
        result = count_boxes(10)
        self.assertEqual(result['small'], 1)
        self.assertEqual(result['medium'], 0)
        self.assertEqual(result['large'], 1)
        result = count_boxes(12)
        self.assertEqual(result['small'], 1)
        self.assertEqual(result['medium'], 0)
        self.assertEqual(result['large'], 1)
        result = count_boxes(13)
        self.assertEqual(result['small'], 0)
        self.assertEqual(result['medium'], 0)
        self.assertEqual(result['large'], 2)
        result = count_boxes(15)
        self.assertEqual(result['small'], 0)
        self.assertEqual(result['medium'], 0)
        self.assertEqual(result['large'], 2)
        result = count_boxes(16)
        self.assertEqual(result['small'], 0)
        self.assertEqual(result['medium'], 0)
        self.assertEqual(result['large'], 2)
        result = count_boxes(19)
        self.assertEqual(result['small'], 1)
        self.assertEqual(result['medium'], 0)
        self.assertEqual(result['large'], 2)
        result = count_boxes(22)
        self.assertEqual(result['small'], 0)
        self.assertEqual(result['medium'], 1)
        self.assertEqual(result['large'], 2)
        result = count_boxes(25)
        self.assertEqual(result['small'], 0)
        self.assertEqual(result['medium'], 0)
        self.assertEqual(result['large'], 3)
        result = count_boxes(25)
        self.assertEqual(result['small'], 0)
        self.assertEqual(result['medium'], 0)
        self.assertEqual(result['large'], 3)
        result = count_boxes(31)
        self.assertEqual(result['small'], 0)
        self.assertEqual(result['medium'], 1)
        self.assertEqual(result['large'], 3)
        result = count_boxes(34)
        self.assertEqual(result['small'], 0)
        self.assertEqual(result['medium'], 0)
        self.assertEqual(result['large'], 4)

    def test_containers(self):
        result = count_boxes(1)
        self.assertEqual(result['container'], 0)
        result = count_boxes(10)
        self.assertEqual(result['container'], 1)
        result = count_boxes(28)
        self.assertEqual(result['container'], 2)

    def test_input_int(self):
        with self.assertRaises(Warning):
            count_boxes(2.5)

    def test_input_range(self):
        with self.assertRaises(Warning):
            count_boxes(0)
        with self.assertRaises(Warning):
            count_boxes(-1)
        with self.assertRaises(Warning):
            count_boxes(101)




if __name__ == '__main__':
    unittest.main()