import pygame
import time
import random

pygame.init()

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
blue = (0,0,200)

displayWidth = 900
displayHeight = 600

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))

pygame.display.set_caption("Rock Paper Scissors")

clock = pygame.time.Clock()

wins = 0
losses = 0
ties = 0

def drawRectangle(xpos, ypos, width, height, color):
    pygame.draw.rect(gameDisplay, color, [xpos, ypos, width, height])

def drawText(text, xpos, ypos, size, color):
    myFont = pygame.font.Font('freesansbold.ttf', size)
    textSurface = myFont.render(text, True, color)
    textRectangle = textSurface.get_rect()
    textRectangle.center = ((xpos, ypos))
    gameDisplay.blit(textSurface, textRectangle)

def drawButton(xpos, ypos, width, height, colorBox, colorText, sizeText, text, function):
    drawRectangle(xpos, ypos, width, height, colorBox)
    drawText(text, xpos + (width//2), ypos + (height//2), sizeText, white)
    
    # if clicked then do function
    mouse = pygame.mouse.get_pos()
    if (xpos + width > mouse[0] > xpos and ypos + height > mouse[1] > ypos):
        click = pygame.mouse.get_pressed()
        if click[0] == 1:
            function()

def getComputerChoice():
    randomInt = random.randint(1,4)
    if randomInt == 1:
        return "rock"
        
    if randomInt == 2:
        return "paper"
    
    if randomInt == 3:
        return "scissors"

def playerChoseRock():
    computerChoice = getComputerChoice()
    whoWon("rock", computerChoice)

def playerChosePaper():
    computerChoice = getComputerChoice()
    whoWon("paper", computerChoice)

def playerChoseScissors():
    computerChoice = getComputerChoice()
    whoWon("scissors", computerChoice)
        
def whoWon(playerChoice, computerChoice):
    if playerChoice == computerChoice:
        tie(playerChoice, computerChoice)
    
    if playerChoice == "rock" and computerChoice == "paper":
        lose(playerChoice, computerChoice)
    
    if playerChoice == "rock" and computerChoice == "scissors":
        win(playerChoice, computerChoice)
    
    if playerChoice == "paper" and computerChoice == "rock":
        win(playerChoice, computerChoice)
    
    if playerChoice == "paper" and computerChoice == "scissors":
        lose(playerChoice, computerChoice)
    
    if playerChoice == "scissors" and computerChoice == "rock":
        lose(playerChoice, computerChoice)
    
    if playerChoice == "scissors" and computerChoice == "paper":
        win(playerChoice, computerChoice)

def decisionScreen():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
            gameDisplay.fill(white)
            drawText("Rock, Paper, or Scissors?", displayWidth//2, displayHeight//4, 36, black)
            middleButtonXPos = displayWidth//2 - 50
            drawButton(middleButtonXPos - 200, 300, 100, 100, black, white, 15, "Rock", playerChoseRock)
            drawButton(middleButtonXPos, 300, 100, 100, black, white, 15, "Paper", playerChosePaper)
            drawButton(middleButtonXPos + 200, 300, 100, 100, black, white, 15, "Scissors", playerChoseScissors)
            
            drawText("Wins: " + str(wins), 50, 25, 15, black)
            drawText("Losses: " + str(losses), 50, 50, 15, black)
            drawText("Ties: " + str(ties), 50, 75, 15, black)
            pygame.display.update()


def tie(p, c):
    global ties
    ties += 1
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
            gameDisplay.fill(white)
            drawText("It was a tie!", displayWidth//2, displayHeight//4, 36, black)
            drawText("Player Choice: " + p, displayWidth//2, displayHeight//2, 36, black)
            drawText("Computer Choice: " + c, displayWidth//2, displayHeight - displayHeight//4, 36, black)
            pygame.display.update()
            time.sleep(2)
            running = False

def win(p, c):
    global wins
    wins += 1
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
            gameDisplay.fill(white)
            drawText("You win!", displayWidth//2, displayHeight//4, 36, black)
            drawText("Player Choice: " + p, displayWidth//2, displayHeight//2, 36, black)
            drawText("Computer Choice: " + c, displayWidth//2, displayHeight - displayHeight//4, 36, black)
            pygame.display.update()
            time.sleep(2)
            running = False
            
def lose(p, c):
    global losses
    losses += 1
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
            gameDisplay.fill(white)
            drawText("You lost!", displayWidth//2, displayHeight//4, 36, black)
            drawText("Player Choice: " + p, displayWidth//2, displayHeight//2, 36, black)
            drawText("Computer Choice: " + c, displayWidth//2, displayHeight - displayHeight//4, 36, black)
            pygame.display.update()
            time.sleep(2)
            running = False
    
decisionScreen()