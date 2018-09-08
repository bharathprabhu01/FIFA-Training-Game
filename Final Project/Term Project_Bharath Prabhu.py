# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *
import random
import math


# almostEqual function from Lab1 : 15-112

def almostEqual(d1, d2, epsilon=3):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

####################################
# customize these functions
####################################

def init(data):
    # user score and starting mode
    data.score = 0
    data.mode = "mainScreen"
    # data for different modes
    mainScreenData(data)
    helpScreenData(data)
    controlScreenData(data)
    L1Objective(data)
    L2Objective(data)
    L3Objective(data)
    soccerField(data)
    playGame(data)
    finalStat(data)
    passing(data)
    
def passing(data):
    # counters to keep track of passing accuracy
    # and interceptions by the AI
    data.level1Interceptions = 0
    data.m1Passes = 0
    data.m1MissedPasses = 0
    data.s1Passes = 0
    data.s1MissedPasses = 0
    data.level2Interceptions = 0
    data.m2Passes = 0
    data.m2MissedPasses = 0
    data.s2Passes = 0
    data.s2MissedPasses = 0
    data.m3Passes = 0
    data.m3MissedPasses = 0
    data.s3Passes = 0
    data.s3MissedPasses = 0
    data.w3Passes = 0
    data.w3MissedPasses = 0
    data.level3Interceptions = 0
    
    
def mainScreenData(data):
    # measurements to create buttons
    data.rectMargin = 50
    data.fontMargin = 150
    data.rectWidth = 200
    data.rectHeight = 50
    # image taken from --> http://www.trumarkathletics.com/
    filename = "C:/Users/Bharath Prabhu/Desktop/Term Project/images/soccer.gif"
    data.background = PhotoImage(file = filename)
    # image taken from --> http://www.fifplay.com/fifa-17-logo/
    filename = "C:/Users/Bharath Prabhu/Desktop/Term Project/images/logo2.gif"
    data.logo = PhotoImage(file = filename)
    
def helpScreenData(data):
    data.helpTitleMargin = 40
    data.instrMargin = 20
    
def controlScreenData(data):
    data.controlTitleMargin = 40
    data.controlInstrMargin = 40
    
def L1Objective(data):
    # image taken from --> http://brandthunder.com/wp/wp-content/uploads/2014/06/Lionel-Messi-Soccer-Background-1024x576.jpg
    filename = "C:/Users/Bharath Prabhu/Desktop/Term Project/images/L1background.gif"
    data.L1Background = PhotoImage(file = filename)
    data.textShiftMargin = 200
    data.L1TitleMargin = 40
    
def L2Objective(data):
    # image taken from --> http://4.bp.blogspot.com/-bimOSiIjooU/UQ7Kl7RYjsI/AAAAAAAAQBY/1_Sx-kAdDUE/s1600/Liverpool+2013+Wallpapers+HD+Luis+Suarez.jpg
    filename = "C:/Users/Bharath Prabhu/Desktop/Term Project/images/L2background.gif"
    data.L2Background = PhotoImage(file = filename)
    data.L2TitleMargin = 40
    
def L3Objective(data):
    # image taken from --> http://www.wallpaperbackgrounds.org/wp-content/uploads/Borussia-Dortmund_8.jpg
    filename = "C:/Users/Bharath Prabhu/Desktop/Term Project/images/L3background.gif"
    data.L3Background = PhotoImage(file = filename)
    data.L3TitleMargin = 40
    
def soccerField(data):
    # to draw Field
    data.cols = 9
    data.colWidth = data.width/data.cols
    data.colHeight = data.height
    data.fieldColor = None
    data.fieldMargin = 35
    data.fieldWidth = data.width - (2*data.fieldMargin)
    data.fieldHeight = data.height - (2*data.fieldMargin)
    # to draw all spot kicks
    data.spotKickRadius = 7
    # to draw Centre Circle
    data.centreCircleRadius = 60
    # to draw GoalBoxes
    data.eighteenYardBoxWidth = (5/3) * data.colWidth
    data.eighteenYardBoxHeight = (data.height - 2*data.fieldMargin)*(4/6)
    data.sixYardBoxWidth = (2/3) * data.colWidth
    data.sixYardBoxHeight = (data.height - (2*data.fieldMargin)) *(1/3)
    # draw goalPost
    data.goalPostHeight = (1/3) * data.sixYardBoxHeight
    
def playGame(data):
    data.teamColors = ["Red", "orange"]
    data.playerRadius = 20
    data.ballRadius = 15
    data.roundOverTextMargin = 70
    level1(data)
    level2(data)
    level3(data)
    

# data common to all 3 levels of gameplay

def commonData(data):
    data.passesLeft = 5
    data.timerCount = 0
    data.strikerMarking = 10
    data.moveBall = False
    data.moveDefender = False
    data.moveStriker = False
    # midfielder coords
    data.mX = data.width/2
    data.mY = data.height/2
    x0, y0, x1, y1 = getRight18YardBoxBounds(data)
    # striker coords
    data.sX = random.randint(int(x0), int(x1))
    data.sY = random.randint(int(y0), int(y1))
    # defender coords
    data.dX = data.sX + data.playerRadius + data.strikerMarking
    dY0 = data.sY - data.playerRadius - data.strikerMarking
    dY1 = data.sY + data.playerRadius + data.strikerMarking
    data.dY = random.randint(int(dY0), int(dY1))
    data.bX = data.mX + data.playerRadius + data.ballRadius
    data.bY = data.mY
    # where the ball will be passed to
    data.newPassX = data.bX
    data.newPassY = data.bY
    # player speeds
    data.defenderSpeed = random.randint(5, 12)
    data.strikerSpeed = random.randint(8, 10)

def level1(data):
    data.level1Player = "midfielder"
    data.round1Over = None
    data.round = 1
    data.gamePlayLevel1 = False
    data.highScore1 = 10
    commonData(data)
    
def level2(data):
    commonData(data)
    data.gamePlayLevel2 = False
    data.level2Player = "midfielder"
    data.round2Over = None
    # where the midfielder will move after passing the ball
    data.newMidfielderX = data.sX
    data.newMidfielderY = data.sY
    data.moveMidfielder = False
    data.midfielderSpeed = random.randint(5, 10)
    # new position for defender marking striker
    data.newPosX = data.sX
    data.newPosY = data.sY
    data.highScore2 = 20
    
def level3(data):
    commonData(data)
    level2(data)
    data.highScore3 = 35
    data.gamePlayLevel3 = False
    data.round3Over = None
    data.level3Player = "midfielder"
    x0, y0, x1, y1 = getRightGoalPostBounds(data)
    # winger
    data.wX = int(x0)
    data.wY = random.randint(int(y0), int(y1))
    # defender 1 marking striker
    data.d1X = data.sX + data.playerRadius + data.strikerMarking
    A = data.sY - data.playerRadius - data.strikerMarking
    B = data.sY + data.playerRadius + data.strikerMarking
    data.d1Y = random.randint(int(A), int(B))
    # defender 2 marking winger
    data.d2X = data.wX + data.playerRadius + data.strikerMarking
    A1 = data.wY - data.playerRadius - data.strikerMarking
    B1 = data.wY + data.playerRadius + data.strikerMarking
    data.d2Y = random.randint(int(A1), int(B1))
    data.moveWinger = False
    data.moveDefender1 = False
    data.moveDefender2 = False
    # speeds for the winger and 2 defenders
    data.wingerSpeed = random.randint(5, 10)
    data.defender1Speed = random.randint(5, 10)
    data.defender2Speed = random.randint(5, 10)
    # where the 2 defenders will move to
    data.newPosD1X = data.sX
    data.newPosD1Y = data.sY
    data.newPosD2X = data.wX
    data.newPosD2Y = data.wY
    # where your striker will run to
    data.newStrikerX = data.wX
    data.newStrikerY = data.wY
    # where your winger will run to
    data.newWingerX = data.mX
    data.newWingerY = data.mY

    
def finalStat(data):
    filename = "C:/Users/Bharath Prabhu/Desktop/Term Project/images/statBackground.gif"
    data.statBackground = PhotoImage(file = filename)
    data.boxCols = 4
    data.boxRows = 5
    data.tableMargin = 70
    data.statTitleMargin = 40
    
    
    
    
#### Mode Dispatcher ####

# From event based animations Lecture (Mode Demo)

def mousePressed(event, data):
    if(data.mode == "mainScreen") : mainScreenMousePressed(event, data)
    if(data.mode == "helpScreen") : helpScreenMousePressed(event, data)
    if(data.mode == "controlScreen") : controlScreenMousePressed(event, data)
    if(data.mode == "L1Objective"): L1ObjectiveMousePressed(event, data)
    if(data.mode == "L1Hint") : L1HintMousePressed(event, data)
    if(data.mode == "L2Objective") : L2ObjectiveMousePressed(event, data)
    if(data.mode == "L2Hint") : L2HintMousePressed(event, data)
    if(data.mode == "L3Objective") : L3ObjectiveMousePressed(event, data)
    if(data.mode == "L3Hint") : L3HintMousePressed(event, data)
    if(data.mode == 1) : level1MousePressed(event, data)
    if(data.mode == 2) : level2MousePressed(event, data)
    if(data.mode == 3) : level3MousePressed(event, data)
    if(data.mode == "finalStat") : finalStatMousePressed(event, data)
    

def keyPressed(event, data):
    if(data.mode == "mainScreen") : mainScreenKeyPressed(event, data)
    if(data.mode == "helpScreen") : helpScreenKeyPressed(event, data)
    if(data.mode == "controlScreen") : controlScreenKeyPressed(event, data)
    if(data.mode == "L1Objective"): L1ObjectiveKeyPressed(event, data)
    if(data.mode == "L1Hint") : L1HintKeyPressed(event, data)
    if(data.mode == "L2Objective") : L2ObjectiveKeyPressed(event, data)
    if(data.mode == "L2Hint") : L2HintKeyPressed(event, data)
    if(data.mode == "L3Objective") : L3ObjectiveKeyPressed(event, data)
    if(data.mode == "L3Hint") : L3HintKeyPressed(event, data)
    if(data.mode == 1) : level1KeyPressed(event, data)
    if(data.mode == 2) : level2KeyPressed(event, data)
    if(data.mode == 3) : level3KeyPressed(event, data)
    if(data.mode == "finalStat") : finalStatKeyPressed(event, data)

def timerFired(data):
    if(data.mode == "mainScreen") : mainScreenTimerFired(data)
    if(data.mode == "helpScreen") : helpScreenTimerFired(data)
    if(data.mode == "controlScreen") : controlScreenTimerFired(data)
    if(data.mode == "L1Objective"): L1ObjectiveTimerFired(data)
    if(data.mode == "L1Hint") : L1HintTimerFired(data)
    if(data.mode == "L2Objective") : L2ObjectiveTimerFired(data)
    if(data.mode == "L2Hint") : L2HintTimerFired(data)
    if(data.mode == "L3Objective") : L3ObjectiveTimerFired(data)
    if(data.mode == "L3Hint") : L3HintTimerFired(data)
    if(data.mode == 1) : level1TimerFired(data)
    if(data.mode == 2) : level2TimerFired(data)
    if(data.mode == 3) : level3TimerFired(data)
    if(data.mode == "finalStat") : finalStatTimerFired(data)
    

def redrawAll(canvas, data):
    if(data.mode == "mainScreen") : mainScreenRedrawAll(canvas, data)
    if(data.mode == "helpScreen") : helpScreenRedrawAll(canvas, data)
    if(data.mode == "controlScreen") : controlScreenRedrawAll(canvas, data)
    if(data.mode == "L1Objective"): L1ObjectiveRedrawAll(canvas, data)
    if(data.mode == "L1Hint") : L1HintRedrawAll(canvas, data)
    if(data.mode == "L2Objective") : L2ObjectiveRedrawAll(canvas, data)
    if(data.mode == "L2Hint") : L2HintRedrawAll(canvas, data)
    if(data.mode == "L3Objective") : L3ObjectiveRedrawAll(canvas, data)
    if(data.mode == "L3Hint") : L3HintRedrawAll(canvas, data)
    if(data.mode == 1): level1RedrawAll(canvas, data)
    if(data.mode == 2): level2RedrawAll(canvas, data)
    if(data.mode == 3): level3RedrawAll(canvas, data)
    if(data.mode == "finalStat") : finalStatRedrawAll(canvas, data)
    
    
#### Main Screen Mode ####

def getPlayButtonBounds(data):
    x0 = data.width/2 - (1/2)*data.rectWidth
    x1 = x0 + data.rectWidth
    y0 = data.height/2 - (1/2)*data.rectHeight
    y1 = y0 + data.rectHeight
    return (x0, y0, x1, y1)
    
def getControlButtonBounds(data):
    x0 = data.width/2 - (1/2)*data.rectWidth
    x1 = x0 + data.rectWidth
    y0 = data.height/2 + (1/2)*data.rectHeight + data.rectMargin
    y1 = y0 + data.rectHeight
    return (x0, y0, x1, y1)
    
def getHelpButtonBounds(data):
    x0 = data.width/2 - (1/2)*data.rectWidth
    x1 = x0 + data.rectWidth
    y0 = data.height/2 + (3/2)*data.rectHeight + (2*data.rectMargin)
    y1 = y0 + data.rectHeight
    return (x0, y0, x1, y1)

def mainScreenMousePressed(event, data):
    x, y = event.x, event.y
    hx0, hy0, hx1, hy1 = getHelpButtonBounds(data)
    if(hx0 <= x <= hx1) and (hy0 <= y <= hy1):
        data.mode = "helpScreen"
    cx0, cy0, cx1, cy1 = getControlButtonBounds(data)
    if(cx0 <= x <= cx1) and (cy0 <= y <= cy1):
        data.mode = "controlScreen"
    px0, py0, px1, py1 = getPlayButtonBounds(data)
    if(px0 <= x <= px1) and (py0 <= y <= py1):
        data.mode = "L1Objective"
    
def mainScreenKeyPressed(event, data):
    pass
    
def mainScreenTimerFired(data):
    pass
    
def mainScreenRedrawAll(canvas, data):
    drawMainBackground(canvas, data)
    drawLogo(canvas, data)
    drawPlayButton(canvas, data)
    drawControlButton(canvas, data)
    drawHelpButton(canvas, data)
    
def drawMainBackground(canvas, data):
    canvas.create_image(0, 0, anchor = NW, image = data.background)
    
def drawLogo(canvas, data):
    logoX = data.width/2
    logoY = data.height/2 - (data.fontMargin)
    canvas.create_image(logoX, logoY, image = data.logo)
    
def drawPlayButton(canvas, data):
    x0, y0, x1, y1 = getPlayButtonBounds(data)
    canvas.create_rectangle(x0, y0, x1, y1, fill = "green")
    text = "Play Game"
    textX = (x0 + x1)/2
    textY = (y0 + y1)/2
    canvas.create_text(textX, textY, text = text, fill = "yellow", 
                       font = "Arial 20")
                       
def drawControlButton(canvas, data):
    x0, y0, x1, y1 = getControlButtonBounds(data)
    canvas.create_rectangle(x0, y0, x1, y1, fill = "green")
    text = "Controls"
    textX = (x0 + x1)/2
    textY = (y0 + y1)/2
    canvas.create_text(textX, textY, text = text, fill = "yellow", 
                       font = "Arial 20")
                       
def drawHelpButton(canvas, data):
    x0, y0, x1, y1 = getHelpButtonBounds(data)
    canvas.create_rectangle(x0, y0, x1, y1, fill = "green")
    text = "Help"
    textX = (x0 + x1)/2
    textY = (y0 + y1)/2
    canvas.create_text(textX, textY, text = text, fill = "yellow", 
                       font = "Arial 20")
                       
#### Help Screen Mode ####

def helpScreenMousePressed(event, data):
    pass
    
def helpScreenKeyPressed(event, data):
    if(event.keysym == "b"):
        data.mode = "mainScreen"
    
def helpScreenTimerFired(data):
    pass
    
def helpScreenRedrawAll(canvas, data):
    drawHelpBackground(canvas, data)
    drawHelpTitle(canvas, data)
    drawHelpInstructions(canvas, data)
    
def drawHelpBackground(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "darkkhaki")

def drawHelpTitle(canvas, data):
    x0 = data.width/2
    y0 = data.helpTitleMargin
    text = "Instructions"
    canvas.create_text(x0, y0, text = text,font = "Arial 20 bold underline")
    
def drawHelpInstructions(canvas, data):
    instrM = data.instrMargin
    titleM = data.helpTitleMargin
    text1 = "1. You have control of red team players"
    canvas.create_text(instrM, instrM + (2*titleM), anchor = W, 
                       text = text1, font = "Arial 15")
                       
    text2 = """2. Your objective is to score a goal by passing the ball between your team players without losing possession
    using various tactics that you will learn progressively level by level"""
    canvas.create_text(instrM, instrM + (3.5*titleM), anchor = W, 
                       text = text2, font = "Arial 15")
                       
    text3 = """3. You always start with controlling your midfielder, and only your midfielder can be controlled using movement.
    Once the game starts, movement for all players except your midfielder is not allowed."""
    canvas.create_text(instrM, instrM + (5*titleM), anchor = W, 
                       text = text3, font = "Arial 15")
                       
    text4 = "3. The yellow team defenders (computer AI) will try to intercept and clear the ball"
    canvas.create_text(instrM, instrM + (6.5*titleM), anchor = W, 
                       text = text4, font = "Arial 15")
                       
    text5 = "4. If the yellow team defenders intercept the ball and clear it, you lose that level"
    canvas.create_text(instrM, instrM + (7.5*titleM), anchor = W, 
                       text = text5, font = "Arial 15")
                       
    text6 = "5. If you lose possession of the ball while passing between your players, you lose that level"
    canvas.create_text(instrM, instrM + (8.5*titleM), anchor = W, 
                       text = text6, font = "Arial 15")
                       
    text7 = "6. If you complete all the levels, you win the game!"
    canvas.create_text(instrM, instrM + (9.5*titleM), anchor = W, 
                       text = text7, font = "Arial 15")
                       
    text8 = "7. press 'b' to go back"
    canvas.create_text(instrM, instrM + (10.5*titleM), anchor = W, 
                       text = text8, font = "Arial 15")

#### Control Screen Mode ####

def controlScreenMousePressed(event, data):
    pass
    
def controlScreenKeyPressed(event, data):
    if(event.keysym == "b"):
        data.mode = "mainScreen"
    
def controlScreenTimerFired(data):
    pass
    
def controlScreenRedrawAll(canvas, data):
    drawControlBackground(canvas, data)
    drawControlTitle(canvas, data)
    drawControlDescriptions(canvas, data)
    
def drawControlBackground(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "sienna1")
    
def drawControlTitle(canvas, data):
    x0 = data.width/2
    y0 = data.controlTitleMargin
    text = "Controls"
    canvas.create_text(x0, y0, text = text,font = "Arial 20 bold underline")

def drawControlDescriptions(canvas, data):
    instrM = data.controlInstrMargin
    titleM = data.controlTitleMargin
    text1 = "1. (Up, Down, Right, Left) Arrow keys : Move the Player"
    canvas.create_text(instrM, instrM + (2*titleM), anchor = W, 
                       text = text1, font = "Arial 15")
                       
    text2 = "2. Mouseclick : Select point on the soccer field you want to pass to or shoot to"
    canvas.create_text(instrM, instrM + (3*titleM), anchor = W, 
                       text = text2, font = "Arial 15")
                       
    text3 = "3. Space : Pass the ball / Shoot the ball"
    canvas.create_text(instrM, instrM + (4*titleM), anchor = W, 
                       text = text3, font = "Arial 15")
                       
    text4 = "4. 'r' : Restart the level"
    canvas.create_text(instrM, instrM + (5*titleM), anchor = W, 
                       text = text4, font = "Arial 15")
                       
    text5 = "5. Press 'b' to go back"
    canvas.create_text(instrM, instrM + (6*titleM), anchor = W, 
                       text = text5, font = "Arial 15")
                       
#### Common Objective Functions ####

def getBackButtonBounds(data):
    x0 = data.width/2 + data.textShiftMargin
    x1 = x0 + data.rectWidth
    y0 = data.height/2 + (1/2)*data.textShiftMargin - (1/2)*data.rectHeight
    y1 = y0 + data.rectHeight
    return (x0, y0, x1, y1)
    
def getHintButtonBounds(data):
    x0 = data.width/2 + data.textShiftMargin
    x1 = x0 + data.rectWidth
    y0 = (data.height/2 + (1/2)*data.textShiftMargin + 
        (1/2)*data.rectHeight + (1/5)*data.rectMargin)
    y1 = y0 + data.rectHeight
    return (x0, y0, x1, y1)
    
def getContinueButtonBounds(data):
    x0 = data.width/2 + data.textShiftMargin
    x1 = x0 + data.rectWidth
    y0 = (data.height/2 + (1/2)*data.textShiftMargin + 
         (3/2)*data.rectHeight + (2/5)*data.rectMargin)
    y1 = y0 + data.rectHeight
    return (x0, y0, x1, y1)

def drawBackButton(canvas, data):
    x0, y0, x1, y1 = getBackButtonBounds(data)
    canvas.create_rectangle(x0, y0, x1, y1, fill = "green")
    text = "Back"
    textX = (x0 + x1)/2
    textY = (y0 + y1)/2
    canvas.create_text(textX, textY, text = text, fill = "yellow", 
                       font = "Arial 20")
    
def drawContinueButton(canvas, data):
    x0, y0, x1, y1 = getContinueButtonBounds(data)
    canvas.create_rectangle(x0, y0, x1, y1, fill = "green")
    text = "Continue"
    textX = (x0 + x1)/2
    textY = (y0 + y1)/2
    canvas.create_text(textX, textY, text = text, fill = "yellow", 
                       font = "Arial 20")
    
def drawHintButton(canvas, data):
    x0, y0, x1, y1 = getHintButtonBounds(data)
    canvas.create_rectangle(x0, y0, x1, y1, fill = "green")
    text = "Hint"
    textX = (x0 + x1)/2
    textY = (y0 + y1)/2
    canvas.create_text(textX, textY, text = text, fill = "yellow", 
                       font = "Arial 20")
                       
                       
#### L1Objective Screen Mode ####

def L1ObjectiveMousePressed(event, data):
    mouseX, mouseY = event.x, event.y
    x0, y0, x1, y1 = getBackButtonBounds(data)
    if(x0 <= mouseX <= x1) and (y0 <= mouseY <= y1):
        data.mode = "mainScreen"
    x0, y0, x1, y1 = getHintButtonBounds(data)
    if(x0 <= mouseX <= x1) and (y0 <= mouseY <= y1):
        data.mode = "L1Hint"
    x0, y0, x1, y1 = getContinueButtonBounds(data)
    if(x0 <= mouseX <= x1) and (y0 <= mouseY <= y1):
        data.mode = 1
    
def L1ObjectiveKeyPressed(event, data):
    pass

def L1ObjectiveTimerFired(data):
    pass
    
def L1ObjectiveRedrawAll(canvas, data):
    drawL1ObjectiveBackground(canvas, data)
    drawL1ObjectiveTitle(canvas, data)
    drawL1ObjectiveSteps(canvas, data)
    drawBackButton(canvas, data)
    drawHintButton(canvas, data)
    drawContinueButton(canvas, data)

def drawL1ObjectiveBackground(canvas, data):
    canvas.create_image(0, 0, anchor = NW, image = data.L1Background)
    
def drawL1ObjectiveTitle(canvas, data):
    x0 = data.width/2 + data.textShiftMargin
    y0 = data.L1TitleMargin
    text = "LEVEL 1 OBJECTIVE"
    canvas.create_text(x0, y0, text = text,font = "Arial 20 bold")
    
def drawL1ObjectiveSteps(canvas, data):
    textX = data.width/2 + data.textShiftMargin
    titleM = data.L1TitleMargin
    text1 = """\n\n\n\n\n\n\n\n\n\n\n
    Your objective for this level is to score a goal on the right hand
    side of the field by training your midfielder and striker in one touch 
    passing. A computer defender will be constantly marking your 
    striker and your aim is to make sure that the defender doesn't 
    intercept and clear the ball. If he does, you lose the round.
    
    The minimum number of passes / shots on goal you must use : 3
    The maximum number of passes / shots on goal you can use : 5
    
    """
    canvas.create_text(textX, 2*titleM, 
                       text = text1, font = "Arial 15")
                       
                       
#### L2Objective Screen Mode ####

def L2ObjectiveMousePressed(event, data):
    mouseX, mouseY = event.x, event.y
    x0, y0, x1, y1 = getHintButtonBounds(data)
    if(x0 <= mouseX <= x1) and (y0 <= mouseY <= y1):
        data.mode = "L2Hint"
    x0, y0, x1, y1 = getContinueButtonBounds(data)
    if(x0 <= mouseX <= x1) and (y0 <= mouseY <= y1):
        data.mode = 2
    
def L2ObjectiveKeyPressed(event, data):
    if(event.keysym == "b"):
        data.mode = "L2Objective"
    
def L2ObjectiveTimerFired(data):
    pass
    
def L2ObjectiveRedrawAll(canvas, data):
    drawL2ObjectiveBackground(canvas, data)
    drawL2ObjectiveTitle(canvas, data)
    drawL2ObjectiveSteps(canvas, data)
    drawHintButton(canvas, data)
    drawContinueButton(canvas, data)

def drawL2ObjectiveBackground(canvas, data):
    canvas.create_image(0, 0, anchor = NW, image = data.L2Background)
    
def drawL2ObjectiveTitle(canvas, data):
    x0 = data.width/2 + data.textShiftMargin
    y0 = data.L2TitleMargin
    text = "LEVEL 2 OBJECTIVE"
    canvas.create_text(x0, y0, text = text, font = "Arial 20 bold", fill = "white")
    
def drawL2ObjectiveSteps(canvas, data):
    textX = data.width/2 + data.textShiftMargin
    titleM = data.L2TitleMargin
    text1 = """\n\n\n\n\n\n\n\n\n\n
    Your objective in this level is the same as the previous level.
    However, instead of just intercepting, the defender will judge if 
    he can intercept, otherwise he will position himself such that your 
    players can't make passes back at each other. Your task is to 
    evade the defender and try and score a goal. Keep in mind that 
    your midfielder and striker will make run ins after passing
    the ball rather than remain stationary
    
    The minimum number of passes / shots on goal you must use : 3
    The maximum number of passes / shots on goal you can use : 5
    """
    canvas.create_text(textX, 2*titleM, 
                       text = text1, font = "Arial 15", fill = "white")
                       

#### L3Objective Screen Mode ####

def L3ObjectiveMousePressed(event, data):
    mouseX, mouseY = event.x, event.y
    x0, y0, x1, y1 = getHintButtonBounds(data)
    if(x0 <= mouseX <= x1) and (y0 <= mouseY <= y1):
        data.mode = "L3Hint"
    x0, y0, x1, y1 = getContinueButtonBounds(data)
    if(x0 <= mouseX <= x1) and (y0 <= mouseY <= y1):
        data.mode = 3
    
def L3ObjectiveKeyPressed(event, data):
    if(event.keysym == "b"):
        data.mode = "L3Objective"
    
def L3ObjectiveTimerFired(data):
    pass
    
def L3ObjectiveRedrawAll(canvas, data):
    drawL3ObjectiveBackground(canvas, data)
    drawL3ObjectiveTitle(canvas, data)
    drawL3ObjectiveSteps(canvas, data)
    drawHintButton(canvas, data)
    drawContinueButton(canvas, data)

def drawL3ObjectiveBackground(canvas, data):
    canvas.create_image(0, 0, anchor = NW, image = data.L3Background)
    
def drawL3ObjectiveTitle(canvas, data):
    x0 = data.width/2 + data.textShiftMargin
    y0 = data.L3TitleMargin
    text = "LEVEL 3 OBJECTIVE"
    canvas.create_text(x0, y0, text = text, font = "Arial 20 bold", fill = "white")
    
def drawL3ObjectiveSteps(canvas, data):
    textX = data.width/2 + data.textShiftMargin
    titleM = data.L3TitleMargin
    text1 = """\n\n\n\n\n\n\n\n\n\n
    Your objective in this level is the same as the previous level which 
    is to score a goal on the right hand side. However in this level 
    you have another player (winger) and you have to deal with 2 
    defenders. The defenders will intercept and position themselves 
    based on your player positions. This level can be tricky, but it is 
    an amalgamation of the tactics developed in the previous 2 levels
    
    The minimum number of passes / shots on goal you must use : 5
    The maximum number of passes / shots on goal you can use : 8
    """
    canvas.create_text(textX, 2*titleM, 
                       text = text1, font = "Arial 15", fill = "white")
                       
#### Functions common to Hints ####

def drawHintBackground(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "lightblue")
    
def drawHintTitleLevel1(canvas, data):
    x0 = data.width/2
    y0 = data.height/2
    text = """Hint :   Try dragging the defender away from goal so that your 
            midfielder has a clear shot on goal
            
            (press 'b' to go back)"""
    canvas.create_text(x0, y0, text = text,font = "Arial 20 bold")
    
def drawHintTitleLevel2(canvas, data):
    x0 = data.width/2
    y0 = data.height/2
    text = """Hint :     Use the one touch football and tactic of dragging the
              defender away that you developed in round 1  in this round. 
              Try to create space as the player you do not control will run 
              into that space after passing
            
            (press 'b' to go back)"""
    canvas.create_text(x0, y0, text = text,font = "Arial 20 bold")
    
def drawHintTitleLevel3(canvas, data):
    x0 = data.width/2
    y0 = data.height/2
    text = """Hint :     Use the tactic you learnt in round 2 of dragging
              the defender out in round 3. The only difference is there 
              are 2 defenders. Once you drag one defender out, and your
              player makes the run in, it will become a 2 vs 1 situation
              which you have learnt how to handle from previous rounds
            
            (press 'b' to go back)"""
    canvas.create_text(x0, y0, text = text,font = "Arial 20 bold")
    

#### L1Hint Screen Mode ####

def L1HintMousePressed(event, data):
    pass

def L1HintKeyPressed(event, data):
    if(event.keysym == 'b'):
        data.mode = "L1Objective"
    
def L1HintTimerFired(data):
    pass
    
def L1HintRedrawAll(canvas, data):
    drawHintBackground(canvas, data)
    drawHintTitleLevel1(canvas, data)
    
#### L2Hint Screen Mode ####

def L2HintMousePressed(event, data):
    pass

def L2HintKeyPressed(event, data):
    if(event.keysym == 'b'):
        data.mode = "L2Objective"
    
def L2HintTimerFired(data):
    pass
    
def L2HintRedrawAll(canvas, data):
    drawHintBackground(canvas, data)
    drawHintTitleLevel2(canvas, data)
    
#### L3Hint Screen Mode ####

def L3HintMousePressed(event, data):
    pass

def L3HintKeyPressed(event, data):
    if(event.keysym == 'b'):
        data.mode = "L3Objective"
    
def L3HintTimerFired(data):
    pass
    
def L3HintRedrawAll(canvas, data):
    drawHintBackground(canvas, data)
    drawHintTitleLevel3(canvas, data)
    

####### DRAW SOCCER FIELD ##############

def getColBounds(col, data):
    x0 = col * data.colWidth
    x1 = (col + 1) * data.colWidth
    y0 = 0
    y1 = data.height
    return(x0, y0, x1, y1)
    
def getLeft18YardBoxBounds(data):
    x01 = data.fieldMargin
    x11 = x01 + data.eighteenYardBoxWidth
    y01 = data.fieldMargin + ((data.fieldHeight) * (1/6))
    y11 = y01 + data.eighteenYardBoxHeight
    return(x01, y01, x11, y11)
    
def getRight18YardBoxBounds(data):
    x12 = data.width - data.fieldMargin
    x02 = x12 - data.eighteenYardBoxWidth
    y12 = (data.height - data.fieldMargin - ((data.fieldHeight) * (1/6)))
    y02 = y12 - data.eighteenYardBoxHeight
    return(x02, y02, x12, y12)
    
def getLeft6YardBoxBounds(data):
    x01 = data.fieldMargin
    x11 = x01 + data.sixYardBoxWidth
    y01 = data.fieldMargin + (data.height - 2*data.fieldMargin) * (1/3)
    y11 = y01 + data.sixYardBoxHeight
    return(x01, y01, x11, y11)
    
def getRight6YardBoxBounds(data):
    x02 = data.width - data.fieldMargin - data.sixYardBoxWidth
    x12 = x02 + data.sixYardBoxWidth
    y12 = data.height - data.fieldMargin - ((1/3) * data.fieldHeight)
    y02 = y12 - data.sixYardBoxHeight
    return(x02, y02, x12, y12)
    
def getLeftGoalPostBounds(data):
    x01 = data.fieldMargin/2
    x11 = data.fieldMargin
    y01 = ((data.fieldHeight - data.goalPostHeight)/2) + data.fieldMargin
    y11 = y01 + data.goalPostHeight
    return(x01, y01, x11, y11)
    
def getRightGoalPostBounds(data):
    x02 = data.width - data.fieldMargin
    x12 = data.width - ((1/2) * data.fieldMargin)
    y02 = ((data.fieldHeight - data.goalPostHeight)/2) + data.fieldMargin
    y12 = y02 + data.goalPostHeight
    return(x02, y02, x12, y12)
    
def drawSoccerField(canvas, data):
    for col in range(data.cols):
        x0, y0, x1, y1 = getColBounds(col, data)
        if(col % 2 == 1):
            data.fieldColor = "lime green"
        elif(col % 2 == 0):
            data.fieldColor = "chartreuse"
        canvas.create_rectangle(x0, y0, x1, y1, fill = data.fieldColor, 
                                                outline = data.fieldColor)

def drawOutFieldBox(canvas, data):
    x0 = data.fieldMargin
    y0 = data.fieldMargin
    x1 = data.width - data.fieldMargin
    y1 = data.height - data.fieldMargin
    canvas.create_rectangle(x0, y0, x1, y1, fill = None, width = 5, 
                                                         outline = "white")

def drawCentreLine(canvas, data):
    x0 = data.width/2
    x1 = data.width/2
    y0 = data.fieldMargin
    y1 = data.height - data.fieldMargin
    canvas.create_line(x0, y0, x1, y1, width = 5, fill = "white")
    
def drawCentreSpot(canvas, data):
    x0 = data.width/2 - data.spotKickRadius
    y0 = data.height/2 - data.spotKickRadius
    x1 = data.width/2 + data.spotKickRadius
    y1 = data.height/2 + data.spotKickRadius
    canvas.create_oval(x0, y0, x1, y1, fill = "white", outline = "white")

def drawCentreCircle(canvas, data):
    x0 = data.width/2 - data.centreCircleRadius
    y0 = data.height/2 - data.centreCircleRadius
    x1 = data.width/2 + data.centreCircleRadius
    y1 = data.height/2 + data.centreCircleRadius
    canvas.create_oval(x0, y0, x1, y1, width = 5, outline = "white")
    
def draw18YardBoxes(canvas, data):
    x01, y01, x11, y11 = getLeft18YardBoxBounds(data)
    canvas.create_rectangle(x01, y01, x11, y11, width = 5, outline = "white")
    x02, y02, x12, y12 = getRight18YardBoxBounds(data)
    canvas.create_rectangle(x02, y02, x12, y12, width = 5, outline = "white")
    
def draw6YardBoxes(canvas, data):
    x01, y01, x11, y11 = getLeft6YardBoxBounds(data)
    canvas.create_rectangle(x01, y01, x11, y11, width = 5, outline = "white")
    x02, y02, x12, y12 = getRight6YardBoxBounds(data)
    canvas.create_rectangle(x02, y02, x12, y12, width = 5, outline = "white")

def drawLeftSpotKick(canvas, data):
    # 18 Yard and 6 yardBox coords
    Ex01, Ey01, Ex11, Ey11 = getLeft18YardBoxBounds(data)
    Sx01, Sy01, Sx11, Sy11 = getLeft6YardBoxBounds(data)
    # centreY is same as centre of 18 Yardbox
    cY = (Ey01 + Ey11)/2
    cX = (Sx11 + Ex11)/2
    x0 = cX - data.spotKickRadius
    x1 = cX + data.spotKickRadius
    y0 = cY - data.spotKickRadius
    y1 = cY + data.spotKickRadius
    canvas.create_oval(x0, y0, x1, y1, fill = "white", outline = "white")
    
def drawRightSpotKick(canvas, data):
    Ex02, Ey02, Ex12, Ey12 = getRight18YardBoxBounds(data)
    Sx02, Sy02, Sx12, Sy12 = getRight6YardBoxBounds(data)
    cY = (Ey02 + Ey12)/2
    cX = (Sx02 + Ex02)/2
    x0 = cX - data.spotKickRadius
    x1 = cX + data.spotKickRadius
    y0 = cY - data.spotKickRadius
    y1 = cY + data.spotKickRadius
    canvas.create_oval(x0, y0, x1, y1, fill = "white", outline = "white")

def drawGoalPosts(canvas, data):
    # goalPost1
    x01, y01, x11, y11 = getLeftGoalPostBounds(data)
    canvas.create_rectangle(x01, y01, x11, y11, width = 5, outline = "white")
    # goalPost2
    x02, y02, x12, y12 = getRightGoalPostBounds(data)
    canvas.create_rectangle(x02, y02, x12, y12, width = 5, outline = "white")
    
def drawPassesLeft(canvas, data):
    x0 = data.fieldMargin
    y0 = data.fieldMargin
    x1 = data.width - data.fieldMargin
    y1 = data.height - data.fieldMargin
    textX = (x0 + (x1/2))/2
    textY = data.fieldMargin/2
    text = "Passes Left : %d" % data.passesLeft
    canvas.create_text(textX, textY, text = text, font = "Arial 15")
    

def drawScore(canvas, data):
    x0 = data.fieldMargin
    y0 = data.fieldMargin
    x1 = data.width - data.fieldMargin
    y1 = data.height - data.fieldMargin
    difference = x1 - (x1-x0)/2
    textX = data.width/2 + (difference/2)
    textY = data.fieldMargin/2
    text = "Total Score: %d" % data.score
    canvas.create_text(textX, textY, text = text, font = "Arial 15")
    
def drawField(canvas, data):
    drawSoccerField(canvas, data)
    drawOutFieldBox(canvas, data)
    drawCentreLine(canvas, data)
    drawCentreSpot(canvas, data)
    drawCentreCircle(canvas, data)
    draw18YardBoxes(canvas, data)
    draw6YardBoxes(canvas, data)
    drawLeftSpotKick(canvas, data)
    drawRightSpotKick(canvas, data)
    drawGoalPosts(canvas, data)
    drawPassesLeft(canvas, data)
    drawScore(canvas, data)
    
    
##### Common Helper Functions across all levels of the game #####

def getMidfielderBounds(data):
    x0 = data.mX - data.playerRadius
    x1 = data.mX + data.playerRadius
    y0 = data.mY - data.playerRadius
    y1 = data.mY + data.playerRadius
    return(x0, y0, x1, y1)

def getStrikerBounds(data):
    x0 = data.sX - data.playerRadius
    x1 = data.sX + data.playerRadius
    y0 = data.sY - data.playerRadius
    y1 = data.sY + data.playerRadius
    return(x0, y0, x1, y1)
    
def getDefenderBounds(data):
    x0 = data.dX - data.playerRadius
    x1 = data.dX + data.playerRadius
    y0 = data.dY - data.playerRadius
    y1 = data.dY + data.playerRadius
    return(x0, y0, x1, y1)

def getBallBounds(data):
    x0 = data.bX - data.ballRadius
    x1 = data.bX + data.ballRadius
    y0 = data.bY - data.ballRadius
    y1 = data.bY + data.ballRadius
    return(x0, y0, x1, y1)
    
def drawLevel1(canvas, data):
    drawPlayersLevel1(canvas, data)
    drawBall(canvas, data)
    
def drawPlayersLevel1(canvas, data):
    # midfielder
    x0, y0, x1, y1 = getMidfielderBounds(data)
    canvas.create_oval(x0, y0, x1, y1, fill = data.teamColors[0])
    textX = (x0 + x1)/2
    textY = (y0 + y1)/2
    canvas.create_text(textX, textY, text = "M")
    # striker
    x0, y0, x1, y1 = getStrikerBounds(data)
    canvas.create_oval(x0, y0, x1, y1, fill = data.teamColors[0])
    textX = (x0 + x1)/2
    textY = (y0 + y1)/2
    canvas.create_text(textX, textY, text = "S")
    # defender
    x0, y0, x1, y1 = getDefenderBounds(data)
    canvas.create_oval(x0, y0, x1, y1, fill = data.teamColors[1])
    textX = (x0 + x1)/2
    textY = (y0 + y1)/2
    canvas.create_text(textX, textY, text = "D")

def drawBall(canvas, data):
    x0, y0, x1, y1 = getBallBounds(data)
    canvas.create_oval(x0, y0, x1, y1, outline = "black", fill = "white")
    
def drawRoundWin(canvas, data):
    textX = data.width/2
    textY = data.height/4
    text = "YOU WIN ROUND %d" % (data.round)
    canvas.create_text(textX, textY, text = text, fill = "Black",
                       font = "Arial 50 bold")
    text = "Click anywhere to continue, 'r' to restart..."
    canvas.create_text(textX, textY + data.roundOverTextMargin, text = text,
                       fill = "Black", font = "Arial 25 bold")
                       
def drawRoundLose(canvas, data):
    textX = data.width/2
    textY = data.height/4
    text = "YOU LOSE ROUND %d" % (data.round)
    canvas.create_text(textX, textY, text = text, fill = "Black",
                       font = "Arial 50 bold")
    text = "Press 'r' to restart..."
    canvas.create_text(textX, textY + data.roundOverTextMargin, text = text,
                       fill = "Black", font = "Arial 25 bold")

def midfielderNearBall(data):
    xDistance = (abs(data.bX - data.mX))**2
    yDistance = (abs(data.bY - data.mY))**2
    totalDistance = (xDistance + yDistance)**0.5
    return totalDistance <= data.playerRadius + data.ballRadius
           
def defenderNearBall(data):
    xDistance = (abs(data.bX - data.dX))**2
    yDistance = (abs(data.bY - data.dY))**2
    totalDistance = (xDistance + yDistance)**0.5
    return totalDistance <= data.playerRadius + data.ballRadius
           
def strikerNearBall(data):
    xDistance = (abs(data.bX - data.sX))**2
    yDistance = (abs(data.bY - data.sY))**2
    totalDistance = (xDistance + yDistance)**0.5
    return totalDistance <= data.playerRadius + data.ballRadius
           
def midFielderControls(event, data):
    if(midfielderNearBall(data)):
        if(event.keysym == "Left"):
            data.mX = (data.mX - 10) % data.width
            data.bX = (data.bX - 10) % data.width
        elif(event.keysym == "Right"):
            data.mX = (data.mX + 10) % data.width
            data.bX = (data.bX + 10) % data.width
        elif(event.keysym == "Up"):
            data.mY = (data.mY - 10) % data.height
            data.bY = (data.bY - 10) % data.height
        elif(event.keysym == "Down"):
            data.mY = (data.mY + 10) % data.height
            data.bY = (data.bY + 10) % data.height
            
def clearBall(data):
    if(0 <= data.dY < data.height/2):
        data.newPassX = random.randint(0, data.width)
        data.newPassY = random.randint(0, data.fieldMargin)
        data.moveBall = True
    if(data.height/2 <= data.dY <= data.height):
        data.newPassX = random.randint(0, data.width)
        data.newPassY = random.randint(data.height - data.fieldMargin, data.height)
        data.moveBall = True
        
def winRound1(data):
    x0, y0, x1, y1 = getRightGoalPostBounds(data)
    if((y0 <= data.bY <= y1) and (x0 <= data.bX <= x1)
      and (0 <= data.passesLeft < 3) and (data.gamePlayLevel1 == True)) :
        return True
    else: return False
    
def loseRound1(data):
    x0, y0, x1, y1 = getRightGoalPostBounds(data)
    if(ballOutOfPlay(data) or losePossession(data)):
        return True
    # if minimum pass requirement is not met
    elif((data.passesLeft >= 3) and (y0 <= data.bY <= y1) and 
        (x0 <= data.bX <= x1)):
            return True
    # if you have exceeded max passes
    if(data.passesLeft < 0):
        return True
    else: return False
    
def ballOutOfPlay(data):
    if((0 < data.bY < data.fieldMargin) or 
       (data.height - data.fieldMargin < data.bY < data.height)or
       (0 < data.bX < data.fieldMargin) or
       (data.width - data.fieldMargin < data.bX < data.width)):
           return True
    else: return False

def losePossession(data):
    if((midfielderNearBall(data) == False) 
      and (defenderNearBall(data) == False)
      and (strikerNearBall(data) == False)
      and (data.moveBall == False)
      and (data.moveDefender == False)
      and (data.moveStriker == False)):
          return True
    else: return False

#### Level1 Mode ####

def level1MousePressed(event, data):
    if(data.round1Over == True):
        data.mode = "L2Objective"
        level2(data)
    data.newPassX, data.newPassY = event.x , event.y
    
def level1KeyPressed(event, data):
    if(event.keysym == "b"):
        data.mode = "L1Objective"
    if(event.keysym == "r"):
        level1(data)
    if(data.level1Player == "midfielder"):
        midFielderControls(event, data)
    if(event.keysym == "space"):
        data.gamePlayLevel1 = True
        # reduce number of passes left
        if(data.passesLeft > 0):
            data.passesLeft -= 1
        # if the midfielder/striker passes the ball, move the other players
        if(midfielderNearBall(data) and data.level1Player == "midfielder"):
            data.m1Passes += 1
            data.moveBall = True
            data.moveDefender = True
            data.moveStriker = True
        elif(strikerNearBall(data) and data.level1Player == "striker"):
            data.s1Passes += 1
            data.moveBall = True
    
def level1TimerFired(data):
    if(data.round1Over == True) or (data.round1Over == False):
        data.level1Player = None
    if(winRound1(data) and data.round1Over == None):
        data.moveDefender = False
        data.moveStriker = False
        data.round1Over = True
        roundScore = 5*data.passesLeft
        # tabulate score at the end of the round
        if(data.score == 0):
            data.score += (5*data.passesLeft)
        elif(roundScore < data.highScore1) and (roundScore > data.score):
            data.score = roundScore
        elif(roundScore < data.highScore1) and (roundScore < data.score):
            data.score = data.score
        elif(roundScore == data.highScore1):
            data.score = data.highScore1
    if(loseRound1(data) and data.round1Over == None):
        data.moveDefender = False
        data.moveStriker = False
        data.round1Over = False
    # if the ball has reached the point you want to pass to
    # stop moving the ball 
    if(almostEqual(data.bX, data.newPassX) and 
      (almostEqual(data.bY, data.newPassY))):
          data.moveBall = False
    # movement of ball and players
    if(data.moveBall == True):
        xDistance = data.newPassX - data.bX
        yDistance = data.newPassY - data.bY
        deltaX = xDistance/3
        deltaY = yDistance/3
        data.bX += deltaX
        data.bY += deltaY
    if(data.moveDefender == True):
        xDistance = data.newPassX - data.dX
        yDistance = data.newPassY - data.dY
        deltaX = xDistance/data.defenderSpeed
        deltaY = yDistance/data.defenderSpeed 
        data.dX += deltaX
        data.dY += deltaY
    if(data.moveStriker == True):
        xDistance = data.newPassX - data.sX
        yDistance = data.newPassY - data.sY
        deltaX = xDistance/data.strikerSpeed
        deltaY = yDistance/data.strikerSpeed 
        data.sX += deltaX
        data.sY += deltaY
    # stop player movement when any of the players intercept the ball
    if(defenderNearBall(data)):
        if(data.level1Player == "midfielder"):
            data.m1MissedPasses += 1
        if(data.level1Player == "striker"):
            data.s1MissedPasses += 1
        clearBall(data)
        data.level1Interceptions += 1
        data.moveDefender = False
        data.moveStriker = False
    elif(strikerNearBall(data)):
        data.level1Player = "striker"
        data.moveDefender = False
        data.moveStriker = False
    elif(midfielderNearBall(data)):
        data.level1Player = "midfielder"

    
def level1RedrawAll(canvas, data):
    drawField(canvas, data)
    drawLevel1(canvas, data)
    if(data.round1Over == True): drawRoundWin(canvas, data)
    if(data.round1Over == False): drawRoundLose(canvas, data)
    
##### DRAW LEVEL2 #####
    
def drawLevel2(canvas, data):
    drawPlayersLevel2(canvas, data)
    drawBallLevel2(canvas, data)
    
def drawPlayersLevel2(canvas, data):
    # midfielder
    x0, y0, x1, y1 = getMidfielderBounds(data)
    canvas.create_oval(x0, y0, x1, y1, fill = data.teamColors[0])
    textX = (x0 + x1)/2
    textY = (y0 + y1)/2
    canvas.create_text(textX, textY, text = "M")
    # striker
    x0, y0, x1, y1 = getStrikerBounds(data)
    canvas.create_oval(x0, y0, x1, y1, fill = data.teamColors[0])
    textX = (x0 + x1)/2
    textY = (y0 + y1)/2
    canvas.create_text(textX, textY, text = "S")
    # defender
    x0, y0, x1, y1 = getDefenderBounds(data)
    canvas.create_oval(x0, y0, x1, y1, fill = data.teamColors[1])
    textX = (x0 + x1)/2
    textY = (y0 + y1)/2
    canvas.create_text(textX, textY, text = "D")

def drawBallLevel2(canvas, data):
    x0, y0, x1, y1 = getBallBounds(data)
    canvas.create_oval(x0, y0, x1, y1, outline = "black", fill = "white")
    
#### Level 2 Functions ####

# random movement of striker and defender while trying to receive
# the ball from the midfielder

def moveStrikerAndDefender(data):
    xDistance = data.newPosX - data.sX
    yDistance = data.newPosY - data.sY
    deltaX = xDistance/data.strikerSpeed
    deltaY = yDistance/data.strikerSpeed
    data.sX += deltaX
    data.sY += deltaY
    data.dX = data.sX + data.playerRadius + data.strikerMarking
    dY0 = data.sY - data.playerRadius - data.strikerMarking
    dY1 = data.sY + data.playerRadius + data.strikerMarking
    data.dY = random.randint(int(dY0), int(dY1))
    
# position the defender between the 2 players so a pass can't be made
    
def intelligentDefender(data):
    newX = int((data.newMidfielderX + data.sX)/2)
    newY = int((data.newMidfielderY + data.sY)/2)
    xDistance = newX - data.dX
    yDistance = newY - data.dY
    deltaX = xDistance/data.defenderSpeed
    deltaY = yDistance/data.defenderSpeed
    data.dX += deltaX
    data.dY += deltaY
    
def distanceDefender(data):
    xDistance = (data.newPassX - data.dX)**2
    yDistance = (data.newPassY - data.dY)**2
    totalDistance = (xDistance + yDistance)**0.5
    return totalDistance
    
def distanceStriker(data):
    xDistance = (data.newPassX - data.sX)**2
    yDistance = (data.newPassY - data.sY)**2
    totalDistance = (xDistance + yDistance)**0.5
    return totalDistance
    
def winRound2(data):
    x0, y0, x1, y1 = getRightGoalPostBounds(data)
    if((y0 <= data.bY <= y1) and (x0 <= data.bX <= x1)
      and (0 <= data.passesLeft < 3) and (data.gamePlayLevel2 == True)) :
        return True
    else: return False
    
def loseRound2(data):
    x0, y0, x1, y1 = getRightGoalPostBounds(data)
    if(ballOutOfPlay(data) or losePossessionLevel2(data)):
        return True
    elif((data.passesLeft >= 3) and (y0 <= data.bY <= y1) and 
        (x0 <= data.bX <= x1)):
            return True
    if(data.passesLeft < 0):
        return True
    else: return False

def losePossessionLevel2(data):
    if((midfielderNearBall(data) == False) 
      and (defenderNearBall(data) == False)
      and (strikerNearBall(data) == False)
      and (data.moveBall == False)
      and (data.moveDefender == False)
      and (data.moveStriker == False)
      and (data.moveMidfielder == False)):
          return True
    else: return False

        
#### Level2 Mode ####

def level2MousePressed(event, data):
    if(data.round2Over == True):
        data.mode = "L3Objective"
        level3(data)
    data.newPassX, data.newPassY = event.x , event.y
    
def level2KeyPressed(event, data):
    if(event.keysym == "b"):
        data.mode = "L2Objective"
    if(event.keysym == "r"):
        level2(data)
    if(data.level2Player == "midfielder"):
        # movement of midfielder
        midFielderControls(event, data)
    if(event.keysym == "space"):
        data.gamePlayLevel2 = True
        if(data.passesLeft > 0):
            data.passesLeft -= 1
        if(midfielderNearBall(data) and data.level2Player == "midfielder"):
            data.m2Passes += 1
            data.moveMidfielder = True
            data.moveBall = True
            data.moveDefender = True
            data.moveStriker = True
        elif(strikerNearBall(data) and data.level2Player == "striker"):
            data.s2Passes += 1
            data.moveBall = True
            data.newMidfielderX = data.newPassX
            data.newMidfielderY = data.newPassY
            data.moveMidfielder = True
            data.moveDefender = True

def level2TimerFired(data):
    data.round = 2
    if(winRound2(data) and data.round2Over == None):
        data.moveDefender = False
        data.moveStriker = False
        data.moveMidfielder = False
        data.round2Over = True
        roundScore = data.score + 5*data.passesLeft
        if(data.score == 0):
            data.score += (5*data.passesLeft)
        elif(roundScore < data.highScore2) and (roundScore > data.score):
            data.score = roundScore
        elif(roundScore < data.highScore2) and (roundScore < data.score):
            data.score = data.score
        elif(roundScore >= data.highScore2):
            data.score = data.highScore2
    if(loseRound2(data) and data.round2Over == None):
        data.moveDefender = False
        data.moveStriker = False
        data.moveMidfielder = False
        data.round2Over = False
    data.timerCount += 1
    # random movement of striker and defender in 18yard box
    if(data.gamePlayLevel2 == False):
        if(data.timerCount % 20 == 0):
            x0, y0, x1, y1 = getRight18YardBoxBounds(data)
            data.newPosX = random.randint(int(x0), int(x1))
            data.newPosY = random.randint(int(y0), int(y1))
            moveStrikerAndDefender(data)
    if(almostEqual(data.bX, data.newPassX) and 
      (almostEqual(data.bY, data.newPassY))):
          data.moveBall = False
    if(almostEqual(data.mX, data.newMidfielderX) and 
      (almostEqual(data.mY, data.newMidfielderY))):
          data.moveMidfielder = False
    if(data.moveBall == True):
        xDistance = data.newPassX - data.bX
        yDistance = data.newPassY - data.bY
        deltaX = xDistance/3
        deltaY = yDistance/3
        data.bX += deltaX
        data.bY += deltaY
    if(data.moveDefender == True):
        # defender calculates time it will take to intercept ball 
        # based on his speed and striker's speed
        timeDefender = distanceDefender(data)/data.defenderSpeed
        timeStriker = distanceStriker(data)/data.strikerSpeed
        # if he is faster, he will try to intercept ball (not 100% accurate)
        x0, y0, x1, y1 = getRightGoalPostBounds(data)
        if(timeDefender < timeStriker) or (y0 <= data.newPassY <= y1):
            xDistance = data.newPassX - data.dX
            yDistance = data.newPassY - data.dY
            deltaX = xDistance/data.defenderSpeed
            deltaY = yDistance/data.defenderSpeed
            data.dX += deltaX
            data.dY += deltaY
        # if not he positions himself such that you cant make a pass back
        # to your team player
        else:
            intelligentDefender(data)
    if(data.moveStriker == True):
        xDistance = data.newPassX - data.sX
        yDistance = data.newPassY - data.sY
        deltaX = xDistance/data.strikerSpeed
        deltaY = yDistance/data.strikerSpeed
        data.sX += deltaX
        data.sY += deltaY
    if(data.moveMidfielder == True):
        xDistance = data.newMidfielderX - data.mX
        yDistance = data.newMidfielderY - data.mY
        deltaX = xDistance/data.midfielderSpeed
        deltaY = yDistance/data.midfielderSpeed
        data.mX += deltaX
        data.mY += deltaY
    if(defenderNearBall(data)):
        if(data.level2Player == "midfielder"):
            data.m2MissedPasses += 1
        if(data.level2Player == "striker"):
            data.s2MissedPasses += 1
        clearBall(data)
        data.level2Interceptions += 1
        data.moveDefender = False
        data.moveStriker = False
    if(strikerNearBall(data)):
        data.level2Player = "striker"
        data.moveDefender = False
        data.moveStriker = False
    if(midfielderNearBall(data)):
        data.level2Player = "midfielder"
        data.moveDefender = False
        data.moveStriker = False
        data.moveMidfielder = False

def level2RedrawAll(canvas, data):
    drawField(canvas, data)
    drawLevel2(canvas, data)
    if(data.round2Over == True): drawRoundWin(canvas, data)
    if(data.round2Over == False): drawRoundLose(canvas, data)
    
    
#### Draw Level 3 ####
    
def getWingerBounds(data):
    x0 = data.wX - data.playerRadius
    x1 = data.wX + data.playerRadius
    y0 = data.wY - data.playerRadius
    y1 = data.wY + data.playerRadius
    return(x0, y0, x1, y1)
    
def getDefender1Bounds(data):
    x0 = data.d1X - data.playerRadius
    x1 = data.d1X + data.playerRadius
    y0 = data.d1Y - data.playerRadius
    y1 = data.d1Y + data.playerRadius
    return(x0, y0, x1, y1)

def getDefender2Bounds(data):
    x0 = data.d2X - data.playerRadius
    x1 = data.d2X + data.playerRadius
    y0 = data.d2Y - data.playerRadius
    y1 = data.d2Y + data.playerRadius
    return(x0, y0, x1, y1)

def drawLevel3(canvas, data):
    drawPlayersLevel3(canvas, data)
    drawBallLevel3(canvas, data)
    
def drawPlayersLevel3(canvas, data):
    # midfielder
    x0, y0, x1, y1 = getMidfielderBounds(data)
    canvas.create_oval(x0, y0, x1, y1, fill = data.teamColors[0])
    textX = (x0 + x1)/2
    textY = (y0 + y1)/2
    canvas.create_text(textX, textY, text = "M")
    # striker
    x0, y0, x1, y1 = getStrikerBounds(data)
    canvas.create_oval(x0, y0, x1, y1, fill = data.teamColors[0])
    textX = (x0 + x1)/2
    textY = (y0 + y1)/2
    canvas.create_text(textX, textY, text = "S")
    # winger 
    x0, y0, x1, y1 = getWingerBounds(data)
    canvas.create_oval(x0, y0, x1, y1, fill = data.teamColors[0])
    textX = (x0 + x1)/2
    textY = (y0 + y1)/2
    canvas.create_text(textX, textY, text = "W")
    # defender 1
    x0, y0, x1, y1 = getDefender1Bounds(data)
    canvas.create_oval(x0, y0, x1, y1, fill = data.teamColors[1])
    textX = (x0 + x1)/2
    textY = (y0 + y1)/2
    canvas.create_text(textX, textY, text = "D1")
    # defender 2
    x0, y0, x1, y1 = getDefender2Bounds(data)
    canvas.create_oval(x0, y0, x1, y1, fill = data.teamColors[1])
    textX = (x0 + x1)/2
    textY = (y0 + y1)/2
    canvas.create_text(textX, textY, text = "D2")

def drawBallLevel3(canvas, data):
    x0, y0, x1, y1 = getBallBounds(data)
    canvas.create_oval(x0, y0, x1, y1, outline = "black", fill = "white")
    
    
#### Level 3 Functions ####
           
def defender1NearBall(data):
    xDistance = (abs(data.bX - data.d1X))**2
    yDistance = (abs(data.bY - data.d1Y))**2
    totalDistance = (xDistance + yDistance)**0.5
    return totalDistance <= data.playerRadius + data.ballRadius
    
def defender2NearBall(data):
    xDistance = (abs(data.bX - data.d2X))**2
    yDistance = (abs(data.bY - data.d2Y))**2
    totalDistance = (xDistance + yDistance)**0.5
    return totalDistance <= data.playerRadius + data.ballRadius
    
def wingerNearBall(data):
    xDistance = (abs(data.bX - data.wX))**2
    yDistance = (abs(data.bY - data.wY))**2
    totalDistance = (xDistance + yDistance)**0.5
    return totalDistance <= data.playerRadius + data.ballRadius
            
def clearBallLevel3(data):
    if(0 <= data.d1Y < data.height/2) or (0 <= data.d2Y < data.height/2):
        data.newPassX = random.randint(0, data.width)
        data.newPassY = random.randint(0, data.fieldMargin)
        data.moveBall = True
    if((data.height/2 <= data.d1Y <= data.height) or 
       (data.height/2 <= data.d2Y <= data.height)):
        data.newPassX = random.randint(0, data.width)
        data.newPassY = random.randint(data.height - data.fieldMargin, data.height)
        data.moveBall = True
    
def moveStrikerAndDefender1(data):
    xDistance = data.newPosD1X - data.sX
    yDistance = data.newPosD1Y - data.sY
    deltaX = xDistance/data.strikerSpeed
    deltaY = yDistance/data.strikerSpeed
    data.sX += deltaX
    data.sY += deltaY
    data.d1X = data.sX + data.playerRadius + data.strikerMarking
    dY0 = data.sY - data.playerRadius - data.strikerMarking
    dY1 = data.sY + data.playerRadius + data.strikerMarking
    data.d1Y = random.randint(int(dY0), int(dY1))
    
def moveWingerAndDefender2(data):
    xDistance = data.newPosD2X - data.wX
    yDistance = data.newPosD2Y - data.wY
    deltaX = xDistance/data.wingerSpeed
    deltaY = yDistance/data.wingerSpeed
    data.wX += deltaX
    data.wY += deltaY
    data.d2X = data.wX + data.playerRadius + data.strikerMarking
    dY0 = data.wY - data.playerRadius - data.strikerMarking
    dY1 = data.wY + data.playerRadius + data.strikerMarking
    data.d2Y = random.randint(int(dY0), int(dY1))
    
def distanceWinger(data):
    xDistance = (data.newPassX - data.wX)**2
    yDistance = (data.newPassY - data.wY)**2
    totalDistance = (xDistance + yDistance)**0.5
    return totalDistance
    
def distanceMidfielder(data):
    xDistance = (data.newPassX - data.mX)**2
    yDistance = (data.newPassY - data.mY)**2
    totalDistance = (xDistance + yDistance)**0.5
    return totalDistance

def distanceDefender1(data):
    xDistance = (data.newPassX - data.d1X)**2
    yDistance = (data.newPassY - data.d1Y)**2
    totalDistance = (xDistance + yDistance)**0.5
    return totalDistance
    
def distanceDefender2(data):
    xDistance = (data.newPassX - data.d2X)**2
    yDistance = (data.newPassY - data.d2Y)**2
    totalDistance = (xDistance + yDistance)**0.5
    return totalDistance
    
def defenderDistanceComparison(data):
    if(distanceDefender1(data) < distanceDefender2(data)):
        data.moveDefender1 = True
    else:
        data.moveDefender2 = True
    
def intelligentDefender1(data):
    newX = int((data.newMidfielderX + data.sX)/2)
    newY = int((data.newMidfielderY + data.sY)/2)
    xDistance = newX - data.d1X
    yDistance = newY - data.d1Y
    deltaX = xDistance/data.defender1Speed
    deltaY = yDistance/data.defender1Speed
    data.d1X += deltaX
    data.d1Y += deltaY

def intelligentDefender2(data):
    newX = int((data.newMidfielderX + data.wX)/2)
    newY = int((data.newMidfielderY + data.wY)/2)
    xDistance = newX - data.d2X
    yDistance = newY - data.d2Y
    deltaX = xDistance/data.defender2Speed
    deltaY = yDistance/data.defender2Speed
    data.d2X += deltaX
    data.d2Y += deltaY
    
def winRound3(data):
    x0, y0, x1, y1 = getRightGoalPostBounds(data)
    if((y0 <= data.bY <= y1) and (x0 <= data.bX <= x1)
      and (0 <= data.passesLeft <= 3) and (data.gamePlayLevel3 == True)) :
        return True
    else: return False
    
def loseRound3(data):
    x0, y0, x1, y1 = getRightGoalPostBounds(data)
    if(ballOutOfPlay(data) or losePossessionLevel3(data)):
        return True
    elif((data.passesLeft > 3) and (y0 <= data.bY <= y1) and 
        (x0 <= data.bX <= x1)):
            return True
    if(data.passesLeft < 0):
        return True
    else: return False

def losePossessionLevel3(data):
    # None of the players have the ball and all the 
    # players stop movement
    if((midfielderNearBall(data) == False) 
      and (defender1NearBall(data) == False)
      and (defender2NearBall(data) == False)
      and (strikerNearBall(data) == False)
      and (wingerNearBall(data) == False)
      and (data.moveBall == False)
      and (data.moveDefender == False)
      and (data.moveStriker == False)
      and (data.moveMidfielder == False)
      and (data.moveDefender1 == False)
      and (data.moveDefender2 == False)):
          return True
    else: return False
    
    
#### Level3 Mode ####

def level3MousePressed(event, data):
    if(data.round3Over == True):
        data.mode = "finalStat"
    data.newPassX, data.newPassY = event.x , event.y
    
def level3KeyPressed(event, data):
    if(event.keysym == "b"):
        data.mode = "L3Objective"
    if(event.keysym == "r"):
        level3(data)
    if(event.keysym == "q"):
        data.mode = "finalStat"
    # player controls
    if(data.level3Player == "midfielder"):
        midFielderControls(event, data)
    
    # when you start playing the game
    if(event.keysym == "space"):
        data.gamePlayLevel3 = True
        if(data.passesLeft > 0):
            data.passesLeft -= 1
        # where the midfielder has to move after he passes the ball
        if(midfielderNearBall(data) and data.level3Player == "midfielder"):
            data.moveMidfielder = True
            data.moveBall = True
            data.m3Passes += 1
            if(distanceStriker(data) < distanceWinger(data)):
                data.newMidfielderX = data.sX
                data.newMidfielderY3 = data.sY
                data.newStrikerX = data.newPassX
                data.newStrikerY = data.newPassY
                data.moveStriker = True
                defenderDistanceComparison(data)
                
            elif(distanceWinger(data) < distanceStriker(data)):
                data.newMidfielderX = data.wX
                data.newMidfielderY = data.wY
                data.newWingerX = data.newPassX
                data.newWingerY = data.newPassY
                data.moveWinger = True
                defenderDistanceComparison(data)
        
        # where the striker has to move after he passes the ball
        if(strikerNearBall(data) and data.level3Player == "striker"):
            data.moveStriker = True
            data.moveBall = True
            data.s3Passes += 1
            if(distanceMidfielder(data) < distanceWinger(data)):
                data.newStrikerX = data.mX
                data.newStrikerY = data.mY
                data.newMidfielderX = data.newPassX
                data.newMidfielderY = data.newPassY
                data.moveMidfielder = True
                defenderDistanceComparison(data)
                    
            elif(distanceMidfielder(data) > distanceWinger(data)):
                data.newStrikerX = data.wX
                data.newStrikerY = data.wY
                data.newWingerX = data.newPassX
                data.newWingerY = data.newPassY
                data.moveWinger = True
                defenderDistanceComparison(data)
                
        # where the striker has to move after he passes the ball
        if(wingerNearBall(data) and data.level3Player == "winger"):
            data.moveWinger = True
            data.moveBall = True
            data.w3Passes += 1
            if(distanceMidfielder(data) < distanceStriker(data)):
                data.newWingerX = data.mX
                data.newWingerY = data.mY
                data.newMidfielderX = data.newPassX
                data.newMidfielderY = data.newPassY
                data.moveMidfielder = True
                defenderDistanceComparison(data)
                    
            elif(distanceMidfielder(data) > distanceStriker(data)):
                data.newWingerX = data.sX
                data.newWingerY = data.sY
                data.newStrikerX = data.newPassX
                data.newStrikerY = data.newPassY
                data.moveStriker = True
                defenderDistanceComparison(data)
                

def level3TimerFired(data):
    if(data.gamePlayLevel3 == False):
        data.passesLeft = 8
    data.round = 3
    if(almostEqual(data.bX, data.newPassX) and 
      (almostEqual(data.bY, data.newPassY))):
          data.moveBall = False
    data.timerCount += 1
    if(winRound3(data) and data.round3Over == None):
        data.moveDefender1 = False
        data.moveDefender2 = False
        data.moveStriker = False
        data.moveMidfielder = False
        data.moveWinger = False
        data.round3Over = True
        roundScore = data.score + 5*data.passesLeft
        if(data.score == 0):
            data.score += (5*data.passesLeft)
        elif(roundScore < data.highScore3) and (roundScore > data.score):
            data.score = roundScore
        elif(roundScore < data.highScore3) and (roundScore < data.score):
            data.score = data.score
        elif(roundScore >= data.highScore3):
            data.score = data.highScore3
    if(loseRound3(data) and data.round3Over == None):
        data.moveDefender1 = False
        data.moveDefender2 = False
        data.moveStriker = False
        data.moveMidfielder = False
        data.moveWinger = False
        data.round3Over = False
    # random movement of striker and defender 
    if(data.gamePlayLevel3 == False):
        if(data.timerCount % 20 == 0):
            x0, y0, x1, y1 = getRight18YardBoxBounds(data)
            data.newPosD1X = random.randint(int(x0), int(x1))
            data.newPosD2X = random.randint(int(x0), int(x1))
            data.newPosD1Y = random.randint(int(y0), int(y0 + (y1-y0)/2))
            data.newPosD2Y = random.randint(int(y1 - (y1-y0)/2), int(y1))
            moveStrikerAndDefender1(data)
            moveWingerAndDefender2(data)
    
    if(data.moveBall == True):
        xDistance = data.newPassX - data.bX
        yDistance = data.newPassY - data.bY
        deltaX = xDistance/3
        deltaY = yDistance/3
        data.bX += deltaX
        data.bY += deltaY
        
    #############################################
    
    if(data.moveStriker == True):
        xDistance = data.newPassX - data.sX
        yDistance = data.newPassY - data.sY
        deltaX = xDistance/data.strikerSpeed
        deltaY = yDistance/data.strikerSpeed
        data.sX += deltaX
        data.sY += deltaY
    
    # AI defender 1 movements
    if(data.moveDefender1 == True):
        timeDefender1 = distanceDefender1(data)/data.defender1Speed
        timeStriker = distanceStriker(data)/data.strikerSpeed
        x0, y0, x1, y1 = getRightGoalPostBounds(data)
        if(timeDefender1 < timeStriker) or (y0 <= data.newPassY <= y1):
            xDistance = data.newPassX - data.d1X
            yDistance = data.newPassY - data.d1Y
            deltaX = xDistance/data.defender1Speed
            deltaY = yDistance/data.defender1Speed
            data.d1X += deltaX
            data.d1Y += deltaY
        else:
            intelligentDefender1(data)
            
    # AI defender 2 movements
    if(data.moveDefender2 == True):
        timeDefender2 = distanceDefender2(data)/data.defender2Speed
        timeWinger = distanceWinger(data)/data.wingerSpeed
        x0, y0, x1, y1 = getRightGoalPostBounds(data)
        if(timeDefender2 < timeWinger) or (y0 <= data.newPassY <= y1):
            xDistance = data.newPassX - data.d2X
            yDistance = data.newPassY - data.d2Y
            deltaX = xDistance/data.defender2Speed
            deltaY = yDistance/data.defender2Speed
            data.d2X += deltaX
            data.d2Y += deltaY
        else:
            intelligentDefender2(data)
            
    # where each player has to move if they move
    if(data.moveStriker == True):
        xDistance = data.newStrikerX - data.sX
        yDistance = data.newStrikerY - data.sY
        deltaX = xDistance/data.strikerSpeed
        deltaY = yDistance/data.strikerSpeed
        data.sX += deltaX
        data.sY += deltaY
    if(data.moveWinger == True):
        xDistance = data.newWingerX - data.wX
        yDistance = data.newWingerY - data.wY
        deltaX = xDistance/data.wingerSpeed
        deltaY = yDistance/data.wingerSpeed
        data.wX += deltaX
        data.wY += deltaY
    if(data.moveMidfielder == True):
        xDistance = data.newMidfielderX - data.mX
        yDistance = data.newMidfielderY - data.mY
        deltaX = xDistance/data.midfielderSpeed
        deltaY = yDistance/data.midfielderSpeed
        data.mX += deltaX
        data.mY += deltaY
        
    # Which players stop moving when another player or AI takes control
    if(strikerNearBall(data)):
        data.level3Player = "striker"
        data.moveDefender1 = False
        data.moveDefender2 = False
        data.moveStriker = False
        data.moveMidfielder = False
        data.moveWinger = False
    if(wingerNearBall(data)):
        data.level3Player = "winger"
        data.moveDefender2 = False
        data.moveDefender1 = False
        data.moveWinger = False
        data.moveStriker = False
        data.moveWinger = False
    if(defender1NearBall(data)):
        if(data.level3Player == "midfielder"):
            data.m3MissedPasses += 1
        if(data.level3Player == "striker"):
            data.s3MissedPasses += 1
        if(data.level3Player == "winger"):
            data.w3MissedPasses += 1
        clearBallLevel3(data)
        data.level3Interceptions += 1
        data.moveDefender1 = False
        data.moveStriker = False
        data.moveDefender2 = False
        data.moveWinger = False
    if(defender2NearBall(data)):
        if(data.level3Player == "midfielder"):
            data.m3MissedPasses += 1
        if(data.level3Player == "striker"):
            data.s3MissedPasses += 1
        if(data.level3Player == "winger"):
            data.w3MissedPasses += 1
        clearBallLevel3(data)
        data.level3Interceptions += 1
        data.moveDefender2 = False
    if(midfielderNearBall(data)):
        data.level3Player = "midfielder"
        data.moveMidfielder = False
        data.moveDefender1 = False
        data.moveDefender2 = False
        data.moveStriker = False
        data.moveWinger = False
        
def level3RedrawAll(canvas, data):
    drawField(canvas, data)
    drawLevel3(canvas, data)
    if(data.round3Over == True): drawRoundWin(canvas, data)
    if(data.round3Over == False): drawRoundLose(canvas, data)
    

#### finalStat Mode ####
def getBoxBounds(row, col, data):
    tableWidth = data.width - (2*data.tableMargin)
    tableHeight = data.height - (2*data.tableMargin)
    boxWidth = tableWidth / data.boxCols
    boxHeight = tableHeight / data.boxRows
    x0 = data.tableMargin + col * boxWidth
    x1 = data.tableMargin + (col+1) * boxWidth
    y0 = data.tableMargin + row * boxHeight
    y1 = data.tableMargin + (row+1) * boxHeight
    return (x0, y0, x1, y1)


def finalStatMousePressed(event, data):
    pass
    
def finalStatKeyPressed(event, data):
    pass
    
def finalStatTimerFired(data):
    pass
    
def finalStatRedrawAll(canvas, data):
    drawStatisticsBackground(canvas, data)
    drawStatisticsTitle(canvas, data)
    drawStatisticsTable(canvas, data)
    drawTableInput(canvas, data)
    

def drawStatisticsBackground(canvas, data):
    canvas.create_image(0, 0, anchor = NW, image = data.statBackground)
    
def drawStatisticsTitle(canvas, data):
    textX = data.width/2
    textY = data.statTitleMargin
    text = "GAME STATISTICS"
    canvas.create_text(textX, textY, text = text,
                       fill = "White", font = "Arial 25 bold")
    
def drawStatisticsTable(canvas, data):
    for row in range(data.boxRows):
        for col in range(data.boxCols):
            x0, y0, x1, y1 = getBoxBounds(row, col, data)
            canvas.create_rectangle(x0, y0, x1, y1, fill = "lightBlue")
            
def drawTableInput(canvas, data):
    for row in range(data.boxRows):
        for col in range(data.boxCols):
            x0, y0, x1, y1 = getBoxBounds(row, col, data)
            textX = (x0 + x1)/2
            textY = (y0 + y1)/2
            text = decideText(row, col, data)
            canvas.create_text(textX, textY, text = text, 
                               font = "Arial 11 bold", fill = "black")
                    
def decideText(row, col, data):
    text = ""
    
    # col headings
    if(row == 0) and (col == 1):
        text = "Level 1"
    elif(row == 0) and (col == 2):
        text = "Level 2"
    elif(row == 0) and (col == 3):
        text = "Level 3"
        
    # row 1 values
    elif(row == 1) and (col == 0):
        text = "Interceptions"
    elif(row == 1) and (col == 1):
        text = "%d" % data.level1Interceptions
    elif(row == 1) and (col == 2):
        text = "%d" % data.level2Interceptions
    elif(row == 1) and (col == 3):
        text = "%d" % data.level3Interceptions
        
    # row 2 values
    elif(row == 2) and (col == 0):
        text = "Midfielder Passing Accuracy"
    elif(row == 2) and (col == 1):
        if(data.m1Passes == 0):
            text = "0"
        else:
            percentage = str(round(((data.m1Passes-data.m1MissedPasses)/data.m1Passes) * 100))
            text = percentage + "%"
    elif(row == 2) and (col == 2):
        if(data.m2Passes == 0):
            text = "0"
        else:
            percentage = str(round(((data.m2Passes-data.m2MissedPasses)/data.m2Passes) * 100))
            text = percentage + "%"
    elif(row == 2) and (col == 3):
        if(data.m3Passes == 0):
            text = "0"
        else:
            percentage = str(round(((data.m3Passes-data.m3MissedPasses)/data.m3Passes) * 100))
            text = percentage + "%"
            
    # row 3 values
    elif(row == 3) and (col == 0):
        text = "Striker Passing Accuracy"
    elif(row == 3) and (col == 1):
        if(data.s1Passes == 0):
            text = "0"
        else:
            percentage = str(round(((data.s1Passes-data.s1MissedPasses)/data.s1Passes) * 100))
            text = percentage + "%"
    elif(row == 3) and (col == 2):
        if(data.s2Passes == 0):
            text = "0"
        else:
            percentage = str(round(((data.s2Passes-data.s2MissedPasses)/data.s2Passes) * 100))
            text = percentage + "%"
    elif(row == 3) and (col == 3):
        if(data.s3Passes == 0):
            text = "0"
        else:
            percentage = str(round(((data.s3Passes-data.s3MissedPasses)/data.s3Passes) * 100))
            text = percentage + "%"
            
    # row 4 values
    elif(row == 4) and (col == 0):
        text = "Winger Passing Accuracy"
    elif(row == 4) and (col == 1):
        text = "-"
    elif(row == 4) and (col == 2):
        text = "-"
    elif(row == 4) and (col == 3):
        if(data.w3Passes == 0):
            text = "0"
        else:
            percentage = str(round(((data.w3Passes-data.w3MissedPasses)/data.w3Passes) * 100))
            text = percentage + "%"
    return text
    
    
    
####################################
# Test Functions
####################################

# test applies to striker, winger and defenders

def testmidfielderNearBall():
    print("Testing midfielderNearBall()...", end="")
    class Struct(object) : pass
    data = Struct()
    data.mX = 100
    data.mY = 200
    data.bX = 105
    data.bY = 205
    data.playerRadius = 20
    data.ballRadius = 15
    result = midfielderNearBall(data)
    assert(result == True)
    data.bX = 150
    data.bY = 250
    result = midfielderNearBall(data)
    assert(result == False)
    print('Passed.')
    
# test for winning other rounds are similar

def testWinRound1():
    print("Testing winRound1()...", end="")
    class Struct(object) : pass
    data = Struct()
    data.width = 1000
    data.height = 500
    data.fieldMargin = 35
    data.fieldHeight = data.height - (2*data.fieldMargin)
    data.sixYardBoxHeight = (data.height - (2*data.fieldMargin)) *(1/3)
    data.goalPostHeight = (1/3) * data.sixYardBoxHeight
    x0, y0, x1, y1 = getRightGoalPostBounds(data)
    data.passesLeft = 3
    data.gamePlayLevel1 = False
    data.bX = 975
    data.bY = 250
    assert(winRound1(data) == False)
    data.gamePlayLevel1 = True
    data.bX = 940
    data.bY = 200
    assert(winRound1(data) == False)
    data.passesLeft = 2
    data.bX = 975
    data.bY = 250
    assert(winRound1(data) == True)
    print("Passed.")
    
    
####################################
# use the run function as-is
####################################

# from event based animations lecture (15-112)
def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    root = Tk()
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 30 # milliseconds
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1000, 500)