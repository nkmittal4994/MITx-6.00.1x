def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    a='abcdefghijklmnopqrstuvwxyz'
    b=''
    for i in a:
    	if i not in lettersGuessed:
    		b+=i
    return b
print getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's'])		
