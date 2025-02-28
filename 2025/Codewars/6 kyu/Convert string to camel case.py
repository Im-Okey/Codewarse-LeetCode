"""Complete the method/function so that it converts dash/underscore
   delimited words into camel casing. The first word within the output
   should be capitalized only if the original word was capitalized
   (known as Upper Camel Case, also often referred to as Pascal case).
   The next words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"

Regular ExpressionsAlgorithmsStrings"""


def to_camel_case(text: str) -> str:
    return ''.join([i.capitalize() if text.replace('_', ' ').replace('-', ' ').split().index(i) != 0 else i for i in text.replace('_', ' ').replace('-', ' ').split()])



assert to_camel_case('') == ''
assert to_camel_case('the_stealth_warrior') == 'theStealthWarrior'
assert to_camel_case('The-Stealth-Warrior') == 'TheStealthWarrior'
assert to_camel_case('A-B-C') == 'ABC'