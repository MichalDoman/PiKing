import json
import kivy

kivy.require('2.1.0')
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.factory import Factory
from datetime import date, datetime
from utils.scores import ScoresScreen, ScoresScreen2, ScoresScreen3, ScoresScreen4
from utils.guides import GuidesScreen, AboutTheAppPageLayout
from settings import *
from utils.pi import pi_decimals

Builder.load_file('kv/PiKing.kv')
Builder.load_file('kv/main_widget.kv')
Builder.load_file('kv/settings.kv')
Builder.load_file('kv/scores_screen.kv')
Builder.load_file('kv/guides.kv')
Window.size = (550, 750)


class MainMenu(Screen):
    pass


class MainWidget(Screen):
    # Save date for records:
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M")

    # Variables to save in SettingsScreen.data:
    keypad_size = NumericProperty(0.4)
    digits_between_spacing = 2
    digits_to_highlight = 10  # Highlights every nth digit by default
    # Layout adjustment variables:
    digit_label_width = NumericProperty(0.08)

    # Combo variables:
    combo_length = 0
    extra_points = 0
    combo_seconds = 0  # Time between clicks in a combo
    combo_overall_seconds = 0  # Overall time of a combo
    combo_time = ''
    combo_timer_on = False  # Necessary to multiply combo points, and change label appearance

    # Overall timer variables:
    timer_on = False  # Used to start overall timer after the first click
    overall_seconds = 0

    # Stats variables to save in ScoresScreen.statistics:
    click_counter = 0  # Number of decimals
    mistakes = 0
    efficacy = 0
    points = 0
    longest_combo = 0
    highest_extra_points = 0
    longest_combo_click_time = ''
    longest_combo_time = ''
    overall_time = ''
    overall_click_time = ''
    digits_per_minute = 0

    # In game labels:
    decimals_label = StringProperty("Decimals:" + "\n" + str(click_counter))
    mistakes_label = StringProperty("Mistakes:" + "\n" + str(mistakes))
    efficacy_label = StringProperty("Efficacy:" + "\n" + str(efficacy) + "%")
    points_label = StringProperty("Points: " + str(points))
    extra_points_label = StringProperty("+ " + str(extra_points))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Show the first integer:
        self.initial_integer = Label(text='3. ',
                                     font_size=dp(120),
                                     color=PiKingApp.text_color,
                                     font_name="fonts/font_1.ttf",
                                     size_hint=(1, None))
        self.initial_integer.bind(texture_size=self.initial_integer.setter('size'))
        self.ids.mw_stack_layout.add_widget(self.initial_integer)

    def on_keypad_button_press(self, text):
        # Start overall timer:
        if not self.timer_on:
            Clock.schedule_interval(self.update_overall_timer, 0)
            self.timer_on = True
        # Measure time when combo starts:
        self.combo_timer_start()
        self.click_counter += 1

        # Check if the digit is correct:
        if not self.check_correctness(text):
            digit_color = 1, 0, 0, 1
            self.combo_timer_stop()
        else:
            digit_color = PiKingApp.text_color
            # Apply additional points for combos only if the digit is correct:
            if self.combo_timer_on and self.combo_length >= 2:
                self.points += self.combo_length
                self.extra_points += (self.combo_length - 1)
                digit_color = blue
            else:
                self.points += 1
            # Apply special digit colors:
            if self.click_counter % self.digits_to_highlight == 0:
                digit_color = yellow

        # Show new number of decimals and score:
        if self.combo_timer_on and self.combo_length >= 2:
            self.points_label = "Combo: " + str(self.combo_length)
            animation = Animation(font_size=dp(35), color=dark_blue, duration=0.1)
            animation.start(self.ids.mw_points_label)
        else:
            self.points_label = "Points: " + str(self.points)
        self.decimals_label = "Decimals:" + "\n" + str(self.click_counter)

        # Calculate efficacy:
        self.efficacy = int((1 - (self.mistakes / self.click_counter)) * 100)
        self.efficacy_label = "Efficacy:" + "\n" + str(self.efficacy) + "%"

        # Save the longest combo:
        if self.longest_combo < self.combo_length:
            self.longest_combo = self.combo_length

        # Save highest amount of extra points gained in combos:
        if self.highest_extra_points < self.extra_points:
            self.highest_extra_points = self.extra_points

        # Save stats:
        self.calculate_combo_time_stats()
        self.calculate_overall_click_time()
        self.save_stats()

        # Add a digit:
        digit = Factory.DigitLabel(text=text, color=digit_color, size_hint=(self.digit_label_width, None))
        self.ids.mw_stack_layout.add_widget(digit)

        # Animate decimals label:
        if self.click_counter % self.digits_to_highlight == 0:
            self.animate(self.ids.decimals_label)

        # Implement spacing every n digits:
        if self.click_counter % self.digits_between_spacing == 0:
            space = Factory.DigitLabel(size_hint=(self.digit_label_width, None))
            self.ids.mw_stack_layout.add_widget(space)

    def check_correctness(self, digit):
        if digit == pi_decimals[self.click_counter - 1]:
            return True
        else:
            self.mistakes += 1
            self.mistakes_label = "Mistakes:" + "\n" + str(self.mistakes)
            return False

    def show_correct_digit(self):
        pass

    def reset(self):
        # Sum up:
        self.end_overall_timer()
        # Clear all the digits:
        self.ids.mw_stack_layout.clear_widgets()
        # Reset variables:
        self.click_counter = 0
        self.mistakes = 0
        self.efficacy = 0
        self.points = 0
        self.longest_combo = 0
        self.extra_points = 0
        self.highest_extra_points = 0
        self.longest_combo_click_time = 0
        # Reset labels:
        self.ids.mw_stack_layout.add_widget(self.initial_integer)
        self.decimals_label = "Decimals:" + "\n" + str(self.click_counter)
        self.mistakes_label = "Mistakes:" + "\n" + str(self.mistakes)
        self.efficacy_label = "Efficacy:" + "\n" + str(self.efficacy) + "%"
        self.points_label = "Points: " + str(self.points)
        animation = Animation(pos_hint={"center_x": 1.1, "center_y": 0.92}, duration=0)
        animation.start(self.ids.extra_points_label)

    def save_stats(self):
        # Save stats for all four categories of statistics if new records are made:
        stats = ScoresScreen.statistics
        # Game with most decimals:
        if self.click_counter > stats['most_decimals']['decimals'] or (
                self.click_counter == stats['most_decimals']['decimals'] and self.points >
                stats['most_decimals']['points']):
            stats['most_decimals']['decimals'] = self.click_counter - self.mistakes
            stats['most_decimals']['mistakes'] = self.mistakes
            stats['most_decimals']['efficacy'] = self.efficacy
            stats['most_decimals']['points'] = self.points
            stats['most_decimals']['longest_combo'] = self.longest_combo
            stats['most_decimals']['extra_combo_points'] = self.highest_extra_points
            stats['most_decimals']['longest_combo_click_time'] = self.longest_combo_click_time
            stats['most_decimals']['combo_time'] = self.longest_combo_time
            stats['most_decimals']['overall_click_time'] = self.overall_click_time
            stats['most_decimals']['overall_time'] = self.overall_time
            if self.click_counter > 1:
                stats['most_decimals']['digits_per_minute'] = round(
                    60 / (self.overall_seconds / (self.click_counter - 1)), 1)

            stats['most_decimals']['current_date'] = f"{self.current_date}   {self.current_time}"
        # Game with most points:
        if self.points > stats['highest_score']['points'] or (
                self.points == stats['highest_score']['points'] and self.click_counter >
                stats['highest_score']['decimals']):
            stats['highest_score']['decimals'] = self.click_counter - self.mistakes
            stats['highest_score']['mistakes'] = self.mistakes
            stats['highest_score']['efficacy'] = self.efficacy
            stats['highest_score']['points'] = self.points
            stats['highest_score']['longest_combo'] = self.longest_combo
            stats['highest_score']['extra_combo_points'] = self.highest_extra_points
            stats['highest_score']['longest_combo_click_time'] = self.longest_combo_click_time
            stats['highest_score']['combo_time'] = self.longest_combo_time
            stats['highest_score']['overall_click_time'] = self.overall_click_time
            stats['highest_score']['overall_time'] = self.overall_time
            if self.click_counter > 1:
                stats['highest_score']['digits_per_minute'] = round(
                    60 / (self.overall_seconds / (self.click_counter - 1)), 1)

            stats['highest_score']['current_date'] = f"{self.current_date}   {self.current_time}"

        # Game with most decimals without making any mistakes:
        if self.mistakes == 0 and self.click_counter > stats['no_mistakes']['decimals'] or (
                self.mistakes == 0 and self.click_counter == stats['no_mistakes']['decimals'] and self.points > stats['no_mistakes']['points']):
            stats['no_mistakes']['decimals'] = self.click_counter
            stats['no_mistakes']['mistakes'] = self.mistakes
            stats['no_mistakes']['points'] = self.points
            stats['no_mistakes']['longest_combo'] = self.longest_combo
            stats['no_mistakes']['extra_combo_points'] = self.highest_extra_points
            stats['no_mistakes']['longest_combo_click_time'] = self.longest_combo_click_time
            stats['no_mistakes']['combo_time'] = self.longest_combo_time
            stats['no_mistakes']['overall_click_time'] = self.overall_click_time
            stats['no_mistakes']['overall_time'] = self.overall_time
            if self.click_counter > 1:
                stats['no_mistakes']['digits_per_minute'] = round(
                    60 / (self.overall_seconds / (self.click_counter - 1)), 1)

            stats['no_mistakes']['current_date'] = f"{self.current_date}   {self.current_time}"
        # Game with the longest combo:
        if self.combo_length > stats['longest_combo']['longest_combo'] or (
                self.combo_length == stats['longest_combo']['longest_combo'] and (
                self.longest_combo_time) < stats['longest_combo']['combo_time']):
            stats['longest_combo']['longest_combo'] = self.longest_combo
            stats['longest_combo']['extra_combo_points'] = self.highest_extra_points
            stats['longest_combo']['longest_combo_click_time'] = self.longest_combo_click_time
            stats['longest_combo']['combo_time'] = self.longest_combo_time
            if self.combo_length > 1:
                stats['longest_combo']['digits_per_minute'] = round(
                    60 / (self.combo_overall_seconds / (self.combo_length - 1)), 1)

            stats['longest_combo']['current_date'] = f"{self.current_date}   {self.current_time}"

        with open('json/statistics.json', 'w') as stats_file:
            json.dump(stats, stats_file)

    @staticmethod
    def animate(widget):
        animation = Animation(font_size=dp(40), color=yellow, duration=0.4)
        animation += Animation(font_size=dp(17), color=PiKingApp.text_color, duration=0.4)
        animation.start(widget)

    def update_combo_timer(self, tick):
        self.combo_seconds += tick
        if self.combo_seconds >= 1:  # Set time between clicks to keep the combo
            self.combo_timer_stop()

    def combo_timer_start(self):
        self.combo_length += 1
        # Reset previous combo timer and apply new one:
        Clock.unschedule(self.update_combo_timer)
        self.combo_overall_seconds += self.combo_seconds
        self.combo_seconds = 0
        Clock.schedule_interval(self.update_combo_timer, 0)
        self.combo_timer_on = True
        if self.combo_length >= 2:
            animation = Animation(pos_hint={"center_x": 1.1, "center_y": 0.92}, duration=0.1)
            animation.start(self.ids.extra_points_label)

    def combo_timer_stop(self):
        # Show and reset extra points:
        self.extra_points_label = "+" + str(self.extra_points)
        if self.combo_length >= 2:
            animation = Animation(pos_hint={"center_x": 0.87, "center_y": 0.92}, duration=0.4)
            animation.start(self.ids.extra_points_label)
            self.extra_points = 0
        # Reset variables:
        Clock.unschedule(self.update_combo_timer)
        self.combo_timer_on = False
        self.combo_seconds = 0
        self.combo_overall_seconds = 0
        self.combo_length = 0
        # End combo animation:
        self.points_label = "Points: " + str(self.points)
        animation = Animation(font_size=dp(27), color=black, duration=0.1)
        animation.start(self.ids.mw_points_label)
        print('The combo has ended')

    def calculate_combo_time_stats(self):
        # Save the click time for the longest combo in a game (combo is 2 digits or more):
        if self.combo_length > 1:
            seconds_per_click = self.combo_overall_seconds / (self.combo_length - 1)
            part_seconds = seconds_per_click * 1000 % 1000
            if self.combo_length >= self.longest_combo:
                self.longest_combo_click_time = f'{int(seconds_per_click):02}.{int(part_seconds):03}'
            # Calculate combo time:
            minutes, seconds = divmod(self.combo_overall_seconds, 60)
            part_seconds = seconds * 1000 % 1000
            self.combo_time = f'{int(minutes):02}:{int(seconds):02}.{int(part_seconds):03}'
            if self.combo_length == self.longest_combo:  # Has to equal since the longest combo updates beforehand
                self.longest_combo_time = self.combo_time

    def update_overall_timer(self, tick):
        self.overall_seconds += tick
        minutes, seconds = divmod(self.overall_seconds, 60)
        hours, minutes = divmod(minutes, 60)
        part_seconds = seconds * 1000 % 1000
        self.overall_time = f'{int(hours):02}:{int(minutes):02}:{int(seconds):02}.{int(part_seconds):03}'

    def end_overall_timer(self):
        # Used while resetting the whole widget:
        Clock.unschedule(self.update_overall_timer)
        self.overall_seconds = 0
        self.timer_on = False

    def calculate_overall_click_time(self):
        if self.click_counter > 1:  # Avoid dividing by zero
            seconds_per_click = self.overall_seconds / (self.click_counter - 1)
            minutes, seconds = divmod(seconds_per_click, 60)
            part_seconds = seconds * 1000 % 1000
            self.overall_click_time = f'{int(minutes):02}:{int(seconds):02}.{int(part_seconds):03}'

    def update_keypad_size(self):
        # Has to be a separate function, because the whole layout adjusts to the keypad size.
        # If changed directly from settings, only keypad size would change.
        if SettingsScreen.data['keypad_size'] == 1:
            self.keypad_size = 0.3
        elif SettingsScreen.data['keypad_size'] == 2:
            self.keypad_size = 0.4
        elif SettingsScreen.data['keypad_size'] == 3:
            self.keypad_size = 0.5
        elif SettingsScreen.data['keypad_size'] == 4:
            self.keypad_size = 0.6

    def adjust_stack_layout(self):
        # Adjust labels width:
        if self.digits_between_spacing == 4 or self.digits_between_spacing == 9:
            self.digit_label_width = 0.1
        elif self.digits_between_spacing == 6:
            self.digit_label_width = 0.0714
        elif self.digits_between_spacing == 7:
            self.digit_label_width = 0.117
        elif self.digits_between_spacing == 8:
            self.digit_label_width = 0.111
        elif self.digits_between_spacing == 10:
            self.digit_label_width = 0.09
        else:
            self.digit_label_width = 0.08

        # Update highlighted digits:
        self.digits_to_highlight = SettingsScreen.data["mw_digits_to_highlight"]


class PiTrainingWidget(Screen):
    min_amount = 0
    max_amount = 100
    digits_to_load = 50
    digits_to_highlight = 100  # Highlights every nth digit
    digits_between_spacing = 2
    digit_label_width = NumericProperty()
    number_of_loads = 0

    def show_pi_decimals(self, min_amount, max_amount):
        for i in range(min_amount, max_amount):
            # Change color for different labels:
            if (i + 1) % self.digits_to_highlight == 0:
                digit_color = yellow
            else:
                digit_color = PiKingApp.text_color

            # Add a specific number of digits as labels:
            digit = pi_decimals[i]

            # Color digits already remembered:
            if self.min_amount % 2 != 0:  # If min_amount is odd, add one digit before to make even spacing
                i -= 1
            if (i + 1) <= (ScoresScreen.statistics['no_mistakes']['decimals']):
                digit_color = azure
            digit_label = Factory.PtDigitLabel(text=digit, color=digit_color, size_hint=(self.digit_label_width, None))
            self.ids.pt_stack_layout.add_widget(digit_label)

            # Add adequate spacing:
            if (i + 1) % self.digits_between_spacing == 0:
                space = Factory.PtDigitLabel(size_hint=(self.digit_label_width, None))
                self.ids.pt_stack_layout.add_widget(space)

    def load_more_digits(self):
        # Load only new digits:
        previous_max_amount = self.max_amount + (self.digits_to_load * self.number_of_loads)
        self.number_of_loads += 1
        new_max_amount = self.max_amount + (self.digits_to_load * self.number_of_loads)
        self.show_pi_decimals(previous_max_amount, new_max_amount)

    def reset(self):
        # Clear all the digits:
        self.ids.pt_stack_layout.clear_widgets()
        # Reset variables:
        self.number_of_loads = 0
        # Reset labels:
        self.ids.pt_stack_layout.add_widget(self.ids.pt_label)
        self.update_pt_screen()
        self.show_pi_decimals(self.min_amount, self.max_amount)

    def update_pt_screen(self):
        # Adjust width of the digits:
        if self.digits_between_spacing == 4 or self.digits_between_spacing == 9:
            self.digit_label_width = 0.1
        elif self.digits_between_spacing == 6:
            self.digit_label_width = 0.0714
        elif self.digits_between_spacing == 7:
            self.digit_label_width = 0.117
        elif self.digits_between_spacing == 8:
            self.digit_label_width = 0.111
        elif self.digits_between_spacing == 10:
            self.digit_label_width = 0.09
        else:
            self.digit_label_width = 0.08

        # Change initial digits to display:
        if SettingsScreen.data['pt_start_from_record']:
            self.min_amount = ScoresScreen.statistics['no_mistakes']['decimals']
        else:
            self.min_amount = 0


class SettingsScreen(Screen):
    # Create a data file to save:
    data = {
        'dark_mode': False,
        'keypad_size': 2,
        'mw_digits_between_spacing': 2,
        'mw_digits_to_highlight': 10,
        'pt_digits_to_load': 50,
        'pt_digits_between_spacing': 2,
        'pt_digits_to_highlight': 10,
        'pt_start_from_record': False,
    }
    try:
        with open('json/settings.json') as settings_file:
            data = json.load(settings_file)
    except FileNotFoundError:
        print('File created')

    # Set settings size screen:
    screen_height = 1.4
    # MainWidget variables:
    keypad_label = StringProperty()
    dbs_label = StringProperty()
    hd_title_label = StringProperty("Highlight every n[sup]th[/sup] digit: ")
    hd_label = StringProperty()
    # Pi Training variables:
    pt_dtl_label = StringProperty()
    pt_dbs_label = StringProperty()
    pt_hd_title_label = StringProperty("Highlight every n[sup]th[/sup] digit: ")
    pt_hd_label = StringProperty()

    def on_kp_slider_value(self, slider):
        if slider.value == 1:
            self.data['keypad_size'] = 1
            self.keypad_label = 'small'
        elif slider.value == 2:
            self.data['keypad_size'] = 2
            self.keypad_label = 'medium'
        elif slider.value == 3:
            self.data['keypad_size'] = 3
            self.keypad_label = 'large'
        else:
            self.data['keypad_size'] = 4
            self.keypad_label = 'gargantuan'

        with open('json/settings.json', 'w') as data_file:
            json.dump(self.data, data_file)

    def on_dbs_slider_value(self, slider):
        self.dbs_label = str(int(slider.value))
        MainWidget.digits_between_spacing = int(slider.value)
        self.data['mw_digits_between_spacing'] = int(slider.value)

        with open('json/settings.json', 'w') as data_file:
            json.dump(self.data, data_file)

    def on_hd_slider_value(self, slider):
        self.hd_label = str(int(slider.value))
        MainWidget.digits_to_highlight = int(slider.value)
        self.data['mw_digits_to_highlight'] = int(slider.value)

        with open('json/settings.json', 'w') as data_file:
            json.dump(self.data, data_file)

    def on_pt_dtl_slider_value(self, slider):
        self.pt_dtl_label = str(int(slider.value))
        PiTrainingWidget.digits_to_load = int(slider.value)
        self.data['pt_digits_to_load'] = int(slider.value)

        with open('json/settings.json', 'w') as data_file:
            json.dump(self.data, data_file)

    def on_pt_dbs_slider_value(self, slider):
        self.pt_dbs_label = str(int(slider.value))
        PiTrainingWidget.digits_between_spacing = int(slider.value)
        self.data['pt_digits_between_spacing'] = int(slider.value)

        with open('json/settings.json', 'w') as data_file:
            json.dump(self.data, data_file)

    def on_pt_hd_slider_value(self, slider):
        self.pt_hd_label = str(int(slider.value))
        PiTrainingWidget.digits_to_highlight = int(slider.value)
        self.data['pt_digits_to_highlight'] = int(slider.value)

        with open('json/settings.json', 'w') as data_file:
            json.dump(self.data, data_file)

    def update_sliders(self):
        # Update keypad size slider:
        kp_value = self.data['keypad_size']
        self.ids.kp_slider.value = kp_value
        if kp_value == 1:
            self.keypad_label = 'small'
        if kp_value == 2:
            self.keypad_label = 'medium'
        if kp_value == 3:
            self.keypad_label = 'large'
        if kp_value == 4:
            self.keypad_label = 'gargantuan'

        # Update main widget sliders:
        self.ids.dbs_slider.value = self.data['mw_digits_between_spacing']
        self.dbs_label = str(self.data['mw_digits_between_spacing'])

        self.ids.hd_slider.value = self.data['mw_digits_to_highlight']
        self.hd_label = str(self.data['mw_digits_to_highlight'])

        # Update Pi Training sliders:
        self.ids.pt_dtl_slider.value = self.data['pt_digits_to_load']
        self.pt_dtl_label = str(self.data['pt_digits_to_load'])

        self.ids.pt_dbs_slider.value = self.data['pt_digits_between_spacing']
        self.pt_dbs_label = str(self.data['pt_digits_between_spacing'])

        self.ids.pt_hd_slider.value = self.data['pt_digits_to_highlight']
        self.pt_hd_label = str(self.data['pt_digits_to_highlight'])

    def start_from_record_switch(self, value):
        if value:
            self.data['pt_start_from_record'] = True
        else:
            self.data['pt_start_from_record'] = False

        with open('json/settings.json', 'w') as settings_file:
            json.dump(self.data, settings_file)


class PiKingApp(MDApp):
    if SettingsScreen.data['dark_mode']:
        text_color = white
        bg_color = dark_grey
    else:
        text_color = black
        bg_color = white

    def build(self):
        self.title = 'Pi King'
        # Change colors for switches and sliders:
        self.theme_cls.primary_palette = 'Amber'
        self.theme_cls.primary_hue = '700'

        sm = ScreenManager()
        screens = [MainMenu(name="main_menu"),
                   MainWidget(name="main_widget"),
                   PiTrainingWidget(name='pi_training_widget'),
                   ScoresScreen(name='scores_screen'),
                   ScoresScreen2(name='scores_screen_2'),
                   ScoresScreen3(name='scores_screen_3'),
                   ScoresScreen4(name='scores_screen_4'),
                   SettingsScreen(name='settings_screen'),
                   GuidesScreen(name='guides_screen'),
                   AboutTheAppPageLayout(name='about_the_app_screen')]
        for screen in screens:
            sm.add_widget(screen)

        sm.current = "main_menu"
        return sm

    @staticmethod
    def dark_mode_switch(value):
        if value:
            SettingsScreen.data['dark_mode'] = True
        else:
            SettingsScreen.data['dark_mode'] = False
        with open('json/settings.json', 'w') as settings_file:
            json.dump(SettingsScreen.data, settings_file)


if __name__ == '__main__':
    PiKingApp().run()
