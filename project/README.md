# Project

For my Project, my aim was to create a morphological analyzer for Korean. The goal was to take a corpus of data, in this case an article about tigers, and segment it word by word.

The second part of my project was to decompose the hangul letters using the Jamo library in Python. I was able to successfully install the library and even run a couple of test functions by switching into python in the terminal, but ran into a big issue when I went to apply it to the IPA translation. The regular functions would not work on the data, so I used a generator function. However, this returned values not readable in the desired format. For example, instead of returning the IPA value, it returns the value as a general expression. From my research, this is unfortunately what happens with generator expressions. It seemed like there were ways to return the values of the generator functions, but in my research, I could only find that to be true in the case of working with a list of integers.

Nevertheless, I am proud of my project. Starting out with minimal coding experience and never having worked in terminal, I did not imagine I could have made this by the end of the course. Though conceptually simple, as my first go at these types of tasks, it was my goal to create the baseline for future work with this data (hopefully implementing speech data in the future), so I feel satisfied with it. By the point of the project's completion, I had yet to complete the practical on matrices (train.py), so unfortunatelly, I was not able to add that into the project at this moment.

It seems like I do not have access to move the files into the project folder, so here is a list of the ones for my project (they all start with 'k'):

karticle.txt
kjamo.py
koreanipa.tsv
ksegmenter.oy
ktokenizer.py
ktranscriber.py

I would recommend downloading the files and running them similar to the Data Structures practical with the following in the command line:

$ cat karticle.txt | python3 ksegmenter.py | python3 ktokenizer.py | python3 ktranscriber.py

Let me know if you have any questions on this! I will do my best to answer them.
