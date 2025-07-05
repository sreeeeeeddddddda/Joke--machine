#greet the user
print("welcome to the joke machine, enter an answer and get a joke!")
print()

#Animal joke
animal = input("Name an animal:")
print(f"you chose {animal}! That's a great choice, but let's hear a cat joke instead!")
joke_1_q = input("What do you call a pile of kittens? ")
print(f"Good guess, but the answer is: A MEOW-NTAIN!")
print()

#Food joke
food = input("Name your favourite food: ")
print(f"Ah, {food}! sounds delicious have you ever tried fries let make a joke about that insted!")
joke_2_q=input("what do you call a fries that plays piano?")
print(f"You're close! ,The answer is: BEETHOVEN FRIES!")
print()

# Game joke
game = input("Name your favorite game: ")
print(f"oh, {game}! Fun! but how about making a joke about minecraft hope you find it funny")
joke_3_q = input("why don't minecraft player ever get lost? ")
print(f"Nice try! It's because they always follow their compass-ion ")
print()

# Entertainment joke
entertainment= input("Name your favourite entertainment joke: ")
print(f"You picked{entertainment}! Interesting. Let's try an entertainment joke hope you like it .")
joke_4_q = input ("Why did the TV go to school? ")
print(f"Not quite! The right answer is because it wnted to become a smart TV bet u didn't expect that 🤣😂!")
print()

#school joke
school_joke_q = input("Tell me your favourite subject: ")
print(f" '{school_joke_q}' is a cool subject! Here's a jokefor you let see how smart you are cause this is a very popular joke let see!")
joke_5_q= input("why did the student eat his homework? ")
print(f"Haha, the answer is: Because the teacher said it was as easy as a piece of cake!")
print()

# New category: Weather jike
weather_input = ("What's your favorite type of weather")
print(f"'{weather_input}'is lovely! Here's a quick weather joke.")
joke_6_q = input("what do you call a snowman wit six-pack? ")
print(f"You're thinking hard! sorry to say but the answer is : An abdominal snowman! ")
print()

#main.py2
print("Mini-introduction to section 2")
print("/NAlrigth, you've mastered the first round of jokes! ready to dive into **section 2**")
print("we're crancking up the fun with even more laughs in brand-new category")
print("get ready to strentch those funnt bones./N")

#---New jokes section 2---

#Technology joke
print("---Let's try a technology joke now--")
tech_input =input("Name a piece of technology you can't live with?")
print(f"Ah, {tech_input}! Essential! But here's a joke about computers.")
joke_7_q= input ("why was the computer cold?")
print(f"Not exactly! but actually it  left its window open 😜🪟!")
print()

tech_input=input("what has a thousand eyes, but cannot see ? this is quite easy though")
print(f"Intersting thought, '{tech_input}', nut the answer is:A SIEVE!🗑️")
print("don't be shocked but still stay with us the COOL JOKES 😎 ")
print()

#sport jokes
sport_input = input("I'm present in every sport, but i'm never on the field or court. what am i ?")
print(f"Interesting guess, '{sport_input}'. The answe is : THE LETTER 'T' !")
print()

#Movie jokes
print("---one last mind bending joke about movies!---")
movie_input=("what has to be broken before you can use it?")
print(f"Your guess of '{movie_input}' is commendable, but the answeris: An egg!")
print()

#main.py3
print("welcome to section 3.py")
print("/nAlrigth ,you've made it to the third round of te Reedah joke machine! welcome welcome let dive into  the joke")
print("this round is going to be sligthly diffreent just hang  on there to see the surprise format of this round")
print("in this section you will be the one to pick a category, choose a concept, invent a pun,write a setup question, deler a punchline and there you go ") 

print("let's build a joke machine together, step by step./n")

#step1: chose a category
category= input(f"step : choose your joke category (e.g, science ,travel, fantasy): "). capitalize()
print(f"Great choice! {category} it is./n")

#step2: pick a concept
concept=input(f"step 2 Now, pick something form the world of{category}to joke about (e.g gravity, suitcase, wizard): ")
print (f"'{concept}' sounds promising/n")

#step3: wordplay or pun
pun= input(f"can you think of a pun or like a wordplay or double meaning for '{concept}'? or make something up! ")
print(f"nice that give us something to work with :{pun}/n")
if os.path.exists(sound_file_path):
    playsound(sound_file_path)

#step4: set up the question
setup= input ("step4 : Now write a funny or confusing question to tease your punchline? ")
print("/nHere we go !/n")

#step5: 
punchline =input("step 5: time to drop the mic-what's your punchline? ")
print("/nHere we go!/n")

print("🃏YOUR CUSTOM JOKE🃏")
print(f"Q: {setup}")
print(f"A:  {punchline}")
print("/nHilarious! save one for the open mic night.🎤🌃 ")
print (" I would lyk to comend you on the complementation of theis round you've achieve this easier than i predict")