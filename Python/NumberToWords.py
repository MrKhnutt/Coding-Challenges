def numberToWords(num: int) -> str:
    teens = {'10':'Ten', '11': 'Eleven', '12':'Twelve', '13':'Thirteen', '14':'Fourteen', '15':'Fifteen', '16':'Sixteen', '17':'Seventeen', '18':'Eighteen', '19': 'Nineteen'}
    tens = {'2': 'Twenty', '3': 'Thirty', '4':'Forty', '5':'Fifty', '6':'Sixty', '7':'Seventy', '8':'Eighty', '9':'Ninety', '0':''}
    places = ['Hundred','Thousand','Million','Billion']
    ones = {'1':'One', '2':'Two', '3':'Three', '4':'Four', '5':'Five', '6':'Six', '7':'Seven', '8':'Eight', '9':'Nine', '0':''}
    output = ''
    bits = []
    rev = str(num)[::-1]
    while rev != '':
        bits.append(rev[0:3][::-1])
        rev = rev[3:]
    bits = bits[::-1]

    if num == 0:
        return 'Zero'

    place = len(bits) - 1
    for bit in bits:
        if bit == '000':
            place -= 1
            continue
        if len(bit) == 3:
            if bit[0] != '0':
                output += ones[bit[0]] + ' ' + places[0] + ' '
            if bit[1] == '1':
                output += teens[bit[1:]] + ' '
            elif bit[1] != '0':
                output += tens[bit[1]] + ' ' + ones[bit[2]] + ' '
            else:
                output += ones[bit[2]] + ' '
        elif len(bit) >= 2:
            if bit[0] == '1':
                output += teens[bit] + ' '
            elif bit[0] != '0':
                output += tens[bit[0]] + ' ' + ones[bit[1]] + ' '
            else:
                output += ones[bit[0]] + ' '
        else:
            output += ones[bit] + ' '
        if place != 0:
            output += places[place] + ' '
        place -= 1

    return output.replace('  ', ' ').strip()
