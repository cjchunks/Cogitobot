import tkinter as tk
import openai
import random

api_key = 'your_api_key'
openai.api_key = api_key

def reply():
    user_input = entry.get("1.0", tk.END).strip()
    if user_input.lower() == 'exit':
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Goodbye")
    else:
        prompt_text = f"User: {user_input}\nAI:"

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt_text,
            max_tokens=200  # Generating longer responses
        )

        bot_response = response.choices[0].text.strip()
        if random.choice([True, False]):
            bot_response += " dude"
        else:
            bot_response += " bro"

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Cogito Bot:\n{bot_response}")


root = tk.Tk()
root.title("Cogito Bot - Your one and only Cool Dude")
root.geometry('500x570+100+30')
root.config(bg='deep pink')

logo_pic = tk.PhotoImage(file='abcd.png')


small_icon = logo_pic.subsample(3)


logo_pic_label = tk.Label(root, image=small_icon, bg='#67ACA5')
logo_pic_label.pack()



center_frame = tk.Frame(root)
center_frame.pack()
label = tk.Label(center_frame, text="Cogito Bot can do anything but cannot eat a pizza! Type 'exit' to quit.")
label.pack()


entry= tk.Text(root, width=60, height=15, wrap=tk.WORD)
entry.pack(pady=10)

output_text = tk.Text(center_frame, width=100, height=20)
output_text.pack()
button = tk.Button(center_frame, text="Ask CogitoBot", command=reply)
button.pack()

root.mainloop()

