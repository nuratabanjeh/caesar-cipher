from typing import Text
from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import *


def test_version():
    assert __version__ == '0.1.0'

def test_one():
   text='my name is nura'
   key = 2
   assert encrypt(text, key) == 'oapcogkupwtc'

def test_two():
    text='oapcogkupwtc'
    key=2
    assert decrypt(text, key) == 'mynameisnura'

def test_three():
   text='652//**  --'
   key = 2
   assert encrypt(text, key) == ''