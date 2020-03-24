import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector

class PongBall(Widget):

    # velocity of the ball on x and y axies
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    # referencelist property so we can use ball.velocity as
    # a shorthand, just like e.g w.pos for w.x and w.y
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # "move" function will move the ball one step. This
    # will be called in equal intervals to animate the ball
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    pass


class PongApp(App):
    
    def build(self):
        return PongGame()

if __name__ == '__main__':
    PongApp().run()