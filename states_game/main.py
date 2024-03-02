import turtle as t
import pandas

screen = t.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
t.shape(image)

'''Already have the coor in a csv file'''
# def get_click_coor(x, y): #get coordinates of the click
#     print(x, y)

# t.onscreenclick(get_click_coor)
# t.mainloop() #keep screen open after click

data = pandas.read_csv("50_states.csv")
all_states = data['state'].to_list()
guessed = []

while len(guessed)<50:
    ans_state = screen.textinput(title = f'{len(guessed)}/50 correct', prompt = "What's a name of a State").title()

    if ans_state == 'Exit':
        missing = []
        for state in all_states:
            if state not in guessed:
                missing.append(state)
        print(missing)
        break
    if ans_state in all_states:
        guessed.append(ans_state)
        tur = t.Turtle()
        tur.hideturtle()
        tur.penup()
        state_data = data[data.state == ans_state]
        tur.goto(int(state_data.x), int(state_data.y))
        tur.write(ans_state)

        
screen.exitonclick()
    
