# PiKing

### About app:
This is the first bigger app that I made with python. I made it while learning on my own, at the beginning of my programming journey. Its purpose is to facilitate memory training. In the simplest explanation, the app lets you type in the numbers and tells you whether the number is correct or not and it is about pi number decimals. It is a mobile app made with python libraries: kivy and kivyMD. PiKing was made with the aim to let the user customize how the main widget looks, as well as provide the most detailed statistic and scoring system. Below there is a brief explanation what every view is for.

___
### Main menu:
The main screen on which you can access: settings, scores, main widget, training mode and guides.

<p align="center">
    <img src="https://github.com/MichalDoman/PiKing/blob/main/screenshots/piking_main_menu.png"  width="20%" height="30%">
</p>

___
### App Settings:
The settings screen is divided into sections. Each section corresponds to the specific widget. All the adjustable values are explained in the views that they modify. When it comes to overall settings there is a possibility to change dark/light mode which also requires restarting the app. Second option is to show your status on the main screen. This functionality is planned for the future, and the idea is that when a user would unlock an achievement, new titles would unlock that could be shown on the main screen.
<p align="center">
    <img src="https://github.com/MichalDoman/PiKing/blob/main/screenshots/piking_settings_1.png"  width="20%" height="30%">
    <img src="https://github.com/MichalDoman/PiKing/blob/main/screenshots/piking_settings_2.png"  width="20%" height="30%">
</p>

___
### Main widget:
This is the main view of the app. Here is where you type in the numbers. If the number is incorrect it appears red. However, if you type in the numbers quick enough you gain a combo, which is indicated by blue digits. A combo increases the score which is displayed at the right top and it stops either when the user does not click fast enough or when they make a mistake. To the right of the score there is show extra score gained by combo.
<p align="center">
    <img src="https://github.com/MichalDoman/PiKing/blob/main/screenshots/piking_main_widget.png"  width="20%" height="30%">
    <img src="https://github.com/MichalDoman/PiKing/blob/main/screenshots/piking_main_widget_white.png"  width="20%" height="30%">
</p>

In the settings it is possible to change how big is the keypad. You can also modify how many digits are displayed between each space and which digit is highlighted. The highlight has the aim to indicate e.g. every 100th number typed.

___
### Training mode:
This view let the user see the pi number and learn from it. The plus button loads more digits to display in this mode.
<p align="center">
    <img src="https://github.com/MichalDoman/PiKing/blob/main/screenshots/piking_training.png"  width="20%" height="30%">
</p>

In the settings it is also possible to change digits displayed between space as well as which ones to highlight. Additionally, In the training mode, one can adjust how many digits display at once and how many to load with every plus-button click. You can also set the option to start the training mode from the previous best record.

___
### Scores:
The scores section offers a lot. There are 4 categories of high scores. First one is the game with most decimals which counts how many correct digits were given. Second one is the game with the biggest score. Third one is the game with most digits given, up to the first mistake and the last category is the longest combo maintained.
Every category has its own statistics which are adjusted to the category specifications. The statistics are: 
1. Decimals - how many digits were scored 
2. Points - score amount
3. Efficacy - % of correct decimals typed
4. The longest combo - how many digits were in the longest combo
5. Extra points - all extra points gained through combos
6. Time per combo digit - how many milliseconds it took on average to type digits during combos
7. Combo time - how much time was spend in combos
8. Time per digit - Average time to type digits overly
9. Play time - how long was the game until restart or exit
10. Digits per minute - the temp of typing digits per minute
11. Date - when the high score was reached
 <p align="center">
    <img src="https://github.com/MichalDoman/PiKing/blob/main/screenshots/piking_scores_1.png"  width="20%" height="30%">
    <img src="https://github.com/MichalDoman/PiKing/blob/main/screenshots/piking_scores_2.png"  width="20%" height="30%">
    <img src="https://github.com/MichalDoman/PiKing/blob/main/screenshots/piking_scores_3.png"  width="20%" height="30%">
    <img src="https://github.com/MichalDoman/PiKing/blob/main/screenshots/piking_scores_4.png"  width="20%" height="30%">
</p>

___
### Guides:
This view was made with the purpose of providing user with guides about the use of the app, understanding scores as well as developing their own Mnemonic Major Systems. 
<p align="center">
    <img src="https://github.com/MichalDoman/PiKing/blob/main/screenshots/piking_guides.png"  width="20%" height="30%">
</p>
