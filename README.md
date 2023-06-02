# pythonProject_1_Guess_game
# Guess Game

This is a simple word guessing game where the player needs to guess the missing letters in a sentence. Each correct guess earns points, while incorrect guesses result in a deduction of points. The player has a time limit to complete each round, and a bonus is awarded if the round is completed within the time limit.

## Installation

To run the game, you need to have Python installed on your system. Clone or download the project files and run the `guess_game.py` script.

```bash
git clone https://github.com/your-username/guess-game.git
cd guess-game
python3 guess_game.py
```

## Gameplay

1. The game will display a sentence with missing letters represented by underscores. The player's task is to guess the missing letters and complete the sentence.

2. Enter your guess as a single letter and press Enter.

3. If the guessed letter is correct and appears in the sentence, it will be revealed in the corresponding position(s) in the sentence. The score will increase by 5 points.

4. If the guessed letter is incorrect or does not appear in the sentence, the score will be reduced by 1 point.

5. You cannot guess the same letter again.

6. The game continues until all the missing letters are guessed correctly or the time limit (30 seconds) is exceeded.

7. If the round is completed within the time limit, a bonus of 100 points is awarded.

8. After each round, the player's score is displayed, and they are given the option to play again or exit the game.

## Functions

- `create_blank_list(sentence)`: Creates a blank list for the selected sentence.

- `get_a_guess(chosen_list, guess_display, points)`: Gets a guess from the user and updates the score based on the correctness of the guess.

- `score(letter_is_correct, points)`: Updates the score based on whether the guess is correct or not.

- `check_if_letter_exists_in_word(chosen_list, guess, guess_display, i, letter_is_correct)`: Checks if the guessed letter exists in the sentence.

- `change_display(guess, guess_disp, i, j)`: Edits the words in case of a correct guess.

- `play_game()`: The main function that initiates and controls the gameplay.

