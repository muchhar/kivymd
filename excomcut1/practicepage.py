#from concurrent.futures import thread
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
from kivymd.uix.dialog import MDDialog
#import threading
#import time
#from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDFlatButton
#from kivy.uix.widget import Widget 
from datapage import datapage
#from kivy.graphics import RoundedRectangle, Color

#from functools import partial
#from kivymd.uix.tab import MDTabsBase
from random import randint
Builder.load_file("practicepage.kv")
     
class RectangularRippleButton(RectangularRippleBehavior,Button):
    pass


class PracticePage(Screen):
    moka=0
    ans=""
    wrong_q=0
    main_data=[]
    wordexe_data=["wordexe/c0.png","wordexe/c1.png","wordexe/c2.png","wordexe/c3.png","wordexe/c3.png","wordexe/c4.png","wordexe/c5.png","wordexe/c6.png","wordexe/c7.png","wordexe/c8.png","wordexe/c9.png","wordexe/c10.png","wordexe/c11.png","wordexe/c12.png","wordexe/c13.png","wordexe/c14.png","wordexe/c15.png","wordexe/c16.png","wordexe/c17.png","wordexe/c18.png","wordexe/c19.png","wordexe/c20.png","wordexe/c21.png","wordexe/c22.png","wordexe/c23.png","wordexe/c24.png","wordexe/c4.png","wordexe/c25.png","wordexe/c26.png","wordexe/c25.png","wordexe/c26.png","wordexe/c27.png","wordexe/c26.png","wordexe/c28.png","wordexe/c26.png","wordexe/c29.png","wordexe/c30.png","wordexe/c31.png","wordexe/c30.png","wordexe/c32.png","wordexe/c33.png","wordexe/c34.png","wordexe/c35.png","wordexe/c36.png","wordexe/c37.png","wordexe/c13.png","wordexe/c38.png","wordexe/c14.png","wordexe/c39.png","wordexe/c40.png","wordexe/c41.png","wordexe/c16.png","wordexe/c42.png","wordexe/c16.png","wordexe/c44.png","wordexe/c45.png","wordexe/c46.png"]
    excel_data=["excelexe/e0.png","excelexe/e1.png","excelexe/e0.png","excelexe/e2.png","excelexe/e3.png","excelexe/e4.png","excelexe/e5.png","excelexe/e6.png","excelexe/e7.png","excelexe/e8.png","excelexe/e9.png","excelexe/e10.png","excelexe/e11.png","excelexe/e6.png","excelexe/e4.png"]
    power_data=["powerexe/p0.png","powerexe/p1.png","powerexe/p2.png","powerexe/p3.png","powerexe/p4.png","powerexe/p5.png","powerexe/p6.png","powerexe/p7.png","powerexe/p8.png","powerexe/p9.png","powerexe/p10.png"]
    general_data=["generalexe/g0.png","generalexe/g1.png","generalexe/g1.png","generalexe/g2.png","generalexe/g3.png","generalexe/g4.png","generalexe/g5.png","generalexe/g6.png","generalexe/g7.png","generalexe/g8.png","generalexe/g8.png"]

    def blogin(self):
        app=MDApp.get_running_app()
        app.screen_switch_homeback()
   
    def add_keybod(self):
        app=MDApp.get_running_app()
        a=app.data_tables_tran.row_data
        jawab=a[app.qnum][2][24:-15]#answer
        r_key=[]
        colectkey=""
        for i in jawab:
            if i=="+":
                if colectkey=="&bl;":
                    colectkey="["
                r_key.append(colectkey)
                colectkey=""
            else:
                colectkey=colectkey+i
        if colectkey!="":
            if colectkey=="&bl;":
                    colectkey="["
            r_key.append(colectkey)

        
        #############keyboard key group############################
        og1=["F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","F11","F12"]
        g1=[self.ids.fun1.text,self.ids.fun2.text,self.ids.fun3.text,self.ids.fun4.text]#function key
       # g2=[self.ids.leftk.text,self.ids.rightk.text,self.ids.upk.text,self.ids.dnk.text]#arrow key
        g3=[self.ids.alpha1.text,self.ids.alpha2.text,self.ids.alpha3.text,self.ids.alpha4.text]
        og3=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        g4=[self.ids.num1.text,self.ids.num2.text,self.ids.num3.text,self.ids.num4.text]#number key
        og4=["0","1","2","3","4","5","6","7","8","9"]
        #g5=[]#constant key
        g6=[self.ids.signb1.text,self.ids.signb2.text,self.ids.signb3.text,self.ids.signb4.text]#sign and extra key
        og6=["Home","Insert","Del","End","<",">","[","]","{","}","*",";"]
        og2=["<left arrow>","<right arrow>","<up arrow>","<down arrow>"]
        ###########################################################
        if len(r_key)==1:
            if r_key[0] in og1:
                if r_key[0] in g1:
                    pass
                else:
                    d=int(r_key[0][1:])
                    if d<5:
                        self.ids.fun1.text="F1"
                        self.ids.fun2.text="F2"
                        self.ids.fun3.text="F3"
                        self.ids.fun4.text="F4"
                    elif d<9:
                        self.ids.fun1.text="F5"
                        self.ids.fun2.text="F6"
                        self.ids.fun3.text="F7"
                        self.ids.fun4.text="F8"
                    elif d<13:
                        self.ids.fun1.text="F9"
                        self.ids.fun2.text="F10"
                        self.ids.fun3.text="F11"
                        self.ids.fun4.text="F12"
            else:
                if r_key[0]=="Esc":
                    self.ids.tab.text="Esc"
                else:
                    self.ids.tab.text="Tab"
                print("there is a single key but not function")

        elif len(r_key)==2:
            if r_key[1] in og1:
                if r_key[1] in g1:
                    pass
                else:

                    d=int(r_key[1][1:])
                    if d<5:
                        self.ids.fun1.text="F1"
                        self.ids.fun2.text="F2"
                        self.ids.fun3.text="F3"
                        self.ids.fun4.text="F4"
                    elif d<9:
                        self.ids.fun1.text="F5"
                        self.ids.fun2.text="F6"
                        self.ids.fun3.text="F7"
                        self.ids.fun4.text="F8"
                    elif d<13:
                        self.ids.fun1.text="F9"
                        self.ids.fun2.text="F10"
                        self.ids.fun3.text="F11"
                        self.ids.fun4.text="F12"
            elif r_key[1] in og3:
                if r_key[1] in g3:
                    pass
                else:
                    ik=[og3.index(r_key[1])]
                    while len(ik)!=4:
                        al=randint(0,25)
                        if al not in ik:
                            ik.append(al)
                    ik.sort()
                    
                    self.ids.alpha1.text=og3[ik[0]]
                    self.ids.alpha2.text=og3[ik[1]]
                    self.ids.alpha3.text=og3[ik[2]]
                    self.ids.alpha4.text=og3[ik[3]]
            elif r_key[1] in og6:
                if r_key[1] in g6:
                    pass
                else:
                    ik=[og6.index(r_key[1])]
                    while len(ik)!=4:
                        al=randint(0,9)
                        if al not in ik:
                            ik.append(al)
                    ik.sort()
                    self.ids.signb1.text=og6[ik[0]]
                    self.ids.signb2.text=og6[ik[1]]
                    self.ids.signb3.text=og6[ik[2]]
                    self.ids.signb4.text=og6[ik[3]]
            elif r_key[1] in og4:
                if r_key[1] in g4:
                    pass
                else:
                    ik=[og4.index(r_key[1])]
                    while len(ik)!=4:
                        al=randint(0,9)
                        if al not in ik:
                            ik.append(al)
                    ik.sort()
                    self.ids.num1.text=og4[ik[0]]
                    self.ids.num2.text=og4[ik[1]]
                    self.ids.num3.text=og4[ik[2]]
                    self.ids.num4.text=og4[ik[3]]
            else:
                pass
            pass
        elif len(r_key)==3:
            if r_key[2] in og1:
                if r_key[2] in g1:
                    pass
                else:

                    d=int(r_key[2][1:])
                    if d<5:
                        self.ids.fun1.text="F1"
                        self.ids.fun2.text="F2"
                        self.ids.fun3.text="F3"
                        self.ids.fun4.text="F4"
                    elif d<9:
                        self.ids.fun1.text="F5"
                        self.ids.fun2.text="F6"
                        self.ids.fun3.text="F7"
                        self.ids.fun4.text="F8"
                    elif d<13:
                        self.ids.fun1.text="F9"
                        self.ids.fun2.text="F10"
                        self.ids.fun3.text="F11"
                        self.ids.fun4.text="F12"
            elif r_key[2] in og3:
                if r_key[2] in g3:
                    pass
                else:
                    ik=[og3.index(r_key[2])]
                    while len(ik)!=4:
                        al=randint(0,25)
                        if al not in ik:
                            ik.append(al)
                    ik.sort()
                    self.ids.alpha1.text=og3[ik[0]]
                    self.ids.alpha2.text=og3[ik[1]]
                    self.ids.alpha3.text=og3[ik[2]]
                    self.ids.alpha4.text=og3[ik[3]]
            elif r_key[2] in og6:
                if r_key[2] in g6:
                    pass
                else:
                    ik=[og6.index(r_key[2])]
                    while len(ik)!=4:
                        al=randint(0,9)
                        if al not in ik:
                            ik.append(al)
                    ik.sort()
                    self.ids.signb1.text=og6[ik[0]]
                    self.ids.signb2.text=og6[ik[1]]
                    self.ids.signb3.text=og6[ik[2]]
                    self.ids.signb4.text=og6[ik[3]]
            elif r_key[2] in og4:
                if r_key[2] in g4:
                    pass
                else:
                    ik=[og4.index(r_key[2])]
                    while len(ik)!=4:
                        al=randint(0,9)
                        if al not in ik:
                            ik.append(al)
                    ik.sort()
                    self.ids.num1.text=og4[ik[0]]
                    self.ids.num2.text=og4[ik[1]]
                    self.ids.num3.text=og4[ik[2]]
                    self.ids.num4.text=og4[ik[3]]
            else:
                pass

            pass
        else:
            print("Answer contan more then three key")
        pass
       
                
              
    def ctrl(self,txt):
        
        if txt=="<--":
            txt="<left arrow>"
        elif txt=="-->":
            txt="<right arrow>"
        elif txt=="Up":
            txt="<up arrow>"
        elif txt=="Dn":
            txt="<down arrow>"
        else:
            pass
        if len(self.ans)!=0:
            if self.ans[-1]!="+":
                self.ans=""
                
        #make shift and alt like ctrl and finish keyboard
        if txt=="Ctrl" or txt=="Shift" or txt=="Alt":
            if "Ctrl" in self.ans and txt=="Ctrl":
                self.ans=""
                
            elif "Shift" in self.ans and txt=="Shift":
                self.ans=""
            elif "Alt" in self.ans and txt=="Alt":
                self.ans=""   
            else:
                self.ans=self.ans+txt+"+"
        
        else:
            self.ans=self.ans+txt
        
        app=MDApp.get_running_app()
        a=app.data_tables_tran.row_data
        
        comn=a[app.qnum][2][24:-15]
        if comn=="Ctrl+&bl;":
            comn="Ctrl+["
        if self.ans==comn:
            app.qnum+=1
            
            self.corework(app.qnum)
            if len(a)==app.qnum:
                #self.ids.img_q.source=self.main_data[-1]

                app.qnum=0
                self.condialog = MDDialog(
                title="Score",
                type="custom",
                text="Your Score is [b]" +str(len(a)-self.wrong_q)+"[/b] From [b]"+ str(len(a))+"[/b]",
                size_hint=(0.8,0.8),
                buttons=[
                    
                    MDFlatButton(
                        text="OK",
                        on_release=self.dismisd,
                        theme_text_color="Custom",
                        text_color=[255/256,193/256,7/256,1],
                    ),
                        ],
                    )
                
                self.condialog.open()
                
            self.ids.qnow.text=a[app.qnum][0] +" How "+a[app.qnum][1][24:-15]+" Using Shortcut."
            
            self.moka=0
            self.ids.notel.text=" Good! Correct Answer. For "+a[app.qnum-1][1][24:-15]+" Shortcut use [color=2ead58]"+ a[app.qnum-1][2][24:-15] +"[/color]"
            self.ids.notel.text_color=[0,255/256,0,1]
            self.add_keybod()
        else:
            if len(self.ans)!=0 and self.ans[-1]!="+":
                if self.moka ==0:
                    self.ids.notel.text=" Wrong Answer! Please Try Again."
                    self.moka+=1
                    self.wrong_q+=1
                elif self.moka==1:
                    self.ids.notel.text=" Wrong Again! Try Again."
                    self.moka+=1
                elif self.moka>1 :
                    self.ids.notel.text=" OK! Good Try. Press [color=cf1747]"+a[app.qnum][2][24:-15]+"[/color] for pass the Question."
                    #self.moka+=1
                self.ids.notel.text_color=[255/256,0,0,1]
            #return
        
        if self.ans.count("+")>2:
            self.ans=""
            
        
        if self.ans=="Ctrl+[":
            self.ans="Ctrl+&bl;"
        self.ids.indicat.text=self.ans
        ############Ctrl###########
        if "Ctrl+" in self.ans or self.ans=="Ctrl+":
            self.ids.bctrl.background_color=[51/256,164/256,206/256,1]
            
        else:
            self.ids.bctrl.background_color=[88/256,88/256,88/256,1]
        ###################Shift###############
        if "Shift+" in self.ans or self.ans=="Shift+":
            self.ids.shift.background_color=[51/256,164/256,206/256,1]
            
        else:
            self.ids.shift.background_color=[88/256,88/256,88/256,1]
        ##################Alt##########################
        if "Alt+" in self.ans or self.ans=="Alt+":
            self.ids.alt.background_color=[51/256,164/256,206/256,1]
            
        else:
            self.ids.alt.background_color=[88/256,88/256,88/256,1]
        if len(self.ans)!=0 and self.ans[-1]!="+":
            self.ids.bctrl.background_color=[88/256,88/256,88/256,1]
            self.ids.shift.background_color=[88/256,88/256,88/256,1]
            self.ids.alt.background_color=[88/256,88/256,88/256,1]
    def dismisd(self,*args):
        self.condialog.dismiss()
        
        self.blogin()
    def corework(self,x):
        
        self.ids.img_q.source=self.main_data[x]
        
            
    def on_enter(self):
        self.ids.notel.text=" Note: Click first key and then other key from below keyboard(this is not standard keyboard just for practice)."
        self.ids.notel.text_color=[0,0,255/256,1]
        self.moka=0
       # self.ids.abvl.height=dp(0)
        self.ids.indicat.text=""
        
        app=MDApp.get_running_app()
        ##########depend upon pages#######################################
        if app.way=="general":
            app.data_tables_tran.row_data=datapage().general_data
            self.ids.img_q.source=self.general_data[0]
            self.main_data=self.general_data
        elif app.way=="word":
            app.data_tables_tran.row_data=datapage().word_data
            self.ids.img_q.source=self.wordexe_data[0]
            self.main_data=self.wordexe_data
        elif app.way=="excel":
            app.data_tables_tran.row_data=datapage().excel_data
            self.ids.img_q.source=self.excel_data[0]
            self.main_data=self.excel_data
        else:
            app.data_tables_tran.row_data=datapage().power_data
            self.ids.img_q.source=self.power_data[0]
            self.main_data=self.power_data
        ##################################################################
        app.qnum=0 #must be zero for start quations from q.1
        self.add_keybod()
        a=app.data_tables_tran.row_data
        self.ids.qnow.text=a[app.qnum][0]+" How "+a[app.qnum][1][24:-15]+" Using Shortcut."
        
        pass
            
            
            
        

            
   