import tkinter as tk
import gtts
import os

window = tk.Tk()
window.title('Text to Speech Converter')
window.geometry('800x800')

def convertTextToSpeech():
    entry = f'Hello! My name is {nameEntry.get()}. My favourite hobby is {hobbyEntry.get()}. My favourite book is {bookEntry.get()} by {authorEntry.get()}.'
    submitBtn.config(state = 'disabled', cursor = 'hand2')

    if entry:
        audio = gtts.gTTS(entry, lang = 'en')
        audio.save('Audio.mp3')
        os.system('Audio.mp3')

    submitBtn.config(state = 'normal', cursor = 'hand2')


heading = tk.Label(window, text='Speak My Info', font=('Verdana', 30), fg="#81638B", bg='#E4B7E5', width=200, height=2)
heading.pack()

nameLabel = tk.Label(window, text = 'What is your Name?', font = ('Verdana', 20))
nameLabel.pack(pady = 10)

nameEntry = tk.Entry(window, font=('Verdana', 20))
nameEntry.pack(pady = 20)

hobbyLabel = tk.Label(window, text = 'What is your favourite hobby?', font = ('Verdana', 20))
hobbyLabel.pack(pady = 10)

hobbyEntry = tk.Entry(window, font = ('Verdana', 20))
hobbyEntry.pack(pady = 20)

bookLabel = tk.Label(window, text = 'What is your favourite book?', font = ('Verdana', 20))
bookLabel.pack(pady = 10)

bookEntry = tk.Entry(window, font = ('Verdana', 20))
bookEntry.pack(pady = 20)

authorLabel = tk.Label(window, text = 'Who is the author of your favourite book?', font = ('Verdana', 20))
authorLabel.pack(pady = 10)

authorEntry = tk.Entry(window, font = ('Verdana', 20))
authorEntry.pack(pady = 20)


submitBtn = tk.Button(window, font=('Verdana', 20), text = 'Submit', command = convertTextToSpeech)
submitBtn.pack(pady = 20)

window.mainloop()