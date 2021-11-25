from pywebio.output import *
from pywebio.session import go_app
from pywebio.input import *
from pywebio import *
import pywebio
import math

def find_first_vowel(word):
    i = 0
    while i < len(word):
        if word[i] in vowels:
            return i
        i += 1
    return len(word) - 1

def first_vowel(word):
    for index, char in enumerate(word):
        if char in 'aeiou':
            return index

def convert(word):
    index = first_vowel(word)
    return word[index:] + "-" + word[:index] + 'ay'

capitol = ['A', 'E', 'I', 'O', 'U', 'Y', '|']
words = ['slit', 'gay', 'due', 'pair', 'per', 'put', 'bate', 'bab', 'pat', 'poot', 'shoot', 'good', 'new', 'first',
         'last', 'long', 'great', 'little', 'own', 'other', 'old', 'right', 'big']
# closed = ['i', 'u', 'e', 'ɘ', 'ʊ','ɪ']
vowelCloseT = ['I', 'U', 'E', 'T']
vowelOPenT = ['A', '|', 'Y', 'O']

initialReplacements = ['sh', 'th', 'j', 'ch']
bilabial = ['p', 'b', 'm']
labiodental = ['f', 'v']
alveolar = ['t', 'n', 'r', 'd', 's', '?', '?', '?', '?', 'l']
retroflex = ['ʈ', 'ɖ', 'ɳ', 'ɽ', 'ʂ', 'ʐ', 'ɻ', 'ɭ']
velar = ['k', 'g']
palatal = ['c', 'j']
glottal = ['ʕ']
swede_syllabic = ['ɳ', 'ɭ']
syllabic = ['n̩', 'm̩', 'l̩']
rcolored = ['ɔ˞', 'ɑ˞']
vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U']
doublecon = ['ll', 'tt', 'ss']
inventory = bilabial + labiodental + alveolar + retroflex + velar + palatal + glottal
commonWords = ['a'
               'about', 'all', 'also', 'and', 'as', 'at', 'be', 'because', 'but', 'by', 'can', 'come', 'could', 'day',
               'do', 'even', 'find', 'first', 'for', 'from', 'get', 'give', 'go', 'have', 'he', 'her', 'here', 'him',
               'his', 'how', 'I', 'if', 'in', 'into', 'it', 'its', 'just', 'know', 'like', 'look', 'make', 'man',
               'many', 'me', 'more', 'my', 'new', 'no', 'not', 'now', 'of', 'on', 'one', 'only', 'or', 'other', 'our',
               'out', 'people', 'say', 'see', 'she', 'so', 'some', 'take', 'tell', 'than', 'that', 'the', 'their',
               'them', 'then', 'there', 'these', 'they', 'thing', 'think', 'this', 'those', 'to', 'two', 'up', 'use',
               'very', 'want', 'way', 'we', 'well', 'what', 'when', 'which', 'who', 'will', 'with', 'would', 'year',
               'you', 'your']



def replace1(word):
    with use_scope('Replace1', clear=True):
        for i in range(len(word)):
            # initial replacement of automatic consonants
            word = word.replace('ck', 'k', 1)
            word = word.replace('ll', 'l', 1)
            word = word.replace('sh', u'ʃ', 1)
            word = word.replace('th', u'θ', 1)
            word = word.replace('j', u'ʤ', 1)
            word = word.replace('ch', u'ʧ', 1)
            if word.endswith('g'):
                word = word.replace('g', u'ʔ', 1)  # TODO: ghlotal
            if word.endswith('r'):
                word = word.replace('r', 'R',
                                    1)  # adds a glottal since most retroflexive or r-colored endings (especially with shorter words) can stand is bound morphemes
            if 'ee' or 'ea' in word:
                word = word.replace('ee', 'I', 1)
                word = word.replace('ea', 'I', 1)
            if 'aw' or 'ou' in word:
                word = word.replace('aw', 'T',
                                    1)  # overlap of 'ou' like in: thought vs thouugh -- due to context, Conclass is kinda 50/50 to get it right
                word = word.replace('ou', 'T', 1)
            if 'oo' or 'ew' in word:
                word = word.replace('oo', 'U', 1)
                word = word.replace('ew', 'U', 1)
            if 'oy' or 'oi' in word:
                word = word.replace('oy', 'Y', 1)
                word = word.replace('oi', 'Y', 1)
            if 'oy' or 'oi' in word:
                word = word.replace('oy', 'Y', 1)
                word = word.replace('oi', 'Y', 1)
            if 'uy' or 'ye' in word:
                word = word.replace('uy', '|', 1)
                word = word.replace('ye', '|', 1)
            if 'ei' or 'ai' or 'ay' in word:
                word = word.replace('ei', 'A', 1)
                word = word.replace('ai', 'A', 1)
                word = word.replace('ay', 'A', 1)
            if tuple(vowels) and 'e' in word:
                word = word.replace('a', 'A', 1)
                word = word.replace('i', '|', 1)
                word = word.replace('u', 'U', 1)
def vowelReplace1(word):
    if len(word) <= 3:
        with use_scope('3letter', clear=True):
            for i in range(len(word)):
                if len(word) <= 2:
                    if word.endswith(tuple(vowelCloseT)):
                        word = word + retroflex[1]
                    if word.endswith(tuple(vowelOPenT)):
                        word = word + retroflex[3]
                if len(word) == 3 and word[1] in capitol:
                    word = word.replace('s', u'ʂ',
                                        1)  # TODO: import retroflexes, add into 4+ letter by running against common words - it will add a label
                    word = word.replace('d', u'ɖ', 1)
                    word = word.replace('t', u'ʈ', 1)
                    word = word.replace('n', u'ɳ', 1)
                    word = word.replace('l', u'ɭ', 1)
                    word = word[:2] + u'l̩'
                if len(word) == 3 and word[1] not in capitol and not word.endswith(u'ʔ' or 'R'):
                    word = word.replace('a', u'æ', 1)
                    word = word.replace('o', u'ɔ', 1)
                    word = word.replace('u', u'ʌ', 1)
                    word = word.replace('i', u'ɪ', 1)
                    word = word.replace('e', u'ɜ', 1)
                    word = word[2] + word[1] + word[
                        0]
def cutDown(word):
    lenof = len(word)
    print(lenof)
    endTicket = lenof / 4  # as the minimum characters in this category is 4
    print(endTicket)
    fp = math.ceil(endTicket)  # this finds, the porportion to the number of phonemes in a longer word
    print(fp)
    finalPos = lenof - fp  # to allow longer words without taking or ading too many conclass classifier suffixes, we remove 1 ending per every phoneme over 4
      # the cutdown word
    print(finalPos)
    word = word[:finalPos]

def close():
    close_popup()


def scroll2Bib():
    scroll_to('bib')


def citaion(str, link):
    put_link(str, link, new_window=True)


def intro():
    with use_scope('Intro', clear=True):
        put_text('Conclass is a system to edit English words, similar to how adding certain suffixes or words'
                 'can make a definition oposite of the base word or paint words a different way -- the Conclass method'
                 'makes words to be literal.')


def enterWord():
    with use_scope('EnterWord', clear=True):
        put_text('Let give try!')
        word = input.input('Enter a word: ')
        write(word)


def firstReplacement(word):
    for i in range(len(word)):
        # initial replacement of automatic consonants
        word = word.replace('ck', 'k', 1)
        word = word.replace('ll', 'l', 1)
        word = word.replace('sh', u'ʃ', 1)
        word = word.replace('th', u'θ', 1)
        word = word.replace('j', u'ʤ', 1)
        word = word.replace('ch', u'ʧ', 1)
        if word.endswith('g'):
            word = word.replace('g', u'ʔ', 1)  # TODO: ghlotal
        if word.endswith('r'):
            word = word.replace('r', 'R',
                                1)  # adds a glottal since most retroflexive or r-colored endings (especially with shorter words) can stand is bound morphemes
        if 'ee' or 'ea' in word:
            word = word.replace('ee', 'I', 1)
            word = word.replace('ea', 'I', 1)
        if 'aw' or 'ou' in word:
            word = word.replace('ee', 'T',
                                1)  # overlap of 'ou' like in: thought vs thouugh -- due to context, Conclass is kinda 50/50 to get it right
            word = word.replace('ea', 'T', 1)
        if 'oo' or 'ew' in word:
            word = word.replace('oo', 'U', 1)
            word = word.replace('ew', 'U', 1)
        if 'oy' or 'oi' in word:
            word = word.replace('oy', 'Y', 1)
            word = word.replace('oi', 'Y', 1)
        if 'oy' or 'oi' in word:
            word = word.replace('oy', 'Y', 1)
            word = word.replace('oi', 'Y', 1)
        if 'uy' or 'ye' in word:
            word = word.replace('uy', '|', 1)
            word = word.replace('ye', '|', 1)
        if 'ei' or 'ai' or 'ay' in word:
            word = word.replace('ei', 'A', 1)
            word = word.replace('ai', 'A', 1)
            word = word.replace('ay', 'A', 1)
        if tuple(vowels) and 'e' in word:
            word = word.replace('a', 'A', 1)
            word = word.replace('i', '|', 1)
            word = word.replace('u', 'U', 1)
    put_text(word)


def three(word):
    for i in range(len(word)):
        if len(word) <= 2:
            if word.endswith(tuple(vowelCloseT)):
                word = word + syllabic[2]
            if word.endswith(tuple(vowelCloseT)):
                word = word + retroflex[2]
        if len(word) == 3 and word[1] in capitol:
            word = word.replace('s', u'ʂ',
                                1)  # TODO: import retroflexes, add into 4+ letter by running against common words - it will add a label
            word = word.replace('d', u'ɖ', 1)
            word = word.replace('t', u'ʈ', 1)
            word = word.replace('n', u'ɳ', 1)
            word = word.replace('l', u'ɭ', 1)
            word = word[:2] + u'l̩'
        if len(word) == 3 and word[1] not in capitol and not word.endswith(u'ʔ' or 'R'):
            word = word.replace('a', u'æ', 1)
            word = word.replace('o', u'ɔ', 1)
            word = word.replace('u', u'ʌ', 1)
            word = word.replace('i', u'ɪ', 1)
            word = word.replace('e', u'ɜ', 1)
            word = word[2] + word[1] + word[
                0]  # why the reverse? 3 letter wor are often words missuesed - hence, conclass makes them obviously seperate to emphasize clarity


def longerVowel(word):
    for w in range(len(word)):
        def vowelLocator(
                word):  # locates non-dipthong vowels in the first position in longer words - for words longer then 4 characters lead the first vowel to be elongated or become an extended dipthong
            for c in word:
                if c in vowels:
                    return word.index(c)

        if len(word) >= 4:
            vowelPos = vowelLocator(word)  # vowelPos is the first vowel's physical position
            vowel1 = word[vowelPos]  # what the vowel is
            word = word[:vowelPos + 1] + ':' + word[vowelPos + 1:]
            word = cutDown(word)
            put_text('Your word before adding the endings. A sneak peak:', word)


def next():
    next = actions('What next?', ['Explore Phonetic Inventory', 'Learn about Rules', 'Further explore your word'])
    if next == 'Explore Phonetic Inventory':
        use_scope('Next')
        phoneticInventory()


def conent(word):
    if word in commonWords:
        note = actions(
            'The word you inputted is immensly common and is in CITE common words which mainly contain auxillary words and pronouns which don\t often change meaning in the way conclass can help. Do you want to input another word?',
            ['Yes', 'No'],
            help_text='Can you see your word benefiting from a literal definition? If the answer is yes, click NO, if the answer is no, click YES')
        if note == 'Yes':
            popup(
                'If you would like to learn about any possible straying from a concrete meaning, feel free to check out:'), put_link(
                'Urban dictionary', 'https://www.urbandictionary.com/')
            with use_scope('EnterWord'):
                word = input.input('Enter the word again: ')
        if note == 'No':
            popup('You can explore even more about your word\'s connotation once you input it!')
    if word.endswith('s'):
        plural = actions('*Is your word plural*', ['Yes', 'No'],
                         help_text='Is the word you input pluralized when it could be singular?')
        if plural == 'Yes':
            popup('Note on plurals',
                  'In the future we will teach about adding plurals, for now, enter your word in it\'s simplest form')
            with use_scope('EnterWord'):
                word = input.input('Enter the word again: ')
        if plural == 'No':
            popup('Note on plurals',
                  'Great! In the future, adding plurals will be adding a \"z\" sound no matter enviroment.')
    if word.endswith('ly' or 'able' or 'er' or 'ed' or 'ing'):
        put_text(
            'The system detected suffixes that serve as bound morphemes providing tense or changing a word to an adverb.')
        simple = actions('Are you using the simplist syntax to relay your meaning and intention', ['Yes', 'No'],
                         help_text='Is the word you input pluralized when it could be singular?')
        if simple == 'Yes':
            put_text(
                'Good to know! In this language, since the words being edited are often nouns or adjectives to describe a person or thing does not need to be edited with \"ly\" or \"able\" because the words in this language are exclusively positive, they can\'t be negated')
            word = input.input('Enter the word again: ')
        if simple == 'No':
            with use_scope('EnterWord'):
                word = input.input('Enter the word again: ')


def phoneticInventory():
    img = open('photos/consonants.png', 'rb').read()

    uniqueConsonants = put_text(
        'Syllabic Consonants: Syllabic consonants are what we recognize as consonants which, when in a final position, can also represent a vowel.',
        'Syllabic consonants are often marked by a line diuretic below.',
    ), put_table(
        [
            ['Example', 'IPA',
             put_link('Source of Example', url='https://en.wikipedia.org/wiki/Syllabic_consonant')],
            ['even(even) [English]', 'even [iːvn̩]', put_link('Syllabic Consonants [English] Example Source',
                                                              url='https://en.wikipedia.org/wiki/Syllabic_consonant#cite_note-2',
                                                              new_window=True)],
            ['Sedm (seven) [Czech]', '/sədəm/ [sedm̩]',
             put_link('Wikipedia: Syllabic Consonants [Slavic Language]; Example Source',
                      url='https://en.wikipedia.org/wiki/Syllabic_consonant#cite_note-8', new_window=True)],
            ['Cykel (bike) [Dutch]', '/ˈsykəl/ = [ˈsykl̩]',
             put_link('Wikipedia: Syllabic Consonants [Slavic Language]; Example Source',
                      url='https://en.wikipedia.org/wiki/Syllabic_consonant#cite_note-8', new_window=True)]
        ]
    )
    put_tabs([
        {'title': 'Consonant Chart', 'content': put_image(img)},
        {'title': 'Unique Consonants', 'content': uniqueConsonants},
        {'title': 'More content', 'content': [
            put_table([
                ['Commodity', 'Price'],
                ['Apple', '5.5'],
                ['Banana', '7'],
            ]),
            put_link('pywebio', 'https://github.com/wang0618/PyWebIO')
        ]},
    ])


def pluralTab(word):
    put_text('To make a word plural, you simply add a \'z\','
             'However, there is little need for plurals when speaking in conclass'
             'as the words most likely to use the conclass classifier are adjective, verbs, or nouns that are specific to a singular person.')
    put_markdown('---')
    plural = word + 'z'
    put_text('Plural of your word is:', plural)
    put_markdown('---')
    put_text('This suffix was chosen as it works well with conclass\' suffixes')


def tenseTab(word):
    put_text('Tense is not necessairly dealt with in Conclass.')
    put_text('As conclass deals with specific words within a sentence, surrounding words often indicate tense.')
    put_markdown('*was*, *felt*, *had*, *were*')
    put_text(
        'For words such as run/ran, or see/saw which are irregular and have no local tense indicators, conclass allows the addition of a glottal sound after the first syllable.'
        'Other tense exceptions include verbs that maintain in past tense, and those to have the added glottal.'
        'Examples: I '
        'Feel free to experiment below:')
    put_markdown('---')
    for i in range(6):
        tenseSentence = 'I felt like'
        if 'was' or 'felt' or 'had' or 'used' or 'did' or 'were' in tenseSentence:
            tenseSentence = tenseSentence.replace('was', 'WAS', 1)
            tenseSentence = tenseSentence.replace('felt', 'FELT', 1)
            tenseSentence = tenseSentence.replace('had', 'HAD', 1)
            tenseSentence = tenseSentence.replace('used', 'USED', 1)
            tenseSentence = tenseSentence.replace('did', 'DID', 1)
            tenseSentence = tenseSentence.replace('were', 'WERE', 1)
            put_text('This sentence has identifiers:', tenseSentence)


def systemDetects(str):
    put_text('The system detects your inputed word might be a' + str)


def PluralPop():
    systemDetects('plural')
    plural = actions('Is your word plural', ['Yes', 'No'])
    if plural == 'Yes':
        clear('Check')
    else:
        pass


def Definition():
    put_text('Check out the definition?')
    put_buttons(['Read about the definition'], [lambda: go_app('EnterWord.py')])


def task_2():
    put_text('task_2')
    put_buttons(['Go task 1'], [lambda: go_app('Begin')])


def index():
    put_link('Go task 1', app='HomePage.py')  # Use `app` parameter to specify the task name
    put_link('Go task 2', app='Begin.py')


def vowelLocator(word):
    for c in word:
        if c in vowels:
            print(word.index(c))


# locates non-dipthong vowels in the first position in longer words - for words longer then 4 characters lead the first vowel to be elongated or become an extended dipthong
# equal to `start_server({'index': index, 'task_1': task_1, 'task_2': task_2})`
def process(title):
    from main import word
    popup(title, [
        put_text('Note: capitol letters represent dipthongs or elongated sounds due to character balance.', word)
    ]
          )


def Input():
    input('Word: ')


def Next(file):
    pywebio.session.go_app(file, new_window=False)


def task_1():
    put_text('Begin with word')
    put_buttons(['Continue!'], [lambda: go_app('begin')])


def replace1(word):
    word = word.replace('sh', u'?', 1)
    word = word.replace('th', u'?', 1)
    word = word.replace('j', u'?', 1)
    word = word.replace('ch', u'?', 1)
    word = word.encode("utf8")
    print(word)


def home():
    pywebio.session.go_app('HomePage.py', new_window=False)


system = style(put_text('system'), 'color: pink')


def purple(text):
    style(put_text(text), 'color: purple')


def write(word):
    f = open("words.csv", 'w')
    f.write(word)
    f.close()


def writeNext(word):
    f = open("words.csv", "a+")
    f.writelines(
        [',', word]
    )


def read(line):
    f = open("words.csv", 'r')
    f.readlines(line)


def literal(dictWord):
    from dictionaryio import DictionaryIO
    dictWord = DictionaryIO(dictWord)  # replace `happy` with any word of your choice
    dictWord.meaning()  # returns the meaning of the word
