# Crossword Genertation

## Implimentation 1: ( https://stackoverflow.com/questions/943113/algorithm-to-generate-a-crossword )

I came up with a solution which probably isn't the most efficient, but it works well enough. Basically:

  1. Sort all the words by length, descending.
  2. Take the first word and place it on the board.
  3. Take the next word.
  4. Search through all the words that are already on the board and see if there are any possible intersections (any common letters) with this word.
  5. If there is a possible location for this word, loop through all the words that are on the board and check to see if the new word interferes.
  6. If this word doesn't break the board, then place it there and go to step 3, otherwise, continue searching for a place (step 4).
  7. Continue this loop until all the words are either placed or unable to be placed.

This makes a working, yet often quite poor crossword. There were a number of alterations I made to the basic recipe above to come up with a better result.

  - At the end of generating a crossword, give it a score based on how many of the words were placed (the more the better), how large the board is (the smaller the better), and the ratio between height and width (the closer to 1 the better). Generate a number of crosswords and then compare their scores and choose the best one.
    - Instead of running an arbitrary number of iterations, I've decided to create as many crosswords as possible in an arbitrary amount of time. If you only have a small word list, then you'll get dozens of possible crosswords in 5 seconds. A larger crossword might only be chosen from 5-6 possibilities.

  - When placing a new word, instead of placing it immediately upon finding an acceptable location, give that word location a score based on how much it increases the size of the grid and how many intersections there are (ideally you'd want each word to be crossed by 2-3 other words). Keep track of all the positions and their scores and then choose the best one.

---

## Implimentation 2 ( https://puzzel.org/en/features/create-crossword/online-generator )

1. Compass-algorithm: This one makes sure that as many words as possible are entered into the generated crossword puzzle grid.

2. Light-algorithm: After placing as many words as possible, the Light-algorithm tries to reduce the number of black squares and select the crossword puzzle with the most connections between answers.

This very simple Python script generates a *clueless* crossword puzzle. It harnesses the capabilities of Python and LaTeX to output the puzzle in a printable PDF.

---

## Implimentation 3 ( https://github.com/gondsm/crossword_generator )

I purposefully designed and implemented this little project without performing research on crossword generation techniques; I wanted to see if I could do it by myself. The very simple algorithm that is implemented here is as follows:

1. The technique receives a list of words, in a .txt file (I tested using [these](http://www.gwicks.net/dictionaries.htm) lists).
2. A number (1000, by default) of words are chosen randomly from the list that is given, and these are the words that will be used hereafter.
3. The technique expands the list of words into a list of possibilities, where each possibility encodes a possible starting location for a word, as well as its direction. This essentially constitutes all possible words that can be placed into the grid.
4. Words that connect to words that are already on the grid are isolated into a connected_possibilities list.
5. A new word is taken from the list of possibilities/connected_possibilities and placed on the grid. This makes it so a number of possibilities are now invalid, and these are removed from the list. Steps 3 through 5 are repeated until the grid is as full as we want it to be, or the script times out.

Output
---

The script depends on LaTeX for producing the PDF output. However, the grid can be (and is, by default) printed to the screen. The PDF is print-ready, and includes both the puzzle (with the needed words) and the solution, making the output of each run completely self-contained.


Performance Considerations
---

On my consumer-grade machine (i7-6700HQ) the algorithm can generate a 20x20 grid with 50% completion in some ~~45~~ ~~10~~ ~~4~~ seconds (with the new algorithm). I am currently looking into ways of improving this mark, and already have a ton of ideas, so stay tuned!

Usage
---

All you have to do is run the script on a folder where a "words.txt" file with one word per line exists. I recommend using the aforementioned lists! Run `./crossword_generator -h` to see all available options.
