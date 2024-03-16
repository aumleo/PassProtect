from tkinter import *

def convert():
    miles=float(miles_ip.get())
    km=miles*1.609
    km_res_label.config(text=str(km))


window = Tk()
window.title('Miles to Kilometer')
window.config(padx=25, pady=25)

miles_ip =  Entry(width=6)
miles_ip.grid(column=1, row=0)

miles_label = Label(text = 'Miles')
miles_label.grid(column=2, row=0)

is_equal_label = Label(text = 'is equal')
is_equal_label.grid(column=0, row=1)

km_res_label = Label(text="0")
km_res_label.grid(column=1, row=1)

km_label =  Label(text="Km")
km_label.grid(column=2, row=1)

calc_button =  Button(text="Calculate",command = convert)
calc_button.grid(column=1, row=2)

window.mainloop()

