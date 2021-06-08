MORSE = {'.-':    'a', '-...':  'b', '-.-.':  'c',
         '-..':   'd', '.':     'e', '..-.':  'f',
         '--.':   'g', '....':  'h', '..':    'i',
         '.---':  'j', '-.-':   'k', '.-..':  'l',
         '--':    'm', '-.':    'n', '---':   'o',
         '.--.':  'p', '--.-':  'q', '.-.':   'r',
         '...':   's', '-':     't', '..-':   'u',
         '...-':  'v', '.--':   'w', '-..-':  'x',
         '-.--':  'y', '--..':  'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
        }

key_list = list(MORSE.keys())
value_list = list(MORSE.values())

def encode(text):
    phrase= ''
    words = text.lower().split()
    for word in words:
        for letter in word:
            phrase += key_list[value_list.index(letter)]
            phrase += ' '
        phrase += '   '
    phrase = phrase.rstrip()
    return phrase


def decode(code):
    phrase = ''
    words = code.split('  ')
    for word in words:
        for letter in word.split():
            phrase += MORSE[letter]
        phrase += ' '
    phrase = phrase.capitalize().rstrip()
    return phrase
