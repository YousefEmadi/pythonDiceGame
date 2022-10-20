

from glob import glob
from flask import Flask, redirect, url_for, request, render_template
import random
from flask import g
from flask import Flask

app = Flask(__name__)


# global vars
player1 = ""
player2 = ""
currentPlayer = ""
diceNumber = 0
player1Score = 0
player2Score = 0
WINNINGPOINT = 20
print ("global init player1: ", player1)
print ("global init player2: ", player2)


@app.route('/')
def number():
    return render_template("playerForm.html") 

@app.route('/background_process_test')
def background_process_test():
    print ("Hello")
    return ("nothing")


# Players insert their names
@app.route('/gotodicegame' , methods=['POST'])
def insertPlayerNames():
    global player1, player2, currentPlayer
    player1 = request.form["player1"]
    player2 = request.form["player2"]
    currentPlayer = player1    
    print ("player1: ", player1)
    print ("player2: ", player2)
    print('global current player: ', currentPlayer)  
    
    return render_template("dice.html" , player1 = player1 , player2 = player2 ) 
        
        
def dicePicture(diceNumber):
    diceArray = ["hold" , "Die1" , "Die2" , "Die3" , "Die4" , "Die5" , "Die6"]
    
    if diceNumber == 0:
        return diceArray[0]
    if diceNumber == 1:
        return diceArray[1]
    if diceNumber == 2:
        return diceArray[2]
    if diceNumber == 3:
        return diceArray[3]
    if diceNumber == 4:
        return diceArray[4]
    if diceNumber == 5:
        return diceArray[5]
    if diceNumber == 6:
        return diceArray[6]
        
        
# Request Hold function to show current player
@app.route('/hold')
def hold():
    global currentPlayer, player1, player2, player1Score, player2Score
    print ("hold func player1: ", player1)
    print ("hold func player2: ", player2)
    print ("currentPlayer b4 hold:", currentPlayer)
    if currentPlayer == player1:
        currentPlayer = player2
    elif currentPlayer == player2:
        currentPlayer = player1
    
    dicePic = 0
    dicePic = dicePicture(diceNumber) 
    
    
    print ("currentPlayer after hold:", currentPlayer)

    return render_template("dice.html", player1 = player1 , player2 = player2, yousefPlayer = currentPlayer , score1 = player1Score , score2 = player2Score, dicePic =  dicePic) 
 
# Score calculation after Rolling the dice
 

@app.route('/rollDice' , methods=['GET'])
def rollDice():
    global currentPlayer, player1Score, player2Score , player1, player2, WINNINGPOINT
    maxDice= 6
    minDice = 1
    diceNumber = random.randint(1,6)
    dicePic= dicePicture(diceNumber)
    print ("currentPlayer :", currentPlayer)
    print ("dice :", diceNumber)
    winner = ""
    flag1 =""
    flag2 =""
    
    if diceNumber == 1 :
        if currentPlayer == player1:
            player1Score =0
            flag1 = "Oops!Lost scores."
        else:
            player2Score =0
            flag2 = "Oops!Lost scores."
        hold()
        return render_template("dice.html", player1 = player1 , player2 = player2, yousefPlayer = currentPlayer , score1 = player1Score , score2 = player2Score, dicePic =dicePic , flag1 =flag1 , flag2 = flag2) 
        
    if currentPlayer == player1 :
        player1Score = player1Score + diceNumber
    else:
        player2Score = player2Score + diceNumber
        
    if player1Score >= WINNINGPOINT:
        print( player1 , "Horay! YOU WONNNN!")
        winner = player1 , " YOU WONNNN! "
        exit()
    
    if player2Score >= WINNINGPOINT:
        print("winner is" , player2)
        winner = player2 , "YOU WONNNN! " 
        exit()
    
    
    print (player1, " score:", player1Score)
    
    print (player2, " score:", player2Score)

    # dicePicture(diceNumber)
    # return render_template('dicegame.html', currentPlayer = currentPlayer ,player1Score = player1Score , player2Score =player2Score )
    
    
    return render_template("dice.html", player1 = player1 , player2 = player2, yousefPlayer = currentPlayer , score1 = player1Score , score2 = player2Score, dicePic= dicePic, winner = winner) 


@app.route('/newGame', methods = ['GET'])
def newGame():
    global currentPlayer, player1Score, player2Score , player1, player2
    player1 = ""
    player2 = ""
    currentPlayer = ""
    player1Score = 0
    player2Score = 0

    return render_template("playerForm.html")      

@app.route('/exit', methods = ['GET'])
def exit():
    
    return render_template("playerForm.html")      
          
if __name__ == "__main__":
    app.run(debug =True)
    
 