#!/usr/bin/env python
# tests.py -- for vesting

from unittest import TestCase
from unittest.mock import patch
import pandas as pd
from pandas.testing import assert_frame_equal
import vesting

class FakeResult:
    text = 'smt'

class TestVesting(TestCase):

    def setUp(self):
        """ Your setUp """
        INPUT_DIR = 'tests/'
        test_file_name =  'vesting_events.csv'
        try:
            data = pd.read_csv(INPUT_DIR + test_file_name,
                header = None)
        except IOError:
            print ('Can not open file')
        self.fixture = data

    def test_df_constructed(self):
        df = pd.DataFrame()
        assert_frame_equal(self.fixture, df)

    # @patch('pd.read_csv')
    # def test_helloworld(self, mock_get):
    #     mock_get.return_value = FakeResult()

    #     vesting.get_parameters()
    #     mock_get.assert_called_with(URL)

if __name__ == '__main__':
    from unittest import main
    main()

