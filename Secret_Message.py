# used to decrypt special message
def lasso_letter(letter, shift_amount):
    letter_code = ord(letter.lower())
    # next 3 lines used to account for a shift over ascii value of 122
    a_ascii = ord('a')
    alphabet_size = 26
    true_leter_code = a_ascii + (((letter_code - a_ascii)+ shift_amount) % alphabet_size) 
    decoded_letter = chr(true_leter_code)
    return(decoded_letter)

def lasso_word(word, shift_amount):
    # stores all decoded letters into a string
    decoded_word = ''
    for letter in word:
        decoded_letter = lasso_letter(letter, shift_amount)
        decoded_word = decoded_word + decoded_letter
    return decoded_word

word1 = lasso_word('craa',-13)
word2 = lasso_word('rszsd',-25)
word3 = lasso_word('acksa',18)
word4 = lasso_word('fn',1)
word5 = lasso_word('kdltb',-9)

print(word1 + " " + word2 + " " + word3 + ". " + word4 + " " + word5 +"!")