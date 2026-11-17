"""IF statement

@see: https://docs.python.org/3/tutorial/controlflow.html

There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is
short for ‘else if’, and is useful to avoid excessive indentation.

An if … elif … elif … sequence is a substitute for the switch or case statements found
in other languages.
"""


def test_if_statement():
    """IF statement"""

    number = 15
    conclusion = ''

    if number < 0:
        conclusion = 'Number is less than zero'
    elif number == 0:
        conclusion = 'Number equals to zero'
    elif number < 1:
        conclusion = 'Number is greater than zero but less than one'
    else:
        conclusion = 'Number bigger than or equal to one'

    assert conclusion == 'Number bigger than or equal to one'

def test_nested_conditions():
    grade = 50
    enrolled = True
    if grade >= 50:
        if enrolled:
            result = 'Passed'
        else:
            result = 'Not enrolled'
    else:
        result = 'Failed'
    assert result == 'Passed'

def test_multiple_elif_branches():
    def grade(score):
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        else:
            return 'F'

    assert grade(98) == 'A'
    assert grade(82) == 'B'
    assert grade(76) == 'C'
    assert grade(39) == 'F'
