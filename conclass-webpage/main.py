from PyDictionary import *
from dictionaryio import DictionaryIO
from pywebio import *
from pywebio.input import *
from pywebio.output import *
from flask import Flask

app = Flask(__name__)
app.debug = True
if __name__ == '__main__':
    app.run()
from definitionsCode import *
from inventory import *

dictionary = PyDictionary()
words = ['good', 'new', 'first', 'last', 'long', 'great', 'little', 'own', 'other', 'old', 'right', 'big']
adverbEndings = ['ly', 'able','er', 'ed','ing', 'al']
put_markdown('## Welcome to Conclass Page')
intro()

with use_scope('EnterWord', clear=True):
    put_text('Let give try!')
    word = input.input('Enter a word: ')
    write(word)

put_text('Your word is ' + word).style('text-decoration-line: overline underline; text-decoration-style: wavy')

if word in commonWords:
    popup('Common Word Warning:', [
        put_text('You inputted a word in the 100 most common English words Common words  mainly are auxillary words and pronouns which don\t often change meaning in the way conclass can help.'),
        put_link('100 Most Common words', 'https://www.ef.edu/english-resources/english-vocabulary/top-100-words/', new_window=True),
        put_buttons(['Scroll to Bibliography', 'Close'], onclick=[scroll2Bib(), close()])
        ]
          )
    note = actions('Do you want to input another word?', ['Yes', 'No'],
                   help_text='Can you see your word benefiting from a literal definition? If the answer is yes click NO, if the answer is no, click YES')
    if note == 'Yes':
        popup(
            'If you would like to learn about any possible straying from a concrete meaning, feel free to check out:',
            put_link(
                'Urban dictionary', 'https://www.urbandictionary.com/', new_window=True))
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
if word.endswith(tuple(adverbEndings)):
    popup(
        'The system detected suffixes that serve as bound morphemes providing tense or changing a word to an adverb.')
    simple = actions('Are you using the simplist syntax to relay your meaning and intention', ['Yes', 'No'],
                     help_text='Example: if you are trying the word: suicidal, you can simply type \'suicide\' other changes later')
    if simple == 'Yes':
        put_text(
            'Good to know! In this language, since the words being edited are often nouns or adjectives to describe a person or thing does not need to be edited with \"ly\" or \"able\" because the words in this language are exclusively positive, they can\'t be negated')
        word = input.input('Enter the word again: ')
    if simple == 'No':
        with use_scope('EnterWord'):
            word = input.input('Enter the word again: ')


import math


from pywebio.input import *
from pywebio.output import *



import time

with open("word.txt", 'w') as f:
    f.write(word)
put_processbar('process')
set_processbar('process', 2 / 10, 'IPA')
time.sleep(1)
set_processbar('process', 4 / 10, 'Analyzing vowels')
time.sleep(1)
set_processbar('process', 6 / 10, 'Applying Conclass phonemes')
time.sleep(1)
set_processbar('process', 8 / 10, 'Adding suffixes')
time.sleep(1)
set_processbar('process', 9 / 10, 'Verifying rules')
time.sleep(1)
set_processbar('process', 10 / 10, 'Verifying rules')
# TODO: fix labels
with use_scope('replace1', clear=True):
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
    if 'ee' or 'ea' or 'ey' or 'ei' or 'ie':
        word = word.replace('ee', 'I', 1)
        word = word.replace('ea', 'I', 1)
        word = word.replace('ey', 'I', 1)
        word = word.replace('ei', 'I', 1)
        word = word.replace('ie', 'I', 1)
    if 'aw' or 'ou' in word:
        word = word.replace('aw', 'T',
                            1)  # overlap of 'ou' like in: thought vs thouugh -- due to context, Conclass is kinda 50/50 to get it right
        word = word.replace('ou', 'T', 1)
    if 'oo' or 'ew' or 'ue' in word:
        word = word.replace('oo', 'U', 1)
        word = word.replace('ew', 'U', 1)
        word = word.replace('ue', 'U', 1)
    if 'oe' or 'oa' in word:
        word = word.replace('oo', 'O', 1)
        word = word.replace('ew', 'O', 1)
    if 'oy' or 'oi' in word:
        word = word.replace('oy', 'Y', 1)
        word = word.replace('oi', 'Y', 1)
    if 'oy' or 'oi' in word:
        word = word.replace('oy', 'Y', 1)
        word = word.replace('oi', 'Y', 1)
    if 'uy' or 'ye' or 'igh' in word:
        word = word.replace('uy', '|', 1)
        word = word.replace('ye', '|', 1)
    if 'ai' or 'ay' or 'ea' or 'eigh' or 'ey':
        word = word.replace('ei', 'A', 1)
        word = word.replace('ai', 'A', 1)
        word = word.replace('ay', 'A', 1)
    if tuple(vowels) and 'e' in word:
        word = word.replace('a', 'A', 1)
        word = word.replace('i', '|', 1)
        word = word.replace('u', 'U', 1)
    #checks if there are other dipthongs



if len(word) <= 4:
    print(len(word))
    with use_scope('3letter', clear=True):
            if len(word) <= 4:
                print('ummm')
                # this section adds endings to words CVV
                if word.endswith(tuple(vowelCloseT)):
                    put_info(put_text('Your word consists of an onset and a nucleus'),
                             put_table([
                                 ['Initial', 'Nucleus', 'Notes'],
                                [word[0], word[1], 'A closed vowel']]),
                             put_text('What does this mean?'
                              'With a', put_text('C initial').style('color: yellow'), 'and a', put_text('Closed Vowel').style('color: orange'),'in the final',
                             put_text(retroflex[1]).style('color: brown'),'is added')),
                    # words with C and closed vowel
                    word = word + retroflex[1]
                elif word.endswith(tuple(vowelOPenT)):
                    word = word + retroflex[3]
                    put_info(put_text('Your word consists of an onset and a nucleus'),
                             put_table([
                                 ['Initial', 'Nucleus', 'Notes'],
                                [ word[0], word[2], 'an open vowel']
                             ]),
                             put_row([
                                 put_text('With a'),
                                 put_text('C initial').style('color: yellow'),
                                 put_text('and an'),
                                 put_text('open Vowel').style('color: orange'),
                                 put_text('in the final'),
                                 put_text(retroflex[3]).style('color: brown'),
                                 put_text('is added')
                                 ]
                             )
                             )
                    # words with C and open vowel
            if len(word) == 3 and word[1] in capitol:
                if word.endswith(tuple(alveolar)):
                    word = word +  u'ʂ' # TODO: import retroflexes, add into 4+ letter by running against common words - it will add a label
                if word.endswith(tuple(velar)):
                    word = word +u'ɖ'
                if word.endswith(tuple(bilabial)):
                    word = word + u'ʈ'
                if word.endswith(tuple(labiodental)):
                    word = word + u'ɳ'
                if word.endswith(tuple(palatal)):
                    word = word +  u'ɽ'
                if word.endswith(tuple(glottal)):
                    word = word + u'ɭ'
            # if CVC pattern and the V not a dipthong, the vowel maintains the same
            if len(word) == 3 and word[1] not in capitol and not word.endswith(u'ʔ' or 'R'):
                word = word.replace('a', u'æ', 1)
                word = word.replace('o', u'ɔ', 1)
                word = word.replace('u', u'ʌ', 1)
                word = word.replace('i', u'ɪ', 1)
                word = word.replace('e', u'ɜ', 1)
                print('get switched')
                word = word[:2] + u'ʔ' + word[2] + u'l'
                put_text(word)
            if 'ʔ' in word:
                print('present')
            if len(word) <= 5:
                print('ummm')
                # this section adds endings to words CVV
                if not word.endswith(tuple(vowels)):
                    put_info(put_text('Your word consists of an onset, nucleus, and rhyme'),
                             put_table([
                                 ['Initial', 'Nucleus', 'Rhyme'],
                                [word[0], word[1], word[1:]]
                                 ]
                             ),
                             put_collapse('Learn about closed syllable rhymes', [
                                 put_table([
                                     ['Final Consonant', 'Conclass Rhyme', 'Similar'],
                                     ['Alveolar', 'ʂ', '' ]
                                 ]),
                                 put_text('Important Note: depending on if your nuclei is a dipthong or not the words will have different endings'),
                                 put_text('Most three letter words tend to allow for minimal pairs hence along with adapting different endings it is thorough to change the endings further'),
                                 put_text('Most Conclass words are short and resemble other words if spoken quickly. While we account for this with the social resembling factor, it is good to distance the words as fa as possible')
                             ], open=True))

if len(word) > 4 and u'ʔ' not in word and not word.endswith(tuple(retroflex)):
    print('dam doesnt work')
    # for words wih more then one syllable, the first initial vowel gets elongated
    def firstvowelLocator(word):
        for index, c in enumerate(word):
            if c in vowels:
                return index
    firstvowelLocator(word)
    index = firstvowelLocator(word)
    print(index)
    word = word[:index + 1] + ':' + word[index + 1:]
    def vowelCount(word):
        count = 0
        for i in word:
            if i in vowels:
                count = count + 1
        return count
    # if there are still several vowels that remain in other syllables, it is replaced with i:
    if vowelCount(word) > 2:
        for i in range(index + 1, len(word)):
            print(word[i])
            if word[i] in vowels:
                word = word.replace(word[i], 'I')
if len(word) > 4 and u'ʔ' not in word and not word.endswith(tuple(retroflex)):
    lenof = len(word)
    print(lenof)
    endTicket = lenof / 4  # as the minimum characters in this category is 4
    fp = math.ceil(endTicket)  # this finds, the porportion to the number of phonemes in a longer word
    finalPos = lenof - fp + 1  # to allow longer words without taking or ading too many conclass classifier suffixes, we remove 1 ending per every phoneme over 4
    # the cutdown word
    word = word[:finalPos]
    print(word)
    for i in range(len(word) - 1):
        if word[i] in vowels and word[i + 1] in vowels:
            print(word[i] + 1)
            word = word[:i + 1] + word[i + 2:]
    print(word)
    with use_scope('FinalReplacements', clear=True):
        for w in word:
            if word.endswith(tuple(vowelCloseT)):
                word = word + retroflex[1]
            if word.endswith(tuple(vowelOPenT)):
                word = word + retroflex[3]
            if word.endswith(tuple(alveolar)):
                word = word[: -1] + syllabic[2]
            elif word.endswith(tuple(bilabial)):
                word = word[: -1] + syllabic[1]
            elif word.endswith(tuple(labiodental)):
                word = word[: -1] + rcolored[0]
            elif word.endswith(tuple(velar)):
                word = word[: -1] + swede_syllabic[0]
            elif word.endswith(tuple(palatal)):
                word = word[: -1] + rcolored[0]
            if word.endswith(tuple(alveolar)) and not word.endswith('l'):
                word = word + syllabic[2]
            if word.endswith(tuple(alveolar)) and word.endswith('l'):
                word = word.replace('l', '/', 1)
            if word.endswith(tuple(bilabial)) and not word.endswith('m'):
                word = word + syllabic[1]
            if word.endswith(tuple(bilabial)) and word.endswith('m'):
                word = word + syllabic[2]
            if word.endswith(tuple(labiodental)):
                word = word + rcolored[0]
            if word.endswith(tuple(velar)):
                word = word[: -1] + glottal[0] + word[2:]
            if word.endswith(tuple(palatal)):
                word = word[: -1] + glottal[0] + word[2:]
            elif not word.endswith(tuple(inventory)):
                word = word[: -1] + glottal[0] + swede_syllabic[0]

print(type(word))
word = word.replace('I', 'i:')
word = word.replace('A', u'eɪ')
word = word.replace('|',u'ai')
word = word.replace('Y', u'ɔi')
word = word.replace('U', 'u:')
word = word.replace('T', u'au')
put_text(word)
word = word

put_text('Your word before adding the endings. A sneak peak:', word)



put_text(word).style('color: blue; font-size: 20px')
put_markdown('## I want to make my word:')
with use_scope('Customize'):
    plural = word + 'z'
    pluralDetailed = put_text(plural).style('color: pink; border-style: solid')
    indent = '\n'
    line = put_markdown('---')
    with open("word.txt", 'r') as f:
        dictWord = f.read()
    meaning = dictionary.meaning(dictWord)
    pointer = put_text('\n Notice the negative connotations?').style('color: red'), meaning
    dictWord = DictionaryIO(dictWord)
    literalMeaning = DictionaryIO.meaning(dictWord)
    ambigousFix = word + 'sh'  # TODO: add retroflex s


    def tenseSentenceTab():
        tenseSentence = input.input('Enter a sample sentence: ')
        for i in range(6):
            if 'was' or 'felt' or 'had' or 'used' or 'did' or 'were' in tenseSentence:
                put_text('This sentence has identifiers:', tenseSentence)


    pluralTab = put_text('To make a word plural, you simply add a \'z\'', indent,
                         'However, there is little need for plurals when speaking in conclass'
                         'as the words most likely to use the conclass classifier are adjective, verbs, or nouns that are specific to a singular person.'), line, \
                ('The plural of your word is: '), pluralDetailed, line
    tenseTab = put_text('Tense is not necessairly dealt with in Conclass.'
                        ' As conclass deals with specific words within a sentence, surrounding words often indicate tense.'), put_markdown(
        '*was*, *felt*, *had*, *were*'), \
               (
                   'For words such as run/ran, or see/saw which are irregular and have no local tense indicators, conclass allows the addition of a glottal sound after the first syllable.'
                   'Other tense exceptions include verbs that maintain in past tense, and those to have the added glottal.'
                   'If there is a need to dictate tense, as you will see when you explore the language more, you assert a glottal stop'
                   'Examples: I '
                   'Feel free to experiment below:'), put_markdown('---'), ('Currently not oporatable')
    # TODO add examples
    caseTab = put_markdown('## \' Feeling Case \''), put_text(
        'As formentioned, the words that mostly are used with the conclass classifiers are adjectives, verbs and nouns.'), \
              put_markdown(
                  '_As Conclass focuses on literal meanings of words - there is a new case that is applied to further distinguish the differences_'), \
              put_text('This is the \'Feeling Case.\' This case is used to seperated claims like the following'), \
              put_table([
                  ['English Sentence', 'Conclass meaning', 'Base conclass word', 'The word in the feeling case'],
                  ['I feel like I am dying', 'this means you feel ill enough to go to the emergency room.', 'daɪ',
                   'Feel case'],  # TODO add proper example
                  ['I am dying', 'this means you are, clinically dying', '', '']
              ]), \
              put_text('To also refer to tense - note: an addition of the glottal').style('10px'), put_markdown('**'), (
                  'Try it out yourself')
    meaningTab = put_text('See how your word benefits from conclass.',
                          'Dictionary definition via Word.net:'), \
                 put_markdown('---'), put_text(meaning, indent).style('color: red; border-style: dotted'), put_markdown(
        '---'), put_text('Here is a more literal basic defition that relays a conclass word\'s meaning'), put_markdown(
        '---'), put_text(literalMeaning).style('color: green; border-style: dotted'), put_markdown('---')
    tooClose = put_text(
        'Do you think your result sounds too much like another english word or let you get a combination that can sound like a slang contratction like'), put_markdown(
        '**'), put_text(
        'Adding the retroflex s \'sh\' at the end of the word can dennote any other menining'), put_markdown(
        '---'), put_text(ambigousFix), put_markdown('---')  # TODO: input murder word
    socialAspect = put_text('The main purpose of this language is to help the ambiguoty of social situations - here is who it can help, and who it can benefit'), \
                   put_table([
                       ['Population/Situation', 'Reasoning'],
                       ['People with conditions like ASD', 'With ASD, understing meaning of things that are hold different meanings or the intention is not clear in the words.'],
                       ['Social Anxiety', 'Social anxiety causes people to doubt themselves and over think the slightest thing if the meaning is unsure'],
                       ['Formal Situations', 'English, which is the base of this new system does not have a formal or informal classifiers hence possibly elders or adults may fail to grasp a conversation' ]
                   ])

    put_tabs([
        {'title': 'Plural', 'content': pluralTab},
        {'title': 'Different Tense', 'content': tenseTab},
        {'title': 'Cases', 'content': caseTab},
        {'title': 'Explore Connotation', 'content': meaningTab},
        {'title': 'Correct any English similarity', 'content': tooClose},
        {'title': 'How this helps people?', 'content': socialAspect},
        {'title': 'See the code', 'content': 'boo'},  # TODO add previous code
    ])
with use_scope('bib'):
    put_collapse('Bibliography', content=[
    put_text('Rice, Curt. "Gjert Kristoffersen (2000). The phonology of Norwegian . Oxford: Oxford University Press. Pp. xvi+366." Phonology 18.03 (2001): 434-438. 13 10 2021. <https://cambridge.org/core/journals/phonology/article/gjert-kristoffersen-2000-the-phonology-of-norwegian-oxford-oxford-university-press-pp-xvi366/c4d0d181589d5a717b82d8cc88279e38>.', indent,  'Solhaug, Tor Havard. Retroflexion in Norwegian. Master Thesis. Stavanger: Universitetet i Tromsø , 2010. Document.')], open=True, scope='bib', position=1)


