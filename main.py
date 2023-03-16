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
        blank_str = ''
        for _ in word:
            blank_str += '_'
        blank_list.append(blank_str)
    return blank_list


def get_a_guess(chosen_list, guess_display):
    points = 0
    start = 0.0
    start = time.time()
    while guess_display != chosen_list:
        guess = input('Enter your guess: ')
        letter_is_correct = False
        # Check if
        for i in range(len(chosen_list)):
            letter_is_correct, points = check_if_letter_exists_in_word(chosen_list,
                                                                       guess,
                                                                       guess_display,
                                                                       i,
                                                                       letter_is_correct,
                                                                       points)
        if not letter_is_correct:
            print('wrong letter')
            points -= 1
        print(guess_display)
    end = time.time()
    if (end - start) < 30:
        points += 100
    return points


def check_if_letter_exists_in_word(chosen_list, guess, guess_display, i, letter_is_correct, points):
    word_len = len(chosen_list[i])
    if guess in chosen_list[i]:
        for j in range(word_len):
            if guess == chosen_list[i][j]:
                letter_is_correct, points = change_display_and_give_points(guess, guess_display, i, j, points)
    return letter_is_correct, points


def change_display_and_give_points(guess, guess_disp, i, j, points):
    guess_disp[i] = guess_disp[i][:j] + guess + guess_disp[i][j + 1:]
    letter_is_correct = True
    points += 5
    return letter_is_correct, points


def play_game():
    play = True
    while play:
        print('welcome to guess game, HAVE FUN:-)')
        selected_number = random.randint(0, 9)
        sentence = sentences_list[selected_number]
        display = create_blanc_list(sentence)
        print(display)
        points = get_a_guess(sentence, display)
        print(f'you won, your score is:{points}')
        play_again = input('Do you want to play again? press (y/n)')
        if play_again == 'n':
            play = False


play_game()
