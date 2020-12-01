Trying:
    encode('SOS')
Expecting:
    '... --- ...'
ok
Trying:
    encode('MAI-PYTHON-2019')
Expecting:
    '-- .- .. -....- .--. -.-- - ....
    --- -. -....- ..--- ----- .---- ----.'
ok
Trying:
    encode('I-LIKE-AVITO') # doctest: +ELLIPSIS
Expecting:
    '.. ... ---'
ok
Trying:
    encode("ЯНДЕКС") # doctest: +IGNORE_EXCEPTION_DETAIL
Expecting:
    Traceback (most recent call last):
    KeyError: 'Я'
ok
2 items had no tests:
    morse
    morse.decode
1 items passed all tests:
   4 tests in morse.encode
4 tests in 3 items.
4 passed and 0 failed.
Test passed.
