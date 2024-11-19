import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Hesap Makinesi")
        self.root.geometry("300x400")
        self.root.configure(bg='#f0f0f0')

        # Sonuç ekranı
        self.result_var = tk.StringVar(value="0")
        self.display = ttk.Entry(
            root, 
            textvariable=self.result_var, 
            justify="right",
            font=('Arial', 24)
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

        # Hesaplama için değişkenler
        self.current_number = "0"
        self.previous_number = ""
        self.operation = ""
        self.start_new_number = True

        # Butonları oluştur
        self.create_buttons()

        # Grid yapılandırması
        for i in range(6):  
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

    def create_buttons(self):
        button_data = [
            ('C', 1, 0), ('/', 1, 1), ('*', 1, 2), ('-', 1, 3),  
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('+', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('+', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3),
        ]

        # Tüm butonlar
        for (text, row, col) in button_data:
            btn = ttk.Button(
                self.root,
                text=text,
                command=lambda t=text: self.button_click(t)
            )
            btn.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")

    def button_click(self, value):
        if value.isdigit() or value == '.':
            if self.start_new_number:
                self.current_number = value
                self.start_new_number = False
            else:
                self.current_number += value
            self.result_var.set(self.current_number)
        
        elif value in ['+', '-', '*', '/']:
            self.previous_number = self.current_number
            self.operation = value
            self.start_new_number = True
        
        elif value == '=':
            if self.previous_number and self.operation:
                try:
                    result = eval(f"{self.previous_number}{self.operation}{self.current_number}")
                    self.result_var.set(result)
                    self.current_number = str(result)
                except ZeroDivisionError:
                    self.result_var.set("Hata!")
                except:
                    self.result_var.set("Hata!")
                self.previous_number = ""
                self.operation = ""
                self.start_new_number = True

        elif value == 'C':
            self.current_number = "0"
            self.previous_number = ""
            self.operation = ""
            self.start_new_number = True
            self.result_var.set("0")

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
