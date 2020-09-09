import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside2 = GridLayout()
        self.inside.cols = 1
        self.inside2.cols = 2

        self.inside.add_widget(Label(text=""))
        self.inside.add_widget(Label(text="BMI BUDDY", font_size=50))
        self.inside.add_widget(Label(text=""))

        self.inside.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Height: CM."))
        self.height1 = TextInput(multiline=False)
        self.inside.add_widget(self.height1)

        self.inside.add_widget(Label(text="Weight: KG."))
        self.weight = TextInput(multiline=False)
        self.inside.add_widget(self.weight)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

        self.solution = TextInput(multiline=True, font_size=30)
        self.add_widget(self.solution)


        self.inside2.add_widget(Label(text="Made by Mr.guy thongtrachoo ", font_size=15))

        #self.submit2 = Button(text="Exit", font_size=15)
        #self.submit2.bind(on_press=self.pressed2)
        #self.add_widget(self.submit2)

        self.add_widget(self.inside2)

    def pressed(self, instance):
        name = self.name.text
        height1 = self.height1.text
        height1_int = int(height1)
        weight = self.weight.text
        weight_int = int(weight)

        if height1_int > 90:
          height1_int = height1_int/100

        bmi_process = height1_int * height1_int
        bmi = weight_int / bmi_process

        if bmi < 18.5:
           explain = ("UNDER WEIGHT")
        if bmi >= 18.5 and bmi <= 22.9:
           explain = ("FIT n FIRM")
        if bmi >= 23.0 and bmi <= 24.9:
           explain = ("OVER WEIGHT")
        if bmi >= 25.0 and bmi <= 29.9:
           explain = ("FAT")
        if bmi > 30:
           explain = ("FUCKING FAT")

        print("Name:", name, "Height:", height1, "Weight:", weight)
        print("BMI : ",bmi)
        print(explain)
     
        self.name.text = ""
        self.height1.text = ""
        self.weight.text = ""

        all_res_v2 = "Name:  "+ name +" "+ "Height:  "+ height1+" CM. "+ "Weight:  "+ weight +" KG. "+"Result:  "+explain

        self.solution.text = all_res_v2

    #def pressed2(self, instance):
    #    print("Exit")
    #    MyApp().stop()

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()