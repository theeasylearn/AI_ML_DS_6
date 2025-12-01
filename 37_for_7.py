#for loop with dictionary
players = {"Rohit":78, "Gill":45, "Kohli":92, "Iyer":36, "Rahul":58, "Hardik":24, "Jadeja":41, "Ashwin":15, "Shami":10, "Bumrah":5, "Siraj":8}
#findout total team score
#task (findout average run made by player, findout minimum and maximum run made by player)
total = 0
for name in players:
    total+=players[name]
    
print("total score ",total)