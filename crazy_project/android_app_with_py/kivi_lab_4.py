import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


#make class "MyGrid" from 'GridLayout' function.

class MyGrid(GridLayout):

    # define something????

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        #deine how many colum

        self.cols = 1

        #define 'GridLayout' as "inside" varieble.

        self.inside = GridLayout()

        #deine how many colum in  varieble "inside".

        self.inside.cols = 1

        #create label by add_widget function.

        self.inside.add_widget(Label(text="This app made by mr.guy thongtrachoo "))
        self.inside.add_widget(Label(text="mr.guy thongtrachoo is handsome"))


        self.solution = TextInput(multiline=False)
        self.add_widget(self.solution)


        #admit to insert add_widget to inside

        self.add_widget(self.inside)

        # create button by define 'submit' varieble to get Button function.

        self.submit = Button(text="Yes mr.guy is handsome.", font_size=20)

        #define what would happen if button 'submit' was pressed.
        self.submit.bind(on_press=self.pressed) #<-- here is function.

        #admit to confirm submit varieble to be add_widget function (add_widget is like a output in this module'kivi')

        self.add_widget(self.submit)

        # the same as upper.

        self.submit2 = Button(text="No he is just attractive.", font_size=20)
        self.submit2.bind(on_press=self.pressed2)

        # the same as upper

        self.add_widget(self.submit2)



    #define function when the button was pressed.

    def pressed(self, instance):

        print("my dick is big ass well")
        self.solution.text = "mr.guy thongtrachoo"


    def pressed2(self, instance):

        print("my dick is big ass well555555555")
        
        self.solution.text = ""
  


# create class MyApp to receive everything in class MyGrid.

class MyApp(App):
    def build(self):
        return MyGrid()


# run app if ----- if __name__ == "__main__":

if __name__ == "__main__":
    MyApp().run()
