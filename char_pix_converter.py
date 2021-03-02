'''
import math
OnePixToChar = 0.125
OneCharToPix = 8

def PixToChar(pixels, charFont=1):
    return math.ceil(pixels*OnePixToChar*charFont)


def CharToPix(chars, charFont=1):
    return math.ceil(chars*charsFont*OneCharToPix)
'''