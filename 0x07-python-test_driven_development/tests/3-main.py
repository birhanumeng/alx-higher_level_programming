#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("Berhanu", "Haylie")
say_my_name("Hailu", "Goshe")
say_my_name("Erkihun")
try:
    say_my_name(12, "Johne")
except Exception as e:
    print(e)
