import tkinter as tk

def create_window1():
    window = tk.Toplevel()
    window.title("Window for Check Boxes")
    window.geometry("400x400")

    label = tk.Label(window, text="I'm working on some check boxes!")
    label.pack(pady=10)

    toggle_state = tk.BooleanVar()

    toggle_button = tk.Checkbutton(
        window, 
        text="Check Me", 
        variable=toggle_state, 
        onvalue=True, 
        offvalue=False,
        command=lambda: label.config(text="You checked my box!" if toggle_state.get() else "You unchecked my box!")
    )
    toggle_button.pack(pady=10)

    label2 = tk.Label(window, text="This is a new change to window1!")
    label2.pack(pady=20)

    is_toggled = False

