import pandas as pd
import numpy as np

from path import Path


def convert_comma_float_to_float(points):
    if isinstance(points, str):
        return points.replace(',', '.')
    return points


class OffersAssigner:
    def __init__(self):
        self.candidates_file = Path('candidates.ods')
        self.results_file = Path('results.ods')
        self.candidates = pd.read_excel(self.candidates_file)
        self.format_data()

    def format_data(self):
        self.candidates = self.candidates.replace(np.nan, '', regex=True)
        self.candidates['points'] = self.candidates['points'].map(convert_comma_float_to_float)
        if self.convert_points_to_float():
            self.candidates = self.candidates.drop(self.candidates[self.candidates['points'] > 85].index)
            self.candidates = self.candidates.sort_values(by=['points'], ascending=False)
            self.candidates['assigned offer'] = ""

    def write_to_file(self):
        self.candidates.to_excel(self.results_file, index=False)

    def assign_offers(self):

        for row, candidate in self.candidates.iterrows():

            available_offers = np.setdiff1d(candidate[1:4].to_list(), self.candidates['assigned offer'].tolist())

            if available_offers.size:
                self.candidates.at[row, 'assigned offer'] = available_offers[0]

    def convert_points_to_float(self):
        for row, points in enumerate(self.candidates['points']):
            try:
                self.candidates.at[row, 'points'] = float(points)
            except ValueError:
                print(f'ERROR at row {row} with points of candidates : { points}')
                return False
        return True
