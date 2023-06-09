
class Buttons:
    def __init__(self):
        self.buttons = []
    def add_button(self, button):
        self.buttons.append(button)
    def drawButtons(self):
        for button in self.buttons:
            button.draw()
