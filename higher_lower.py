import random 
import os

data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 174,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 172,
        'description': 'Reality TV personality and businesswoman and Self-Made Billionaire',
        'country': 'United States'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 167,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 149,
        'description': 'Footballer',
        'country': 'Argentina'
    },
    {
        'name': 'Beyoncé',
        'follower_count': 145,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Neymar',
        'follower_count': 138,
        'description': 'Footballer',
        'country': 'Brasil'
    },
]

def get():
    return random.choice(data)

def print_data(account):
    name = account['name']
    desc = account['description']
    country = account['country']
    return f'{name}, {desc} from {country}'

def ask():
    user = input(" A or B : ").lower()
    return user

def compare(score, guess, a_followers, b_followers):
    if a_followers > b_followers and guess == 'a':
        score += 1
        print(f'Right! {score}')
    elif b_followers > a_followers and guess == 'b':
        score += 1
        print(f'Right! {score}')
    else:
        print(f'Wrong! Final Total ={score}')
    
    input("Press Enter to continue...")
    os.system('clear' if os.name == 'posix' else 'cls')

    return score


def game():
    score=0
    over = False
    a = get()
    b = get()

    while not over:
        a = b
        b = get()
        while a == b:
            b = get()
            
        print(f"Compare A: {print_data(a)}.")
        print('vs')
        print(f"Against B: {print_data(b)}.")
        

        guess = ask()
        a_follower_count = a['follower_count']
        b_follower_count = b['follower_count']
    

        score = compare(score, guess, a_follower_count, b_follower_count)
        

game()
