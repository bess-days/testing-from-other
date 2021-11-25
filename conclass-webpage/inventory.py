from pywebio.output import *
from pywebio.session import go_app
from pywebio.input import *
from pywebio import *
import pywebio
import math
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

vowelPairs = ['ae','ai','ao','au','aA','aE','aI','aO','aU','aT','a|','ay','aY','a','ea','ei','eo','eu','eA','eE','eI','eO','eU','eT','e|','ey','eY','e','ia','ie','io','iu','iA','iE','iI','iO','iU','iT','i|','iy','iY','i','oa','oe','oi','ou','oA','oE','oI','oO','oU','oT','o|','oy','oY','o','ua','ue','ui','uo','uA','uE','uI','uO','uU','uT','u|','uy','uY','u','Aa','Ae','Ai','Ao','Au','AE','AI','AO','AU','AT','A|','Ay','AY','A','Ea','Ee','Ei','Eo','Eu','EA','EI','EO','EU','ET','E|','Ey','EY','E','Ia','Ie','Ii','Io','Iu','IA','IE','IO','IU','IT','I|','Iy','IY','I','Oa','Oe','Oi','Oo','Ou','OA','OE','OI','OU','OT','O|','Oy','OY','O','Ua','Ue','Ui','Uo','Uu','UA','UE','UI','UO','UT','U|','Uy','UY','U','Ta','Te','Ti','To','Tu','TA','TE','TI','TO','TU','T|','Ty','TY','T','|a','|e','|i','|o','|u','|A','|E','|I','|O','|U','|T','|y','|Y','|','ya','ye','yi','yo','yu','yA','yE','yI','yO','yU','yT','y|','yY','y','Ya','Ye','Yi','Yo','Yu','YA','YE','YI','YO','YU','YT','Y|','Yy']