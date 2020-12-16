song = ["Djadja", 
        "NTM", 
        "FUCK", 
        "HighWayToHELLLL"]
print(song[0])
print(song[1])
print(song[2])
print(song[3])
song[0]="nirvana"
print(song[0])
print(song[1])
print(song[2])
print(song[3])

rick = ["Rick", "Grimes", 38, 180, False]
loana = ["loana", "joe", 87, 155, False]
brad = ["brad", "booze", 2, 190, True]

print(" ")
print(rick[1])
print(loana[1])
print(brad[1])

print(" ")

employees = ["Richard Swift", "Marie-Anne Petrie", "Cody Lightfoot", "Laure Simmons"]
employees.reverse()

print(employees)

print(" ")

song = ["Djadja", 
        "NTM", 
        "FUCK", 
        "HighWayToHELLLL"]
print(song[0])
print(song[1])
print(song[2])
print(song[3])
song.sort()
print(song[0])
print(song[1])
print(song[2])
print(song[3])
song.append("plz bitch")
print(song)
print ("There are " + str(len(song)) + " songs !")

song.pop(2)
print(song)
print (len(song))
