from tkinter import *
import re
import long_responses as lg
from tkinter import messagebox

ptr = 1
bubbles = []


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Goodbye!', ['bye', 'goodbye'], single_response=True)
    response('Thank you!', ['you', 'are', 'great', 'good','awesome','smart'], required_words=['you'])
    response('Alright!', ['i', 'am', 'doing', 'good', 'awesome'], required_words=['i','am'])
    response('I am a Bot!', ['who', 'are', 'you'], required_words=['who','you'])
    response(lg.joke(), ['joke', 'a', 'me', 'tell', 'a'], required_words=['joke'])
    response(lg.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(lg.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(lg.R_Born, ['how', 'were', 'you','born'], required_words=['born'])
    response(lg.R_Play, ['do', 'you', 'play', 'games'], required_words=['play'])
    response(lg.R_Play, ['do', 'you', 'play', 'games'], required_words=['play'])
    response('Yes I am a Bot yet smarter than most', ['are', 'you', 'a', 'robot'], required_words=['robot','are'])
    response('You can ask me simple questions.\nHow about try asking something about me?', ['what', 'can', 'you', 'do'],
             required_words=['can', 'do'])
    response('Yes? How may I help you?', ['i', 'have', 'a', 'question'], required_words=['question'])
    response('Yes? How may I help you?', ['can', 'you', 'help', 'me'], required_words=['help'])
    response('I don\'t have a name. You can refer to me as Chatbot.', ['what', 'is', 'your', 'name'],
             required_words=['your', 'name'])
    response('Sayan and Sanidhya coded me.', ['who', 'developed', 'made', 'you'],
             required_words=['who', 'you'])

    response('I am? Thanks!', ['you', 'are', 'smart'], required_words=['you', 'smart'])
    response('I calculate probability and give the most probable response', ['how', 'do', 'you', 'work'],
             required_words=['how', 'you', 'work'])
    response(lg.fact(), ['tell', 'me', 'a', 'fact'], required_words=['fact'])
    response('I love feasting on electricity!', ['what', 'is', 'your', 'favourite', 'food'], required_words=['food'])
    response('I am quite young. I have just recently been developed.', ['how', 'old', 'are', 'you'],
             required_words=['how', 'old'])
    response('I am developed using python.', ['what', 'programming', 'language', 'do', 'you', 'use'],
             required_words=['programming', 'language'])
    response('I think you are quite smart. That what Sanidhya asked me to tell you', ['what', 'do', 'you', 'think', 'of', 'me'],
             required_words=['what', 'think', 'me'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # -------------------------------------------------------------------------------------------------------------------

    return lg.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Tkinter_GUI ----------------------------------------------------------------------------------------------------------
window = Tk()
window.title("Chatbot")
window.geometry("499x462")
window.configure(bg="#ffffff")
window.iconbitmap(f'1.ico')

# Main_Screen
main_screen = Canvas(window, bg="#C4C4C4", height=462, width=499, bd=0, highlightthickness=0, relief="ridge")
main_screen.place(x=0, y=0)
background_img = PhotoImage(file=f"background.png")
background = main_screen.create_image(249.5, 231.0, image=background_img)

# Chat_Area
chat_area = Canvas(window, bg="grey", height=399, width=499, bd=0, highlightthickness=0, relief="ridge")
chat_area.place(x=0, y=0)

# Scroll_Bar for Chat_Area
hbar = Scrollbar(window, orient=VERTICAL)
hbar.place(relx=1, rely=0, anchor='ne', height=400)
hbar.config(command=chat_area.yview)
chat_area.config(yscrollcommand=hbar.set)


# User Chat_Bubble
class UserBubble:
    def __init__(self, master, message=""):
        self.master = master
        self.frame1 = Frame(master, bg="light grey")
        self.i = self.master.create_window(20, 300, anchor="sw", window=self.frame1)
        Label(self.frame1, text="You", font=("Helvetica", 7), bg="light grey").grid(row=0, column=0, sticky="w", padx=5)
        Label(self.frame1, text=message, font=("Helvetica", 9), bg="light grey").grid(row=1, column=0, sticky="w",
                                                                                      padx=5, pady=3)
        window.update_idletasks()


# Bot Chat_Bubble
class BotBubble:
    def __init__(self, master, message=""):
        self.master = master
        self.frame1 = Frame(master, bg="light blue")
        self.i = self.master.create_window(460, 353, anchor="se", window=self.frame1)
        Label(self.frame1, text="Bot", font=("Helvetica", 7), bg="light blue").grid(row=0, column=0, sticky="e", padx=5)
        Label(self.frame1, text=message, font=("Helvetica", 9), bg="light blue").grid(row=1, column=0, sticky="e",
                                                                                      padx=5, pady=3)
        window.update_idletasks()


# Function to Clear Entry_Box
def clrscn(event):
    global ptr
    ptr = 0
    entry.delete(0, END)
    if entry['fg'] == 'grey':
        entry['fg'] = 'black'


# Function For Send_Event
def send_message(event='<Return>'):
    if (entry.get() == '') or (ptr == 1):
        messagebox.showerror("Error", "No Input")
        return

    if bubbles:
        chat_area.move(ALL, 0, -105)

    a = UserBubble(chat_area, message=entry.get())
    bubbles.append(a)
    window.after(300)
    BotBubble(chat_area, message=get_response(entry.get()))
    x1, y1, x2, y2 = chat_area.bbox("all")

    chat_area.configure(scrollregion=[x1, y1 - 20, x2, y2 + 20])
    entry.delete(0, END)


# Customising Send_Button
send_img = PhotoImage(file=f"img0.png")
send_button = Button(image=send_img, borderwidth=0, highlightthickness=0, command=send_message, relief="flat")
send_button.place(x=428, y=411, width=38, height=38)

# Customising Entry_Box
entry_img = PhotoImage(file=f"img_textBox0.png")
entry_bg = main_screen.create_image(212.5, 430.0, image=entry_img)
entry = Entry(bd=0, bg="#fbf3f3", highlightthickness=0, fg='grey')
entry.insert(0, "Enter Your Message Here")
entry.bind('<Return>', send_message)
entry.bind("<FocusIn>", clrscn)
entry.place(x=33.0, y=411, width=359.0, height=36)

window.resizable(False, False)
window.mainloop()

# -----------------------------------------------------------------------------------------------------------------------
