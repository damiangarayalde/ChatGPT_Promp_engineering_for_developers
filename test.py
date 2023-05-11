import panel as pn

from panel.interact import interact, fixed
from panel import widgets

pn.extension()


def Slider(x):
    return x*x


interact(Slider, x=5)
