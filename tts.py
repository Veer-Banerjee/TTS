import tkinter as tk
import pyttsx3

engine = pyttsx3.init()

class Widget():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('TTS')
        self.root.resizable(0,0)
        self.root.configure(background="blue")
        self.label1 = tk.Label(self.root, bg="blue", fg="yellow", font="Arial 25 bold", text="What do you want me to speak?")
        self.label1.pack(pady=20)
        self.entry = tk.Entry(self.root, width=35, font="Arial 20")
        self.entry.pack(pady=20)
        self.button = tk.Button(self.root, bg="blue", fg="yellow", font="Arial 25 bold", text="Speak!", command=self.clicked)
        self.button.pack(pady=20)
        self.root.mainloop()

    def clicked(self):    
        text = self.entry.get()
        self.speak(text)

    def speak(self,text):
        engine.say(text)    
        engine.runAndWait()

if __name__ == "__main__":
    widget = Widget()
