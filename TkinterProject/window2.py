import tkinter as tk

def create_window2():
    window = tk.Toplevel()
    window.title("Window for Radio Buttons")
    window.geometry("400x400")

    label = tk.Label(window, text="I'm working on some Radio Buttons")
    label.pack(pady=10)

    selected_option = tk.StringVar(value="Option 1")

    def update_label():
        label.config(text=f"Selected: {selected_option.get()}")

    options = ["Click me!", "No, Click me!", "Click me plz"]
    results = ["Woohoo", "Booyah", "Aww yeah"]
    for option, result in zip(options, results):
        radio_button = tk.Radiobutton(
            window, 
            text=option, 
            variable=selected_option, 
            value=result,
            command=update_label
        )
        radio_button.pack(pady=5, anchor="w")

    label2 = tk.Label(window, text="This is a new change to window2!!!!!")
    label2.pack(pady=20)
