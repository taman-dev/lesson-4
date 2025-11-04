amount = int(input("enter a value"))
note_1 = amount//100
note_2 = (amount%100)//50
note_3 = ((amount%100)%50)//10
print("number of 100 rupee notes",note_1) 