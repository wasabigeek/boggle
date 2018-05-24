WORK-IN-PROGRESS

### HOW TO PLAY
- In command line, go to folder and run `python app.py`. Note that Python 3.6 is required to run.

### DESIGN CONSIDERATIONS
- Storing the Board
    - Could have done a Grid with Rows and Cols in a nested list e.g. `[ [A, B, C, D], [...], ... ]`. Easier to figure out adjacent letters, but have to double-for-loop through and harder to tell the row and col from the tile alone.
    - Instead just used the `0` to `15` index. Needs a bit more logic to figure out adjacent letters but makes the rest of the code simpler.
- Checking a Word
    - Broke down into two checks, done in this order:
        1. Word can be formed on the board
        2. Word can be found in the dictionary
    - For (1), check if the starting letter is on the board, then recursively check through adjacent tiles to find if the entire word can be formed.
        - Use the starting letter for simplicity (don't need to consider if in reverse or middle letters) and since it won't impact the time much (just loop through 16 tiles).
        - Recursion used a word can be formed in multiple possible routes, so will need to try all routes till a valid one is found.
    - For (2), currently just dumping the dictionary into memory each time `check_word()` is invoked, ideally should be able to store it once in the game loop with a Trie (I'm not very familiar with implementing this yet but can try), so it's faster to check and takes up less memory.
