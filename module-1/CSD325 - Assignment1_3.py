# This is a input-driven countdown program in the style of the song "99 Bottles of Beer"

#Program Start / User Input 
print("The traditional folk song '99 Bottles of Beer on the Wall' is often used in programming to demonstrate loops.") 
BEER_BTLS = int(input('How many bottles of beer are on the wall? ')) 


#Algorithm
while BEER_BTLS > 0:
    print(f"{BEER_BTLS} bottles of beer on the wall, {BEER_BTLS} bottles of beer!") 
    print(f"Take one down, pass it around, {BEER_BTLS-1} bottles of beer on the wall!\n") 
    BEER_BTLS -= 1
print("Oh no! We are all out of bottles!") 

## When the countdown reaches zero, the script terminates and returns the user to the shell