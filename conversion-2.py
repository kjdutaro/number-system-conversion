import tkinter as tk
from tkinter import ttk

def from_binary(to_type, value):
    try:
        value = int(value, 2)
        if to_type == 'Octal':
            return oct(value)[2:]
        elif to_type == 'Decimal':
            return str(value)
        elif to_type == 'Hexadecimal':
            return hex(value)[2:]
    except ValueError as e:
        return f"Invalid input. {str(e)}"
    
def from_octal(to_type, value):
    try:
        value = int(value, 8)
        if to_type == 'Binary':
            return bin(value)[2:]
        elif to_type == 'Decimal':
            return str(value)
        elif to_type == 'Hexadecimal':
            return hex(value)[2:]
    except ValueError as e:
        return f"Invalid input. {str(e)}"
    
def from_decimal(to_type, value):
    try:
        value = int(value, 10)
        if to_type == 'Binary':
            return bin(value)[2:]
        elif to_type == 'Octal':
            return oct(value)[2:]
        elif to_type == 'Hexadecimal':
            return hex(value)[2:]
    except ValueError as e:
        return f"Invalid input. {str(e)}"
    
def from_hexadecimal(to_type, value):
    try:
        value = int(value, 16)
        if to_type == 'Binary':
            return oct(value)[2:]
        elif to_type == 'Octal':
            return oct(value)[2:]
        elif to_type == 'Decimal':
            return str(value)
    except ValueError as e:
        return f"Invalid input. {str(e)}"

def on_convert():
    from_type = from_var.get()
    value = value_entry.get()
    
    if from_type == 'Binary':
        result_1 = from_binary('Octal', value)
        result_2 = from_binary('Decimal', value)
        result_3 = from_binary('Hexadecimal', value)
        
        result_label_1.config(text=f"Octal: {result_1}")
        result_label_2.config(text=f"Decimal: {result_2}")
        result_label_3.config(text=f"Hexadecimal: {result_3}")
        
    elif from_type == 'Octal':
        result_1 = from_octal('Binary', value)
        result_2 = from_octal('Decimal', value)
        result_3 = from_octal('Hexadecimal', value)
        
        result_label_1.config(text=f"Binary: {result_1}")
        result_label_2.config(text=f"Decimal: {result_2}")
        result_label_3.config(text=f"Hexadecimal: {result_3}")
        
    elif from_type == 'Decimal':
        result_1 = from_decimal('Binary', value)
        result_2 = from_decimal('Octal', value)
        result_3 = from_decimal('Hexadecimal', value)
        
        result_label_1.config(text=f"Binary: {result_1}")
        result_label_2.config(text=f"Octal: {result_2}")
        result_label_3.config(text=f"Hexadecimal: {result_3}")

    elif from_type == 'Hexadecimal':
        result_1 = from_hexadecimal('Binary', value)
        result_2 = from_hexadecimal('Octal', value)
        result_3 = from_hexadecimal('Decimal', value)
        
        result_label_1.config(text=f"Binary: {result_1}")
        result_label_2.config(text=f"Octal: {result_2}")
        result_label_3.config(text=f"Decimal: {result_3}")


window = tk.Tk()
window.title("Number System Converter")

from_var = tk.StringVar()
to_var = tk.StringVar()

from_label = tk.Label(window, text="From:")
from_label.grid(row=0, column=0, padx=10, pady=10)

from_dropdown = ttk.Combobox(window, textvariable=from_var, values=['Binary', 'Octal', 'Decimal', 'Hexadecimal'])
from_dropdown.grid(row=0, column=1, padx=10, pady=10)

value_label = tk.Label(window, text="Enter value:")
value_label.grid(row=2, column=0, padx=10, pady=10)

value_entry = tk.Entry(window)
value_entry.grid(row=2, column=1, padx=10, pady=10)

convert_button = tk.Button(window, text="Convert", command=on_convert)
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(window, text="RESULTS")
result_label.grid(row=4, column=0, columnspan=2, pady=5)

result_label_1 = tk.Label(window)
result_label_1.grid(row=5, column=0, columnspan=2, pady=0)

result_label_2 = tk.Label(window)
result_label_2.grid(row=6, column=0, columnspan=2, pady=0)

result_label_3 = tk.Label(window)
result_label_3.grid(row=7, column=0, columnspan=2, pady=0)


window.mainloop()
