from kivy.lang import Builder
#from kivy.uix.boxlayout import BoxLayout
#from kivy.properties import StringProperty
#import time
from kivymd.app import MDApp
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen,SwapTransition,ScreenManager
from kivymd.theming import ThemeManager
from homepagemain import *
from notepagetopic import *
from practicepage import *
from datapage import datapage
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.datatables import MDDataTable
#import threading
#from functools import partial


class ComputerShortcut(MDApp):
    def __init__(self):
        super(ComputerShortcut, self).__init__()
        self.screen= Screen()
        self.sm= ScreenManager()
        self.theme_cls  = ThemeManager()
        self.theme_cls.primary_palette = "Amber"
        self.a=Builder.load_file("main.kv")
        self.way="hello"
        self.qnum=0
        menu_items = [
            {
                "text": "Share",
                "viewclass": "OneLineListItem",
                "height": dp(50),
                "on_release": lambda x="Share": self.menu_callback(x),
            } ,
            {
                "text": "Review",
                "viewclass": "OneLineListItem",
                "height": dp(50),
                "on_release": lambda x="Review": self.menu_callback(x),
            } 
        ]
        self.menu = MDDropdownMenu(
            caller=self.a.ids.fscreen.ids.buttonmenu,
            items=menu_items,
            max_height=dp(100),
            radius=[24, 0, 24, 0],
            width_mult=3,
        )
        self.data_tables_tran = MDDataTable(
                use_pagination=True,
                rows_num=8,
                column_data=[
                    ("No.",dp(10)),
                    ("Application or Info", dp(40)),
                    ("Key or Value", dp(30)),
                    
                
                ],
                row_data=datapage().word_data
                
                )
        
    def menu_callback(self, text_item):
        print(text_item)

        
        
    def build(self):
        self.theme_cls.primary_palette = "Amber"
        
        
        
        
        
       
        return self.a
    def screen_switch_notescreen(self):
        self.a.transition=SwapTransition()
        self.a.current = 'NoteBook'
    def screen_switch_homeback(self):
        self.a.transition=SwapTransition()
        self.a.current = 'HomePage'
    def screen_switch_practicep(self):
        self.a.transition=SwapTransition()
        self.a.current = 'PracticePage'
    
        
        
        
if __name__ == '__main__':
    ComputerShortcut().run()

