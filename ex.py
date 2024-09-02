from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import numpy as np

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from matplotlib.figure import Figure


KV = '''
BoxLayout:
    orientation: 'vertical'
    MDTopAppBar:
        title: 'Matplotlib in KivyMD'
        elevation: 10
    BoxLayout:
        id: plot_container
        canvas.before:
            Rectangle:
                pos: self.pos
                size: self.size
'''

class MatplotlibWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.plot()

    def plot(self):
        # Create a matplotlib figure
        fig = Figure()
        ax = fig.add_subplot(111)

        # Plot some data
        ax.plot([1, 2, 3, 4], [10, 20, 25, 30], 'r-')

        # Create a FigureCanvasKivyAgg instance
        canvas = FigureCanvasKivyAgg(fig)
        canvas.draw()

        # Add the canvas to the widget
        self.add_widget(canvas)

class MatplotlibApp(MDApp):
    def build(self):
        self.root = Builder.load_string(KV)
        plot_container = self.root.ids.plot_container

        # Add MatplotlibWidget to the plot_container
        plot_widget = MatplotlibWidget()
        plot_container.add_widget(plot_widget)
        return self.root

if __name__ == '__main__':
    MatplotlibApp().run()
