from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen , ScreenManager
from kivymd.uix.filemanager import MDFileManager
from kivy.properties import StringProperty
from kivymd.uix.dialog import MDDialog
import os
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.list import  IconLeftWidget
from kivy.properties import BooleanProperty
from kv import helper1
from kivy.core.window import Window  
from kivy.animation import Animation
from  kivymd.uix.floatlayout import FloatLayout
from  kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from kivy.graphics import Canvas 
from kivy.graphics import Rectangle 
from kivymd.uix.button import MDIconButton
from kivymd.uix.menu import MDDropdownMenu  
from kivymd.uix.button import MDFlatButton 
from kivy.metrics import dp
from sql import session, DB_heart
from joblib import load
import pandas as pd

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from matplotlib.figure import Figure
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import numpy as np

class LoginScreen(Screen):
    text = StringProperty()
class SignupScreen(Screen):
    text = StringProperty()  
    vid_img_scr = BooleanProperty(True)
class MainScreeen(Screen):
    vid_img_scr = BooleanProperty(True)
class ForgotScreen(Screen):
    pass
class HistoryScreen(Screen):
    pass
class Video_screen(Screen):
    pass
class About_us(Screen):
    pass
class Heart_attack_screen1(Screen):
     pass
class Predict1(Screen):
     pass
class Cardio_vascular(Screen):
     pass

class Main_screen(Screen):
     pass


class Start_page_UI(Screen):
    def __init__(self, **kwargs):
        super(Start_page_UI, self).__init__(**kwargs)
        
        
        box_layout = FloatLayout()
        self.image = Image(source='logo-2.jpg', pos_hint={'center_x': 0.1, 'center_y': 0.1}, size = (self.height*1, self.width*1), size_hint=(None, None))
        self.md_label = MDLabel(text='Heart Health Predictor', halign='center', size=(self.height*0, self.width*0), size_hint_y=None, font_style='H4', bold=True, theme_text_color="Custom",
            text_color=(0,0,0,1))
        self.animate_lable()
        box_layout.add_widget(self.md_label)
        self.animate_image()
        self.add_widget(self.image)
        button1 = MDIconButton(icon = "next_button.jpg", pos_hint={"center_x": .5, 'center_y': 0.1} ,icon_size =  "100sp",  on_release=self.main)
        
        box_layout.add_widget(button1)
        self.add_widget(box_layout)
    
    def main(self, *args):
        if self.manager:
            self.manager.current = 'main'
        else:
            print("Error: 'manager' is not defined")

    def animate_image(self, *args):
        anim = Animation(size = (self.height,self.width ))
        anim += Animation(size = (self.height*2, self.width*2),pos_hint={'center_x': 0.5, 'center_y': 0.6}, transition = 'linear')
        anim.start(self.image)
    def animate_lable(self, *args):
        anim_lable = Animation(size = (self.height, self.width ))
        anim_lable += Animation(size = (self.height*4, self.width*4), transition = 'linear')
        anim_lable.start(self.md_label)




class apps(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ##Load all models of Heart attack
        self.scaler = load('model_heart_disease/scalers.joblib')
        self.model1 = load('model_heart_disease/ExtraTreesClassifier.joblib')
        self.model2 =  load('model_heart_disease/RandomForestClassifier.joblib')
        self.model3 = load('model_heart_disease/GradientBoostingClassifier.joblib')
        self.model4 = load('model_heart_disease/XGBClassifier.joblib')

        self.scaler_cardio = load('model_heart_disease/scalers_cardio.joblib')
        self.model5 = load('model_heart_disease/AdaBoostClassifier_cardio.joblib')
        self.model6 =  load('model_heart_disease/GradientBoostingClassifier_cardio.joblib')
        self.model7 = load('model_heart_disease/RandomForestClassifier_cardio.joblib')
        self.model8 = load('model_heart_disease/RandomForestClassifier1_cardio.joblib')
        self.model9 = load('model_heart_disease/XGBClassifier_cardio.joblib')

        self.h = 0
    
    
    def show_dropdown(self, button):  
        menu_items = [  
            {"text": "Male", "viewclass": "OneLineListItem","height": dp(54), "on_release": lambda x="Item 1": self.item('male')},  
            {"text": "Female", "viewclass": "OneLineListItem","height": dp(54), "on_release": lambda x="Item 2": self.item('female')},  
              
        ]  

        self.dropdown_menu = MDDropdownMenu(  
            caller=button,  
            items=menu_items,  
            width_mult=4,  
        )  
        self.dropdown_menu.open() 


    def item(self, x):
        if self.root.get_screen('h_scr1'):
            self.root.get_screen('h_scr1').ids.drop_item.text = x

        if self.root.get_screen('cardi'):
            self.root.get_screen('cardi').ids.drop_item.text = x

    
         
        

    def show_dropdown1(self, button):  
            menu_items = [  
                {"text": "typical angina", "viewclass": "OneLineListItem","height": dp(54), "on_release": lambda x="Item 1": self.item1("typical angina")},  
                {"text": "atypical angina", "viewclass": "OneLineListItem","height": dp(54), "on_release": lambda x="Item 2": self.item1("atypical angina")},
                {"text": "non-anginal pain", "viewclass": "OneLineListItem","height": dp(54), "on_release": lambda x="Item 3": self.item1("non-anginal pain")},
                {"text": "asymptomatic", "viewclass": "OneLineListItem","height": dp(54), "on_release": lambda x="Item 4": self.item1("asymptomatic")}  
                
            ]  


            self.dropdown_menu = MDDropdownMenu(  
                caller=button,  
                items=menu_items,  
                width_mult=4,  
            )  
            self.dropdown_menu.open()   

    def item1(self, x):
         self.root.get_screen('h_scr1').ids.drop_item1.text = x
                 

    def show_dropdown2(self, button):  
            menu_items = [  
                {"text": "0", "viewclass": "OneLineListItem","height": dp(54), "on_release": lambda x="Item 1": self.item2('0')},  
                {"text": "1", "viewclass": "OneLineListItem","height": dp(54), "on_release": lambda x="Item 2": self.item2('1')},
        
                
            ]  

            self.dropdown_menu = MDDropdownMenu(  
                caller=button,  
                items=menu_items,  
                width_mult=4,  
            )  
            self.dropdown_menu.open()  
            
    def item2(self, x):
         self.root.get_screen('h_scr1').ids.drop_item2.text = x

    def show_dropdown3(self, button):  
            menu_items = [  
                {"text": "normal", "viewclass": "OneLineListItem","height": dp(54), "on_release": lambda x="Item 1": self.item3('normal')},  
                {"text": "ST-T wave abnormality", "viewclass": "OneLineListItem","height": dp(54), "on_release": lambda x="Item 2": self.item3('ST-T wave abnormality')},
                {"text": "left ventricular hypertrophy", "viewclass": "OneLineListItem","height": dp(54), "on_release": lambda x="Item 2": self.item3('left ventricular hypertrophy')},
                 
                
            ]  

            self.dropdown_menu = MDDropdownMenu(  
                caller=button,  
                items=menu_items,  
                width_mult=4,  
            )  
            self.dropdown_menu.open() 

    def item3(self, x):
         self.root.get_screen('h_scr1').ids.drop_item3.text = x 

    def show_dropdown4(self, button):  
            menu_items = [  
                {"text": "0", "viewclass": "OneLineListItem","height": dp(54), "on_release": lambda x="Item 1": self.item4('0')},  
                {"text": "1", "viewclass": "OneLineListItem","height": dp(54), "on_release": lambda x="Item 2": self.item4('1')},
                 
                
            ]  

            self.dropdown_menu = MDDropdownMenu(  
                caller=button,  
                items=menu_items,  
                width_mult=4,  
            )  
            self.dropdown_menu.open()  

    def item4(self, x):
         self.root.get_screen('h_scr1').ids.drop_item4.text = x 

    def show_dropdown5(self, button):  
            menu_items = [  
                {"text": "upsloping", "viewclass": "OneLineListItem","height": dp(54), "on_release": lambda x="Item 1": self.item5('upsloping')},  
                {"text": "flat", "viewclass": "OneLineListItem","height": dp(54), "on_release": lambda x="Item 2": self.item5('flat')},
                {"text": "downsloping", "viewclass": "OneLineListItem","height": dp(54), "on_release": lambda x="Item 3": self.item5('downsloping')},
                 
                
            ]  

            self.dropdown_menu = MDDropdownMenu(  
                caller=button,  
                items=menu_items,  
                width_mult=4,  
            )  
            self.dropdown_menu.open()  

    def item5(self, x):
         self.root.get_screen('h_scr1').ids.drop_item5.text = x 

    def drop_item_car_chale(self, button):  
            menu_items = [  
                {"text": "Normal", "viewclass": "OneLineListItem","height": dp(54), "on_release": lambda x="Item 1": self.item6('1')},  
                {"text": " Above normal", "viewclass": "OneLineListItem","height": dp(54), "on_release": lambda x="Item 2": self.item6('2')},
                {"text": "Well above normal", "viewclass": "OneLineListItem","height": dp(54), "on_release": lambda x="Item 3": self.item6('3')},
                 
                
            ]  

            self.dropdown_menu = MDDropdownMenu(  
                caller=button,  
                items=menu_items,  
                width_mult=4,  
            )  
            self.dropdown_menu.open()  

    def item6(self, x):
         self.root.get_screen('cardi').ids.drop_item_car_chales.text = x 

    def glo_level(self, button):  
            menu_items = [  
                {"text": "Normal", "viewclass": "OneLineListItem","height": dp(54), "on_release": lambda x="Item 1": self.item7('1')},  
                {"text": "Above normal", "viewclass": "OneLineListItem","height": dp(54), "on_release": lambda x="Item 2": self.item7('2')},
                {"text": "Well above normal", "viewclass": "OneLineListItem","height": dp(54), "on_release": lambda x="Item 3": self.item7('3')},
                 
                
            ]  

            self.dropdown_menu = MDDropdownMenu(  
                caller=button,  
                items=menu_items,  
                width_mult=4,  
            )  
            self.dropdown_menu.open()  

    def item7(self, x):
         self.root.get_screen('cardi').ids.golucose.text = x 


    def smoker(self, button):  
            menu_items = [  
                {"text": "Smoker", "viewclass": "OneLineListItem","height": dp(54), "on_release": lambda x="Item 1": self.item8('1')},  
                {"text": "Non-Smoker", "viewclass": "OneLineListItem","height": dp(54), "on_release": lambda x="Item 2": self.item8('0')},
               
                 
                
            ]  

            self.dropdown_menu = MDDropdownMenu(  
                caller=button,  
                items=menu_items,  
                width_mult=4,  
            )  
            self.dropdown_menu.open()  

    def item8(self, x):
         self.root.get_screen('cardi').ids.smoke.text = x 

    def Acholer(self, button):  
            menu_items = [  
                {"text": "Alcholer", "viewclass": "OneLineListItem","height": dp(54), "on_release": lambda x="Item 1": self.item9('1')},  
                {"text": "Non-Alcholer", "viewclass": "OneLineListItem","height": dp(54), "on_release": lambda x="Item 2": self.item9('0')},
                
                 
                
            ]  

            self.dropdown_menu = MDDropdownMenu(  
                caller=button,  
                items=menu_items,  
                width_mult=4,  
            )  
            self.dropdown_menu.open()  

    def item9(self, x):
         self.root.get_screen('cardi').ids.alcohol.text = x 


    def active(self, button):  
            menu_items = [  
                {"text": "Physical inactive", "viewclass": "OneLineListItem","height": dp(54), "on_release": lambda x="Item 1": self.item10('0')},  
                {"text": "Physical Active", "viewclass": "OneLineListItem","height": dp(54), "on_release": lambda x="Item 2": self.item10('1')},
               
                 
                
            ]  

            self.dropdown_menu = MDDropdownMenu(  
                caller=button,  
                items=menu_items,  
                width_mult=4,  
            )  
            self.dropdown_menu.open()  

    def item10(self, x):
         self.root.get_screen('cardi').ids.active.text = x 

    def heart_db(self):
        Name = self.root.get_screen('h_scr1').ids.name.text
        Age = self.root.get_screen('h_scr1').ids.age.text
        Gender = self.root.get_screen('h_scr1').ids.drop_item.text
        chest_pain = self.root.get_screen('h_scr1').ids.drop_item1.text
        blood_pressure = self.root.get_screen('h_scr1').ids.bp.text
        cholesterol = self.root.get_screen('h_scr1').ids.cholestrol_level.text
        fbs = self.root.get_screen('h_scr1').ids.drop_item2.text
        rest_ecg = self.root.get_screen('h_scr1').ids.drop_item3.text
        max_heart_rate = self.root.get_screen('h_scr1').ids.heart_rate.text
        exercise_angina = self.root.get_screen('h_scr1').ids.drop_item4.text
        oldpeak = self.root.get_screen('h_scr1').ids.oldpeak.text
        slope = self.root.get_screen('h_scr1').ids.drop_item5.text

        if Name!=''  and Gender != 'Select Gender' and Age!='' and slope != 'ST Slope':
            new_user = DB_heart(name=Name, age=Age, gender = Gender, chest_pain =chest_pain,blood_pressure = blood_pressure,cholestrol = cholesterol, fbs = fbs,restecg = rest_ecg, max_heart_rate =  max_heart_rate, angina = exercise_angina,  oldpeak = oldpeak, slope =  slope )
            session.add(new_user)
            session.commit()
            

            #Prediction of model Here:
            # Sample new data point
            new_data = pd.DataFrame({
                'age': [int(Age)],
                'resting_blood_pressure': [int(blood_pressure)],
                'cholesterol': [int(cholesterol)],
                'fasting_blood_sugar': [int(fbs)],
                'max_heart_rate_achieved': [int(max_heart_rate)],
                'exercise_induced_angina': [int(exercise_angina)],
                'st_depression': [float(oldpeak)],
                'sex': [Gender],
                'chest_pain_type': [chest_pain],
                'rest_ecg': [rest_ecg],
                'st_slope': [slope]
            })

            # Convert categorical features
            new_data['sex_male'] = new_data['sex'].map({'male': 1, 'female': 0})
            new_data['chest_pain_type_atypical angina'] = new_data['chest_pain_type'].map({'atypical angina': 1, 'non-anginal pain': 0, 'typical angina': 0, 'asymptomatic': 0})
            new_data['chest_pain_type_non-anginal pain'] = new_data['chest_pain_type'].map({'atypical angina': 0, 'non-anginal pain': 1, 'typical angina': 0, 'asymptomatic': 0})
            new_data['chest_pain_type_typical angina'] = new_data['chest_pain_type'].map({'atypical angina': 0, 'non-anginal pain': 0, 'typical angina': 1, 'asymptomatic': 0})
            new_data['rest_ecg_left ventricular hypertrophy'] = new_data['rest_ecg'].map({'normal': 0, 'ST-T wave abnormality': 0, 'left ventricular hypertrophy': 1})
            new_data['rest_ecg_normal'] = new_data['rest_ecg'].map({'normal': 1, 'ST-T wave abnormality': 0, 'left ventricular hypertrophy': 0})
            new_data['st_slope_flat'] = new_data['st_slope'].map({'upsloping': 0, 'flat': 1, 'downsloping': 0})
            new_data['st_slope_upsloping'] = new_data['st_slope'].map({'upsloping': 1, 'flat': 0, 'downsloping': 0})

            # Drop the original categorical columns
            new_data = new_data.drop(['sex', 'chest_pain_type', 'rest_ecg', 'st_slope'], axis=1)

            # Ensure the new data includes all required columns
            required_columns = [
                'age', 'resting_blood_pressure', 'cholesterol', 'fasting_blood_sugar',
                'max_heart_rate_achieved', 'exercise_induced_angina', 'st_depression',
                'sex_male', 'chest_pain_type_atypical angina', 'chest_pain_type_non-anginal pain',
                'chest_pain_type_typical angina', 'rest_ecg_left ventricular hypertrophy',
                'rest_ecg_normal', 'st_slope_flat', 'st_slope_upsloping'
            ]

            for col in required_columns:
                if col not in new_data.columns:
                    new_data[col] = 0

            new_data = new_data[required_columns]

            # Convert 0s and 1s to True and False
            for col in ['sex_male', 'chest_pain_type_atypical angina', 'chest_pain_type_non-anginal pain',
                        'chest_pain_type_typical angina', 'rest_ecg_left ventricular hypertrophy',
                        'rest_ecg_normal', 'st_slope_flat', 'st_slope_upsloping']:
                new_data[col] = new_data[col].astype(bool)

            # Assuming the scaler was fitted on the training data

            # Transform the new data
            new_data_scaled = new_data.copy()
            new_data_scaled[['age', 'resting_blood_pressure', 'cholesterol', 'max_heart_rate_achieved', 'st_depression']] = self.scaler.transform(
                new_data[['age', 'resting_blood_pressure', 'cholesterol', 'max_heart_rate_achieved', 'st_depression']]
            )

            predict1 = self.model1.predict(new_data_scaled)
            predict2 = self.model2.predict(new_data_scaled)
            predict3 = self.model3.predict(new_data_scaled)
            predict4 = self.model4.predict(new_data_scaled)

            final_predict = (predict1+predict2+predict3+predict4)/4
            if final_predict > 0.7:
                 self.h = 1
                 z = 'Heart Attack Predict'
                 self.root.get_screen('pred1').ids.heart_lab.text = z
                 self.root.get_screen('pred1').ids.heart_lab.text_color = 1, 0, 0, 1
                 
            else:
                 self.h = 0
                 z = 'No Heart Attack Predict'
                 self.root.get_screen('pred1').ids.heart_lab.text = z
                 self.root.get_screen('pred1').ids.heart_lab.text_color = 0, 1, 0, 1
                 

            plot_widget = self.root.get_screen('pred1').ids.plot_widget
            plot_widget.plot(self.h)
            self.screen.current = 'pred1'

            dialog = MDDialog(
            title="Success",
            text=z,
            size_hint=(0.5, 0.3)
            )
            dialog.open()
           
           
        else:
            dialog = MDDialog(
            title="Warning",
            text="Some Feilds are empty fill them",
            size_hint=(0.5, 0.3)
            )
            dialog.open()


    def cardivascular_dis(self):
        Name = self.root.get_screen('cardi').ids.name.text
        Age = self.root.get_screen('cardi').ids.age.text
        Gender = self.root.get_screen('cardi').ids.drop_item.text
        height = self.root.get_screen('cardi').ids.ht.text
        weight = self.root.get_screen('cardi').ids.wt.text
        Blood_press_hi = self.root.get_screen('cardi').ids.ap_hi.text
        Blood_press_low = self.root.get_screen('cardi').ids.ap_low.text
        chalestrol = self.root.get_screen('cardi').ids.drop_item_car_chales.text
        golucose = self.root.get_screen('cardi').ids.golucose.text
        smoker = self.root.get_screen('cardi').ids.smoke.text
        alcholer = self.root.get_screen('cardi').ids.alcohol.text
        active = self.root.get_screen('cardi').ids.active.text

        if Name!=''  and Gender != 'Select Gender' and Age!='' and active != 'Active':
            # new_user = DB_heart(name=Name, age=Age, gender = Gender, chest_pain =chest_pain,blood_pressure = blood_pressure,cholestrol = cholesterol, fbs = fbs,restecg = rest_ecg, max_heart_rate =  max_heart_rate, angina = exercise_angina,  oldpeak = oldpeak, slope =  slope )
            # session.add(new_user)
            # session.commit()
            if Gender == 'male':
                 g = 1
            else:
                 g = 2


            #Prediction of model Here:
            # Sample new data point
            new_data1 = pd.DataFrame({
                'age': [int(Age)],
                'gender': [int(g)],
                'height': [int(height)],
                'weight': [int(weight)],
                'ap_hi': [int(Blood_press_hi)],
                'ap_lo': [int(Blood_press_low)],
                'cholesterol': [float(chalestrol)],
                'gluc': [int(golucose)],
                'smoke': [int(smoker)],
                'alco': [int(alcholer)],
                'active': [int(active)]
            })

            
           
           
            new_data_scaled1 = new_data1.copy()
            new_data_scaled1[['age', 'height', 'weight', 'ap_hi', 'ap_lo']] = self.scaler_cardio.transform(
                new_data1[['age', 'height', 'weight', 'ap_hi', 'ap_lo']]
            )

            predict5 = self.model5.predict(new_data_scaled1)
            predict6 = self.model6.predict(new_data_scaled1)
            predict7 = self.model7.predict(new_data_scaled1)
            predict8 = self.model8.predict(new_data_scaled1)
            predict9 = self.model9.predict(new_data_scaled1)

            final_predict = (predict5+predict6+predict7+predict8+predict9)/5

       
            if final_predict > 0.7:
                 self.h = 1
                 z = 'Cardivascular Disease Detect'
                 self.root.get_screen('pred1').ids.heart_lab.text = z
                 self.root.get_screen('pred1').ids.heart_lab.text_color = 1, 0, 0, 1
                 self.screen.current = 'pred1'
            else:
                 self.h = 0
                 z = 'No Cardivascular Disease Detect'
                 self.root.get_screen('pred1').ids.heart_lab.text = z
                 self.root.get_screen('pred1').ids.heart_lab.text_color = 0, 1, 0, 1
                 self.screen.current = 'pred1'

            dialog = MDDialog(
            title="Success",
            text=z,
            size_hint=(0.5, 0.3)
            )
            dialog.open()
           
           
        else:
            dialog = MDDialog(
            title="Warning",
            text="Some Feilds are empty fill them",
            size_hint=(0.5, 0.3)
            )
            dialog.open()



    def build(self):
        
        self.screen = Builder.load_string(helper1)
        
################################################ Screen Managers #######################################################################################
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name ='login'))
        sm.add_widget(SignupScreen(name='signup'))
        sm.add_widget(MainScreeen(name='main'))
        sm.add_widget(ForgotScreen(name='forgotpass'))
        sm.add_widget(HistoryScreen(name='history'))
        sm.add_widget(Video_screen(name='video_screen'))
        sm.add_widget(About_us(name='about_us'))
        sm.add_widget(Start_page_UI(name = 'start_page'))
        sm.add_widget(Predict1(name = 'pred1'))
        sm.add_widget(Heart_attack_screen1(name ='h_scr1'))
        sm.add_widget(Cardio_vascular(name = 'cardi'))
        sm.add_widget(Main_screen(name = 'main'))

        self.screen.current = 'start_page'
        
        self.cls = True

       
        
        plot_container = self.screen.get_screen('pred1').ids.plot_container
        plot_widget = MatplotlibWidget(app_instance=self)
        plot_container.add_widget(plot_widget)
        # Save a reference to the plot widget for updating later
        self.screen.get_screen('pred1').ids.plot_widget = plot_widget
        
        return self.screen
    

class CustomFigureCanvasKivyAgg(FigureCanvasKivyAgg):
    def motion_notify_event(self, x, y, guiEvent=None):
        try:
            super().motion_notify_event(x, y, guiEvent)
        except AttributeError:
            pass  # Ignore the error and prevent it from stopping the app

class MatplotlibWidget(Widget):
    def __init__(self, app_instance, **kwargs):
        super().__init__(**kwargs)
        self.app_instance = app_instance  # Store the instance of apps
        self.update()  
        self.orientation = 'horizontal'
        self.canvas_widget = None
        
    def update(self):
         h_value = self.app_instance.h
         self.plot(h_value)
        

    def plot(self,h):
        h_value = h
        # Create a figure and a set of subplots
        
        fig = Figure(figsize=(8, 4))  # Width: 10 inches, Height: 8 inches
        
        # Create multiple subplots in the figure
        axs = fig.subplots(1, 2)  # 1 row, 2 columns for horizontal orientation

        # Sample data for the line plot
        time = np.arange(0, 10, 1)
        if h_value ==1:
            risk_probability = np.sin(time) + np.random.normal(0, 0.1, len(time))
        if h_value == 0:
             risk_probability = np.sin(time) + np.random.normal(0, 0.1, 1)
        
        # First subplot: Risk Probability Over Time (Line plot)
        axs[0].plot(time, risk_probability, 'b-', marker='o')
        axs[0].set_title('Heart Attack Risk Probability Over Time')
        axs[0].set_xlabel('Time')
        axs[0].set_ylabel('Risk Probability')
        axs[0].grid(True)

        # Sample data for the pie chart
        labels = ['Low Risk', 'Moderate Risk', 'High Risk']
        print(h_value)
        if h_value == 1:
            sizes = [10, 70, 20]  # Example percentages
            colors = ['green', 'orange', 'red']
            explode = (0, 0.1, 0.1)  # Explode the second and third slices
            print('if')
        else:
            sizes = [80, 10, 10]  # Example percentages
            colors = ['green', 'orange', 'red']
            explode = (0, 0.1, 0.1)  # Explode the second and third slices
    
       

        # Second subplot: Risk Distribution (Pie chart)
        axs[1].pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
        axs[1].set_title('Heart Attack Risk Distribution')

        # Add the canvas to the widget
        canvas = CustomFigureCanvasKivyAgg(fig) 
        canvas.draw()
        self.add_widget(canvas)
    
apps().run()