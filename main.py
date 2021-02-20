
import kivy
from kivy.app import App


from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
#from kivy.uix.gridlayout import GridLayout
#from kivy.uix.textinput import TextInput
#from kivy.uix.button import Button
# our class has to inherit from Widget
from kivy.properties import ObjectProperty
from kivy.properties import NumericProperty

class MyLayout(Widget):
    #ddmm = NumericProperty()
    #dmm = NumericProperty()
    #input_type='number'
    def calcular(self, ddmm, dmm, nespiras, pasointerior):
        #self.ids.knmm.text = (self.ddmm)'+'(self.dmm)
        ddmmaux = self.ids.ddmm.text
        dmmaux=self.ids.dmm.text
        nespirasaux=self.ids.nespiras.text
        pasointerioraux=self.ids.pasointerior.text
        ddmasd = f'{ddmmaux}+{dmmaux}+{nespirasaux}+{pasointerioraux}'
        #print(ddmasd)
        #separamos los números
        if "+" in ddmasd:
            num_list=ddmasd.split("+")
            ddmm_def=float(num_list[0])
            dmm_def = float(num_list[1])
            nespiras_def = float(num_list[2])
            pasointerior_def = float(num_list[3])
            knmm_def=(81400*(dmm_def*dmm_def*dmm_def*dmm_def))/(8*((ddmm_def-dmm_def)*(ddmm_def-dmm_def)*(ddmm_def-dmm_def))*nespiras_def)
            klbinch_def=knmm_def*25.4/4.45
            maxcompmm_def=pasointerior_def*(nespiras_def-1)
            #print(knmm_def)
            #print(maxcompmm_def)
            self.ids.knmm.text=str(knmm_def)
            self.ids.klbinch.text=str(klbinch_def)
            self.ids.maxcompmm.text=str(maxcompmm_def)

        return self.ids.knmm.text

class jbscalckApp(App):


    def build(self):
        return MyLayout()
        #return FloatLayout()


if __name__ == "__main__":
    jbscalckApp().run()