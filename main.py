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


def create_blank_list(sentence):
    """
    create blank list for the selected sentence
    :param sentence: randomly selected sentence for this round of the game.
    :return: blank list.
    """
    blank_list = []
    for word in sentence:
        blank_str = ''
        for _ in word:
            blank_str += '_'
        blank_list.append(blank_str)
    return blank_list


def get_a_guess(chosen_list, guess_display):
    """
    getting a guess from the user
    :param chosen_list: Randomly selected sentence for this round of the game.
    :param guess_display: The blanc list plus the changes, it used to display the status after guesses.
    :return: Points, the number of points the user gets.
    """
    points = 0
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
    """
    Check if the letter exists in the sentence.
    :param chosen_list: Randomly selected sentence for this round of the game.
    :param guess: The user guesses.
    :param guess_display: The blanc list plus the changes, it used to display the status after guesses.
    :param i: The index of the words in the sentences.
    :param letter_is_correct: flag to if the user guess is correct.
    :param points: The number of points the user gets.
    :return: letter_is_correct, points
    """
    word_len = len(chosen_list[i])
    if guess in chosen_list[i]:
        for j in range(word_len):
            if guess == chosen_list[i][j]:
                letter_is_correct, points = change_display_and_give_points(guess, guess_display, i, j, points)
    return letter_is_correct, points


def change_display_and_give_points(guess, guess_disp, i, j, points):
    """
    This function edits the words in case of a correct guess
    :param guess: The user guesses.
    :param guess_disp: The blanc list plus the changes, it used to display the status after guesses.
    :param i: The index of the words in the sentences.
    :param j: The index of the letter in any word.
    :param points: The number of points the user gets.
    :return: letter_is_correct, points
    """
    guess_disp[i] = guess_disp[i][:j] + guess + guess_disp[i][j + 1:]
    letter_is_correct = True
    points += 5
    return letter_is_correct, points


def play_game():
    """
    main function
    :return: none
    """
    play = True
    while play:
        print('welcome to guess game, HAVE FUN:-)')
        sentence = random.choice(sentences_list)
        display = create_blank_list(sentence)
        print(display)
        points = get_a_guess(sentence, display)
        print(f'you won, your score is:{points}')
        play_again = input('Do you want to play again? press (y/n)')
        if play_again == 'n':
            play = False


play_game()
