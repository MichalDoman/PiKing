from kivymd.uix.slider import MDSlider

# Colors:
violet_red = (255 / 255, 59 / 255, 100 / 255, 1)
dark_violet_red = (145 / 255, 0 / 255, 70 / 255, 1)

yellow = (242 / 255, 164 / 255, 12 / 255, 1)
dark_yellow = (219 / 255, 131 / 255, 22 / 255, 1)

blue = (54 / 255, 110 / 255, 240 / 255, 1)
dark_blue = (40 / 255, 74 / 255, 176 / 255, 1)

azure = (121 / 255, 177 / 255, 224 / 255, 1)
dark_azure = (93 / 255, 142 / 255, 181 / 255, 1)
very_dark_azure = (66 / 255, 96 / 255, 122 / 255, 1)

grey = (180 / 255, 180 / 255, 180 / 255, 1)
dark_grey = (40 / 255, 40 / 255, 40 / 255, 1)
black = (0, 0, 0, 1)
white = (1, 1, 1, 1)


class ScrollViewSlider(MDSlider):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            super(ScrollViewSlider, self).on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            super(ScrollViewSlider, self).on_touch_up(touch)

    def on_touch_move(self, touch):
        if self.collide_point(*touch.pos):
            super(ScrollViewSlider, self).on_touch_move(touch)