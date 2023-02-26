# 🚨 Don't change the code below 👇
from msilib import PID_TITLE


row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map_ = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

vertical = int(position[0])-1
horizaontal = int(position[1])-1

map_[vertical][horizaontal] = 'a'

print(f'{map_[0]}\n{map_[1]}\n{map_[2]}')

