import unittest
from unittest.mock import patch
import json
from what_is_year_now import what_is_year_now


class TestWhatIsYearNow(unittest.TestCase):
    def test_year_in_ymd_format(self):
        with patch("urllib.request.urlopen") as mock_urlopen:
            r_val = mock_urlopen.return_value.__enter__.return_value
            r_val.read.return_value = json.dumps(
                {"currentDateTime": "2019-03-01"}
            ).encode("utf-8")
            year = what_is_year_now()
            self.assertEqual(year, 2019)

    def test_year_in_dmy_format(self):
        with patch("urllib.request.urlopen") as mock_urlopen:
            r_val = mock_urlopen.return_value.__enter__.return_value
            r_val.read.return_value = json.dumps(
                {"currentDateTime": "01.03.2019"}
            ).encode("utf-8")
            year = what_is_year_now()
            self.assertEqual(year, 2019)

    def test_invalid_format(self):
        with patch("urllib.request.urlopen") as mock_urlopen:
            r_val = mock_urlopen.return_value.__enter__.return_value
            r_val.read.return_value = json.dumps(
                {"currentDateTime": "01-03-2019"}
            ).encode("utf-8")
            with self.assertRaises(ValueError):
                what_is_year_now()
