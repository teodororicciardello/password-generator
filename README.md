Exercise in python for a password generator starting from 2 words inserted by the user. 
With the password, it will output an estimate of the entropy of the password.

The idea behind this project came to me studying passwords strength versus the difficulty 
to remember them. 
Given 2 words picked randomly from a dictionary, their entropy is given by the number of 
items in the starting dictionary: if the 2 words are picked by the personal information of 
some one, the dictionary is quite small.
Anyway, if the 2 words are altered with some real casual letters like numbers and chars the 
entropy is sensibly increased in proportion to the length of the 2 words.

Notes

This project is an exercise on 2 dimensions:
- first it is an exercise about python as I'm learning it, so it could use trivial and not 
optimal solution for this implementation. Any contribution and improvement it is welcome.
- second it is an exercise about information entropy and password generation; the code is 
based on the python function 'systemRandom' to generate casual alterations and common-sense 
algorithms to alterate the words; I know there could be errors so also here any contribution
and improvement it is welcome. 

TODO 
1. Create an utils program able to check correctness of the entropy calculation 
2. generalize the implementation for 1 to n words 
3. Create an utils program able to check the randomness of the alterations 