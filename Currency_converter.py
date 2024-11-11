from tkinter import *
from tkinter.messagebox import showerror, showwarning, showinfo, askyesno
from tkinter import ttk
from currency_converter import CurrencyConverter

# Create main GUI window
gui = Tk()
gui.title("Currency Converter")
gui.geometry("1920x1080")
gui.configure(bg="#242424")

# Initialize currency converter
c = CurrencyConverter()

# Function to convert currency
def convert_currency():
    try:
        amount = float(entry.get())
        from_currency = combo.get()
        to_currency = combo2.get()
        converted_amount = c.convert(amount, from_currency, to_currency)
        
        result_entry.config(state=NORMAL)
        result_entry.delete(0, END)
        result_entry.insert(0, f"{converted_amount:.2f}")
        result_entry.config(state=DISABLED)
    except Exception as e:
        showerror("Conversion Error", str(e))

# Function to close the application
def ds():
    gui.destroy()

# Main heading
heading = Label(gui, text="Welcome To Currency Converter", font=("calibri", 75, 'bold'), bg="#242424", fg="#FFFFFF")
heading.place(relx=.05, rely=.03)

# Inner Frame
dataframe = Frame(gui, bg="black", relief=RAISED, bd=10)
dataframe.place(relx=0.19, rely=0.23, relwidth=0.60, relheight=.55)

# Labels
texts = Label(dataframe, text="Currency From", font=("Courier", 25, "bold"), bg="black", fg="skyblue")
texts.place(relx=.02, rely=.15)

texts2 = Label(dataframe, text="Currency To", font=("Courier", 25, "bold"), bg="black", fg="skyblue")
texts2.place(relx=.02, rely=.35)

texts3 = Label(dataframe, text="Amount", font=("Courier", 25, "bold"), bg="black", fg="skyblue")
texts3.place(relx=.02, rely=.55)

# Currency options for the Combobox
options = [
    "USD",  # United States Dollar
    "EUR",  # Euro
    "GBP",  # British Pound
    "INR",  # Indian Rupee
    "JPY",  # Japanese Yen
    "AUD",  # Australian Dollar
    "CAD",  # Canadian Dollar
    "CHF",  # Swiss Franc
    "CNY",  # Chinese Yuan
    "NZD",  # New Zealand Dollar
    "SGD"   # Singapore Dollar
]

# Dropdowns for selecting currencies
combo = ttk.Combobox(dataframe, font=("Courier", 15, "bold"), width=10, values=options)
combo.set("Select")
combo.place(relx=.37, rely=.17)

combo2 = ttk.Combobox(dataframe, font=("Courier", 15, "bold"), width=10, values=options)
combo2.set("Select")
combo2.place(relx=.37, rely=.37)

# Entry for the amount to be converted
entry = Entry(dataframe, font=("Courier", 17, "bold"), width=10)
entry.place(relx=.37, rely=.57)

# Frame for displaying the converted amount
aframe = Frame(dataframe, bg="#fff3e6", bd=10)
aframe.place(relx=0.6, rely=0.2, relwidth=0.30, relheight=.40)

# Label and entry for the converted amount
texts3 = Label(aframe, text="CONVERTED", font=("Arial", 25, "bold underline"), bg="#fff3e6", fg="black")
texts3.place(relx=.1, rely=.1)

result_entry = Entry(aframe, font=("Arial", 22, "bold"), width=13)
result_entry.place(relx=.1, rely=.6)
result_entry.config(state=DISABLED)  # Make it read-only initially

# Convert button
convert_button = Button(dataframe, text="Convert", command=convert_currency, font=("Helvetica", 18), width=18, bg="#34495E", fg="#ECF0F1")
convert_button.place(relx=0.37, rely=0.82)

# Run the Tkinter event loop
gui.mainloop()
