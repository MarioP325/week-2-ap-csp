

# ----------------------------------------
# Print Practice Exercises
# ----------------------------------------

# Print Practice #1
# Write Python code that prints the sentence: I love learning Python
print("I love learning Python")


# Print Practice #2
# Write Python code that prints the sentence: Learning with 'TOTAL Python' is super fun!
print("Learning with 'TOTAL Python' is super fun!")


# Print Practice #3
# Write Python code that prints the number 555 to the screen as a result of a mathematical expression
print(500 + 55)

##############################################################################################################
# Find 3 objects around the room and create variables from it,
# Insert those variables into an f-string sentence(look at slide 22)in repl.it
bag="red"
window = 4
computer_mouse = "clicking"
# Nice! yeah
print(f"The bag is the color {bag}, there are {window} windows, and we're currently {computer_mouse} with our mouse!")
# Familiarize yourself with the syntax of the print() function.
# Print your name.
print("Mario")
# Print today's date.
print("October 10, 2025")
# Print the name of your favorite movie.
# Let's print both of our favorite movies. Hey, I know that one! its so peak
print("The Spongebob Squarepants Movie is Antonio's favorite movie.")
print("The project sekai colorful stage is Mario's favorite movie")
# Print your name and age on separate lines using a single print() function.
name_a = "Antonio"
name_m = "Mario"
a_age = 16
m_age = 16
print(f"This is {name_m} and {name_a}'s document. {name_m} is {m_age} years old and {name_a} is {a_age} years old.")
# Use f-strings to print a message like: "In 10 years, [Your Name] will be [Your Age + 10] years old."
print(f"In 15 years, {name_a} will be {a_age + 15} years old.")
print(f"In 10 years, {name_m} will be {m_age + 10} years old")
##############################################################################################################

########################## String Practice #################################
#syntax is the way we write code
# print("Hello World")
# name = "John"
#in other languages, this is different
# in javascript for example, you define
#variables with let or const or var
#in python, you just give your variables a
#name and then define it with a value


#challenge
# find a summary of the movie blue beetle online and create a 
# variable called blue_beetle_summary and print it it out to the screen
blue_beetle_summary = "In Antarctica, members of Kord Industries, led by its co-founder and CEO Victoria Kord, locate an ancient alien artifact known as the Scarab. Meanwhile, Jaime Reyes returns to his hometown of Palmera City after graduating from Gotham Law University, only to learn that his family is facing eviction from their home due to financial difficulties. Jaime's sister Milagro manages to get him a job at Victoria's mansion. However, both are fired after Jaime stops a confrontation between Victoria and her niece Jenny. Jenny later tells Jaime to meet her at Kord Tower the next day to discuss a 'job opportunity'. The next day, Jenny finds that Victoria is using the Scarab for her One Man Army Corps (OMAC) projects. She steals the Scarab and avoids security by giving it to Jaime, hidden inside a Big Belly Burger to-go box. At home, Jaime's family convinces him to open the box, and when Jaime ends up holding the Scarab, it activates and fuses with him, encasing him in an exoskeleton. Jaime then gets launched from the stratosphere to all over the city. Jaime tracks down Jenny for answers, rescuing her from Victoria's armed forces. She tells Jaime the Scarab is a sentient weapon and it has chosen Jaime to be its host. With the help of Jaime's uncle Rudy, Jaime and Jenny break into Kord Tower to retrieve a smartwatch that once belonged to Jenny's father Ted, but are attacked by Victoria's bodyguard Ignacio Carapax, who has an OMAC prototype infused in his body. The Scarab, revealed to be named Khaji-Da, temporarily takes over Jaime's body and battles Carapax, but Jaime refuses to let it kill Carapax. Rudy and Jenny help incapacitate Carapax, then escape with Jaime to Jenny's childhood home. Jenny uses Ted's watch to activate his secret laboratory and reveals that Ted was originally a vigilante named Blue Beetle who spent his life studying Khaji-Da before mysteriously disappearing, leaving his company in Victoria's hands. When they notice Victoria's helicopter flying toward Jaime's home, Jaime summons Khaji-Da and returns to protect his family, but Jaime's father Alberto collapses and dies from a heart attack, distracting Jaime and allowing Carapax to capture him. Jaime is taken to an island fortress near Cuba, where he is strapped to a machine that downloads information from Khaji-Da into the OMACs. While unconscious, Jaime experiences a vision from Alberto in the afterlife, who encourages him to embrace his destiny as the new Blue Beetle. While Jenny and the Reyes family use Ted's Bugship and its weapons arsenal to storm the island, Jaime awakens and escapes as Carapax's OMAC suit evolves into a more powerful form. Jaime reunites with his family, then encounters Carapax and battles him. Jaime nearly kills Carapax but is stopped by Khaji-Da, who shows him Carapax's memories it obtained through the information download, from which Jaime learns of Carapax's tragic past, including his enslavement by Victoria for the OMAC experiments and the death of his mother at her hands. Moved by this revelation, Jaime spares Carapax, who is prompted to turn on Victoria and sets his OMAC suit to explode and destroy the island, himself, and Victoria, as vengeance for his mother. As the Reyes family escapes the island, they take time to mourn Alberto. In the aftermath, Jenny becomes the new CEO of Kord Industries and promises to repair the damage caused to the Reyes family by helping them rebuild their home. As the neighbors gather around the remains of the Reyes family's home and provide support, Jaime kisses Jenny and then offers to fly her to the Kord Estate. In a mid-credits scene, a distorted recording is broadcast in Ted's laboratory, attempting to inform Jenny he is alive."
# The summary above is courtesy of en.wikipedia.org.

# print the length of the summary
print(len(blue_beetle_summary))
# upper case the entire summary
print(blue_beetle_summary.upper())
# print the summary
print(blue_beetle_summary)
# print the summary in lowercase
print(blue_beetle_summary.lower())
# replace the word blue with red
red_beetle_summary = blue_beetle_summary.replace("Blue", "Red")
# print the summary
print(red_beetle_summary)
# string index the word beetle and print it out
# print the last word of the summary
print(blue_beetle_summary[3705:3710])
# print the summary in reverse
print(blue_beetle_summary[::-1]) #works
# Not sure if this works but maybe try it anyway.

########################## Input Practice #############################################
#input is when we ask the user for input/data
# Ask the user to enter their name.

# Input Practice #1
# Write Python code that allows the user to enter their answer, by making them the following question:
# What are you learning today?
# Your code must be able to print to the screen whatever is entered by the user (use the print function).

# Input Practice #2
# Write Python code that allows the user to enter their answer, by making them the following question:
# Where are you from?
# Your code must be able to print to the screen whatever is entered by the user (use the print function).

# Input Practice #3
# Write Python code that displays the user's full name on the screen, by allowing them to enter their first and last name with the following instructions:
# What is your name?
# What is your surname?
# The code must be able to print the user's first and last name on the screen, separated by a space.

# Exercise:
# Write a program that asks the user for their name and favorite color, then prints a message using both pieces of information.









