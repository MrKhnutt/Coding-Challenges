def intToRoman(num: int) -> str:
    '''
    Idea was to use a finite state machine to chunk through the entire thing, works well enough
    with a space/time tradeoff.
    '''
    output = ''
    while (num >= 1000):
        output += 'M'
        num -= 1000
    if num >= 900:
        output += 'CM'
        num -= 900
    if num >= 500:
        output += 'D'
        num -= 500
    if num >= 400:
        output += 'CD'
        num -= 400
    while (num >= 100):
        output += 'C'
        num -= 100
    if num >= 90:
        output += 'XC'
        num -= 90
    if num >= 50:
        output += 'L'
        num -= 50
    if num >= 40:
        output += 'XL'
        num -= 40
    while (num >= 10):
        output += 'X'
        num -= 10
    if num >= 9:
        output += 'IX'
        num -= 9
    if num >= 5:
        output += 'V'
        num -= 5
    if num >= 4:
        output += 'IV'
        num -= 4
    while num >= 1:
        output += 'I'
        num -= 1
        
    return output

if __name__ == '__main__':
    assert intToRoman(512) == 'DXII'
    assert intToRoman(11) == 'XI'
    assert intToRoman(12345) == 'MMMMMMMMMMMMCCCXLV'
    print("Passed!")
