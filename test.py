import pandas as pd
import unittest

column_names = ['Release Year', 'Amount']
years = [2018, 2019, 2020, 1925, 2021]


class PandasTests(unittest.TestCase):
    def setUp(self):
        """This function will set up the initial DataFrame for further tests"""
        data_frame = pd.read_csv('netflix_titles.csv', delimiter=',',
                                 usecols=['release_year']).value_counts() \
            .to_frame().sort_values(by='release_year') \
            .reset_index().rename(
            columns={'release_year': 'Release Year',
                     0: 'Amount'})
        self.fixture = data_frame

    def test_create_data_frame_columns(self):
        """This function checks if the expected column names matches the actual
         column names received from the CSV file in setUp func to be sure that
         DataFrame contain only required columns"""
        self.assertListEqual(list(self.fixture.columns), column_names)

    def test_create_data_frame_years(self):
        """This function will check if the list of expected released years is
        part of the column with released years received from CSV file"""
        df_years = self.fixture["Release Year"]
        self.assertTrue(all(True for i in years if i in df_years))


if __name__ == "__main__":
    unittest.main()
