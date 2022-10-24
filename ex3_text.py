#!/usr/bin/env python3
from pathlib import Path
import re


def EraseWords():
    WordsToErase = ["we", "cannot", "with"]
    print(f"\nErase words: {WordsToErase}\n")
    TextSample = "We cannot solve our problems with the same thinking we used when we created them."
    TempTextSample = TextSample

    for word in WordsToErase:
        TempTextSample = TempTextSample.replace(word,"")

    print(f"Text before erase: {TextSample}")
    print(f"Test after erase: {TempTextSample}")

def ReplaceWords():
    WordsToReplace = {'we': 'you', 'cannot': 'can', 'with': 'without'}
    print(f"\nReplace words: {WordsToReplace}\n")
    TextSample = "We cannot solve our problems with the same thinking we used when we created them."
    TempTextSample = TextSample

    for word in WordsToReplace:
        TempTextSample = TempTextSample.replace(word,WordsToReplace[word])

    print(f"Text before erase: {TextSample}")
    print(f"Test after erase: {TempTextSample}")


if __name__ == '__main__':
    EraseWords()
    ReplaceWords()