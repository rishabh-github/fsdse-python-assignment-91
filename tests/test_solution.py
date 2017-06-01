from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        res = solution({'X': [78, 85, 96, 80, 86], 'Y': [84, 94, 89, 83, 86], 'Z': [86, 97, 96, 72, 83]})
        import pandas as pd
        self.assertTrue(isinstance(res, pd.DataFrame))
