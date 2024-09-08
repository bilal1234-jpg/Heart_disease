helper1 = '''


ScreenManager:
    Main_screen:
    LoginScreen:
    SignupScreen:
    Start_page_UI:
    Predict1:
    Heart_attack_screen1:
    Cardio_vascular:
    Predict2:



<Main_screen>:
    name: "main"
    BoxLayout:
        orientation: 'vertical'
        padding: dp(50)  
        spacing: dp(20) 

        MDSmartTile:
            radius: 24
            box_radius: [0, 0, 24, 24]
            box_color: 1, 1, 1, .2
            source: "logo-2.jpg"
            pos_hint: {"center_x": .5, "center_y": .5}
            size_hint: None, None
            size: "320dp", "320dp"

        

        MDRectangleFlatIconButton:
            text: "Heart Attack Predictor"
            icon: "heart-cog"
            text_color: "black"
            icon_color: "red"
            font_size: "18sp"
            width: '70'
            md_bg_color: '#44c0f0'
            pos_hint: {'center_x': 0.5,'center_y': 0.5 }
            on_release: root.manager.current = 'h_scr1'
        
        MDRectangleFlatIconButton:
            text: "Cardivascular Disease Predictor"
            icon: "heart-pulse"
            text_color: "black"
            icon_color: "red"
            font_size: "18sp"
            md_bg_color: '#44c0f0'
            pos_hint: {'center_x': 0.5,'center_y': 0.4 }
            on_release: root.manager.current = 'cardi'

<Start_page_UI>:
    name: 'start_page'

<Heart_attack_screen1>:
    name: 'h_scr1'
    BoxLayout:
        orientation: 'vertical'
        padding: dp(50)  
        spacing: dp(20) 
        pos_hint: {'center_x': 0.5}


        BoxLayout:
            orientation: 'horizontal'
            spacing: dp(20)

            MDIconButton:
                icon: "arrow-left"
                on_release: root.manager.current = 'main'
                pos_hint: {'center_y': 0.9}

            MDLabel:
                halign: "center"
                text: "Heart Attack Predictor"
                bold: True
                font_size: '24sp'
                pos_hint: {'center_y': 0.9}

          
            

        BoxLayout:
            orientation: 'horizontal'
            padding: dp(5)  
            spacing: dp(50) 
            pos_hint: {'center_x': 0.5}

            MDTextField:
                id: name
                hint_text: 'Enter Name'
                #mode: "rectangle"
                size_hint_x: 0.1
                width: 250
                line_color_focus: "red"
                hint_text_color_focus: "red"

            MDTextField:
                id: age
                hint_text: 'Enter Age'
                #mode: "rectangle"
                size_hint_x: 0.1
                width: 250
                line_color_focus: "red"
                hint_text_color_focus: "red"

            MDDropDownItem:
                id: drop_item
                text: 'Select Gender'  
                size_hint_x: 0.1
                on_release: app.show_dropdown(self) 

            

        BoxLayout:
            orientation: 'horizontal'
            padding: dp(5)  
            spacing: dp(50) 
            pos_hint: {'center_x': 0.5}

            MDDropDownItem:
                id: drop_item1
                text: 'Chest Pain Type'  
                size_hint_x: 0.1
                on_release: app.show_dropdown1(self) 
            
            MDTextField:
                id: bp
                hint_text: 'Enter Blood Pressure'
                #mode: "rectangle"
                size_hint_x: 0.1
                width: 250
                line_color_focus: "red"
                hint_text_color_focus: "red"

            MDTextField:
                id: cholestrol_level
                hint_text: 'Enter cholestrol'
                #mode: "rectangle"
                size_hint_x: 0.1
                width: 250
                line_color_focus: "red"
                hint_text_color_focus: "red"

        BoxLayout:
            orientation: 'horizontal'
            padding: dp(5)  
            spacing: dp(50) 
            pos_hint: {'center_x': 0.5}

            MDDropDownItem:
                id: drop_item2
                text: 'fasting blood sugar'  
                size_hint_x: 0.1
                on_release: app.show_dropdown2(self)

            MDDropDownItem:
                id: drop_item3
                text: 'resting ecg'  
                size_hint_x: 0.1
                on_release: app.show_dropdown3(self) 
            
            MDTextField:
                id: heart_rate
                hint_text: 'Enter max heart rate'
                #mode: "rectangle"
                size_hint_x: 0.1
                width: 250
                line_color_focus: "red"
                hint_text_color_focus: "red"
                


        BoxLayout:
            orientation: 'horizontal'
            padding: dp(5)  
            spacing: dp(50)  
            pos_hint: {'center_x': 0.5}
                
            MDDropDownItem:
                id: drop_item4
                text: 'exercise angina'  
                size_hint_x: 0.1
                on_release: app.show_dropdown4(self) 

            MDTextField:
                id: oldpeak
                hint_text: 'Enter Old Peak'
                #mode: "rectangle"
                size_hint_x: 0.1
                width: 250
                line_color_focus: "red"
                hint_text_color_focus: "red"

            MDDropDownItem:
                id: drop_item5
                text: 'ST Slope'  
                size_hint_x: 0.1
                on_release: app.show_dropdown5(self) 

        MDRaisedButton:
            text: "Submit"
            size_hint: 0.2, 0.1
            width: dp(100)
            pos_hint:{'center_x':0.5}
            on_release: app.heart_db()
                   
            
            
        
<Predict1>:
    name: 'pred1'
    FloatLayout:
      
        MDIconButton:
            icon: "keyboard-backspace"
            pos_hint: {'center_x': 0.1, 'center_y':0.9}
            on_release: root.manager.current = 'h_scr1'

        MDLabel:
            id: heart_lab
            text: "No Heart Attack Detected"
            bold: True
            font_size: '34sp'
            pos_hint: {'center_x': 0.78, 'center_y':0.9}
            theme_text_color: "Custom"
            text_color: 0, 1, 0, 1

        BoxLayout:
            id: plot_container
            canvas.before:
                Rectangle:
                    pos: self.pos
                    size: self.size

<Cardio_vascular>:

    name:'cardi'
    ScrollView:
        BoxLayout:
            orientation: 'vertical'
            padding: dp(50)  
            spacing: dp(20) 
            pos_hint: {'center_x': 0.5}

            BoxLayout:
                orientation: 'horizontal'
                spacing: dp(20)

                MDIconButton:
                    icon: "arrow-left"
                    on_release: root.manager.current = 'main'
                    pos_hint: {'center_y': 0.9}

                MDLabel:
                    halign: "center"
                    text: "Cardivascular Heart Disease Predictor"
                    bold: True
                    font_size: '24sp'
                    pos_hint: {'center_y': 0.9}


                

            BoxLayout:
                orientation: 'horizontal'
                padding: dp(5)  
                spacing: dp(50) 
                pos_hint: {'center_x': 0.5}

                MDTextField:
                    id: name
                    hint_text: 'Enter Name'
                    #mode: "rectangle"
                    size_hint_x: 0.1
                    width: 250
                    line_color_focus: "red"
                    hint_text_color_focus: "red"

                MDTextField:
                    id: age
                    hint_text: 'Enter Age'
                    #mode: "rectangle"
                    size_hint_x: 0.1
                    width: 250
                    line_color_focus: "red"
                    hint_text_color_focus: "red"

                MDDropDownItem:
                    id: drop_item
                    text: 'Select Gender'  
                    size_hint_x: 0.1
                    on_release: app.show_dropdown(self) 

                

            BoxLayout:
                orientation: 'horizontal'
                padding: dp(5)  
                spacing: dp(50) 
                pos_hint: {'center_x': 0.5}

                MDTextField:
                    id: ht
                    hint_text: 'Enter Height'
                    #mode: "rectangle"
                    size_hint_x: 0.1
                    width: 250
                    helper_text: "Height should be in Foot"
                    helper_text_mode: "on_focus"
                    line_color_focus: "red"
                    hint_text_color_focus: "red"

                
                MDTextField:
                    id: wt
                    hint_text: 'Enter Weight'
                    #mode: "rectangle"
                    size_hint_x: 0.1
                    width: 250
                    helper_text: "Weight should be in Kg"
                    helper_text_mode: "on_focus"
                    line_color_focus: "red"
                    hint_text_color_focus: "red"

                MDTextField:
                    id: ap_hi
                    hint_text: 'Enter Blood Pressure High'
                    #mode: "rectangle"
                    size_hint_x: 0.1
                    width: 250
                    line_color_focus: "red"
                    hint_text_color_focus: "red"

            BoxLayout:
                orientation: 'horizontal'
                padding: dp(5)  
                spacing: dp(50) 
                pos_hint: {'center_x': 0.5}

                MDTextField:
                    id: ap_low
                    hint_text: 'Enter Blood Pressure Low'
                    #mode: "rectangle"
                    size_hint_x: 0.1
                    width: 250
                    line_color_focus: "red"
                    hint_text_color_focus: "red"

                MDDropDownItem:
                    id: drop_item_car_chales
                    text: 'Chalestrol Level'  
                    size_hint_x: 0.1
                    on_release: app.drop_item_car_chale(self) 
                
                MDTextField:
                    id: gluco_level
                    hint_text: 'Enter Golucose Level'
                    size_hint_x: 0.1
                    width: 250
                    line_color_focus: "red"
                    hint_text_color_focus: "red"
                    helper_text_mode: "on_focus"
                    helper_text: "fill it and maximum golucose can be 400"
                    on_text: app.card_display()

                    
                    


            BoxLayout:
                orientation: 'horizontal'
                padding: dp(5)  
                spacing: dp(50)  
                pos_hint: {'center_x': 0.5}
                    
                MDDropDownItem:
                    id: smoke
                    text: 'Smoke test'  
                    size_hint_x: 0.1
                    on_release: app.smoker(self) 

                MDDropDownItem:
                    id: alcohol
                    text: 'Alcohol test'  
                    size_hint_x: 0.1
                    on_release: app.Acholer(self) 

                MDDropDownItem:
                    id: active
                    text: 'Physical activity'  
                    size_hint_x: 0.1
                    on_release: app.active(self) 

            BoxLayout:
                orientation: 'horizontal'
                padding: dp(5)  
                spacing: dp(50)  
                pos_hint: {'center_x': 0.5}
               

                MDDropDownItem:
                    id: hyper
                    text: 'Hypertension'  
                    size_hint_x: 0.1
                    on_release: app.hypertension(self) 
                
                MDDropDownItem:
                    id: heart_dis
                    text: 'Heart Disease'  
                    size_hint_x: 0.1
                    on_release: app.heart_dis(self)

    
                MDTextField:
                    id: bmi
                    hint_text: 'BMI'
                    size_hint_x: 0.04
                    width: 250
                    line_color_focus: "red"
                    hint_text_color_focus: "red"
                    pos_hint: {'center_y': 0.5} 

                MDIconButton:
                    icon: "calculator"
                    pos_hint: {"center_y": .5}
                    theme_text_color: "Hint"
                    on_release:app.bmi()

            BoxLayout:
                orientation: 'horizontal'
                padding: dp(5)  
                spacing: dp(50)  
                pos_hint: {'center_x': 0.5}

                MDDropDownItem:
                    id: work
                    text: 'Work Type'  
                    size_hint_x: 0.1
                    on_release: app.work(self)

                MDDropDownItem:
                    id: married
                    text: 'Ever Married'  
                    size_hint_x: 0.1
                    on_release: app.married(self)

                MDDropDownItem:
                    id: residence
                    text: 'Residence Type'  
                    size_hint_x: 0.1
                    on_release: app.residence(self)
                
                

            MDRaisedButton:
                text: "Submit"
                size_hint: 0.2, 0.1
                width: dp(100)
                pos_hint:{'center_x':0.5}
                on_release: app.cardivascular_dis()

<Predict2>:
    name: 'pred2'
    FloatLayout:
      
        MDIconButton:
            icon: "keyboard-backspace"
            pos_hint: {'center_x': 0.1, 'center_y':0.9}
            on_release: root.manager.current = 'cardi'

        MDLabel:
            id: heart_lab
            text: "No Cardivascular Attack Detected"
            bold: True
            font_size: '34sp'
            pos_hint: {'center_x': 0.78, 'center_y':0.9}
            theme_text_color: "Custom"
            text_color: 0, 1, 0, 1

        MDLabel:
            id: heart_stroke
            text: "No Heart stroke disease detected"
            bold: True
            font_size: '34sp'
            pos_hint: {'center_x': 0.78, 'center_y':0.10}
            theme_text_color: "Custom"
            text_color: 0, 1, 0, 1

        BoxLayout:
            id: plot_container
            canvas.before:
                Rectangle:
                    pos: self.pos
                    size: self.size

    '''