# Python version: 3.6
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import random

from scipy.stats import ttest_ind, shapiro


class Engagement_analysis:
    """
    With this class, the analysis of engagement rate is conducted.
    """
    def __init__(self, len_df, min_votes=None, min_impressions=None
                 , max_votes=None, max_impressions=None):
        """
        Initialization of the call attributes.
        :param len_df: int
        Length of dummy data.
        :param min_votes: int
        Minimum number of votes.
        If None, a default value is given to the attribute.
        :param min_impressions: int
        Minimum number of impressions.
        If None, a default value is given to the attribute.
        :param max_votes: int
        Maximum number of votes.
        If None, a default value is given to the attribute.
        :param max_impressions: int
        Maximum number of impressions.
        If None, a default value is given to the attribute.
        """
        self.len_df = len_df
        self.min_votes = 22 if not min_votes else min_votes
        self.min_impressions = 239 if not min_impressions else min_impressions
        self.max_votes = 223 if not max_votes else max_votes
        self.max_impressions = 2394 if not max_impressions else max_impressions

    def create_dummy_dataframe(self):
        """
        It creates a dummy pandas Dataframe where the columns are:
        - host_customer_id : publisher id
        - poll_customer_id : advertiser id
        - poll_id: poll id
        - visitor_country_code: ISO3 country code
        - impressions_control : number of impressions for the control group
        - cnt_votes_control : number of votes for the control group
        - impressions_control : number of impressions for the test group
        - cnt_votes_control : number of votes for the test group
        """
        one_quarter = int(self.len_df/4)
        one_half = int(self.len_df/2)
        self.df = pd.DataFrame()
        self.df['host_customer_id'] = ['Publisher 1'] * one_quarter + ['Publisher 2'] * one_quarter\
                                      + ['Publisher 3'] * one_quarter + ['Publisher 4'] * one_quarter
        self.df['poll_customer_id'] = ['Advertiser 1'] * one_half + ['Advertiser 2'] * one_half
        self.df['poll_id'] = ["Poll" + self.df['host_customer_id'].iloc[i][-1]+ "_advertiser"
                              + self.df['poll_customer_id'].iloc[i][-1] for i in range(0, self.len_df)]
        self.df['vistor_country_code'] = ['DE'] * one_quarter + ['AT'] * one_quarter +\
                                         ['IT'] * one_quarter + ['FR'] * one_quarter
        self.df['impressions_control'] = [random.randint(self.min_impressions, self.max_impressions) for i in range(0, self.len_df)]
        self.df['cnt_votes_control'] = [random.randint(self.min_votes, self.max_votes) for x in range(0, self.len_df)]
        self.df['impressions_test'] = [random.randint(self.min_impressions, self.max_impressions) for i in range(0, self.len_df)]
        self.df['cnt_votes_test'] = [random.randint(self.min_votes, self.max_votes) for z in range(0, self.len_df)]

    def engagement_rate(self):
        """
        It creates a new column where the engagement rate (votes/impressions)
        is calculated for the control and test data sample.
        """
        self.df['ER_control'] = self.df['cnt_votes_control'] / self.df['impressions_control']
        self.df['ER_test'] = self.df['cnt_votes_test'] / self.df['impressions_test']

    def compare_er_control_test(self):
        """
        It creates a binary column called 'higher_er_test"
        where 1 is given when the engagement of test group is higher than the control group.
        Otherwise 0.
        """
        self.df["higher_er_test"] = 0
        self.df.loc[(self.df['ER_test'] > self.df['ER_control']), 'higher_er_test'] = 1

    def plot_engagement_distr(self):
        """
        It plots the engagement rate distributions of the control and test group.
        """
        for col in ['ER_control', 'ER_test']:
            ax = sn.distplot(self.df[col])
        ax.set(xlabel='engagement rate', ylabel='freq')
        plt.show()

    def normality_test(self, data):
        """
        Shapiro-Wilk to test for distribution normality.
        :param data: pandas Series
        """
        stat, p = shapiro(data)
        if p > 0.05:
            print("The distribution looks Gaussian.")
        else:
            print("The distribution does not look Gaussian.")

    def independent_ttest(self):
        """
        It executes the independent t-test on the distribution of control and test
        engagement rate distributions.
        """
        self.res_t_test = ttest_ind(self.df['ER_test'], self.df['ER_control'])
        if self.res_t_test[1] < 0.05:
            print("The control and test distributions for the engagement rate are significantly different.")
        else:
            print("The control and test distributions for the engagement rate are not significantly different.")
