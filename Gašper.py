print("Hello! Let's talk about Bayes nets!")

from time import sleep as _sleep
import webbrowser as _webbrowser


def what_are_probs():
    print('I strongly believe that probabilities are degrees of belief.')

def what_do_you_mean():
    print('For example, if I say tails is more probable than heads, then I:\n')
    _sleep(2)
    print('¤ would be willing to bet more money on tails\n')
    _sleep(2)
    print('¤ would be more surprised to see heads\n')
    _sleep(2)
    print('¤ would expect to see tails more often if I were to flip the coin many times.\n')
    _sleep(2)
    print("¤ would be more confident that if I flip a coin I'll see heads\n")
    

def who_are_you():
    if input("Type 'I do' if you also want to see my GitHub page: ") == 'I do':
        _webbrowser.open("https://github.com/mirkomartn")
    if input("Type 'I do' if you want to see my MCMP website: ") == 'I do':
        _webbrowser.open("http://www.mcmp.philosophie.uni-muenchen.de/people/doct_fellows/stukelj_gasper/")
