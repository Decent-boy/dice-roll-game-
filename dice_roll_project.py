# pig game
import time
from sty import RgbFg,fg,Style,rs
import random
fg.orange_red=Style(RgbFg(255,69,0))
fg.dark_green=Style(RgbFg(0,100,0))
fg.deep_sky_blue=Style(RgbFg(0,191,255))
try:
    name=input(f"{fg.black}Insert Your Name: {fg.rs}")
    age=int(input(f"{fg.black}Enter Your Age: {fg.rs}"))
    while True:
        
        if age>=12 and age<=70:
            print(f"{fg.dark_green}Loding...{fg.rs}")
            time.sleep(2)
            print(f"{fg.yellow}____WellCome {name} to pig game____{fg.rs}")
        else:
            print(f"{fg.dark_green}Loding...{fg.rs}")
            time.sleep(2)
            print(f"{fg.deep_sky_blue}Age should be between 12 and 70{fg.rs}")
            quit()
except ValueError:
    print(f"{fg.orange_red}Invalid Input{fg.rs}")
def roll():
    roll=random.randint(1,6)
    return roll
# roll()
while True:
    players=input(f"{fg.black}Enter number of players into (2-4): {fg.rs}")
    if players.isdigit():
        players=int(players)
        if 2<=players<=4:
            print(f"{fg.dark_green}Loding...{fg.rs}")
            time.sleep(2)
            print(f"{fg.deep_sky_blue}Let's play a game{fg.rs}")
            break
        else:
            print(f"{fg.dark_green}Loding...{fg.rs}")
            time.sleep(2)
            print(f"{fg.deep_sky_blue}players must be under (2 to 4){fg.rs}")
    else:
        print(f"{fg.dark_green}Loding...{fg.rs}")
        time.sleep(2)
        print(f"{fg.orange_red}Invalid Input{fg.rs}")
max_score=50
player_score=[0 for _ in range(players)]
# print(player_score)

while max(player_score)<max_score:
    for j in range(players):
        print(f"{fg.deep_sky_blue}player number {j+1} has turned\njust started{fg.rs}")
        current_score=0
        while True:
            should_roll=input(f"{fg.black}Would you like to roll type(y) for yes\ntype (Q) for quit\nType here: {fg.rs}")
            if should_roll.lower().strip()=="q":
                print(f"{fg.dark_green}Loding...{fg.rs}")
                time.sleep(2)
                print(f"{fg.da_cyan}Done!{fg.rs}")
                quit()
            elif should_roll.lower().strip()=="y":
                print(f"{fg.dark_green}Loding...{fg.rs}")
                time.sleep(2)
                value=roll()
                # print(roll)
                if value==1:
                    print(f"{fg.dark_green}Loding...{fg.rs}")
                    time.sleep(2)
                    print(F"{fg.da_cyan}You have rolled\nDone{fg.rs}")
                    break
                else:
                    current_score+=value
                    print(f"{fg.dark_green}Loding...{fg.rs}")
                    time.sleep(2)
                    
                    print(f"{fg.deep_sky_blue}you rolled a {value}{fg.rs}")
                print(f"{fg.deep_sky_blue}you got a score {current_score}")
            else:
                print(f"{fg.orange_red}please type valid statement like as y and q {fg.rs}")
        player_score[j] += current_score  # Update player's total score  
        print(f"{fg.da_magenta}Player {j + 1}'s total score is now {player_score[j]}{fg.rs}")
#detrmine score and wining point
# winner = player_score.index(max(player_score)) + 1  
# print(f"{fg.deep_sky_blue}Player {winner} wins with a score of {player_score[winner - 1]}!{fg.rs}")

