import tkinter as tk
from tkinter import ttk

def convert(from_type, to_type, value):
    try:
        if to_type == 'Decimal':
            if from_type == 'Binary':
                value = int(value, 2)
            elif from_type == 'Octal':
                value = int(value, 8)
            elif from_type == 'Hexadecimal':
                value = int(value, 16)
            return str(value)
        
        
        if to_type == 'Binary':
            if from_type == 'Octal':
                value = int(value, 8)
            if from_type == 'Decimal':
                value = int(value, 10)
            if from_type == 'Hexadecimal':
                value = int(value, 16)
            return bin(value)[2:]
        elif to_type == 'Octal':
            if from_type == 'Binary':
                value = int(value, 2)
            if from_type == 'Decimal':
                value = int(value, 10)
            if from_type == 'Hexadecimal':
                value = int(value, 16)
            return oct(value)[2:]
        elif to_type == 'Hexadecimal':
            if from_type == 'Binary':
                value = int(value, 2)
            if from_type == 'Decimal':
                value = int(value, 10)
            if from_type == 'Octal':
                value = int(value, 8)
            return hex(value)[2:]
    except ValueError as e:
        return f"Invalid input. {str(e)}"


def on_convert():
    from_type = from_var.get()
    to_type = to_var.get()
    value = value_entry.get()
    result = convert(from_type, to_type, value)
    result_label.config(text=f"Result: {result}")


window = tk.Tk()
window.title("Number System Converter")

from_var = tk.StringVar()
to_var = tk.StringVar()

from_label = tk.Label(window, text="From:")
from_label.grid(row=0, column=0, padx=10, pady=10)

from_dropdown = ttk.Combobox(window, textvariable=from_var, values=['Binary', 'Octal', 'Decimal', 'Hexadecimal'])
from_dropdown.grid(row=0, column=1, padx=10, pady=10)

to_label = tk.Label(window, text="To:")
to_label.grid(row=1, column=0, padx=10, pady=10)

to_dropdown = ttk.Combobox(window, textvariable=to_var, values=['Binary', 'Octal', 'Decimal', 'Hexadecimal'])
to_dropdown.grid(row=1, column=1, padx=10, pady=10)

value_label = tk.Label(window, text="Enter value:")
value_label.grid(row=2, column=0, padx=10, pady=10)

value_entry = tk.Entry(window)
value_entry.grid(row=2, column=1, padx=10, pady=10)

convert_button = tk.Button(window, text="Convert", command=on_convert)
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(window, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

window.mainloop()
