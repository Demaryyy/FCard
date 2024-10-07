from model import Kard, db

MrBebra = Kard.create(kard_name='Mr.Bebra', rarity='Rare', img='cards/Mr.Bebra.png', procent=50, coficent=1.5,
                      is_relative=True)
SithFreddie = Kard.create(kard_name='Ситх Фредди', rarity='Rare', img='cards/SithFreddie.png', procent=45, coficent=1.5,
                          is_relative=True)
McFreddie = Kard.create(kard_name='Mc.Freddie', rarity='Epic', img='cards/Mc.Freddie.png', procent=35, coficent=2.5,
                        is_relative=True)
BusyFreddie = Kard.create(kard_name='Деловой Фредди', rarity='Epic', img="cards/ДеловойФредди.png", procent=40,
                          coficent=2.5, is_relative=True)
GrandpaFreddie = Kard.create(kard_name='Дед Фредди', rarity='Mythic', img='cards/ДедФредди.png', procent=13, coficent=5,
                             is_relative=True)
Freddie = Kard.create(kard_name='Freddie🤫🧏🏻‍', rarity='Mythic', img='cards/Freddie.png', procent=15, coficent=5,
                      is_relative=True)
CuteFreddie = Kard.create(kard_name='Милии Мшк Фредде', rarity='Legendary', img='cards/МиллиМшкФредде.png', procent=5,
                          coficent=10, is_relative=True)
HappyFreddie = Kard.create(kard_name='Веселый Фредди', rarity='Legendary', img='cards/ВеселыйФредде.png', procent=8,
                           coficent=10, is_relative=True)
SkibidiFreddie = Kard.create(kard_name='Skibidi Freddie', rarity='Legendary', img='cards/SkibidiFreddie.png',
                             procent=10, coficent=10, is_relative=True)
OholeroFreddie = Kard.create(kard_name='Oholero Freddie', rarity='Chromatic', img='cards/OholeroFreddie.png', procent=1,
                             coficent=20, is_relative=True)
BearFreddie = Kard.create(kard_name='Мшк Фредде', rarity='Chromatic', img='cards/МшкФредде.png', procent=1, coficent=20,
                          is_relative=True)
