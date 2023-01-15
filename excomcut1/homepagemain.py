from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.anchorlayout import AnchorLayout
#from kivy.properties import StringProperty
#from kivy.core.image import Image as CoreImage
#import io
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList
#from kivy.uix.carousel import Carousel
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
#import os
#from kivy.metrics import sp, dp
#from kivymd.uix.navigationdrawer import *
#from kivy.uix.label import Label
from kivymd.uix.behaviors import RectangularRippleBehavior
#from kivy.garden.navigationdrawer import NavigationDrawer

#import threading
#import time
#from kivy.uix.widget import Widget 
#from kivy.graphics import RoundedRectangle, Color

#from kivy.clock import Clock, mainthread
#from functools import partial
#from kivymd.uix.menu import MDDropdownMenu
Builder.load_file("homepage.kv")

class ContentNavigationDrawer(BoxLayout):
    def notebook(self,way):
        app=MDApp.get_running_app()
        app.way=way
        app.screen_switch_notescreen()
    pass     
     
class RectangularRippleButton(RectangularRippleBehavior,Button):
    pass


class HomePage(Screen):
 
   

    
    def notebook(self,way):
        app=MDApp.get_running_app()
        app.way=way
        app.screen_switch_notescreen()
    def word_pra(self,way):
        app=MDApp.get_running_app()
        app.way=way
        app.screen_switch_practicep()
     
        
    
    pass
class ItemDrawer(OneLineIconListItem):
   pass


class DrawerList(ThemableBehavior, MDList):
    
    pass

