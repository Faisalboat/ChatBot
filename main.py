from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import*

bot = ChatBot("My Bot")

convo = [
    'hello',
    'hi there',
    'Where do you deliver ?',
    'Currently only serving in Dadar',
    'Whats on your Menu ',
    'We serve different varity of rice, Salad, Chinese/Italian dishes,milkshakes and Juices ',
    'Do You have any Combos?',
    'Yes We have Combos Any rice/Pasta + any juice 10%off and many more ',
    'How can i order food from SavourIT',
    'You can place Order by calling on 8097036761 ',
    'Do you guyz have any app or website ',
    'website under devlopment by that time please place your order on 8097036761',
]

trainer = ListTrainer(bot)

# Now training the bot with the help of trainer

trainer.train(convo)

#answer = bot.get_response("what is your name ?")
#print(answer)

#print("Talk to bot ")
#while True:
#    query=input()
#    if query=='exit':
#        break
#        answer=bot.get_response(query)
#        print("bot : ", answer)

main = Tk()

main.geometry("500x650")

main.title("SavourIT")

img=PhotoImage(file="botimg.png")
photoL=Label(main,image=img)


photoL.pack(pady=5)

def ask_from_bot():
    query=textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END,"YOU : " + query)
    print(type(answer_from_bot))
    msgs.insert(END,"bot : " + str(answer_from_bot))
    textF.delete(0,END)


frame=Frame(main)
sc=Scrollbar(frame)
msgs=Listbox(frame,width=80,height=20)

sc.pack(side=RIGHT,fil=Y)

msgs.pack(side=LEFT,fill=BOTH,pady=10)

frame.pack()

#creating text field

textF=Entry(main,font=("verdana",20))
textF.pack(fill=X,pady=10)

btn=Button(main,text="Ask me anything",font=("verdana",20),command=ask_from_bot)
btn.pack()



main.mainloop()