import tkinter as tk
from window1 import create_window1
from window2 import create_window2


def main():
    root = tk.Tk()
    root.title("Hello World")
    root.geometry("400x400")

    label1 = tk.Label(root, text="I am learning how to use Tkinter\nHere is a button:")
    label1.pack(pady=10)

    button1 = tk.Button(root, text="I am a Button!", command=(lambda:label2.config(text="Hey, you clicked my button!")))
    button1.pack(pady=10)

    label2 = tk.Label(root)
    label2.pack(pady=5)

    button2 = tk.Button(root, text="Open Check Box Window", command=create_window1)
    button2.pack(pady=5)

    button3 = tk.Button(root, text="Open Toggle Button Window", command=create_window2)
    button3.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()