# Q-u-Bert

A python version of the classic '80s game, Q * Bert! 

## Motivation and Goals:
We originally named our team "The Q-Berts," and by chance, the 2021 iQuHack challenge was to code a game! We wanted to code a game that isn't common, and challenge ourselves. have incorporated quantum computing into the layout of the map that generates at the start of the game. We created a 3 qubit circuit with Hadamard gates to place each qubit in a superposition. This gave 2^3 = 8 possible qubit states upon measurement. 

## Description of Work
* Created sprites of characters and map similar to original game
* Used pygame to code motion
* Used AI to code enemy motion
* Used quantum circuits to generate probabilities for each cube to create random maps
* created collision functions to establish interactions between Q-bert and other game items 

## Game Play
* try to avoid all of the enemies while comings in contact with each cube to change its color. Once all of the cubes are blue, you've won!

## For the Future:
* Use classes instead of individual variables
* Add more complex quantum circuits and integrate them into game
* create a win scenario
* stop the movement of the enemies when the game is over



Glhf!
