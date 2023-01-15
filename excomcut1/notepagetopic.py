from kivy.lang import Builder
#from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.anchorlayout import AnchorLayout
#from kivy.properties import StringProperty
from kivymd.app import MDApp
#from kivymd.theming import ThemableBehavior
#from kivymd.uix.list import OneLineIconListItem, MDList
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
#from kivy.metrics import sp, dp
#from kivy.uix.label import Label
from kivymd.uix.behaviors import RectangularRippleBehavior
#from kivymd.uix.dialog import MDDialog
#import threading
#import time
from kivymd.uix.floatlayout import MDFloatLayout
#from kivymd.uix.button import *
#from kivy.uix.widget import Widget 
#from kivy.graphics import RoundedRectangle, Color
#from kivymd.uix.datatables import MDDataTable
#from functools import partial
from kivymd.uix.tab import MDTabsBase
from datapage import datapage
Builder.load_file("notepagetopic.kv")
     
class RectangularRippleButton(RectangularRippleBehavior,Button):
    pass

class Tab(MDFloatLayout, MDTabsBase):
        pass
class NoteBook(Screen):
    
    def blogin(self):
        app=MDApp.get_running_app()
        app.screen_switch_homeback()
    
        
    def on_enter(self):
        
        self.ids.bharat.hide=False
        app=MDApp.get_running_app()
        
        try:
            self.ids.karan.remove_widget(app.data_tables_tran)
        except:
            pass
        
        if app.way== "word":
            self.ids.tbaar.title="Microsoft-Word Shortcut"
            app.data_tables_tran.row_data=datapage().word_data
        elif app.way=="general":
            self.ids.tbaar.title="General Shortcut"
            app.data_tables_tran.row_data=datapage().general_data
        elif app.way=="excel":
            self.ids.tbaar.title="Microsoft-Excel Shortcut"
            app.data_tables_tran.row_data=datapage().excel_data
        elif app.way=="power":
            self.ids.tbaar.title="PowerPoint Shortcut"
            app.data_tables_tran.row_data=datapage().power_data
        
        elif app.way=="lanc":
            self.ids.tbaar.title="Languages and Founder"
            
            app.data_tables_tran.row_data=datapage().lang_data
        elif app.way=="memo":
            self.ids.tbaar.title="Memory Unit"
           
            app.data_tables_tran.row_data=datapage().mem_data
        elif app.way=="fileex":
            self.ids.tbaar.title="File and Extension"
            
            app.data_tables_tran.row_data=datapage().fileex_data
        elif app.way=="abbre":
            self.ids.tbaar.title="Abbreviations"
            
            app.data_tables_tran.row_data=datapage().abb_data
        elif app.way=="cmdc":
            self.ids.tbaar.title="Command Windows"
            
            app.data_tables_tran.row_data=datapage().cmd_data
        
        
        else:
            self.ids.tbaar.title="Microsoft-Word Shortcut"
            app.data_tables_tran.row_data=datapage().word_data
        
            
            
        self.ids.karan.add_widget(app.data_tables_tran)
        self.ids.bharat.hide=True
            
            
            
        

            
   