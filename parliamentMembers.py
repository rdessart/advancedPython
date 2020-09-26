""" All data related to deputies """

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


class MissingDataError(Exception):
    """
    Error to be raised when a data is missing
    """
    def __init__(self, data_name, calling_function_name):
        output_string = "{} was not set before calling {}"
        output_string.format(data_name, calling_function_name)
        super().__init__(output_string)


class SetOfParliamentMembers():
    """
    Order PM per political parties
    """
    def __init__(self, name):
        """default constructor"""
        self.name = name
        self.dataframe = None

    def data_from_csv(self, filepath):
        """ load the dataframe using pandas lib """
        self.dataframe = pd.load_csv(filepath, separator='')

    def data_from_dataframe(self, dataframe):
        """ copy the dataframe """
        self.dataframe = dataframe

    def display_chart(self):
        data = self.dataframe
        female_mps = data[data.sexe == "F"]
        male_mps = data[data.sexe == "H"]

        counts = [len(female_mps), len(male_mps)]
        counts = np.array(counts)
        nb_mps = counts.sum()
        proportions = counts / nb_mps

        labels = [
                 "Female ({})".format(counts[0]),
                 "Male ({})".format(counts[1])]

        fig, ax = plt.subplots()
        ax.axis("equal")
        ax.pie(
                proportions,
                labels=labels,
                autopct="%1.1f pourcents"
                )
        plt.title("{} ({} MPs)".format(self.name, nb_mps))
        plt.show()

    def split_by_politcal_parties(self):
        """
        Split the PM per policals parties.
        Unset data are ignored
        @return dictionnary : key = politacal parties | value = list of PMs
        """
        if self.dataframe is None:
            raise MissingDataError("dataframe",
                                   "SetOfParliamentMember."
                                   "split_by_politcal_parties")
            return
        data = self.dataframe
        result = {}
        parties = data["parti_ratt_financier"].dropna().unique()
        for party in parties:
            data_subset = data[data.parti_ratt_financier == party]
            subset = SetOfParliamentMembers(
                                           'MPs from party "{}"'.format(party))
            subset.data_from_dataframe(data_subset)
            result[party] = subset

        return result
