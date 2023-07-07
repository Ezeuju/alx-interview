import unittest
canUnlockAll = __import__('0-lockboxes').canUnlockAll


class TestUnlockBoxes(unittest.TestCase):
    def test_positive_case(self):
        boxes = [[1], [2], [3], []]
        self.assertTrue(canUnlockAll(boxes))

    def test_negative_case(self):
        boxes = [[1], [2], [7], [0]]
        self.assertFalse(canUnlockAll(boxes))

    def test_empty_boxes(self):
        boxes = []
        self.assertTrue(canUnlockAll(boxes))

    def test_single_box(self):
        boxes = [[]]
        self.assertTrue(canUnlockAll(boxes))

    def test_large_boxes(self):
        boxes = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
        self.assertTrue(canUnlockAll(boxes))

    def test_circular_dependency(self):
        boxes = [[1], [2], [0]]
        self.assertTrue(canUnlockAll(boxes))

    def test_unreachable_boxes(self):
        boxes = [[1], [2], [], [0]]
        self.assertFalse(canUnlockAll(boxes))

    def test_duplicate_keys(self):
        boxes = [[1, 2], [2, 3], [3], []]
        self.assertTrue(canUnlockAll(boxes))

    def test_empty_box(self):
        boxes = [[1], [], [3], []]
        self.assertFalse(canUnlockAll(boxes))

    def test_not_all_boxes_unlocked(self):
        boxes = [[1, 2], [3, 4], [5], []]
        self.assertTrue(canUnlockAll(boxes))

    def test_custom_boxes(self):
        boxes = [[8, 1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
        self.assertTrue(canUnlockAll(boxes))


if __name__ == '__main__':
    unittest.main()
