import wolframalpha
import tkinter as tk

# wolfram stuff
client = wolframalpha.Client("G4H2VA-496G3827Y9")

# GUI
HEIGHT = 100
WIDTH = 600

root = tk.Tk()
root.title("Robby")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#ff4d4d', bd='4')
frame.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.4)

labelFrame = tk.Frame(root, bg='#ff6666')
labelFrame.place(rely=0.5, relwidth=1, relheight=0.5)

# Query entry
entry = tk.Entry(frame, bg='#ff6666', fg='white', font='12')
entry.place(relwidth=0.8, relheight=1)

# Test label
output = tk.StringVar()
label = tk.Label(labelFrame, textvariable=output)
label.place(relwidth=1, relheight=1)

# Enter button


def readText():
    res = client.query(entry.get())
    output.set(next(res.results).text)
    print(next(res.results).text)
    entry.delete(0, 'end')


enterBttn = tk.Button(frame, text="Enter",
                      command=readText, bg='#ff4d4d',  font='15', fg='white')
enterBttn.place(relx=0.84, rely=.1, relwidth=0.15, relheight=0.8)


root.mainloop()
