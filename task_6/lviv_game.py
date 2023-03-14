"""
Journey trough Lviv
"""
again = True

def main():
    def set_neighbours(self, neighbour):
        """
        Sets two Street objects as neighbours.

        Args:
            neighbour (Street): Another Street object to be set as a neighbour.

        Returns:
            None
        """
        self.set_neighbour_street(neighbour)
        neighbour.set_neighbour_street(self)


    def del_smth_from(place, smth):
        """
        Removes an item or a character from a Street or a Building object.

        Args:
            place (Street or Building): A Street or a Building object.
            smth (Item or Character): An Item or a Character object to be removed from place.

        Returns:
            None
        """
        if isinstance(place , Street):
            if isinstance(smth, Item):
                place.items = None
            if isinstance(smth, Character):
                place.characters = None
            
        if isinstance(place , Building):
            if isinstance(smth, Character):
                place.characters = None


    class Player:
        """
        Represents a player in the game.
        """
        def __init__(self, name):
            """
            Initializes a Player object.

            Args:
                name (str): The player's name.
            """
            self.health = 30
            self.time = 100
            self.name = name
            self.backpack = []


    class Character:
        """
        Represents a character in the game.
        """
        def __init__(self, name, words):
            """
            Initializes a Character object.

            Args:
                name (str): The character's name.
                words (str): The character's words.
            """
            self.name = name
            self.words = words


    class Enemy(Character):
        """
        Represents an enemy character in a game.

        Attributes:
            name (str): The name of the enemy character.
            words (str): The words spoken by the enemy character.
            weakness (str): The weakness of the enemy character.
            harm (int): The amount of harm the enemy character can inflict.

        Methods:
            set_weakness(weakness): Set the weakness of the enemy character.
            speak(): Return the words spoken by the enemy character.
            fight(weapon): Check if the weapon used by the player is the enemy character's weakness.

        """
        def __init__(self, name, words, harm, weakness) -> None:
            super().__init__(name, words)
            self.weakness = weakness
            self.harm = harm

        def set_weakness(self, weakness):
            self.weakness = weakness
        
        def speak(self):
            return self.words
        
        def fight(self, weapon):
            if weapon == self.weakness:
                return True
            return False


    class Friend(Character):
        """
        Represents a friendly character in a game.

        Attributes:
            name (str): The name of the friendly character.
            words (str): The words spoken by the friendly character.
            item (str): The item given by the friendly character.

        Methods:
            interact(player): Give the item to the player and print a message.
            speak(): Return the words spoken by the friendly character.

        """
        def __init__(self, name, words, item = None) -> None:
            super().__init__(name, words)
            self.item = item

        def interact(self, player):
            print(self.words)
            print(f'{self.name} gave you {self.item}')
            player.backpack.append(self.item)
        
        def speak(self):
            return self.words


    class Place:
        def __init__(self, name, time_taken) -> None:
            self.name = name
            self.time_taken = time_taken
        
        def set_character(self, chrctr):
            self.characters[chrctr.name] = chrctr
        
        def set_item(self, item):
            self.items[item.name] = item


    class Street(Place):
        """
        Represents a street in a city.

        Attributes:
            name (str): The name of the street.
            time_taken (int): The amount of time taken to traverse the street.
            items (dict): The items present on the street.
            neighbour_streets (dict): The neighbouring streets.
            characters (dict): The characters present on the street.
            buildings (dict): The buildings present on the street.

        Methods:
            set_neighbour_street(new_street): Set a new neighbouring street.
            place_building(building): Place a building on the street.
            move(command): Move to a neighbouring street.
            describe(): Print a description of the street.

        """
        def __init__(self, name, time_taken) -> None:
            super().__init__(name, time_taken)

            self.items = {}
            self.neighbour_streets = {}
            self.characters = {}
            self.buildings = {}

        def set_neighbour_street(self, new_street):
            self.neighbour_streets[new_street.name] = new_street
        
        def place_building(self, building):
            self.buildings[building.name] = building
        
        def move(self, command):
            return self.neighbour_streets[command]

        def describe(self):
            print(f"{self.name} street")
            print('--------------')
            for j in self.neighbour_streets:
                print(f'{j} street is nearby, it would take {self.neighbour_streets[j].time_taken} minutes')

            for i in self.buildings:
                print(f'{i} is here it would take {self.buildings[i].time_taken} minutes')

            if self.items:
                for e in self.items:
                    print(f'{e} is here')



    class Building(Place):
        """
        Represents a building in a city.

        Attributes:
            name (str): The name of the building.
            time_taken (int): The amount of time taken to traverse the building.
            characters (dict): The characters present in the building.

        Methods:
            describe(): Print a description of the building.
            talk(): Have a conversation with the character in the building.

        """
        def __init__(self, name, time_taken) -> None:
            super().__init__(name, time_taken)
            self.characters = {}
        
        def describe(self):
            print(self.name)
            print('--------------')
            if self.characters:
                for i in self.characters:
                    print(f'{i} is here')
            
        def talk(self):
            character = list(self.characters.values())[0]
            print(character.speak())

    class Epicenter(Place):
        """
        Represents the epicenter in a city.

        Attributes:
            name (str): The name of the epicenter.
            time_taken (int): The amount of time taken to traverse the epicenter.
            wrenches (int): The number of wrenches at the epicenter.

        Methods:
            set_wrenches(wrenches): Set the number of wrenches at the epicenter.
            describe(): Print a description of the epicenter.

        """
        def __init__(self, name, time_taken) -> None:
            super().__init__(name, time_taken)
        
        def set_wrenches(self, wrenches):
            self.wrenches = wrenches

        def describe(self):
            print(self.name)
            print('--------------')
            print(f'Wrenches here: {self.wrenches}')


    class Item:
        """
        The Item class represents an item that can be taken by a player.

        Attributes:
            name: (str) The name of the item.
            message: (str) The message to be displayed when the item is taken.
            time: (int) The time taken by the item.

        Methods:
            take(taker):When called, it prints the message of the item to be taken.
        """
        def __init__(self, name, time, message) -> None:
            self.name = name
            self.message = message
            self.time = time

        def take(self, taker):
            print(self.message)


    Intro = """
You are a student of the Lviv Polytechnic,\n\
before leaving for classes, your dad asked\n\
you to go to the Epicenter and buy a size 13 wrench.\n\
There are 3 Epicenters in Lviv, getting to each\n\
epicenter takes energy, and trouble can happen \n\
along the way. You live in Ryasne 2 district,\nremember to go back.\n\n\
You are standing on Stepan Bandera Street, unfortunately,\n\
the Lviv metro is being repaired today, so you will have to walk.
    """
    me = Player('me')
    print(Intro)

    Instruction = """
Instruction
==============
[STOP THE GAME] - to leave the game at any moment
While on street:
--------------
[enter] - to enter building including Home
[enter_ep] - to enter Epicentern
[take] - to take items like apples, or take transport
[steet name ex. [Horodotska]] - to move to another street\n
While in building:
--------------
[leave] - to leave from steet
[talk] - to talk with someone
[fight] - to fight enemy
[lose] - to lose automatically

NOTE: any other commands will be interpreted as leave, lose, or ignored
    """

    print(Instruction)

    dim = Building('Home', 5)
    epicenter_south = Epicenter('Epicenter on Stryiska', 5)
    epicenter_north = Epicenter('Epicenter on Hmelnytskoho', 7)
    epicenter_west = Epicenter('Epicenter on Horodotska', 5)

    epicenter_north.set_wrenches([5, 7, 9, 10, 13, 14, 16, 17, 21, 31])
    epicenter_south.set_wrenches([4, 7, 8, 10, 12, 14, 15, 17, 22, 28])
    epicenter_west.set_wrenches([2, 3, 5, 10, 11, 12, 14, 15, 20, 40])

    Stepana_Bandery_street = Street('Stepana Bandery', 0)
    Mykolaya_Kopernyka_street = Street('Mykolaya Kopernyka', 3)
    Heroyiv_Majdanu_street = Street('Heroyiv Majdanu', 2)
    Stryiska_street = Street('Stryiska', 9)
    Horodotska_street = Street('Horodotska', 8)
    Prospect_Svobody_street = Street('Prospect Svobody', 2)
    Bohdana_Hmelnytskoho_street = Street('Bohdana Hmelnytskoho', 7)
    Kiltseva_street = Street('Kiltseva', 6)
    Shevchenka_street = Street('Shevchenka', 7)

    set_neighbours(Heroyiv_Majdanu_street, Mykolaya_Kopernyka_street)
    set_neighbours(Stryiska_street, Heroyiv_Majdanu_street)
    set_neighbours(Mykolaya_Kopernyka_street, Stepana_Bandery_street)
    set_neighbours(Horodotska_street, Stepana_Bandery_street)
    set_neighbours(Stryiska_street, Kiltseva_street)
    set_neighbours(Prospect_Svobody_street, Mykolaya_Kopernyka_street)
    set_neighbours(Bohdana_Hmelnytskoho_street, Prospect_Svobody_street)
    set_neighbours(Horodotska_street, Prospect_Svobody_street)
    set_neighbours(Kiltseva_street, Horodotska_street)
    set_neighbours(Shevchenka_street, Horodotska_street)
    set_neighbours(Shevchenka_street, Kiltseva_street)


    rover = Item('rover', 5, 'Fast and efficient transport')
    marshrutka = Item('marshrutka', -5, 'Slow and not efficient transport')
    apple = Item('svizhe yabluko', 10, 'An apple a day keeps a doctor away')
    enerhetyk = Item('enerhetyk', -7, 'Energy drinks are evil and unhealthy')
    tsehla = Item('Tsehla', 6, 'Your backpack became heavies, your motivation increased')
    pidzemnyi_perehid = Item('pidzemnyi perehid', -4, 'I told you lviv metro is being repaired, whole underground is closed')

    Mykolaya_Kopernyka_street.set_item(apple)
    Horodotska_street.set_item(rover)
    Stryiska_street.set_item(enerhetyk)
    Prospect_Svobody_street.set_item(marshrutka)
    Kiltseva_street.set_item(tsehla)
    Shevchenka_street.set_item(pidzemnyi_perehid)

    book = Item('book', 0, '')
    reflexes = Item('reflexes', 0, '')
    fastest_lap = Item('fastest lap', 0, '')


    toto_wolf = Enemy('Toto', 'I am Toto, you need to change your car or I will report on you', -10, fastest_lap)
    latifi = Enemy('Latifi', 'I am Latifi, I will crash my car into you', -20, reflexes)
    fia = Enemy('FIA', 'I am FIA(Fédération Internationale de Automobile) I will revrite rules and demand 50000$ from you', -25, book)

    horner = Friend('Christian Horner', f'I am Christian Horner, wrench is not in Epicenter on Stryiska, also take this book, to defend against FIA', book)
    checo = Friend('Checo', 'I am Checo, take this reflexes, to defend against Latifi', reflexes)
    valteri = Friend('Valteri', 'I am Valteri Bottas, take this fastest lap, to defend against Toto', fastest_lap)

    garage = Building('Garage', 5)
    campus = Building('Campus', 6)
    track = Building('Race track', 10)
    wind_tunnel = Building('Wind tunnel', 5)
    petronas_towers = Building('Petronas Towers', 7)
    aztec_stadium = Building('Aztec Stadium', 4)

    wind_tunnel.set_character(horner)
    petronas_towers.set_character(toto_wolf)
    aztec_stadium.set_character(checo)
    track.set_character(latifi)
    campus.set_character(fia)
    garage.set_character(valteri)

    Mykolaya_Kopernyka_street.place_building(garage)
    Heroyiv_Majdanu_street.place_building(wind_tunnel)
    Stepana_Bandery_street.place_building(aztec_stadium)
    Horodotska_street.place_building(petronas_towers)
    Prospect_Svobody_street.place_building(campus)
    Bohdana_Hmelnytskoho_street.place_building(track)
    Stryiska_street.place_building(epicenter_south)
    Horodotska_street.place_building(epicenter_west)
    Bohdana_Hmelnytskoho_street.place_building(epicenter_north)
    Shevchenka_street.place_building(dim)


    current_street = Stepana_Bandery_street

    won = False

    while me.time > 0 and me.health > 0:
        print("\n")
        current_street.describe()
        print(f"Your backpack: {[i.name for i in me.backpack]}")
        print(f'Your health: {me.health}\nYour time: {me.time}')
        
        command = input('> ')

        if command in list(current_street.neighbour_streets.keys()):
            current_street = current_street.move(command)
            me.time -= current_street.time_taken

        elif command == 'STOP THE GAME':
            break

        elif command == 'take':
            if list(current_street.items.keys()):
                item = list(current_street.items.values())[0]
                me.backpack.append(item)
                print(item.message)
                del_smth_from(current_street, item)
                me.time += item.time
            else:
                print('There is nothing here to take!')
        elif command == 'enter':
            if list(current_street.buildings.keys()):
                building = list(current_street.buildings.values())[0]
                if building == dim:
                    me.time -= building.time_taken
                    if me.health > 0 and me.time > 0:
                        if 13 in me.backpack:
                            print('You won')
                            won = True
                            break
                        else:
                            print("You didn`t find right wrench\nGame Over")
                            break
                    else:
                        print('You ran out of time')
                        break

                print()
                building.describe()
                me.time -= building.time_taken
                if building.characters:
                    print('You can talk or leave')
                    command = input('> ')
                    if command == 'leave':
                        continue
                    elif command == 'talk':
                        building.talk()
                        enemy = list(building.characters.values())[0]
                        if isinstance(enemy, Friend):
                            me.backpack.append(enemy.item)
                            del_smth_from(building, enemy)
                        else:
                            harm = enemy.harm
                            print('You either fight or lose, what do you chose')
                            command = input('> ')
                            if command == 'lose':
                                me.health += harm
                            elif command == 'fight':
                                command = input('chose your weapon > ')
                                if command in [i.name for i in me.backpack]:
                                    if enemy.fight(me.backpack[[i.name for i in me.backpack].index(command)]):
                                        print("Well done you won! You get more time")
                                        me.time += 10
                                        del_smth_from(building, enemy)
                                    else:
                                        me.health += harm
                                        print('You lost!')
                                else:
                                    print('You can not fight with that')
                            else:
                                print('All unrecognzed commands are interpreted as leave or lose')
                    else:
                        print('All unrecognzed commands are interpreted as leave')
                else:
                    print('There is no one here!')
            else:
                print('There is nowhere to enter!')
        
        elif command == 'enter_ep':
            help_list = [i.startswith('Epicenter') for i in list(current_street.buildings.keys())]
            if True in help_list:
                building = list(current_street.buildings.values())[help_list.index(True)]
                me.time -= building.time_taken
                print()
                building.describe()
                command = input('take or leave > ')
                if command == 'take' or command == "leave":
                    if command == 'take':
                        command = input('which size > ')
                        try: 
                            command = int(command)
                            if command in building.wrenches:
                                me.backpack.append(Item(command, 0, ''))
                        except:
                            print('All unrecognzed commands are interpreted as leave or lose')
                    else:
                        continue
                else:
                    print('All unrecognzed commands are interpreted as leave or lose')
            else:
                print('There is no Epicenter here')

    if me.time <= 0:
        print()
        print('You ran out of time')
    if me.health <= 0:
        print()
        print('You run out of health')

    if won:
        print('Congratulations again!\nChose [again] or [exit]')
        to_do = input('>')
    else:
        print('That`s unfortunate\nChose [again] or [exit]')
        to_do = input('>')
    return to_do

if again:
    while main() == 'again':
        continue
