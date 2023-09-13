
from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=25, pady=25)

input_mile = Entry(width=10)
input_mile.insert(END, "0")
input_mile.grid(column=1, row=0, pady=5, padx=5)

fr_label = Label(text="is equal to")
fr_label.grid(column=0, row=1, pady=5)

fresult_label = Label(text="0")
fresult_label.grid(column=1, row=1, pady=5, padx=5)

fm_label = Label(text="Miles")
fm_label.grid(column=2, row=0, pady=5, padx=5)

fk_label = Label(text="Km")
fk_label.grid(column=2, row=1, pady=5, padx=5)

input_km = Entry(width=10)
input_km.insert(END, "0")
input_km.grid(column=1, row=3, pady=10, padx=10)

sr_label = Label(text="is equal to")
sr_label.grid(column=0, row=4, pady=5)

sresult_label = Label(text="0")
sresult_label.grid(column=1, row=4, pady=5, padx=5)

sm_label = Label(text="Miles")
sm_label.grid(column=2, row=4, pady=5, padx=5)

sk_label = Label(text="Km")
sk_label.grid(column=2, row=3, pady=5, padx=5)


def mile_to_km():
    """This function converts mile to kilometer"""

    mile = float(input_mile.get())
    # km = round(mile * 1.609)
    km = mile * 1.609
    fresult_label.config(text=f"{km}")

def km_to_mile():
    """This function converts kilometer to mile"""
    km = float(input_km.get())
    mile = km / 1.609
    sresult_label.config(text=f"{mile}")


km_calculate_button = Button(text="Calculate", command=mile_to_km, width=10)
km_calculate_button.grid(column=1, row=2,pady=10, padx=10)

mile_calculate_button = Button(text="Calculate", command=km_to_mile, width=10)
mile_calculate_button.grid(column=1, row=5, pady=10, padx=10)


window.mainloop()
