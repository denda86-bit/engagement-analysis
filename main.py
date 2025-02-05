from engagement_analysis_class import Engagement_analysis

if __name__ == "__main__":

    # EXERCISE 4
    # Task 4.1
    er_obj = Engagement_analysis(len_df=100)

    # creation of a dummy Dataframe with 100 data points
    er_obj.create_dummy_dataframe()

    # calculation of engagement rate for test and control groups
    er_obj.engagement_rate()

    # Descriptive statistics have been executed to infer the engagement rate's distributions:
    # 1. the mean, median, 75th, 50th, 25th percentiles and max and min values
    # for each distribution have been calculated;
    print('Engagement rate distribution for control group:')
    print(er_obj.df.ER_control.describe())
    print('\nEngagement rate distribution for test group:')
    print(er_obj.df.ER_test.describe())

    # 2. the Shapiro-Wilk test has been executed to check whether
    # the two engagement rate's distributions are normally distributed.
    print('Shapiro-Wilk test for control group:')
    er_obj.normality_test(data=er_obj.df.ER_control)
    print('\nShapiro-Wilk test for test group:')
    er_obj.normality_test(data=er_obj.df.ER_test)

    # plot the engagement rate's distributions
    er_obj.plot_engagement_distr()

    # Task 4.2
    # I have to admit that I haven't understood fully the question,
    # although I asked for an additional description per email.

    # Based on my understanding of the question, two types of analysis have been executed.
    # The first type of analysis is conducted to verify whether the engagement rate
    # for a specific country, publisher and advertiser of the test group is higher than the control group.
    er_obj.compare_er_control_test()
    print(er_obj.df["higher_er_test"])

    # The second analysis is conducted to check whether the distributions of the engagement rate
    # of the control and test group are significantly different (t-test),
    # irrespectively of the country, publisher and advertiser.
    er_obj.independent_ttest()

