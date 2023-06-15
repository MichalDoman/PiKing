import json
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

class ScoresScreen(Screen):
    # Create a statistics file to save:
    statistics = {
        'most_decimals': {'decimals': 0,
                          'mistakes': 0,
                          'efficacy': 0,
                          'points': 0,
                          'longest_combo': 0,
                          'extra_combo_points': 0,
                          'longest_combo_click_time': '',
                          'combo_time': '',
                          'overall_click_time': '',
                          'overall_time': '',
                          'digits_per_minute': 0,
                          'current_date': ''},
        'highest_score': {'decimals': 0,
                          'mistakes': 0,
                          'efficacy': 0,
                          'points': 0,
                          'longest_combo': 0,
                          'extra_combo_points': 0,
                          'longest_combo_click_time': '',
                          'combo_time': '',
                          'overall_click_time': '',
                          'overall_time': '',
                          'digits_per_minute': 0,
                          'current_date': ''},
        'no_mistakes': {'decimals': 0,
                        'mistakes': 0,
                        'points': 0,
                        'longest_combo': 0,
                        'extra_combo_points': 0,
                        'longest_combo_click_time': '',
                        'combo_time': '',
                        'overall_click_time': '',
                        'overall_time': '',
                        'digits_per_minute': 0,
                        'current_date': ''},
        'longest_combo': {'longest_combo': 0,
                          'extra_combo_points': 0,
                          'longest_combo_click_time': '',
                          'combo_time': '',
                          'digits_per_minute': 0,
                          'current_date': ''}
    }
    try:
        with open('../json/statistics.json') as stats_file:
            statistics = json.load(stats_file)
    except FileNotFoundError:
        print('File created')

    # Labels:
    decimals_label = StringProperty('Decimals: ' + str(statistics['most_decimals']['decimals']))
    mistakes_label = StringProperty('Mistakes: ' + str(statistics['most_decimals']['mistakes']))
    efficacy_label = StringProperty('Efficacy: ' + str(statistics['most_decimals']['efficacy']) + '%')
    points_label = StringProperty('Points: ' + str(statistics['most_decimals']['points']))

    longest_combo_label = StringProperty('The Longest Combo: ' + str(statistics['most_decimals']['longest_combo']))
    extra_points_label = StringProperty('Extra Points: ' + str(statistics['most_decimals']['extra_combo_points']))
    combo_click_time_label = StringProperty('Time per Combo Digit: ' + str(statistics['most_decimals']['longest_combo_click_time']))
    combo_time_label = StringProperty('Combo Time: ' + str(statistics['most_decimals']['combo_time']))

    overall_click_time_label = StringProperty(
        'Time per Digit: ' + str(statistics['most_decimals']['overall_click_time']))
    overall_time_label = StringProperty('Play Time: ' + str(statistics['most_decimals']['overall_time']))
    digits_per_minute_label = StringProperty('Digits per Minute: ' + str(statistics['most_decimals']['digits_per_minute']))
    date_label = StringProperty('Date: ' + statistics['most_decimals']['current_date'])

    def update_scores(self):
        self.decimals_label = 'Decimals: ' + str(self.statistics['most_decimals']['decimals'])
        self.mistakes_label = 'Mistakes: ' + str(self.statistics['most_decimals']['mistakes'])
        self.efficacy_label = 'Efficacy: ' + str(self.statistics['most_decimals']['efficacy']) + '%'
        self.points_label = 'Points: ' + str(self.statistics['most_decimals']['points'])

        self.longest_combo_label = 'The Longest Combo: ' + str(self.statistics['most_decimals']['longest_combo'])
        self.extra_points_label = 'Extra Points: ' + str(self.statistics['most_decimals']['extra_combo_points'])
        self.combo_click_time_label = 'Time per Combo Digit: ' + str(self.statistics['most_decimals']['longest_combo_click_time'])
        self.combo_time_label = 'Combo Time: ' + str(self.statistics['most_decimals']['combo_time'])

        self.overall_click_time_label = 'Time per Digit: ' + str(self.statistics['most_decimals']['overall_click_time'])
        self.overall_time_label = 'Play Time: ' + str(self.statistics['most_decimals']['overall_time'])
        self.digits_per_minute_label = 'Digits per Minute: ' + str(self.statistics['most_decimals']['digits_per_minute'])
        self.date_label = 'Date: ' + self.statistics['most_decimals']['current_date']


class ScoresScreen2(Screen):
    # Labels:
    decimals_label = StringProperty('Decimals: ' + str(ScoresScreen.statistics['highest_score']['decimals']))
    mistakes_label = StringProperty('Mistakes: ' + str(ScoresScreen.statistics['highest_score']['mistakes']))
    efficacy_label = StringProperty('Efficacy: ' + str(ScoresScreen.statistics['highest_score']['efficacy']) + '%')
    points_label = StringProperty('Points: ' + str(ScoresScreen.statistics['highest_score']['points']))

    longest_combo_label = StringProperty(
        'The Longest Combo: ' + str(ScoresScreen.statistics['highest_score']['longest_combo']))
    extra_points_label = StringProperty(
        'Extra Points: ' + str(ScoresScreen.statistics['highest_score']['extra_combo_points']))
    combo_click_time_label = StringProperty(
        'Time per Combo Digit: ' + str(ScoresScreen.statistics['highest_score']['longest_combo_click_time']))
    combo_time_label = StringProperty('Combo Time: ' + str(ScoresScreen.statistics['highest_score']['combo_time']))

    overall_click_time_label = StringProperty(
        'Time per Digit: ' + str(ScoresScreen.statistics['highest_score']['overall_click_time']))
    overall_time_label = StringProperty('Play Time: ' + str(ScoresScreen.statistics['highest_score']['overall_time']))
    digits_per_minute_label = StringProperty('Digits per Minute: ' + str(ScoresScreen.statistics['highest_score']['digits_per_minute']))
    date_label = StringProperty('Date: ' + ScoresScreen.statistics['highest_score']['current_date'])

    def update_scores(self):
        self.decimals_label = 'Decimals: ' + str(ScoresScreen.statistics['highest_score']['decimals'])
        self.mistakes_label = 'Mistakes: ' + str(ScoresScreen.statistics['highest_score']['mistakes'])
        self.efficacy_label = 'Efficacy: ' + str(ScoresScreen.statistics['highest_score']['efficacy']) + '%'
        self.points_label = 'Points: ' + str(ScoresScreen.statistics['highest_score']['points'])

        self.longest_combo_label = 'The Longest Combo: ' + str(ScoresScreen.statistics['highest_score']['longest_combo'])
        self.extra_points_label = 'Extra Points: ' + str(ScoresScreen.statistics['highest_score']['extra_combo_points'])
        self.combo_click_time_label = 'Time per Combo Digit: ' + str(
            ScoresScreen.statistics['highest_score']['longest_combo_click_time'])
        self.combo_time_label = 'Combo Time: ' + str(ScoresScreen.statistics['highest_score']['combo_time'])

        self.overall_click_time_label = 'Time per Digit: ' + str(ScoresScreen.statistics['highest_score']['overall_click_time'])
        self.overall_time_label = 'Play Time: ' + str(ScoresScreen.statistics['highest_score']['overall_time'])
        self.digits_per_minute_label = 'Digits per Minute: ' + str(ScoresScreen.statistics['highest_score']['digits_per_minute'])
        self.date_label = 'Date: ' + ScoresScreen.statistics['highest_score']['current_date']


class ScoresScreen3(Screen):
    # Labels:
    decimals_label = StringProperty('Decimals: ' + str(ScoresScreen.statistics['no_mistakes']['decimals']))
    mistakes_label = StringProperty('Mistakes: ' + str(ScoresScreen.statistics['no_mistakes']['mistakes']))
    points_label = StringProperty('Points: ' + str(ScoresScreen.statistics['no_mistakes']['points']))

    longest_combo_label = StringProperty(
        'The Longest Combo: ' + str(ScoresScreen.statistics['no_mistakes']['longest_combo']))
    extra_points_label = StringProperty(
        'Extra Points: ' + str(ScoresScreen.statistics['no_mistakes']['extra_combo_points']))
    combo_click_time_label = StringProperty(
        'Time per Combo Digit: ' + str(ScoresScreen.statistics['no_mistakes']['longest_combo_click_time']))
    combo_time_label = StringProperty('Combo Time: ' + str(ScoresScreen.statistics['no_mistakes']['combo_time']))

    overall_click_time_label = StringProperty(
        'Time per Digit: ' + str(ScoresScreen.statistics['no_mistakes']['overall_click_time']))
    overall_time_label = StringProperty('Play Time: ' + str(ScoresScreen.statistics['no_mistakes']['overall_time']))
    digits_per_minute_label = StringProperty('Digits per Minute: ' + str(ScoresScreen.statistics['no_mistakes']['digits_per_minute']))
    date_label = StringProperty('Date: ' + ScoresScreen.statistics['no_mistakes']['current_date'])

    def update_scores(self):
        self.decimals_label = 'Decimals: ' + str(ScoresScreen.statistics['no_mistakes']['decimals'])
        self.mistakes_label = 'Mistakes: ' + str(ScoresScreen.statistics['no_mistakes']['mistakes'])
        self.points_label = 'Points: ' + str(ScoresScreen.statistics['no_mistakes']['points'])

        self.longest_combo_label = 'The Longest Combo: ' + str(ScoresScreen.statistics['no_mistakes']['longest_combo'])
        self.extra_points_label = 'Extra Points: ' + str(
            ScoresScreen.statistics['no_mistakes']['extra_combo_points'])
        self.combo_click_time_label = 'Time per combo digit: ' + str(
            ScoresScreen.statistics['no_mistakes']['longest_combo_click_time'])
        self.combo_time_label = 'Combo time: ' + str(ScoresScreen.statistics['no_mistakes']['combo_time'])

        self.overall_click_time_label = 'Time per digit: ' + str(ScoresScreen.statistics['no_mistakes']['overall_click_time'])
        self.overall_time_label = 'Play Time: ' + str(ScoresScreen.statistics['no_mistakes']['overall_time'])
        self.digits_per_minute_label = 'Digits per Minute: ' + str(ScoresScreen.statistics['no_mistakes']['digits_per_minute'])
        self.date_label = 'Date: ' + ScoresScreen.statistics['no_mistakes']['current_date']


class ScoresScreen4(Screen):
    # Labels:
    longest_combo_label = StringProperty(
        'The Longest Combo: ' + str(ScoresScreen.statistics['longest_combo']['longest_combo']))
    extra_points_label = StringProperty(
        'Extra Points: ' + str(ScoresScreen.statistics['longest_combo']['extra_combo_points']))
    combo_click_time_label = StringProperty(
        'Time per Combo Digit: ' + str(ScoresScreen.statistics['longest_combo']['longest_combo_click_time']))
    combo_time_label = StringProperty('Combo Time: ' + str(ScoresScreen.statistics['longest_combo']['combo_time']))
    digits_per_minute_label = StringProperty('Digits per Minute: ' + str(ScoresScreen.statistics['longest_combo']['digits_per_minute']))


    date_label = StringProperty('Date: ' + ScoresScreen.statistics['longest_combo']['current_date'])

    def update_scores(self):
        self.longest_combo_label = 'The Longest Combo: ' + str(ScoresScreen.statistics['longest_combo']['longest_combo'])
        self.extra_points_label = 'Extra Points: ' + str(
            ScoresScreen.statistics['longest_combo']['extra_combo_points'])
        self.combo_click_time_label = 'Time per Combo Digit: ' + str(
            ScoresScreen.statistics['longest_combo']['longest_combo_click_time'])
        self.combo_time_label = 'Combo Time: ' + str(ScoresScreen.statistics['longest_combo']['combo_time'])
        self.digits_per_minute_label = 'Digits per Minute: ' + str(ScoresScreen.statistics['longest_combo']['digits_per_minute'])

        self.date_label = 'Date: ' + ScoresScreen.statistics['longest_combo']['current_date']
