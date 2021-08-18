from typing import Text
from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import *


def test_version():
    assert __version__ == '0.1.0'

def test_one():
   text='my name is nura'
   key = 2
   assert encrypt(text, key) == 'oa pcog ku pwtc'

def test_two():
    text='oapcogkupwtc'
    key=2
    assert decrypt(text, key) == 'mynameisnura'

def test_three():
   text='652//**  --'
   key = 2
   assert encrypt(text, key) == '           '

def test_decrept():
    text = 'It was the best of times, it was the worst of times.'
    key = 1
    assert decrypt(text, key) == 'Hs vzr sgd adrs ne shldr  hs vzr sgd vnqrs ne shldr '

def test_decrept_decrepted():
    text = 'Hs vzr sgd adrs ne shldr  hs vzr sgd vnqrs ne shldr '
    key = 1
    assert decrypt(text, key) == 'Gr uyq rfc zcqr md rgkcq  gr uyq rfc umpqr md rgkcq '

