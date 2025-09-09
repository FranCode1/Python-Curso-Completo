# ex33d.py

from ex33c import Song

# Crear canciones como instancias de Song
happy_bday = Song([
    "Happy birthday to you",
    "I don't want to get sued",
    "So I'll stop right there"
])

bulls_on_parade = Song([
    "They rally around the family",
    "With a pocket full of shells"
])

# Cantar las canciones
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
