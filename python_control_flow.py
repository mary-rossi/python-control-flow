# exercise-01 Vowel or Consonant
# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z):
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

letter = input("Please enter a letter from the alphabet (a-z) or (A-Z): ").lower()

if letter in ["a", "e", "i", "o", "u", "y"]:
    print(f"the character {letter} is a vowel.")
else:
    print(f"the character {letter} is a constonant.")

# exercise-02 Length of Phrase
# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

phrase = ""

while phrase != "quit":
    phrase = input("Please enter a word or phrase: ")
    print(f"What you entered is {len(phrase)} characters long.")
else:
    print("Bye!")

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

human_years = int(input("Input a dog's age in human years: "))
dog_years = 0

if human_years < 3:
    dog_years = human_years * 10
    print(f"The dog's age in dog years is {dog_years}")
elif human_years > 2:
    dog_years = (human_years - 2) * 7 + 20
    print(f"The dog's age in dog years is {dog_years}")

# exercise-04 What kind of Triangle?
# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

print("Enter the three lengths of a triangle (one at a time): ")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a == b == c:
    print(f"A triangle with sides of {a}, {b}, & {c} is a equalateral triangle.")
elif a != b != c:
    print(f"A triangle with sides of {a}, {b}, & {c} is a scalene triangle.")
else:
    print(f"A triangle with sides of {a}, {b}, & {c} is a isosceles triangle.")

# exercise-05 Fibonacci sequence for first 50 terms
# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

term = 0
num_1 = 0
num_2 = 1

while term < 50:
    if term < 2:
        print(f"term: {term} / number: {term}")
    else:
        num_3 = num_1 + num_2 
        print(f"term: {term} / number: {num_3}")
        num_1 = num_2
        num_2 = num_3
    term += 1

# exercise-06 What's the  Season?
# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the season (Jan - Dec):
# 2. Then propts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

month = input("Enter the month of the season (January - Decemeber): ")
day = int(input("Enter the day of the month: "))

if month in ("January", "February", "March"):
    season = "Winter"
elif month in ("April", "May", "June"):
    season = "Spring"
elif month in ("July", "August", "September"):
    season = "Summer"
elif month in ("October", "November", "December"):
    season = "Fall"

if month == "March" and day > 20:
    season = "Spring"
elif month == "June" and day > 21:
    season = "Summer"
elif month == "September" and day > 22:
    season = "Fall"
elif month == "December" and day > 21:
    season = "Winter"

print(f"{month} {day} is in {season}")
