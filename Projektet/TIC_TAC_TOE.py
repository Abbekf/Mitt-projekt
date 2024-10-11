from tkinter import *                     # importerar allt från tkinter.

""" spelare, regler, ui """
def numbergame():
    # Skapa ett nytt fönster för Number Game
    number_window = Toplevel()
    number_window.geometry("400x400")
    number_window.title("Number Game")
    label = Label(number_window, text="tyvärr, servernm är offline!", font=("Arial", 20))
    label.pack(pady=20)
# h
# TODO: lös 
def tictactoe():
    # Skapa ett nytt fönster för Tic Tac Toe
    tic_tac_toe_window = Toplevel()
    tic_tac_toe_window.geometry("400x400")
    tic_tac_toe_window.title("Tic Tac Toe")
    label = Label(tic_tac_toe_window, text="tyvärr, servern är offline!", font=("Arial", 20))
    label.pack(pady=20)

fönster = Tk()                           # skapar en fönstervariabel.
fönster.geometry("970x500")              # väld storlek på fönster.
fönster.title("Abbes spelhöna")          # sätt titelnamn.
fönster.config(background="black")       # backgrundsfärg. ange färg eller hexa-färgkombo.

bild = PhotoImage(file="höna.png")       # hitta bildfil.
fönster.iconphoto(True,bild)             # sätt ikonbild. som min höna "spelHÖNA".
bild2 = PhotoImage(file="konsol.png")    # hitta bildfil.För att använda variabeln nere i etiketten.


textetikett = Label(fönster,
              text="<-- Välj spel -->", # text.
              font=("Arial",40,"bold"), # typsnitt, storlek, fet text.
              fg="white",               # textfärg.
              bg="black",               # färg bakom texten.
              relief="raised",          # sätter en ram runt texten.
              bd=10,                    # storlek på ramen.
              padx=20,                  # 20 pixlar mellanrum bredvid texten och ramen.
              pady=10,                  # 10 pixlar mellanrum över och under texten och ramen.
              image=bild2,              # lägger till bilden i denna Label funk.
              compound="bottom")        # väljer bildens plats. annars överskrider den texten.
textetikett.pack()                      # placerar texten uppe i mitten.



tic_tac_toe = Button(fönster,text="Tic Tac Toe")
tic_tac_toe.config(command=tictactoe)
tic_tac_toe.config(font=("",19,"bold"))
tic_tac_toe.config(bg="white")
tic_tac_toe.place(x=0,y=0)
bild3 = PhotoImage(file="tictactoe.png")
tic_tac_toe.config(image=bild3)
tic_tac_toe.config(compound="bottom")



number_game = Button(fönster,text="Number game")
number_game.config(command=numbergame)
number_game.config(font=("",19,"bold"))
number_game.config(bg="white")
number_game.place(x=730,y=0)
bild4 = PhotoImage(file="numberguess.png")
number_game.config(image=bild4)
number_game.config(compound="bottom")

fönster.mainloop()                      # kör programmet.
