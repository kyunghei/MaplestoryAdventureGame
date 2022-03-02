
print("""
          .
        ('
        '|
        |'
       [::]
       [::]   _......_
       [::].-'      _.-`.
       [:.'    .-. '-._.-`.
       [/ /\   |  \        `-..
       / / |   `-.'      .-.   `-.
      /  `-'            (   `.    `.
     |           /\      `-._/      
     '    .'\   /  `.           _.-'|
    /    /  /   \_.-'        _.':;:/
  .'     \_/             _.-':;_.-'
 /   .-.             _.-' \;.-'
/   (   \       _..-'     |
\    `._/  _..-'    .--.  |
 `-.....-'/  _ _  .'    '.|
          | |_|_| |      | \  (o)
     (o)  | |_|_| |      | | (\'/)
    (\'/)/  ''''' |     o|  \;:;
     :;  |        |      |  |/)
 LGB  ;: `-.._    /__..--'\.' ;:
          :;  `--' :;   :;  

""")

choose_class = (input("""Hello Maple Adventurer. Ever since you were a wee child, a giant Mushmom has been terrorizing 
your village. As you have come to age, it is your duty now to build your strength, defeat the giant Mushmom, and bring 
peace to your village. It is time to make the hardest decision of your life by choosing your class. Please type
 \"warrior\" to learn the art of the blade, \"mage\" to learn the art of magic, or \"archer\" to learn the art of the
 bow.\n""")).lower()

if choose_class == "warrior":
    print("""Good choice - you chose the warrior class. A surge of strength entered your body and you have learned the
skills of a master swordsman.""")

elif choose_class == "mage":
    print("""Good choice - you chose the magician class. A surge of deep wisdom entered your brain and you have learned 
to cast magic spells.""")
    ice_or_fire = input("""Would you like to learn the element of ice or fire? Type \"ice\" to freeze enemies or 
\"fire\" to burn your enemies.\n""")
    if ice_or_fire == "ice":
        print("Your body's temperature has lowered drastically *BRR*. You can now cast ice spells!")
    elif ice_or_fire == "fire":
        print("Your body's temperature has risen drastically *SCORCH*. You can now cast fire spells!")
    else:
        print("""You did not choose an available element. If you can't choose a proper element, you do not have what it
takes to defeat the Mushmom. Game over.""")
        exit()

elif choose_class == "archer":
    print("""Good choice - you chose the archer class. A surge of energy entered your body and you have learned the art
of archery.""")
    bow_or_cross = input("""Which weapon would you like to master - the bow or crossbow? Type \"bow\" to shoot faster
or type \"crossbow\" to deal more damage per hit.\n""")
    if bow_or_cross == "bow":
        print("You are given Athena Pierce's master bow. It looks ancient with a lot of history.")
    elif bow_or_cross == "crossbow":
        print("""You are given Athena Pierce's master crossbow. It feels heavy in your arms...heavy like the pressure to
defeated the Mushmom.""")
    else:
        print("""You did not choose an available weapon. If you can't choose a proper weapon, you are no match for the 
evil Mushmom. Just go home before you get hurt child. Game over.""")
        exit()

else:
    print("""You did not choose an available class. You do not have the strength to fight the Mushmom and save the 
village. Game over.""")
    exit()


snail_ignore_or_kill = input("""You have gained this new power and feel like you can rule the world! While admiring your
newfound abilities, you notice a teeny snail slinking away. Would you like to go kill or ignore this snail? Type
\"kill\" or \"ignore\".\n""")

if snail_ignore_or_kill == "ignore":
    print("""What is the point of wasting time with a snail? There are better things to do...like searching and 
killing the evil Mushmom.""")

    left_or_right = input("""In search for the evil Mushmom, you tread on for days and pass through many paths until you 
reach a fork in the road. The left path seems to lead into a dark cave with a sinister aura. The right path seems to 
lead into another forest. Which path would you like to take? Type \"left\" or \"right\".\n""")
    if left_or_right == "left":
        print("""You entered the dark cave and discovered a sleeping Balrog. Before you can escape, the giant Balrog 
        wakes up and overpowers you. There is no way you can defeat a Balrog on your own..Game over.""")
        exit()
    elif left_or_right == "right":
        enter_or_run = input("""You entered the forest and ... ! How convenient! You found the Mushmom's secret lair. 
    This seems too good to be true. Do you want to enter the lair or run the other way? Type \"enter\" or \"run\".\n""")
        if enter_or_run == "enter":
            print("""You slowly enter the Mushmom's lair ready to fight. Lo and behold there sits the infamous Mushmom
    looking at you with a sinister grin. Rage builds and you start to fight the Mushmom with all your power. However, it
     is not enough. The Mushmom dodges all your attacks and ends up taking your life. Maybe you need more experience.
    Game over. """)
            exit()
        elif enter_or_run == "run":
            print("""Is it possible to defeat the Mushmom right now? Let's run!
    While you are running, you accidentally trip on a stone and fall to the ground. Before you can get up, the Mushmom 
    body slams you flat like a pancake. Maybe you should have fought the Mushmom head on like a true adventurer.
    Game over.""")
        else:
            print("You did not choose an available option. Game over.")
            exit()

elif snail_ignore_or_kill == "kill":
    print("Skills are not learned overnight. It should be mastered through experience.")
    if choose_class == "warrior":
        print("""You swung your huge blade at the snail. It took a few tries before you were able to make contact and
kill the snail. Phew...that was harder than expected! Why is it so hard to aim?""")
    elif choose_class == "mage" and ice_or_fire == "ice":
        print("""You close your eyes and cast an icey spell at the snail. It took a few tries before your magic spell
froze the snail solid. Phew...that was harder than expected! Why is it so hard to aim?""")
    elif choose_class == "mage" and ice_or_fire == "fire":
        print("""You close your eyes and cast a blazin spell at the snail. It took a few tries before your fireball
hit the snail. Phew...that was harder than expected! A few trees were burned in the process...""")
    elif choose_class == "archer" and bow_or_cross == "bow":
        print("""Aha! It's time to finally use Athena's bow. SHLIING-SHLIING* You shot two arrows at once. The snail 
dodged the arrows. SHHLING-SHLIING* The snail has dodged the arrows. Maybe third time's the charm. SHLIING-SHLIING*
The snail was finally hit. Phew...that was harder than expected!""")
    elif choose_class == "archer" and bow_or_cross == "crossbow":
        print("""Aha! Its time to finally use Athena's crossbow. SHLOOOOONG* An arrow as heavy as a brick is shot
towards the helpless snail but missed. SHLOOOOOONG* The snail has dodged the arrow again. Maybe third time's the charm.
SHLOOOONG* The snail was finally hit. Phew...that was harder than expected!""")
else:
    print("""You did not make a proper decision. If you can't even decide to kill or to ignore a snail, how can you be
responsible for defeating the Mushmom and protecting the village? Game over.""")
    exit()

print("\n")
rest_or_continue = (input("""Whew! You used up more MP than necessary! Would you like to rest and restore your energy or
keep going? Type \"Rest\" or \"Continue\".\n""")).lower()

if rest_or_continue == "rest":
    print("Swarm of snail army takes revenge. You slash through and level up from the experience.")
    water_or_no = input("Get water or no water?")
    if water_or_no == "water":
        print("get water and feel replenished.")
    elif water_or_no == "no water":
        print("do not get water and keep going.")
    else:
        print("If you can't even decide this, how are you supposed to save us from the Mushmom? Game over.")
        exit()
elif rest_or_continue == "continue":
    print("""REST? There is no time for REST!! The whole village is relying on YOU to save them.
    While you continue to tread on, your body is getting heavier and heavier from fatigue. At the worst time possible
    an army of snails come and ambush you in revenge of the snail you killed mercilessly. With little to no energy,
    you die from the snail attack. What a sad way to go..Game over.""")
    exit()
else:
    print("Pick rest or continue. It is not rocket science. Game over.")

enter_or_no = input("After many days of adventure, you find the secret lair of the Mushmom. Enter or run away?")

if enter_or_no == "enter":
    print("FIGHT. You beat the Mushmom. You beat the game.")
elif enter_or_no == "run":
    print("While you are running away, you get slammed by the Mushmom. Game over.")