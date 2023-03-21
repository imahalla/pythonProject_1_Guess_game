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


def get_a_guess(chosen_list, guess_display, points):
    """
    getting a guess from the user
    :param points: The number of points the user gets.
    :param chosen_list: Randomly selected sentence for this round of the game.
    :param guess_display: The blanc list plus the changes, it used to display the status after guesses.
    :return: Points, the number of points the user gets.
    """
    guesses = ''
    start = time.time()
    while guess_display != chosen_list:
        guess = input('Enter your guess: ')
        guess = guess.lower()
        if guess not in guesses:
            if guess.isalpha() and len(guess) == 1:
                letter_is_correct = False
                guesses = guesses + guess
                for i in range(len(chosen_list)):
                    letter_is_correct = check_if_letter_exists_in_word(chosen_list,
                                                                       guess,
                                                                       guess_display,
                                                                       i,
                                                                       letter_is_correct)
                points = score(letter_is_correct, points)

            else:
                print('Guess is too long or is not a letter. Enter one letter')
                points -= 1
        else:
            print(f'you already used this letter:"{guess}" try another one.')
        print(guess_display)
        print(f'your score is:{points}')
    end = time.time()
    if (end - start) < 30:
        points += 100
        print(f'You have got 100 points BONUS!!!')
    return points


def score(letter_is_correct, points):
    """
    update the score of the user.
    :param letter_is_correct: flag to notify if the user guess is correct.
    :param points:The number of points the user gets.
    :return: points
    """
    if letter_is_correct:
        points += 5
    else:
        print('wrong letter')
        points -= 1
    return points


def check_if_letter_exists_in_word(chosen_list, guess, guess_display, i, letter_is_correct):
    """
    Check if the letter exists in the sentence.
    :param chosen_list: Randomly selected sentence for this round of the game.
    :param guess: The user guesses.
    :param guess_display: The blanc list plus the changes, it used to display the status after guesses.
    :param i: The index of the words in the sentences.
    :param letter_is_correct: flag to notify if the user guess is correct.
    :return: letter_is_correct
    """
    word_len = len(chosen_list[i])
    if guess in chosen_list[i]:
        for j in range(word_len):
            if guess == chosen_list[i][j]:
                letter_is_correct = change_display(guess, guess_display, i, j)
    return letter_is_correct


def change_display(guess, guess_disp, i, j):
    """
    This function edits the words in case of a correct guess
    :param guess: The user guesses.
    :param guess_disp: The blanc list plus the changes, it used to display the status after guesses.
    :param i: The index of the words in the sentences.
    :param j: The index of the letter in any word.
    :return: letter_is_correct
    """
    guess_disp[i] = guess_disp[i][:j] + guess + guess_disp[i][j + 1:]
    letter_is_correct = True
    return letter_is_correct


def play_game():
    """
    main function
    :return: none
    """
    play = True
    points = 0
    while play:
        print('welcome to guess game, HAVE FUN:-)')
        sentence = random.choice(sentences_list)
        display = create_blank_list(sentence)
        print(display)
        points = get_a_guess(sentence, display, points)
        print(f'You Won, your score is:{points}')
        play_again = input('Do you want to play again? press (y/n)')
        if play_again == 'n':
            play = False
            print('Bye Bye')


play_game()
