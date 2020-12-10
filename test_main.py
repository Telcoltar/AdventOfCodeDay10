from unittest import TestCase

from main import solution_part_1, solution_part_2


class Test(TestCase):
    def test_solution_part_1(self):
        self.assertEqual(solution_part_1("testData.txt"), 35)
        self.assertEqual(solution_part_1("testData2.txt"), 220)

    def test_solution_part_2(self):
        self.assertEqual(solution_part_2("testData.txt"), 8)
        self.assertEqual(solution_part_2("testData2.txt"), 19208)
