import sys
import random
from os import system
from time import sleep
from colorama import Fore, Style, init
init(autoreset=True)

# this code will hurt your eyes. made in computer programming 1 for second-to-last project. not the best format
# or implementation of the idea because I tried to put it together in two weeks without considering other methods.

class Character:
    def __init__(self, hearts=10, items=None, attack=2):
        self.hearts = hearts
        self.items = [] if items is None else items
        self.attack = attack
        self.room = "start"

    def eat(self):
        # for saving the man's daughter in the slums
        self.hearts = 13

    def bathe(self):
        # for bath in king's quarters
        self.hearts += 2

    def dead_check(self):
        if self.hearts <= 0:
            return True
        return False

    def damage_check(self):
        # check for different items and change player's damage accordingly
        base = 2
        if "sword" in self.items:
            base += 2
        if any(w in self.items for w in ["longsword", "dagger", "rapier"]):
            base += 3
        self.attack = base

    def start(self):
        # beginning of game.
        print("You are in a dungeon. You remember you are a ruler of your people raising an uprising against the malevolent king. "
              "However, seeing as where you are now, you assume you have been captured. You hope your people are okay. "
              "There is an inmate across from you. He appears to be dead, but is an elf. You yourself are unshackled and can move freely. "
              "Your inmate's hand is on the floor, free for the taking. He seems to have died of blood loss after torture, a gruesome death. "
              "There is one door leading out of the dungeon.\n")
        # stats
        print(f"{Fore.GREEN}{Style.BRIGHT}Current stats: {self.hearts} hearts, {self.attack} attack damage. You have no items.\n")
        while True:
            do = input(f"{Fore.BLUE}{Style.BRIGHT}What would you like to do? (leave) (take ____) {Style.RESET_ALL}").strip().lower()
            if "take" in do and "hand" in do and "hand" not in self.items:
                print(f"{Fore.YELLOW}{Style.BRIGHT}Bloody hand added to inventory.\n")
                self.items.append("hand")
            elif do == "leave":
                print("\nYou head towards the dungeon entrance. A guard is standing with his back to you. You twist his neck, killing him. He has a sword.\n")
                while True:
                    do = input(f"{Fore.BLUE}{Style.BRIGHT}What would you like to do? {Style.RESET_ALL}").strip().lower()
                    if "take" in do and "sword" in do and "sword" not in self.items:
                        self.items.append("sword")
                        self.damage_check()
                        print(f"{Fore.YELLOW}{Style.BRIGHT}Sword added to inventory. You can deal {self.attack} attack damage. \n")
                    elif do == "leave":
                        print("\nYou head out of the dungeon into a colosseum. \n")
                        return "colosseum"
                    else:
                        print("Nothing happens.")
            else:
                print("Nothing happens.")

    def colosseum(self):
        print("\nYou are in the colosseum. A guard notices you. \n")
        while True:
            do = input(f"{Fore.BLUE}{Style.BRIGHT}Do you fight or run? {Style.RESET_ALL}").strip().lower()
            if do == "fight":
                if "sword" in self.items:
                    d = random.randint(1, 3)
                    print(f"\nYou deal {self.attack} damage to the guard. He deals {d} damage to you. The guard passes out.\n")
                    self.hearts -= d
                    if self.dead_check():
                        return "dead"
                    print(f"{Fore.GREEN}{Style.BRIGHT}You have {self.hearts} hearts left. \n")
                    break
                else:
                    print("\nThere is no weapon to fight the guard with. You pitifully attempt to fistfight the armored guard, but he stabs you through the stomach. \n")
                    return "dead"
            elif do == "run":
                print("\nYou try to run away. The guard follows, and your weakened state makes him catch up. You "
                "feel a sudden pressure in your stomach, then a burning pain as your body realizes it has been stabbed.\n")
                return "dead"
            else:
                print("Nothing happens.")
        if "key" not in self.items:
            print("\nYou notice something shiny in the guard's pocket. As you bend down to examine it, you notice it is a key.")
        print("\nAs you examine your surroundings, you see five different paths. "
              "One leads back to the dungeon you came from. Another has a rancid stench emanating from it, like one of beasts. "
              "You don't want to enter it to find out, but it seems to be a beast room. Next to the beast room is an identical pathway as your dungeon. "
              "You assume it's the other dungeon you heard about from guard gossip. Turning more, there is the sound of people from the next pathway. "
              "You assume that is the spectator entrance to the colosseum. Yet another path is adorned luxuriously with decor and has a sign on it: \"King's Entrance\". \n")
        print("Places you can go: the Dungeon, the other dungeon, the beast room, the spectator entrance, and the King's entrance.")
        while True:
            go = input(f"\n{Fore.BLUE}{Style.BRIGHT}What would you like to do? {Style.RESET_ALL}").strip().lower()
            if "take" in go and "key" in go and "key" not in self.items:
                print(f"{Fore.YELLOW}{Style.BRIGHT}Key added to inventory.\n")
                self.items.append("key")
            elif "dungeon" in go and "other" not in go:
                print("You head back to your dungeon. \n")
                return "dungeon"
            elif "other dungeon" in go:
                print("You go to the pathway you assume leads to the other dungeon.\n")
                return "other_dungeon"
            elif "beast" in go and "room" in go:
                print("As you head towards the beast room, your mind becomes fuzzy."
                      " The rancid stench becomes heavier in your nostrils, and you start losing your senses. You pass out.\n")
                return "dead"
            elif "spectator" in go and "entrance" in go:
                print("You head towards the sound of people in the spectator entrance.\n")
                return "spectator_entrance"
            elif "king" in go and "entrance" in go:
                print("You head towards the beautifully adorned King's entrance.\n")
                return "kings_entrance"
            else:
                print("Nothing happens.")

    def dungeon(self):
        print("\nYou return to the dungeon you were imprisoned in. The place gives you shivers.")
        if "hand" not in self.items:
            print("Your inmate's bloody hand lies on the ground. You grimace at their lifeless body.")
        while True:
            do = input(f"{Fore.BLUE}{Style.BRIGHT}What would you like to do? {Style.RESET_ALL}").strip().lower()
            if "take" in do and "hand" in do and "hand" not in self.items:
                print(f"{Fore.YELLOW}{Style.BRIGHT}Bloody hand added to inventory.")
                self.items.append("hand")
            elif do == "leave":
                print("You head out of the dungeon into the colosseum.")
                return "colosseum"
            else:
                print("Nothing happens. ")

    def other_dungeon(self):
        print("When you enter the other dungeon, you notice a door with a lock on it. Although the paths are identical, this dungeon has a closed door. ")
        if "key" in self.items:
            print("The door seems like it can be unlocked by the guard's key you took earlier. ")
        while True:
            do = input(f"{Fore.BLUE}{Style.BRIGHT}What would you like to do? {Style.RESET_ALL}").strip().lower()
            # this is where the player w/o a key will leave
            if do == "leave":
                print("You head out of the other dungeon into the colosseum. ")
                return "colosseum"
            # if they have key
            elif ("door" in do or "open" in do or "unlock" in do) and "key" in self.items:
                break
            # invalid inputs obvi
            else:
                print("Nothing happens. ")
        # this only runs if the player has the guard's key and no staff
        if "staff" not in self.items:
            print("\nThere are two prisoners, an elf and an old man. The old man opens his eyes at your"
                 " approach and eyes you up and down. The elf is unshackled, except for a chain binding "
                 "him to the wall. The man has all his limbs chained. When the elf notices you, he smiles"
                 " radiantly even under the grime all over him. \"Hello,\" he says. \"What is your business"
                 " with us?\" he asks. \n")
            print("You tell him you were another prisoner, but escaped and came here to see what was here. "
                 "You ask him if you can free him, and his eyes become melancholy. \"I could free myself "
                 "if I desired, but I remain here to keep this man company. The king... the cruel king, "
                 "he lost the key to this man's bindings, else he could have been released. This man has "
                 "been here for longer than the king himself, serving his sentence when the king rose to "
                 "power. It was initially only a year, for petty theft, and now he has been here for "
                 "as long as anybody can remember. It is unfair to let the actions of one man dictate"
                 " the fate of others.\" The elf rises and produces something from somewhere in the shadows."
                 " \"I refuse to leave, but my spirit is with you. Take my staff. It may help you so.\"\n")
            self.items.append("staff")
            print(f"{Fore.YELLOW}{Style.BRIGHT}Elf's staff added to inventory. \n")
            print("As you thank him and turn to leave back to the colosseum, the old man speaks for the"
                 " first time. \"We will pray for you. Good luck.\" You thank them again and head back to "
                 "the colosseum. ")
            return "colosseum"
        else:
            print("\nThe elf and old man's eyes light up when you enter again. \"You're back,\" the elf"
                 " muses. Seeing him again, you really can't help but admire his looks. You become slightly"
                 " jealous but show nothing of it. ")
            print("\"You really should go. We will do fine here alone. You have your own path to take. Although,"
                  " it was nice seeing you again,\" the elf says. An ethereal smile spreads across his face, dazzling you,"
                 " then he shoos you out of the room, sending you walking back to the colosseum. ")

    def spectator_entrance(self):
        # AKA underground city
        print("You are in the spectator entrance to the colosseum. Across from you are the three main sections of the underground city: the "
             "slums, the market, and the exclusive networks for the rich (the rich neighborhood). Behind you is the colosseum. ")
        while True:
            go = input(f"{Fore.BLUE}{Style.BRIGHT}Where would you like to go? {Style.RESET_ALL}").lower().strip()
            if "colosseum" in go:
                return "colosseum"
            elif "slums" in go:
                return "slums"
            elif "market" in go:
                return "market"
            elif "rich" in go:
                return "rich"
            else:
                print("Nothing happens. ")
                continue

    def slums(self):
        self.hearts -= 1
        print("\nYou head to the filthy slums. A rock hits you, thrown by some child-beggar scorning you, and you lose a heart.")
        if self.dead_check():
            return "dead"
        print(f"{Fore.GREEN}{Style.BRIGHT}You have {self.hearts} hearts left. ")
        if "flyer" in self.items and "coins" not in self.items:
            print("\nYou see some suspicious-looking people a few walks away. They glare at you. You pull out the flyer, and"
                 " they advance upon you. \"Do you have any business with us?\" A burly man asks. You tell them you're searching"
                 " for the girl in the flyer. The men look down at you, scowling. \"And why are you looking for her?\""
                 " You tell them her father asked you to. Behind them, you see something you didn't notice earlier: a girl, "
                 "matching the description and photo on the flyer perfectly, looking up at you with wide, teary eyes. ")
            while True:
                do = input(f"{Fore.BLUE}{Style.BRIGHT}Do you fight or run? {Style.RESET_ALL}").strip().lower()
                if do == "run":
                    print("You head out of the slums back to the market, running from the burly men. ")
                    return "market"
                elif do == "fight":
                    print("\nYou beat up the men. For all their weight and bulk, their fighting skills are"
                         " inferior to yours. You take the girl, soothing her with words that she'll see her "
                         "father, and head back to the market. She clutches your hand on the way, eyeing "
                         "the people around you warily. ")
                    self.items.append("girl")
                    return "market"
                else:
                    print("Nothing happens. ")
        while True:
            go = input(f"{Fore.BLUE}{Style.BRIGHT}Where would you like to go? {Style.RESET_ALL}").strip().lower()
            if ("spectator" in go and "entrance" in go) or "colosseum" in go:
                return "spectator_entrance"
            elif "market" in go:
                return "market"
            elif "rich" in go:
                return "rich neighborhood"
            else:
                print("Nothing happens.")

    def market(self):
        # sluuuurp
        print("\nYou head to the bustling streets of the market. Various peddlers and stalls are around. Mouth-watering "
             "aromas hit you since you've had the same meal of stale bread and cheese, peas, and hard water for the whole"
             " time you were imprisoned. Around you, you see delectable street foods. One stall has hot, fresh xiao long bao."
             " Another has shish kebabs right off the grill. Across from where you're standing, pani puri is being handed out"
             " to patrons. You would love to buy something, but have no money. Numerous other goods are being sold as well, "
             "with a pretty lady modeling for an accessory booth and home goods being sold by a pudgy, friendly-looking fellow. "
              "A quick path through the alleys can lead you to the slums, or heading a little further up the market path can "
              "lead you to the rich neighborhood. Back where you came is the colosseum's spectator entrance. ")
        # if the man's daughter is still kidnapped
        if "coins" not in self.items:
            print("Off in the corner a dewy-eyed, middle-aged man with a dejected look on his face is handing out flyers. ")
        while True:
            go = input(f"{Fore.BLUE}{Style.BRIGHT}\nWhere would you like to go? {Style.RESET_ALL}").strip().lower()
            # we do not want the player walking around with the dad's girl. that is unsafe and concerning.
            if not any(word in go for word in ["man", "guy", "flyer"]) and "girl" in self.items:
                print("You might want to go to the girl's father...")
                continue
            else:
                # start daughter quest
                if any(word in go for word in ["man", "guy", "flyer"]) and "coins" not in self.items:
                    break
                # leave
                elif "slums" in go:
                    return "slums"
                elif "rich" in go:
                    return "rich"
                elif ("spectator" in go and "entrance" in go) or "colosseum" in go:
                    return "spectator_entrance"
                # data validation
                else:
                    print("Nothing happens.")
        # quest for daughter -- 1st encounter
        if "flyer" not in self.items:
            print("\nYou head over to the dejected, dewy-eyed, middle-aged man. You ask if he's okay. ")
            print("\"Am I okay! Of course not! I've been handing these flyers out all morning, and nobody's batted an eye. "
                "That's how all these people here are; nobody's willing to put themselves in harm's way for a little girl's sake. "
                "My daughter was kidnapped by some of those vulgar slum scoundrels! I don't suppose you'd be fine with helping"
                " a guy out, will you?\"")
            help = input().strip().lower()
            # invalid inputs
            while help not in ["n", "y", "no", "yes"]:
                help = input(f"{Fore.BLUE}{Style.BRIGHT}\"Hmm?\" {Style.RESET_ALL}").strip().lower()
            # not helping
            if help in ["n", "no"]:
                print("\nThe man sighs. \"Yeah. I thought so. I'm sorry, I've just been having a bad day. I'll see you around, I"
                    " s'pose.\" The man sighs and goes back to handing out fliers. ")
            # being a good person
            else:
                print("\nThe man's eyes light up. \"Oh, thank you, thank you, bless you. You are a savior. My daughter was"
                    " kidnapped earlier by some nasty slum scum. You could probably find her if you headed over there. "
                    "If you can bring her back, I'll give you a good sum of cash.\" He eyes your clothes. \"You could "
                    "probably get something to eat and maybe some new clothes, too. Thank you.\" Before you leave, "
                    "he hands you a flyer with a picture of his daughter. You tuck it away in your pocket.")
                self.items.append("flyer")
        # return daughter
        else:
            if "girl" in self.items:
                print("The man's eyes light up as you head over with his daughter. A smile lights up his face. "
                "He thanks you profusely while he and his daughter have a heartfelt reunion. He hands you a small bag of coins.")
                self.items.append("coins")
                self.items.remove("girl")
                self.eat()
                print(f"{Fore.GREEN}{Style.BRIGHT}You head over to a stall and buy some food. You ravenously dig in, and "
                      f"it's over before you know it. You have {self.hearts} hearts now.")
            else:
                print("\nThe man says, "
                      "\"You still haven't found her? Okay... Please do find her soon. I hope nothing too bad has happened to her. Please do find her. Please.\"")
        while True:
            go = input(f"{Fore.BLUE}{Style.BRIGHT}Where would you like to go? {Style.RESET_ALL}").strip().lower()
            # leave
            if "slums" in go:
                return "slums"
            elif "rich" in go:
                return "rich"
            elif ("spectator" in go and "entrance" in go) or "colosseum" in go:
                return "spectator_entrance"
            # data validation
            else:
                print("Nothing happens.")

    def rich(self):
        print("\nYou head over to the exclusive network of rich people in the underground city, the rich neighborhood. "
             "It smells like money here, and the streets are free of all dirt. Rich kids playing outside eye your soiled"
             " clothes with distaste. You hear one ask its mommy if you're a beggar.\n")
        print("A stall catches your eye. It is the only one there. A man with an interesting assortment of trinkets"
             " is selling them. You walk up to him. He eyes you warily, clearly distrustful of you. You ask him "
             "if he has anything you can buy. \n\"For you? Nothing. If you have something useful on you, I can give"
             " you some information, though.\" ")
        if "staff" in self.items:
            print("\nYou're suddenly reminded of the staff the elf gave you. You present it to the seller. He "
                 "nods with satisfaction. \"An elf's staff? I don't know where you got this, but it'll do, if"
                 " you're willing to give it up.\"")
            do = input(f"{Fore.BLUE}{Style.BRIGHT}\nWould you like to give him the staff in exchange for information? {Style.RESET_ALL}").strip().lower()
            while do not in ["y", "yes", "n", "no"]:
                do = input(f"{Fore.BLUE}{Style.BRIGHT}Would you like to give him the staff in exchange for information? {Style.RESET_ALL}").strip().lower()
            if do in ["y", "yes"]:
                print("\nYou hand the staff over to him. He grins. \"Great. Let me tell you about the King's castle.\" "
                     "He eyes around you warily, leaning in closer and talking quieter. \"They say the King has a lot"
                     " of secrets. I'd say this is just rumour if I hadn't heard more than a few people talking about"
                     " it. Apparently, on the highest floor, a witch's residency is located, and there's also a chained"
                     " dragon. I believe the king's tryna force them to do his bidding, but that's just speculation; "
                     "who knows? But back to the witch -- it's said that she's blind since the king managed to take out"
                     " her eyes. He's still scared as a dog with its tail between its legs when it comes to her, but "
                     "it's said that if somebody else can take an eye of hers, they get... inhuman powers.\" He looks"
                     " around you. \"You might even be able to get out of the castle. But don't tell anybody I told you"
                    " that. Now shoo.\"")
            else:
                print("The man sighs. \"If that's what you want. My offer still stands if you're ever interested.\"")
        # no elf staff
        else:
            print("You don't have anything useful the man might like. He clicks his tongue and shoos you away from the stall. ")
        print("\nYou head back to the street.")
        while True:
            go = input(f"{Fore.BLUE}{Style.BRIGHT}Where would you like to go? {Style.RESET_ALL}").strip().lower()
            if "market" in go:
                return "market"
            elif "slums" in go:
                return "slums"
            elif ("spectator" in go and "entrance" in go) or "colosseum" in go:
                return "spectator_entrance"
            else:
                print("Nothing happens.")

    def kings_entrance(self):
        # die if 4 or less hearts
        print("\nWalking up to the King's entrance, you see a few guards strolling about. One of them notices you"
             " and alerts the other two. They run towards you, and you're forced to fight. You lose 3 hearts in "
             "the process.\n")
        self.hearts -= 3
        if self.dead_check():
            return "dead"
        print(f"{Fore.GREEN}{Style.BRIGHT}You have {self.hearts} hearts left. ")
        print("\nNow that the guards have been eliminated, you notice a stairwell in the back of the room."
             " It doesn't look like it's supposed to stand out, but it does anyways, contrasting the "
             "colourful furniture with its drab surface. You assume that's the way to the upper floor "
             "and follow it. ")
        return "stairs"

    def stairs(self):
        print("\nYou are at the top of a stairwell. This area is much easier to navigate than the previous;"
             " signs mark where different places are. In one direction, a path leads to the King's hall, "
             "guard quarters, and King's quarters. In the other direction, there is only one thing on the"
             " sign, but it has been scribbled out and replaced in a bright, unnatural purple: 'Room o' "
             "Doom'. For some reason it doesn't give off those kinds of vibes.\n")
        while True:
            go = input(f"{Fore.BLUE}{Style.BRIGHT}Where would you like to go? {Style.RESET_ALL}").strip().lower()
            if "doom" in go and "room" in go:
                return "room_o_doom"
            elif "king" in go and "quarter" in go:
                return "kings_quarters"
            elif "king" in go and "hall" in go:
                return "kings_hall"
            elif "guard" in go and "quarter" in go:
                return "guard_quarters"
            else:
                print("Nothing happens. ")

    def room_o_doom(self):
        print('''
There's a portal in this room. Made of a beautiful black marble, runic script carved into it spells out:

 )_)  _   _ _     ) o  _   _   _)_ ( _   _          o _)_ _ ( _  | _    _ ( _   _   _ ) _
( (  )_) ) )_)   (  ( )_) (    (_   ) ) )_)   )_)_) ( (_ (_  ) )  (    (_( )_) (_) (_( )_) o
    (_    (_         (_   _)           (_                         _)                  (_

You feel like you should go through. Back in one direction are the stairs, and in the other is a hallway.
              ''')
        while True:
            go = input(f"{Fore.BLUE}{Style.BRIGHT}Where would you like to go? {Style.RESET_ALL}").strip().lower()
            if "portal" in go or "through" in go or "witch" in go:
                return "witch_tower"
            elif "hall" in go:
                return "hall"
            elif "stair" in go:
                return "stairs"
            else:
                print("Nothing happens. ")

    def kings_hall(self):
        print("A large set of ornate wooden doors lay before you.")
        # player hasn't killed king.
        if "crown" not in self.items:
            if "eye" not in self.items:
                print("You feel like you shouldn't go in.")
            while True:
                enter = input(f"{Fore.BLUE}{Style.BRIGHT}Do you enter? {Style.RESET_ALL}")
                while enter not in ["y", "yes", "n", "no"]:
                    enter = input(f"{Fore.BLUE}{Style.BRIGHT}Do you enter? {Style.RESET_ALL}")
                if enter in ["y", "yes"]:
                    break
                # leave king's hall for whatever reason
                elif enter in ["n", "no"]:
                    while True:
                        go = input(f"{Fore.BLUE}{Style.BRIGHT}The guard quarters, King's quarters, and stairs are "
                                  f"behind you. Where would you like to go? {Style.RESET_ALL}")
                        if "stair" in go:
                            return "stairs"
                        elif "guard" in go and "quarter" in go:
                            return "guard_quarters"
                        elif "king" in go and "quarter" in go:
                            return "kings_quarters"
                        else:
                            print("Nothing happens.")
            # enter king's hall
            print("You enter the hall. The King smirks at the sight of you, an"
                     " ugly smirk. He has no idea of the power you have possessed "
                     "from the witch. The King speaks, a honeyed voice unfit for his deeds. ")
            print("\"So you have escaped your cell, huh? No matter. This is "
                    "where you will meet your end, false leader. Guards!\"\n")
            # player has witch's eye, kills king
            if "eye" in self.items:
                print("The guards advance upon you, but you raise your hand and they all freeze "
                     "involuntarily. The King, to your satisfaction, looks shocked. He seems to"
                     " want to say something, but your magic shuts his mouth.\n ")
                if "staff" in self.items:
                    print("You speak. \"You may have control over an army. You may have a dragon"
                         " chained in your stronghold. You might believe you are unstoppable "
                         "and powerful for these reasons. However, what of the world outside"
                         " this stronghold, outside the underground city? There are still nobles,"
                         " and children, and magical creatures, and beings superior to us. Yet"
                         " you pay them no heed. All that matters to you is your castle and throne, "
                         "so you eradicate all outside of it. A wise elf, in your castle alone, once"
                         " told me it is unfair to let the actions of one man dictate the fate of "
                         "others. I believe it is even more unfair when this one man has not faced "
                         "anything. You have never led your army into battle. You make others do your"
                         " dirty work. Even all you have at your hands, all the wealth, riches, strength,"
                         " loyalty-- None of it was earned by you. We may have accepted you because of "
                         "your predecessor, but it will be no more. Meet the same fate as the ones "
                         "suffering under your hand.\"")
                else:
                    print("You speak. \"You may have control over an army. You may have wealth"
                         " and riches available at a moment's notice. You might believe you are unstoppable "
                         "and powerful for these reasons. However, what of the world outside"
                         " this stronghold, outside the underground city? There are still nobles,"
                         " and children, and magical creatures, and beings superior to us. Yet"
                         " you pay them no heed. All that matters to you is your castle and throne, "
                         "so you eradicate all outside of it. You are weak and a coward."
                         " You have never led your army into battle. You make others do your"
                         " dirty work. Even all you have at your hands, all the wealth, riches, strength,"
                         " loyalty-- None of it was earned by you. We may have accepted you because of "
                         "your predecessor, but it will be no more. Meet the same fate as the ones "
                         "suffering under your hand.\"")
                print("\nYou flick your hand. Nothing happens at first, but then the king starts"
                     "convulsing violently. You clench your fist, and he curls up into a ball. "
                     "His insides crush and he starts vomiting up blood. A last flick of your hand"
                     " makes the king shriek, and then he is moving no more. You take his crown and "
                     "leave the room with the guards still frozen.\n")
                print(f"{Fore.YELLOW}{Style.BRIGHT}\nKing's crown added to inventory.\n")
                self.items.append("crown")
                return "stairs"
            # player doesn't have witch's eye, dies
            else:
                print("The guards advance upon you. You try to fight back, but their sheer numbers"
                     " overwhelm you. There was nothing you could do to save yourself.")
                return "dead"
        # player killed king
        else:
            print("Your work here is done. You head back to the stairs. ")
            return "stairs"

    def guard_quarters(self):
        print("You walk in on chaos. One guard is slipping on his breeches, another is"
             " working out in the corner, and another seems to have just come from a shower. "
             "All of you freeze for a moment, then another unseen guard yells, \"It's an "
              "escaped prisoner! Kill the knave!\" Multiple arrows protrude from your body less"
             " than a moment later, and you feel tugs in your abdomen before your vision swims. ")
        return "dead"

    def witch_tower(self):
        print("\nYou step out into a circular tower room. The walls seem to shift and twist "
              "whenever you look at them for too long, making your head spin. In the center of the room "
              "stands a woman in tattered robes, her empty eye sockets covered with a strip of cloth.\n")
        if "eye" in self.items:
            # have eye already
            print("The witch tilts her head as if she can still see you. "
                  "\"You have what you came for,\" she murmurs. \"My bargain with fate is already sealed.\" "
                  "You feel an uncomfortable pressure in your skull and decide not to linger here.\n")
            while True:
                go = input(f"{Fore.BLUE}{Style.BRIGHT}The portal is behind you. Off to the side is the weapons chamber,"
                    f" and to the other side is the dragonhold. Where would you like to go? {Style.RESET_ALL}").strip().lower()
                if "portal" in go:
                    return "room_o_doom"
                elif "weapons" in go:
                    return "weapons_chamber"
                elif "dragon" in go:
                    return "dragonhold"
                else:
                    print("Nothing happens.")
        # no eye...yet
        print("The woman turns her head toward you, though her covered eyes could not possibly see. "
              "\"So, another plaything of the king slips through his fingers,\" she says, voice dry and amused. "
              "\"He keeps me here, chained by oaths and my own magic, but even blind I see more than he.\" "
             "She lets out a laugh, making you shiver. ")
        # if the player got the elf staff. :) just something for some ✨FLAIR✨
        if "staff" in self.items:
            print("Her head tilts slightly. \"An elf's touch lingers on you. Odd.\"")
        # Main choice loop
        while True:
            print("\nShe raises a hand toward you, fingers trembling with restrained power.\n"
                  "\"You want justice, don’t you? The king’s blood on the floor, his crown in the people's hands. "
                  "All he fears, I can give you, in one of my eyes. It will cost you… but less than it cost me.\"")
            choice = input(f"{Fore.BLUE}{Style.BRIGHT}\nDo you take one of the witch's eyes? {Style.RESET_ALL}").strip().lower()
            while choice not in ["y", "yes", "n", "no"]:
                choice = input(f"{Fore.BLUE}{Style.BRIGHT}Do you take one of the witch's eyes? {Style.RESET_ALL}").strip().lower()
            # haha player loses if they don't have it but they don't know that yet
            if choice in ["n", "no"]:
                print("\nYou step back. It feels like the witch is looking at you somewhat condescendingly. "
                      "\"Go,\" she says. \"Challenge him with your puny strength alone.\"\n")
                break
            # the player isn't a WEAK COWARD
            else:
                print("\nYou step closer. Her hand cups your face, cold and burning at the same time.\n"
                      "A scream rips through you; yours or hers, you cannot tell. You stagger but remain standing.\n")
                print("Your perception twists. You feel presences in the castle, threads of fear and obedience. You "
                      "feel, with a terrible certainty, the ease of ending a life with a flick of your hand.")
                self.items.append("eye")
                print(f"{Fore.YELLOW}{Style.BRIGHT}\nWitch's eye added to inventory.\n")
                print("The witch laughs sinisterly. \"Go, then. Show him what he has made of me.\"")
                break
        while True:
            go = input(f"{Fore.BLUE}{Style.BRIGHT}The portal is behind you. Off to the side is the weapons chamber,"
                f" and to the other side is the dragonhold. Where would you like to go? {Style.RESET_ALL}").strip().lower()
            if "portal" in go:
                return "room_o_doom"
            elif "weapons" in go:
                return "weapons_chamber"
            elif "dragon" in go:
                return "dragonhold"
            else:
                print("Nothing happens.")

    def kings_quarters(self):
        # Player has just chosen to go to the king's quarters from the middle floor
        print("\nYou step into the King's quarters. The room is lavish: a massive bed, "
              "heavy velvet curtains, golden trim, and a marble floor. In the corner is"
              " a door presumably leading to the bathing chamber. Yet the air feels cold and wrong.\n")

        while True:
            do = input(f"{Fore.BLUE}{Style.BRIGHT}Behind you is the hallway to the stairs. In front is the room and"
                       f" bathing chamber. Where would you like to go? {Style.RESET_ALL}").strip().lower()
            if "bath" in do or "chamber" in do:
                return "kings_bath"
            elif "hall" in do or "stairs" in do:
                print("You leave the King's quarters and return to the stairs.")
                return "stairs"
            else:
                print("Nothing happens.")

    def kings_bath(self):
        print("You enter the bath chamber. Steam clings to the air. A large stone tub dominates the room, "
              "and a cracked mirror hangs above a small basin. The room is quiet and oddly peaceful.\n")
        while True:
            do = input(f"{Fore.BLUE}{Style.BRIGHT}You can take a bath or leave. What would you like to do? {Style.RESET_ALL}").strip().lower()
            if "bath" in do:
                if "clothes" not in self.items:
                    print("You strip and sink into the warm water, heaving a sigh, and wash away the grime of the dungeon. "
                          "You feel a bit more energized.\n")
                    self.bathe()
                    self.items.append("clothes")
                    print(f"{Fore.GREEN}{Style.BRIGHT}You have {self.hearts} hearts now. As you put a set of clean tunic and pants stolen from the king's wardrobe on,"
                         " you notice a tile in the wall next to the mirror is loose. ")
                    break
                else:
                    print("You already took a bath! You shake your head at your forgetfulness. "
                         "You remember the loose tile in the wall next to the mirror. ")
                    break
            elif do == "leave":
                print("You leave the bath chamber and return to the main room of the king's quarters.")
                return "kings_quarters"
            else:
                print("Nothing happens.\n")
        print("You have a feeling you can pry off the tile. There may be something hidden behind it. ")
        pry = input(f"{Fore.BLUE}{Style.BRIGHT}Do you pry off the tile? {Style.RESET_ALL}").strip().lower()
        while pry not in ["y", "yes", "n", "no"]:
            pry = input(f"{Fore.BLUE}{Style.BRIGHT}Do you pry off the tile? {Style.RESET_ALL}").strip().lower()
        if pry in ["y", "yes"]:
            print("You pry up the loose tile, revealing a narrow, hidden passage leading down, and enter.")
            return "nymph_passage"
        print("Like the weak, unadventurous coward you are, you don't pry off the tile. Instead, you"
             " head back to the King's quarters. Little sissy.")
        return "kings_quarters"


    def nymph_passage(self):
        if "dragonhold key" not in self.items:
            print("\nYou squeeze into the hidden passage. The air grows cooler and damp as you descend. "
                  "The stone walls close in as you move toward a faint glow ahead.\n")
            print("Eventually, you emerge into a small cell. A beautiful shackled nymph hangs from glowing chains "
                  "bolted into the wall, her eyes full of ancient sorrow.")
            while True:
                do = input(f"{Fore.BLUE}{Style.BRIGHT}\nYou can talk to the nymph or attempt to free her. What would you like to do? {Style.RESET_ALL}").strip().lower()
                if "talk" in do:
                    print("\"I have been here for longer than I can remember,\" she whispers. "
                          "\"If you can break these chains, I will help you escape this place.\"")
                elif "free" in do:
                    if "hand" in self.items:
                        print("You press the bloody elf hand against the glowing chains. The runes flicker and die, "
                              "and the shackles snap open. The nymph steps free.")
                        print("\"Thank you,\" she says softly. \"I cannot stay, but I can open a way.\" "
                              "She places her hand on the far wall. A hidden doorway grinds open.")
                        print("\"Beyond this path lies a great danger, but also a key to your freedom. "
                              "May fortune favor you.\" With that, she vanishes in a swirl of light.")
                        return "troll_room"
                    else:
                        print("You tug at the chains, but they will not break. The nymph shakes her head.\n"
                              "\"These bindings were forged with blood. Only a piece of the dead can open them. "
                              "You do not have what you need.\"\n")
                        print("You nod sorrowfully, knowing you cannot free her. You head back through the hidden"
                             " passage into the bathing chambers, then back further into the King's quarters.")
                        return "kings_quarters"
                else:
                    print("Nothing happens.\n")
        else:
            print("Your work here is done. You head back to the bathing chamber, then the King's quarters.")
            return "kings_quarters"

    def troll_room(self):
        print("You follow the newly opened passage. The air grows thick with the smell of sweat and old blood. "
              "You step into a cavernous chamber where a hulking troll stands guard before a heavy stone door.\n")
        print("The troll turns toward you, baring jagged teeth, and hefts a massive club.\n")
        # player doesn't have enough hearts
        if self.hearts < 5:
            print("You feel a spike of terror as the troll charges. You are too weak to stand "
                  "a chance. The club crashes down, and everything goes dark.\n")
            return "dead"
        print("You ground yourself and charge. Steel clashes against flesh as you battle the troll.\n")
        # simple battle: trade a random amount of damage, but you always eventually win if you qualify
        for _ in range(2):
            dmg = random.randint(1, 2)
            self.hearts -= dmg
            print(f"The troll lands a crushing blow, dealing {dmg} damage. ")
            input(f"{Fore.BLUE}{Style.BRIGHT}Press something to attack. {Style.RESET_ALL}")
            dmg = random.randint(1, self.attack)
            print(f"You deal {dmg} damage. ")
        print("The troll is dead. ")
        print(f"{Fore.GREEN}{Style.BRIGHT}You stagger, breathing hard. You have {self.hearts} hearts left.")
        print("Behind you, the passage collapses with a deafening rumble. There is no way back, "
              "only the stone door ahead.\n")
        return "riddle_door"

    def riddle_door(self):
        print("You approach the stone door the troll was guarding. Runes glow faintly across its surface. ")
        print("The inscription asks, \"What is not alive but grows, does not breathe but needs air?\"\n")
        while True:
            answer = input(f"{Fore.BLUE}{Style.BRIGHT}What is your answer? {Style.RESET_ALL}").strip().lower()
            if answer == "fire":
                print("The runes flare brightly, then fade. The door grinds open, revealing a small chamber beyond. ")
                print("On a pedestal in the center of the room rests an ornate key shaped like a dragon.")
                if "dragonhold key" not in self.items:
                    self.items.append("dragonhold key")
                    print(f"{Fore.YELLOW}{Style.BRIGHT}\nMysterious key added to inventory.\n")
                print("With the key in hand, you leave the chamber and head back to the King's quarters.")
                return "kings_quarters"
            else:
                print("The runes glow a vicious red. Your chest tightens as heat blooms under your skin. "
                      "In an instant, your body is consumed by invisible flame.\n")
                return "dead"

    def dragonhold(self):
        print("\nYou step into a vast, dim chamber that smells of smoke and old stone, older than the new castle. "
             "Chains as thick as tree trunks stretch from the walls and ceiling to a huge shape curled in the dim light. "
             "You gasp as your eyes behold the majestic creature in the midst of them all. "
             "Its iridescent scales shift like living oil, rainbow hues of white, gold, maroon, and amethyst flashing with every angle. "
             "A single black eye cracks open, the depths of them unseen, but lighted by the white in the dragon's pupils. ")

        # player doesn't have the key to the locks
        if "dragonhold key" not in self.items:
            print("You notice an enormous lock built into the main set of shackles, its surface "
                 "covered in strange runes. Something in you whispers that you are missing the key"
                 " to this prison. The dragon watches you for a moment, then closes its eye again, indifferent.")
            print("There is nothing else you can do here. You return to the witch's tower. ")
            return "witch_tower"
        # player has key to the locks
        else:
            print("As you step closer, the dragon’s eye widens, focusing fully on you. You are reminded"
                  " of the dragonhold key you got in the King's secret chamber tunnel. There is an enormous"
                  " lock built into the main set of shackles, its surface covered in strange runes. In the "
                  "center is a disproportionately small keyhole, but it matches your key perfectly. ")
            print("Your attention goes back to the dragon. Seeing you take out the key, its eye shows"
                 " desperation and pleading. A powerful voice, not your own, whispers in the back of your "
                 "mind, \"Save me. Let the king die at our hands.\"")
            while True:
                free = input(f"{Fore.BLUE}{Style.BRIGHT}Do you free the dragon? {Style.RESET_ALL}").strip().lower()
                while free not in ["y", "yes", "n", "no"]:
                    free = input(f"{Fore.BLUE}{Style.BRIGHT}Do you free the dragon? {Style.RESET_ALL}").strip().lower()
                if free in ["y", "yes"]:
                    print("You walk closer, in front of the keyhole, and take a breath. Inserting the key, you free"
                     " the dragon. ")
                    return "win_dragon"
                else:
                    print("You put the key back in your pocket. A rumble starts in the floor, and you realize the"
                         " dragon is causing it. Fearful, you try to stumble back towards the witch tower, but a "
                         "blast of heat smothers you before you make it all the way there. You scream in agony as"
                         " you are burned alive. In your last moments, you remember what your mother told you about"
                         " dragons when you were a wee babe: \"Never anger a dragon, for their wrath burns hotter than"
                         " any forge and spares none who defy them.\"")
                    return "dead"

    def hall(self):
        print("You enter the hall. It is lit with torches, but shadows still creep in the corners. It is colder here.")
        print("After walking for a little bit, you encounter a griffin. Remembering that they are nonviolent creatures"
              " who survive to serve a purpose, you do not attack. ")
        # king not dead yet
        if "crown" not in self.items:
            print("The griffin speaks. \"I guard this passage beyond the Room o' Doom. Only those who prove worthy may pass.\"")
            # elf's blessing/touch/staff
            if "staff" in self.items:
                print("The griffin eyes you. \"An elf's touch and blessing... very well, prove your worth with a number.\"")
                print("The griffin is thinking of a number between 1 and 10. Guess correctly to pass.")
                secret_number = random.randint(1, 10)
                while True:
                    try:
                        guess = int(input(f"{Fore.BLUE}{Style.BRIGHT}What is your guess? {Style.RESET_ALL}").strip())
                        if guess < 1 or guess > 10:
                            raise ValueError
                        if guess == secret_number:
                            print("Correct! The griffin bows its head. \"You may pass to the Four Seasons Room.\"")
                            return "four_seasons_room"
                        else:
                            print("Wrong! The griffin shrieks.")
                    except ValueError:
                        print("Enter a valid number between 1 and 10.")
            # No staff
            else:
                print("The griffin blocks your path. \"You lack power and wisdom. You are unworthy. Turn back.\"")
            # player is a failure
            while True:
                go = input(f"{Fore.BLUE}{Style.BRIGHT}\nDo you turn back or try to pass anyway? {Style.RESET_ALL}").strip().lower()
                if "back" in go:
                    print("You wisely turn back toward the Room o' Doom.")
                    return "room_o_doom"
                elif "pass" in go:
                    print("The griffin deems you unworthy and strikes you down instantly.")
                    return "dead"
                else:
                    print("The griffin awaits your decision.")
        # king do be dead
        else:
            print("The griffin speaks. \"I guard this path to the outside, and you have proven worthy. Pass.\"")
            return "four_seasons_room"

    def weapons_chamber(self):
        if any(weapon in self.items for weapon in ["longsword", "dagger", "rapier"]):
            print("You already got a weapon, so you return to the witch's toewr. ")
            return "witch_tower"
        print("You enter an armory filled to the brim with weapons. Most are under lock and key, "
             "but a few aren't, including swords, bows, staffs, and subdivisions of them. You"
             " see a few weapons that suit your taste: a longsword, a dagger, and a rapier. ")
        take = input(f"{Fore.BLUE}{Style.BRIGHT}Which weapon would you like to take? {Style.RESET_ALL}").strip().lower()
        while take not in ["longsword", "dagger", "rapier"]:
            take = input(f"{Fore.BLUE}{Style.BRIGHT}Which weapon would you like to take? {Style.RESET_ALL}").strip().lower()
        self.damage_check()
        print(f"You took the {take}. You deal {self.attack} damage now. You return to the witch's tower.")
        return "witch_tower"


    def four_seasons_room(self):
        print("\nYou enter a large, dome shaped room. It is beautiful and chaotic all at once; "
             "each quarter of the room is taken up by a different representation of a season. "
             "Where you are, fresh new spring buds are rising through the dirt at your feet. "
             "A cherry blossom tree's flowers emanate a sweet scent. On the right of this quarter, "
             "snow is falling from god-knows-where onto a bluish-green-needled pine tree. The floor"
             " is blanketed with freshly fallen snow. On the left of this quarter, heat shimmers the"
             " air. Plants in full green lushly cover it, and a bird tweets on one of them. Finally, "
             "across from you, a maple tree drops its leaves in hues of red, orange, and gold onto the"
             "already-carpeted dirt. You now understand why the name is the Four Seasons Room. \n")
        print("\nYou see a pedestal in the center of the room, where the seasons meet."
              "There rests a crystal the size of your fist, slowly cycling through soft green,"
              " blazing gold, deep crimson, and cold blue light. As you draw closer, you recognize"
              " the stories from your homeland: this is the Heart of the Seasons, a stone formed by"
             " the gods placing together a tear of each season's essence, said to nurture the land"
             " and slowly aid the user.\n")
        reach = input(f"{Fore.BLUE}{Style.BRIGHT}The Heart is calling to you. Do you answer? {Style.RESET_ALL}").strip().lower()
        while reach not in ["y", "yes"]:
            reach = input(f"{Fore.BLUE}{Style.BRIGHT}The Heart wants an answer. \n{Style.RESET_ALL}").strip().lower()
        print("You reach out to cradle the Heart.\n")
        if "crown" not in self.items:
            print("\nThe Heart rejects you, unconvinced of your valor and dignity. A heavenly feeling"
                 " spreads through you, then consumes you.")
            return "dead"
        print("\nThe Heart accepts you, convinced of your valor and dignity. You smile looking down at it. ")
        print("You head out of the room into the next corridor. A triangular room opens up before you. ")
        return "exit"

    def exit(self):
        print("\nYou are on one side of the room. On the others, there is a door and a slate with some "
             "writing on it. You walk over to read it. \n")
        print("It says:\nthyseznuffinempyrtint. thadevwsborrd. \nYou wonder what it means and try to sound it out.\n")
        sleep(2)
        while True:
            go = input(f"{Fore.BLUE}{Style.BRIGHT}\nWould you like to head through the door now? {Style.RESET_ALL}").strip().lower()
            while go not in ["y", "yes", "n", "no"]:
                go = input(f"{Fore.BLUE}{Style.BRIGHT}Would you like to head through the door now? {Style.RESET_ALL}").strip().lower()
            if go in ["y", "yes"]:
                return "win_witch"
            print("\nYou stay in the room for a little while longer.\n")
            sleep(3)


    def dead(self):
        sleep(2)
        # ascii art :)
        print(f"""{Fore.RED}{Style.BRIGHT}
------------------------------------------------------------------------------------------------

oooooo   oooo   .oooooo.   ooooo     ooo    oooooooooo.   ooooo oooooooooooo oooooooooo.
 `888.   .8'   d8P'  `Y8b  `888'     `8'    `888'   `Y8b  `888' `888'     `8 `888'   `Y8b
  `888. .8'   888      888  888       8      888      888  888   888          888      888
   `888.8'    888      888  888       8      888      888  888   888oooo8     888      888
    `888'     888      888  888       8      888      888  888   888    "     888      888
     888      `88b    d88'  `88.    .8'      888     d88'  888   888       o  888     d88' .o.
    o888o      `Y8bood8P'     `YbodP'       o888bood8P'   o888o o888ooooood8 o888bood8P'   Y8P

------------------------------------------------------------------------------------------------

""")
        self.hearts = 0
        sleep(1)
        return "end"

    def win_dragon(self):
        # "hidden" ending
        print("\nFor a long moment, the dragon simply stares at you, one colossal eye unblinking. "
        "Then it stretches its wings, stones and dust raining from the ceiling as it rises to its full height. "
        "A voice echoes inside your skull, ancient and grateful, \"Thank you.\" "
        "The dragon lowers its head until you can feel the heat of its breath. "
        "\"Climb on, hatchling of the earth. Let us see this tyrant's beliefs burn.\" "
        "You scramble onto the dragon's back, fingers digging into warm scales. "
        "With a single colossal beat of its wings, the beast smashes through the tower wall. "
        "Night air rushes past as you burst out into the open sky. "
        "Below, the dragon's flames scour the new wings; the king-built wooden halls, gaudy towers, and fresh stonework all ignite. "
        "The original castle stands defiant, its ancient stone walls untouched by the fire. "
        "But the king's proud additions become a pyre, crumbling into glowing ruin. "
        "\n\nYou and the dragon wheel high above the selective inferno, the heat painting the clouds in shades of red and gold. "
        "Without a word, the dragon turns away from the burning additions and flies off into the night, "
        "carrying you toward a future the king will never see. "
        "You have escaped the castle and burned away the king's corrupt expansions. "
        "Somewhere far below, the old world endures in stone, and ahead, a new one waits.\n")
        print(rf"""{Fore.CYAN}{Style.BRIGHT}

                                                   ,.=,,==. ,,_
                                    _ ,====, _    |I|`` ||  `|I `|
                _|\_,              |`I|    || `==,|``   ^^   ``  |
        ,.--,   \_ `a\_            | ``    ^^    ||_,===TT`==,,_ |
   6^`--:_ ||  ,/  ,-,,\           |,==Y``Y==,,__| \L=_-`'   +J/`
  / \```\ \|\_/ /-/\\  `            \|=_  ' -=#J/..-|=_-     =|
 /  \.., | \/  /-/  `                |=_   -;-='`. .|=_-     =|----T--,
/   \..,'|    /-|                    |=/\  -|=_-. . |=_-/^\  =||-|-|::|____
    \__     \_L-==,                  |=||  -|=_-. . |=_-| |  =|-|-||::\____
    |  /   \_.-..= i                 |=LJ  -|=_-. . |=_-|_|  =||-|-|:::::::
    \ /    /--_/\                    |=_   -|=_-_.  |=_-     =|-|-||::::::
   _J`   .'-_,/\_``=                 |=_   -|=//^\. |=_-     =||-|-|:::::::
`X`    \/--_/    `-`i            ,   |/&_,_-|=||  | |=_-     =|-|-||:::::::
/   \   |_/                   ,--``8%,/    ',%||  | |=_-     =||-|-|%::::::
   _/  / /                ,---`_,888`  ,.'''''`-.,|,|/!,--,.&\|&\-,|&#:::::
./`; /`/`                |;:;K`__,...;=\_____,=``           %%%&     %#,---
    \\\\                 |;::::::::::::|       `'.________+-------\   ``
     w- w-         |    /8M%;:::;;:::::|                  |        `-------
    / \/ \         |   |`   88`V  /&8%\|_______,__,,      |
                   |   /,  %8,  ,/&888% &,       ,  `-----`,--..../|--,,,,_
                  / \/88%  88%  8888%88% &,       \,     `\      /     &,,
                  |,M8,  , `8%   ,,8% `8, `         , \,        &\     ,&##
                 /8888%  888`    ```    `            `  `               ```
------------------------------------------------


        """)
        return "end"

    def win_witch(self):
        # main ending
        print("Walking out of the castle, the sun is rising. You bask in the sunlight for a moment, a smile spreading"
             " across your face. At last, the lands are freed of the tyrant. At last, YOU are free again. You walk off"
             " into the forest, heading back towards your village to provide them the great news. ")
        print(rf'''{Fore.CYAN}{Style.BRIGHT}


          ........::::::::::::..           .......|...............::::::::........
     .:::::;;;;;;;;;;;:::::.... .     \   | ../....::::;;;;:::::.......
         .       ...........   / \\_   \  |  /     ......  .     ........./\
...:::../\\_  ......     ..._/'   \\\_  \###/   /\_    .../ \_.......   _//
.::::./   \\\ _   .../\    /'      \\\\#######//   \/\x  //   \_   ....////X
    _/      \\\\   _/ \\\ /  x       \\\\###////     xXXx//     \__  _////Xxx
  ./   x       \\\/     \/ x X           \//////    XxXX           \/////xxXxx
 /     XxX     \\/         XxX X                      Xx            ////  Xx
-----XxX-------------|-------XxX-----------*--------|-X-*-----|------------X--
       X        _X      *    X      **         **     X       x   **    *  X
      _X                    _X           x                *          x     X_


        ''')
        return "end"


def main():
    while True:
        system("clear")
        player = Character()
        while True:
            try:
                room_function = getattr(player, player.room)()
                player.room = room_function
                if room_function == "end":
                    break
            except (EOFError, KeyboardInterrupt):
                print()
                break
        again = input(f"{Fore.BLUE}{Style.BRIGHT}Would you like to play again? (y/n) {Style.RESET_ALL}").strip().lower()
        while again not in ["y", "n"]:
            again = input(f"{Fore.BLUE}{Style.BRIGHT}Would you like to play again? (y/n) {Style.RESET_ALL}").strip().lower()
        if again == "y":
            continue
        break
    print("Thanks for playing!")
    sys.exit(0)


if __name__ == "__main__":
    main()
