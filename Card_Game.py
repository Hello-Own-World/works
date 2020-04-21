import random
import time

class Character:
    """Class to create character"""
    def __init__(self, name, health, power, cost, ability_cost, id):
        self.name = name
        self.health = health
        self.power = power
        self.cost = cost
        self.dead = False
        self.ability_cost = ability_cost
        self.id = id

    def fight(self, other):
        self.health -= other.power
        other.health -= self.power

        if self.health <= 0 and other.health <= 0 or self.health == other.health:
            self.dead = True
            other.dead = True
            return "both"
        elif self.health <= 0  or self.health < other.health:
            self.dead = True
            return "self"  # delete character
        elif other.health <= 0 or other.health < self.health:
            other.dead = True
            return "other"
        return False  # don`t delete

    def __str__(self):
        return "-"*18 + f"id:{self.id}\nname:{self.name}  cost:{self.cost}\npower:{self.power}  health:{self.health}\n skill cost : {self.ability_cost}" +"-"*18

    def __repr__(self):
        return f"|id:{self.id} name:{self.name} cost:{self.cost} power:{self.power} health:{self.health} skill_cost:{self.ability_cost}|"

"""Classes for game characters"""
class Ork(Character):
    def use_skill(self):
        self.power += 2
        print("succes")


class Dwarf(Character):
    def use_skill(self):
        self.health += 2
        print("succes")

class Human(Character):
    def use_skill(self):
        self.power = random.randint(5, 10)
        self.health = random.randint(4, 10)
        print("succes")

class Dark_Elf(Character):
    def use_skill(self):
        self.power = random.randint(5, 10)
        print("succes")


class Elf(Character):
    def use_skill(self):
        self.power = random.randint(5, 10)
        print("succes")


class Undead(Character):
    def use_skill(self):
        self.health = random.randint(4, 10)
        print("succes")


class Deck:
    def __init__(self, start_size):
        self.start_size = start_size
        self.size = 0
        self.cards = []
        self.create_deck()

    def add_card(self, character):
        """Metod used to create deck"""
        counter = 0
        for card in self.cards:
            if card.name == character.name:
                counter += 1
        if counter < 6:
            self.cards.append(character)
            self.size += 1
        else:
            print("Too much same characters")

    def remove_card(self, character_name):
        """Metod ,that delete card from deck by name"""
        for card in self.cards:
            if card.name == character_name:
                self.cards.remove(card)
                self.size -= 1
                break
        else:
            print("the card isn`t in deck")

    def pop_card(self, ind=-1):
        """
        Metod ,that delete last card in deck ,by default.
        And if inputed index > deck`s size - delete ,also last card ,or
        if inputed index < deck`s size - delete first card
        """
        try:
            self.size -= 1
            return self.cards.pop(ind)
        except IndexError:
            if ind > self.size:
                self.size -= 1
                return self.cards.pop()
            else:
                self.size -= 1
                return self.cards.pop(0)

    def create_deck(self):
        """Metod ,that create firs deck (start game)"""
        ends = ["i", "y", "est", "ina", "ena", "a"]
        names = ["Ork", "Elf", "Dwarf", "Undead", "Human","Dark_Elf"]
        classes = [Ork, Elf, Dwarf, Undead, Human, Dark_Elf]
        ability_cost_lst = [3,2,2,3,2,3]
        for i in range(self.start_size):
            random_name = random.choice(names)
            random_index = names.index(random_name)
            name = random_name + random.choice(ends)
            cost = random.randint(1, 10)
            power = random.randint(cost-1, cost+2)
            ability_cost = ability_cost_lst[random_index]
            if (cost+power)//2 - 1 > 0:
                health = random.randint((cost+power)//2-1, (cost+power)//2+1)
            else:
                health = random.randint((cost + power)//2, (cost + power)//2+2)
            self.add_card(classes[random_index](name, health, power, cost,ability_cost, i+1))
    def __repr__(self):
        return "List of cards in deck :"+str(self.cards)


class Player:
    def __init__(self, name): # Not sure , if it requires attribute money
        self.name = name
        self.cards = []
        self.money = 20
        self.score = 0

    def use_ability (self,choise): # Not working correct
        if choise.lower() == "y":
            if self.money >= table.cards[self.name].ability_cost:
                table.cards[self.name].use_skill()
            else:
                print("Not enough money")
        elif choise.lower() == "n":
            return False
        else:
            print("Wrong input")
            self.use_ability(input("Use character ability ? Y/N"))


    def add_card(self, deck):
        """Add card to hand ,delete from deck"""
        self.cards.append(deck.pop_card())

    def put_card(self, character_id):
        """Delete card from hand , return it """
        for card in self.cards:
            if card.id == character_id:
                if self.money >= card.cost:
                    self.money -= card.cost
                    table.cards[self.name] = card
                    self.cards.remove(card)
                    return True
                else:
                    print("Not enough money")
                    self.put_card(int(input("Enter new id :")))

        print("U don`t have this card")
        self.put_card(int(input("Enter new id :")))

    def take_hand(self, deck, amount):
        """Gives player n number of cards"""
        for i in range(amount):
            self.add_card(deck)
    def __str__(self):
        return str(self.cards)
class Table :
    def __init__(self):
        self.cards = {}
        self.game = True
    def start_round (self):
        fight_result = self.cards[change_turn[0].name].fight(self.cards[change_turn[1].name])
        if fight_result == "both":
            self.cards.clear()
            change_turn[0].add_card(deck)
            change_turn[0].money += 7
            change_turn[1].add_card(deck)
            change_turn[1].money += 7
            print("Draw !")
        elif fight_result == "self":
            change_turn[1].score += 1
            change_turn[1].money += 10
            change_turn[0].money += 7
            change_turn[1].add_card(deck)
            change_turn[0].add_card(deck)
            print("In round "+str(round_counter)+" --- "+change_turn[1].name," win !")
        elif fight_result == "other":
            change_turn[0].score += 1
            change_turn[0].money += 10
            change_turn[1].money += 7
            change_turn[0].add_card(deck)
            change_turn[1].add_card(deck)
            print("In round "+str(round_counter)+" --- "+change_turn[0].name, " win !")
        print(change_turn[0].name + " score :" + str(change_turn[0].score)+ "\n" + change_turn[1].name + " score :" + str(change_turn[1].score ))

        if change_turn[0].score == 10 :
            print(change_turn[0].name + " won this game !")
            self.game = False
        elif change_turn[1].score == 10 :
            print(change_turn[1].name + " won this game !")
            self.game = False


    def __str__(self):
        return "Cards on table :" + str(self.cards)

deck = Deck(100)
table = Table()
round_counter = 1
print(deck)
#'''

player1 = Player(str(input("Enter name of P1 :")))
player2 = Player(str(input("Enter name of P2 :")))

player1.take_hand(deck,5)
player2.take_hand(deck,5)

change_turn = [player1,player2]
while table.game == True:

    print("Round-"+str(round_counter))
    print(change_turn[0].name,"(money :",change_turn[0].money,")" ,"cards : ",change_turn[0])
    try:
        change_turn[0].put_card(int(input(change_turn[0].name+" enter card id :")))
    except ValueError :
        print(" Use only numbers ! Restarting round...")
        time.sleep(1.5)
        continue
    print(change_turn[1].name,"(money :",change_turn[1].money,")" ,"cards : ",change_turn[1])
    try:
        change_turn[1].put_card(int(input(change_turn[1].name+" enter card id :")))
    except ValueError:
        print(" Use only numbers ! Restarting round...")
        time.sleep(1.5)
        continue

    print(table)

    change_turn[0].use_ability(input(change_turn[0].name+"(money :"+str(change_turn[0].money)+")" +" Use character ability (cost:"+str(table.cards[change_turn[0].name].ability_cost)+")? Y/N"))
    change_turn[1].use_ability(input(change_turn[0].name+"(money :"+str(change_turn[1].money)+")" +" Use character ability (cost:"+str(table.cards[change_turn[1].name].ability_cost)+")? Y/N"))

    print(table)

    table.start_round()



    round_counter +=1
    change_turn.reverse()


#'''