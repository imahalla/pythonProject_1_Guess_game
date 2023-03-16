import random
import time

sentences_list = [
    ['communicate', 'with', 'clarity'],
    ['believe', 'in', 'yourself'],
    ['believe', 'you', 'can'],
    ['do', 'your', 'best'],
    ['dreams', 'come', 'true'],
    ['love', 'is', 'everything'],
    ['life', 'is', 'beautiful'],
    ['remember', 'to', 'live'],
    ['set', 'clear', 'targets'],
    ['happiness', 'is', 'choice']
]


def create_blanc_list(list1):
    blank_list = []
    for word in list1:
        blank_list.append('')
        for letter in word:
            blank_list[-1] += '_'
    return blank_list


def get_a_guess(chosen_list, guess_disp):
    points = 0
    start = 0.0
    end = 0.0
    while guess_disp != chosen_list:
        guess = input('Enter your guess: ')
        start = time.time()
        list_len = len(chosen_list)
        flag = False
        for i in range(list_len):
            word_len = len(chosen_list[i])
            if guess in chosen_list[i]:
                for j in range(word_len):
                    if guess == chosen_list[i][j]:
                        guess_disp[i] = guess_disp[i][:j] + guess + guess_disp[i][j + 1:]
                        flag = True
                        points += 5
        if not flag:
            print('wrong letter')
            points -= 1
        print(guess_disp)
    end = time.time()
    if (end - start) < 30:
        points += 100
    print(f'your score is: {points}')
    return True


#  *** main program ***
play = 'y'
while play == 'y':
    print('welcome to guess game, HAVE FUN:-)')
    selected_number = random.randint(0, 9)
    display = create_blanc_list(sentences_list[selected_number])
    print(display)
    winner_or_loser = get_a_guess(sentences_list[selected_number], display)
    if winner_or_loser:
        print("you won")
    # else:
    #     print('you lost')
    play = input('Do you want to play again? press (y/n)')
