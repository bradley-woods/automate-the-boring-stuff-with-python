# Automate the Boring Stuff with Python
# Chapter 5 - Dictionaries and Structuring Data: Chess Dictionary Validator

def isValidChessBoard(chessBoard):
    bking_count = wking_count = bpawn_count = wpawn_count = bpiece_count = wpiece_count = 0

    # Check for valid space '1a' to '8h'
    for key in chessBoard.keys():
        if int(key[0]) not in range(1,9):
            return False
        elif key[1:] not in list("abcdefgh"):
            return False

    for value in chessBoard.values():
        # Check for 1 king per player
        if value == "bking":
            bking_count += 1
            bpiece_count += 1
        elif value == "wking":
            wking_count += 1
            wpiece_count += 1
        # Check for max 8 pawns per player
        elif value == "bpawn":
            bpawn_count += 1
            bpiece_count += 1
        elif value == "wpawn":
            wpawn_count += 1
            wpiece_count += 1
        # Check pieces are correctly labelled 
        elif value[1:] not in ['knight', 'bishop', 'rook', 'queen']:
            return False
        # Check for max 16 pieces per player
        elif value[0] == "b":
            bpiece_count += 1
        elif value[0] == "w":
            wpiece_count += 1
        else:
            return False

    if bking_count != 1 or wking_count != 1:
        return False
    elif bpawn_count > 8 or wpawn_count > 8:
        return False
    elif bpiece_count > 16 or wpiece_count > 16:
        return False
    else:
        return True


print(isValidChessBoard({'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}))
