from uib_inf100_graphics import *
def app_started(app):
    app.message = "Tic Tac Toe"
    app.board = [[0,0,0],[0,0,0],[0,0,0]]
    app.player = 1
    app.game_over = False
    app.winner = None   

def draw_board(app,canvas):
    canvas.create_line(150,0,150,450)
    canvas.create_line(300,0,300,450)
    canvas.create_line(0,150,450,150)
    canvas.create_line(0,300,450,300)
    for i in range(3):
        for j in range(3):
            if app.board[i][j] == 1:
                draw_x(canvas,j*150,i*150)
            elif app.board[i][j] == 2:
                draw_o(canvas,j*150,i*150)
def mouse_pressed(app, event):
    print(event.x,event.y)
    if app.game_over:
        return
    if event.x < 150 and event.y < 150:
        app.board[0][0] = app.player
    elif event.x < 150 and event.y < 300:
        app.board[1][0] = app.player
    elif event.x < 150 and event.y < 450:
        app.board[2][0] = app.player
    elif event.x < 300 and event.y < 150:
        app.board[0][1] = app.player
    elif event.x < 300 and event.y < 300:
        app.board[1][1] = app.player
    elif event.x < 300 and event.y < 450:
        app.board[2][1] = app.player
    elif event.x < 450 and event.y < 150:
        app.board[0][2] = app.player
    elif event.x < 450 and event.y < 300:
        app.board[1][2] = app.player
    elif event.x < 450 and event.y < 450:
        app.board[2][2] = app.player
    check_winner(app)
    if app.player == 2:
        app.player = 1
    else:
        app.player = 2
    
def check_winner(app):
    for i in range(3):
        if app.board[i][0] == app.board[i][1] == app.board[i][2] != 0:
            app.game_over = True
            app.winner = app.board[i][0]
        if app.board[0][i] == app.board[1][i] == app.board[2][i] != 0:
            app.game_over = True
            app.winner = app.board[0][i]
    if app.board[0][0] == app.board[1][1] == app.board[2][2] != 0:
        app.game_over = True
        app.winner = app.board[0][0]
    if app.board[0][2] == app.board[1][1] == app.board[2][0] != 0:
        app.game_over = True
        app.winner = app.board[0][2]
    if app.game_over:
        app.message = "Player " + str(app.winner) + " won!"
def board_full(app):
    for i in range(3):
        for j in range(3):
            if app.board[i][j] == 0:
                return False
    return True

def draw_x(canvas,x,y):
    canvas.create_line(x,y,x+150,y+150,fill="red",width=10)
    canvas.create_line(x+150,y,x,y+150,fill="red",width=10)

def draw_o(canvas,x,y):
    canvas.create_oval(x,y,x+150,y+150,fill="blue",width=10)

def redraw_all(app,canvas):
    canvas.create_rectangle(0,0,450,450,fill="white")
    draw_board(app,canvas)
    canvas.create_text(225,470,text=app.message,fill="black",font="Arial 20 bold")
    canvas.create_text(225,500,text="Player " + str(app.player) + " turn",fill="black",font="Arial 20 bold")


run_app(width=450, height=520)

    
