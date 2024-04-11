# pylint: disable=C0114

def reverse(text: str) -> str:
    """
    Return the 'text' backwards.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    str
        The text written backwards.
    """
    return text[::-1]


def first_to_upper(text: str) -> str:
    """
    Changes each first character of the word to uppercase.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    str
        The modified text
    """
    sym = [" ", "\n", "\t", "-", ".", ",", "=", ";", ":"]
    to_compare = ""
    to_return = text[0].upper() # Saving first letter
    for letter in text[1:]:
        if to_compare in sym:
            to_return += letter.upper()
        else:
            to_return += letter
        to_compare = letter

    return to_return

def count_vowels(text: str) -> int:
    """
    Counts number of vovels in the text.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    inp
        Number of vowels.
    """
    vowels = ['y','a','o','i','u','e', 'ą', 'ó', 'ę']
    the_sum = 0

    for char in text:
        if char.lower() in vowels:
            the_sum +=1
    return the_sum



def sum_digits(text: str) -> int:
    """
    Finds all digitts in the text and returns its sum.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    int
        Sum of all digits in the text.
    """
    the_sum = 0
    digits = ['0','1','2','3','4','5','6','7','8','9']
    for char in text:
        if char in digits:
            the_sum += int(char)
    return the_sum

def search_substr(text: str, sub: str) -> int:
    """
    Search for sub(string) in the text. Returns the position or None.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    int or None
        Position of the sub(string) or None.
    """
    for i in range(len(text)):
        test = ""
        for letter in text[i:]:
            test += letter
            if test == sub:
                return i
    return None
