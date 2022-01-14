# Django's standard crypto functions and utilities.

## InvalidAlgorithm(ValueError)
* algorithm is not supported by hashlib.

## salted_hmac
* return the HMAC of ```value```, using a key generated from ```key_salt``` and a ```secret``` (which defaults to settings.SECRET_KEY). Default algorithm is SHA1, but any algorithm name supported by hashlib can be passed.

## NOT_PROVIDED ``` = object()```
* RemovedInDjango400Warning

## RANDOM_STRING_CHARS
* random string

## get_random_string
* return a securely generated random string.
* The bit length of the returned value can be calculated with the formula: log_2(len(allow_chars)^length)

## constant_time_compare
* return ```True``` if the two strings are equals, ```False``` otherwise.

## pbkdf2
* return the hash of password using pbkdf2.
