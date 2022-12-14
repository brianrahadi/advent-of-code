# Reflection
Credit: https://github.com/jonathanpaulson/AdventOfCode/blob/master/2022/14.py

While it was quite hard and I had to learn from the solution, it was refreshing to understand it.
Basically, I was stuck in how to represent in on a 2D array. Realizing that it was unnecessary and it is better to use a hashset 
for the amortized O(1) lookup.

The core algorithm is to just keep the sand falling down in a nested loop. For part 1, if the sand reaches lower than the lowest of the block, then print how many sands have been placed. For part 2, we need to make a whole floor (2 below the lowest) and make a x-axis big enough to make sure the blocks can form a big triangle and the top reaches the source (500, 0), print which order of the sand that will not be able to come out (as source is clogged by other sand)

It was fun coding the solution :D. Thanks r/jonathanpaulson!