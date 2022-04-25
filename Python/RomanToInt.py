import re

def romanToInt(s: str) -> int:
    count = 0
    rule = '(I[VX]|X[LC]|C[DM])'
    rom = {'I': 1, 'V': 5, 'X':10,'L':50, 'C':100, 'D':500, 'M': 1000}
    
    matches = re.findall(rule, s)
    new_s   = re.sub(rule, '', s)
    
    for i in matches:
        count += rom[i[1]] - rom[i[0]]
    for i in new_s:
        count += rom[i]
    return count

if __name__ == '__main__':
    assert romanToInt('XIV') == 14
    assert romanToInt('MCMIV') == 1904
    assert romanToInt('IV') == 4
    print("Passed!")