DEADEND_UP = [
    '  |  ',
    '  o  ',
    '     '
]
DEADEND_DOWN = [
    '     ',
    '  o  ',
    '  |  '
]
DEADEND_LEFT = [
    '     ',
    '--o  ',
    '     '
]
DEADEND_RIGHT = [
    '     ',
    '  o--',
    '     '
]

STRAIGHT_VERTICAL = [
    '  |  ',
    '  o  ',
    '  |  '
]
STRAIGHT_HORIZONTAL = [
    '     ',
    '--o--',
    '     '
]


CORNER_UP = [
    '  |  ', 
    '  o--', 
    '     '
]
CORNER_DOWN = [
    '     ',
    '--o  ',
    '  |  '
]
CORNER_LEFT = [
    '  |  ',
    '--o  ',
    '     '
]
CORNER_RIGHT = [
    '     ',
    '  o--',
    '  |  '
]

TJOIN_UP = [
    '  |  ',
    '--o--',
    '     '
]
TJOIN_DOWN = [
    '     ',
    '--o--',
    '  |  '
]
TJOIN_LEFT = [
    '  |  ',
    '--o  ',
    '  |  '
]
TJOIN_RIGHT = [
    '  |  ',
    '  o--',
    '  |  '
]

def symbol_row(symbols):
    
    row = ""
    for sym in symbols:
        row += sym[0] + ' '
    row += "\n"
    for sym in symbols:
        row += sym[1] + ' '
    row += "\n"
    for sym in symbols:
        row += sym[2] + ' '
    row += "\n"
    
    return row
        