# nested list
delhi_aqi = [
    [145, 210, 189, 320, 275, 410, 380],  # Week 1
    [260, 305, 330, 285, 410, 395, 370],  # Week 2
    [420, 385, 440, 310, 295, 260, 355],  # Week 3
    [280, 360, 340, 455, 380, 410, 290],   # Week 4
    [300,400],   # Week 5
]
# findout average aqi
# nested list
delhi_aqi = [
    [145, 210, 189, 320, 275, 410, 380],  # Week 1
    [260, 305, 330, 285, 410, 395, 370],  # Week 2
    [420, 385, 440, 310, 295, 260, 355],  # Week 3
    [280, 360, 340, 455, 380, 410, 290],   # Week 4
    [300,400],   # Week 5
]
total = 0
count = 0
# findout average aqi
# task minimum aqi, maximum aqi
for week in delhi_aqi:
    for day in week:
        total+=day 
        count+=1

print("total ", total)
print("average ", total/count)
