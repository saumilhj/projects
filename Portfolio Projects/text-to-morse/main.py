MORSE = {'A': '.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....',
         'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.',
         'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--','X':'-..-',
         'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....',
         '6':'-....', '7':'--...', '8':'---..', '9':'----.','0':'-----', ', ':'--..--', '.':'.-.-.-',
         '?':'..--..', '/':'-..-.', '-':'-....-',
         '(':'-.--.', ')':'-.--.-'}
inp = input("Enter the text: ").upper().replace(' ', '')
capitalized_inp = list(inp)
output = True
morse_out = []
# print(capitalized_inp)
for char in capitalized_inp:
    try:
        morse_out.append(MORSE[char])
    except KeyError as err:
        print(f'The morse value for {err} does not exist')
        output = False
        break
if output:
    print(f"Converted output: {' '.join(morse_out)}")
