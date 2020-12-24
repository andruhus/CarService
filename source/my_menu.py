from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivymd.uix.button import MDFlatButton
from kivy.uix.scrollview import ScrollView
from source.Deffects import *

PATH_TO_DEFECT_FILE = "C:/Users/aaade/Desktop/programs/OOP/CarService/resourses/defect_info.txt"

class DemoApp(MDApp):

    def build(self):
        screen = Screen()

        # Creating a Simple List
        scroll = ScrollView()

        list_view = MDList()
        icons = IconLeftWidget(icon="plus")
        items = OneLineIconListItem(text='Add a new defect')
        items.add_widget(icons)
        list_view.add_widget(items)

        with open(PATH_TO_DEFECT_FILE,'r') as f:
            s = f.readlines()
            for line in s:
                defect = Deffect(line)
                icons = IconLeftWidget(icon="fire")
                items = OneLineIconListItem(text=defect.name)
                items.add_widget(icons)
                list_view.add_widget(items)

        scroll.add_widget(list_view)
        # End List

        screen.add_widget(scroll)

        return screen


DemoApp().run()

