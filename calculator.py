from dataclasses import replace
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.lang.builder import Builder
from time import sleep
import re


Builder.load_file('./calculator.kv')
Window.size = (350, 550)
a = 0
class CalculatorWidget(Widget):
    def clear(self):
        self.ids.input_box.text = '0'

    def button_value(self, number):
        prev_num = self.ids.input_box.text

        if prev_num == '0':
            self.ids.input_box.text = ''
            r = self.ids.input_box.text = f'{number}'
        elif 'Error =/' in prev_num:
            sleep(1)
            self.ids.input_box.text = '0'
        else:
            r = self.ids.input_box.text = f'{prev_num}{number}'

    def signs(self, sign):
        prev_num = self.ids.input_box.text
        if self.ids.input_box.text[-1] == '*':
            self.ids.input_box.text = self.ids.input_box.text
        elif self.ids.input_box.text[-1] == '/':
            self.ids.input_box.text = self.ids.input_box.text
        elif self.ids.input_box.text[-1] == '-':
            self.ids.input_box.text = self.ids.input_box.text
        elif self.ids.input_box.text[-1] == '+':
            self.ids.input_box.text = self.ids.input_box.text
        else:
            self.ids.input_box.text = f'{prev_num}{sign}'

    def remove_last(self):
        prev_num = self.ids.input_box.text
        prev_num = prev_num[:-1]
        self.ids.input_box.text = f'{prev_num}'

    def result(self):
        prev_num = self.ids.input_box.text
        try:
            result = eval(prev_num)
            self.ids.input_box.text = f'{result}'
        except:
            self.ids.input_box.text = 'Error =/'
    
    def positive_negative(self):
        prev_num = self.ids.input_box.text

        if '-' in self.ids.input_box.text:
            self.ids.input_box.text = f"{prev_num.replace('-', '')}"
        else:
            self.ids.input_box.text = f'-{prev_num}'
    
    def dot(self):
        prev_num = self.ids.input_box.text
        num_list = re.split("\+|-|/|\*|%", prev_num)

        if ('+' in prev_num or '-' in prev_num or '*' in prev_num or '/' in prev_num or '%' in prev_num) and '.' not in num_list[-1]:
            prev_num = f'{prev_num}.'
            self.ids.input_box.text = prev_num


        elif '.' in prev_num:
            pass
        else:
            prev_num = f'{prev_num}.'
            self.ids.input_box.text = prev_num

            

class CalculatorApp(App):
    def build(self):
        return CalculatorWidget()

if __name__ == '__main__':
    CalculatorApp().run()