from tkinter import *

SIZE_BUTTON_FONT = 40

class Counting_operation:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('300x500')
        self.root.resizable(0, 0)
        self.root.title('Calculator')

        self.frame_for_label = self.create_display_frame()
        self.container_extra_text = ''
        self.container_main_text = ''
        self.extra_text = self.create_extra_text()
        self.main_text = self.create_main_output()
        self.buttons_area = self.create_buttons_zone()
        self.del_button()
        self.number_buttons()
        self.simbol_buttons()

        for x in range(1, 5):
            self.buttons_area.rowconfigure(x, weight =1)
            self.buttons_area.columnconfigure(x, weight =1)



    def create_display_frame(self):
        frame = Frame(self.root, height=221)
        frame.pack(expand=True,
                   fill="both")  # создал единую область фрейм для двух виджетов, то есть для двух надписей label
        return frame

    def create_extra_text(self):
        extra_text = Label(self.frame_for_label, text=self.container_extra_text, font=('SimSun', 30), bg='light gray',
                           fg='black', anchor=E)
        # extra_text.place(width = 350, height = 50)
        extra_text.pack(expand=True, fill='both')
        return extra_text

    def create_main_output(self):
        main_text = Label(self.frame_for_label, text=self.container_main_text, font=('SimSun', 60), fg='black', anchor=E)
        # main_text.place(width = 350 , height = 100)9
        main_text.pack(expand=True, fill='both')
        return main_text

    def create_buttons_zone(self):
        frame_buttons = Frame(self.root)
        frame_buttons.pack(expand=True, fill='both')
        return frame_buttons

    def del_button(self):
        delete = Button(self.buttons_area, text='delete', font=('Simsun', SIZE_BUTTON_FONT), fg='black', bg='gray',
                        command=self.button_delete)
        delete.grid(row=0, column=0, columnspan=3)

    def number_buttons(self):
        numbers_dict = {'7': (1, 0),
                        '8': (1, 1),
                        '9': (1, 2),
                        '4': (2, 0),
                        '5': (2, 1),
                        '6': (2, 2),
                        '1': (3, 0),
                        '2': (3, 1),
                        '3': (3, 2)}
        for key, value in numbers_dict.items():  # items метод, позволяющий получить массив данных, состоящий из кортежей, в которых нулевой эелемент - это ключ, первый - значение
            number_button = Button(self.buttons_area, text=key, font=('Simsun', SIZE_BUTTON_FONT), fg='black', bg='tomato',
                                   command=lambda x=key: self.press_show_big_display(x))  # START HERE command = )
            number_button.grid(row=value[0], column=value[1])
        zero = Button(self.buttons_area, text='0', font=('Simsun', SIZE_BUTTON_FONT), fg='black', bg='tomato',
                      command=lambda x='0': self.press_show_big_display(x))
        zero.grid(row=4, column=0, sticky=NSEW, columnspan=2)
        comma_button = Button(self.buttons_area, text=',', font=('Simsun', SIZE_BUTTON_FONT), fg='black', bg='tomato',
                              command=lambda x='.': self.press_show_big_display(x))
        comma_button.grid(row=4, column=2)

    def simbol_buttons(self):
        simbol_dict = {"\u00F7": (0, 3),
                       '\u00D7': (1, 3),
                       '–': (2, 3),
                       '+': (3, 3),
                       '=': (4, 3)}
        for key, value in simbol_dict.items():
            simbol_button = Button(self.buttons_area, text=key, font=('Simsun', SIZE_BUTTON_FONT), fg='black', bg='salmon',
                                   command=lambda x=key: self.press_symbol(x))
            simbol_button.grid(row=value[0], column=value[1], sticky=NSEW)


    def press_show_big_display(self, button_value):
        if button_value == '.' and '.' not in self.container_main_text:
            self.container_main_text += button_value
            self.main_text.configure(text=self.container_main_text)
        elif button_value != '.':
            self.container_main_text += button_value
            self.main_text.configure(text=self.container_main_text)

    def press_symbol(self, button_value):
        print(button_value)
        if button_value == '=':
            self.container_extra_text += self.container_main_text
            self.container_extra_text = self.container_extra_text.replace('\u00F7', '/')
            self.container_extra_text = self.container_extra_text.replace('\u00D7', '*')
            self.container_extra_text = self.container_extra_text.replace('–', '-')
            try:
                print(eval(self.container_extra_text))
                self.container_main_text = str(eval(self.container_extra_text))
                self.container_extra_text = ""
            except:
                self.container_main_text = "Error"
                self.container_extra_text = ""
            finally:
                self.main_text.configure(text=self.container_main_text)
                self.extra_text.configure(text=self.container_extra_text)
                # self.container_main_text = ''
        elif len(self.container_main_text) == 0:
            self.container_extra_text = self.container_extra_text[:-1] + button_value
        else:
            self.container_extra_text += self.container_main_text + button_value
            self.container_main_text = ''

        self.main_text.configure(text=self.container_main_text)
        self.extra_text.configure(text=self.container_extra_text)

    def button_delete(self):
        self.container_main_text = ''
        self.container_extra_text = ''
        self.main_text.configure(text=self.container_main_text)
        self.extra_text.configure(text=self.container_extra_text)

    def keep_working(self):
        self.root.mainloop()


calc = Counting_operation()
calc.keep_working()
