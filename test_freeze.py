from freeze import *
from freezegun import freeze_time
import datetime
import unittest
@freeze_time("2021-06-21")
class MyTests(unittest.TestCase):
    def test_the_class(self):
        mock_date=datetime.datetime(1955, 11, 12)
        test_t_date=cur_date()
        assert test_t_date==mock_date
