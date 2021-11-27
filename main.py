from tkinter import *
import math
import time

TIMER_SECS=10
LIGHT_BLUE ="#CAF7E3"

first_words = ["great","opportunity","celebration","love","hate",
         "muhammad","angela","school","programming","blue","crush","almost"]

second_words =["hammer","landrover","landcruiser","lamborghini","justice",
               "tyranny","compassion","kindness","football","age"]
score = 0
new_highscore = 0
#------------------------------keypress detect--------------------------------------------------------------------------
def key_pressed(event):
    global score
    global new_highscore
    user_word = user_answer.get().lower()

    if user_word in first_words or user_word in second_words:
        score += 1
        new_highscore = score
        with open("highscore.txt",mode="r") as file:
            content = int(file.read())
            if new_highscore > content:
                with open("highscore.txt", mode="w") as edit:
                    edit.write(f"{new_highscore}")

        try:
            first_words.remove(user_word)
        except ValueError:
            second_words.remove(user_word)

        canvas.itemconfig(first_typing_text, text=first_words)
        canvas.itemconfig(second_typing_text, text=second_words)
        canvas.itemconfig(score_text, text=f"Score:{score}")
        #clearing the input widget
        user_answer.delete(0, 'end')
    else:
        print("word not in list")
#---------------------------------restart button clicked----------------------------------------------------------------
def restart_program():
    global first_words
    global second_words
    global score
    restart_button.place(x=10000000000000,y=1000000000000000)
    user_answer.delete(0, 'end')
    score = 0
    canvas.itemconfig(score_text, text=f"Score:{score}")
    first_words = ["great", "opportunity", "celebration", "love", "hate",
                   "muhammad", "angela", "school", "programming", "blue", "crush", "almost"]

    second_words = ["hammer", "landrover", "landcruiser", "lamborghini", "justice",
                    "tyranny", "compassion", "kindness", "football", "age"]

    start_clicked()


#--------------------------------start button clicked-------------------------------------------------------------------
def start_clicked():
    try:
        with open("highscore.txt",mode="r") as file:
            content = file.read()
            canvas.itemconfig(highscore_text, text=f"Highscore:{content}")
    except FileNotFoundError:
        with open("highscore.txt",mode="w") as file:
            file.write(f"0")


    canvas.itemconfig(timer_text,font=("courier",15,"bold"))
    canvas.itemconfig(first_typing_text,text=first_words,font=("arial",10,"bold"))
    canvas.itemconfig(second_typing_text, text=second_words, font=("arial", 10, "bold"))
    start_button.place(x=100000000000000000,y=1000000000000000000)

    user_answer.place(x=335, y=330)
    user_answer.focus_set()

    count_down(TIMER_SECS)



#------------------------------count timer------------------------------------------------------------------------------
def count_down(count):
    count_minute = math.floor(count/60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text,text=f"{count_minute}:{count_seconds}")
    if count > 0:
        window.after(1000,count_down,count-1)
    if count == 0:
        user_answer.place(x=10000000000000000,y=10000000000000000000)
        canvas.itemconfig(first_typing_text, text=f"")
        canvas.itemconfig(second_typing_text, text=f"test over! your score is {score}")
        restart_button.place(x=380, y=350)



window = Tk()
window.title("typing speed test")
window.config(padx=100,pady=50,bg=LIGHT_BLUE)


canvas = Canvas(width=840,height=1050,bg=LIGHT_BLUE,highlightthickness=0)
typing_img=PhotoImage(file="typing.png")
canvas.create_image(420,525,image=typing_img)
timer_text=canvas.create_text(420,125,text="01:00",fill="white",font=("courier",40,"bold"))
score_text = canvas.create_text(680, 123, text=f"Score:0", fill="white", font=("courier", 10, "bold"))
highscore_text = canvas.create_text(160,123,text=f"Highscore:{new_highscore}",fill="white",font=("courier",10,"bold"))
first_typing_text=canvas.create_text(420,255,text="Typing Test",fill="white",font=("courier",20,"bold"))
second_typing_text=canvas.create_text(420,305,text="",fill="white",font=("courier",20,"bold"))
start_button=Button(text="Start Typing",command=start_clicked)
start_button.place(x=380,y=350)
restart_button=Button(window, text="Type again", command=restart_program)

user_answer = Entry(width=30)




canvas.pack()



window.bind("<Return>",key_pressed)
window.mainloop()