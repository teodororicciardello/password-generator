# Password Generator

Exercise in python for a password generator starting from 2 words inserted by the user. 
With the password, it will output an estimate of the entropy of the password.

The objective is to generate strong passwords easy to remember. 
Given 2 words picked randomly from a dictionary, their base entropy is given by the number 
of items in the starting dictionary.
If the 2 words are altered with some real casual letters like numbers and chars the 
entropy is sensibly increased in proportion to the length of the 2 words.
In order to have easy to remember password the alterations should be some kind of "natural"
(like 'l' for '|'), so letter alterations are taken from a dictionary, while numbers are 
inserted randomly.

2 notes about this project:
1. this is the result of hobby studies on information entropy and password generation, if 
hidden assumptions have been made I'm glad to amend and improve the code.
2. This was an exercise to learn and practice python, so contribution about the coding 
(especially the use of SystemRandom) are welcome.

