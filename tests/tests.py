#!/usr/bin/env python
# tests.py -- for vesting

import sys
import datetime
from unittest import TestCase
from unittest.mock import patch
import vesting

class TestVesting(TestCase):
    def test_get_parameters(self):
        filename = r'C:\Users\Me\Desktop\test.csv'
        target_date = datetime.datetime(2010, 1, 1)
        testargs = ["program", filename, '2010-01-01']
        with patch.object(sys, 'argv', testargs):
            expected_filename, expected_target_date = vesting.get_parameters()

        self.assertEqual(expected_filename, filename)
        self.assertEqual(expected_target_date, target_date)

if __name__ == '__main__':
    from unittest import main
    main()

