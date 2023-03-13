class Character:
    """
    A class that represents a character in the game.

    Attributes:
        name (str): The name of the character.
        victories (int): The number of victories the character has.

    Methods:
        None
    """

    def __init__(self, name):
        self.name = name
        self.victories = 0


class Room:
    """
    A class that represents a room in the game.

    Attributes:
        name (str): The name of the room.
        description (str): The description of the room.
        situation (dict): A dictionary of adjacent rooms.
        character (dict): A dictionary of characters in the room.
        items (str): The items present in the room.

    Methods:
        set_description(description): Set the description of the room.
        link_room(neighbour, direction): Link a room to another room.
        set_character(character): Set a character in the room.
        set_item(item): Set an item in the room.
        get_details(): Get the details of the room.
        get_character(): Get the character in the room.
        get_item(): Get the item in the room.
        move(command): Move to another room.
    """

    def __init__(self, name):
        self.name = name
        self.description = ""
        self.situation = {}
        self.character = {'enemy': '', 'friend': ''}
        self.items = ''

    def set_description(self, description):
        self.description = description

    def link_room(self, neighbour, direction):
        self.situation[direction] = neighbour

    def set_character(self, character):
        if isinstance(character, Enemy):
            self.character['enemy'] = character
        else:
            self.character['friend'] = character

    def set_item(self, item):
        self.items = item

    def get_details(self):
        print(self.name)
        print("--------------------")
        print(self.description)

        if self.situation:
            for direction in self.situation:
                print(f'The {self.situation[direction].name} is {direction}!')

    def get_character(self):
        if self.character:
            if self.character['enemy']:
                return self.character['enemy']

            if self.character['friend']:
                return self.character['friend']

    def get_item(self):
        if self.items:
            return self.items
        return None

    def move(self, command):
        return self.situation[command]


class Enemy:
    """
    A class that represents an enemy in the game.

    Attributes:
        name (str): The name of the enemy.
        description (str): The description of the enemy.
        defeats (int): The number of times the enemy has been defeated.

    Methods:
        set_conversation(words): Set the words of the enemy.
        set_weakness(weakness): Set weakness of the enemy
        talk(): Prints words
        fight(weapon): Check if weapon can defeat enemy
        get_defeated(): returns number of defeats
        describe(): describes himself 
    """
    defeats = 0
    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description
        self.defeats = 0
    
    def set_conversation(self, words):
        self.words = words

    def set_weakness(self, weakness):
        self.weakness = weakness
    
    def talk(self):
        print(f'[{self.name} says]: {self.words}')

    def fight(self, weapon):
        self.weapon = weapon
        if self.weapon == self.weakness:
            return True
        return False
    
    def get_defeated(self):
        return self.defeats

    def describe(self):
        print(f'{self.name} is here!')
        print(self.description)


class Item:
    """
    A class to represent an item in the game world.
    
    Attributes:
    -----------
    name : str
        The name of the item.
    description : str
        The description of the item.
    
    Methods:
    --------
    __init__(name: str)
        Initializes a new instance of the Item class with the given name.
        
    set_description(description: str)
        Sets the description of the item to the given value.
        
    describe()
        Prints a description of the item.
        
    get_name() -> str
        Returns the name of the item.
    """

    def __init__(self, name) -> None:
        self.name = name
    
    def set_description(self, description):
        self.description = description

    def describe(self):
        print(f'The [{self.name}] is here - {self.description}')
    
    def get_name(self):
        return self.name

    


class Friend:
    """
    A class to represent a friend in the game world.
    
    Attributes:
    -----------
    name : str
        The name of the friend.
    description : str
        The description of the friend.
    
    Methods:
    --------
    __init__(name: str, description: str)
        Initializes a new instance of the Friend class with the given name and description.
        
    describe()
        Prints a description of the friend.
        
    talk() -> str
        Returns a string representing the words that the friend says.
    """

    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description
    
    def describe(self):
        print(self.description)

    def talk(self):
        return self.words
    
if __name__ ==  '__main__':
    import doctest
    print(doctest.testmod())