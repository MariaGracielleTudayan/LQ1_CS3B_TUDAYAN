#store the names of all members
gname1 = "Maynard Pardaun Sumbad"
gname2 = "Emerson Mati Manzano"
gname3 = "Maria Gracielle Garingo Tudayan"

#store the age of all members
mem1age = "20"
mem2age = "22"
mem3age = "20"

#convert the string age into intiger
ageMem1 = int(mem1age)
ageMem2 = int(mem2age)
ageMem3 = int(mem3age)

#store the allowance of all member in decimal form
mem1Allowance = float(1000.0)
mem2Allowance = float(1000.0)
mem3Allowance = float(1000.0)

#store the team name
teamName = "Rect"

#prints out the result using concatinate
print("Teame Name: ", teamName)
print("Member 1:", gname1, "his age is", mem1age, "allowance per week is", mem1Allowance)
print("Member 2:", gname2, "his age is", mem2age, "allowance per week is", mem2Allowance)
print("Member 3:", gname3, "her age is", mem3age, "allowance per week is", mem3Allowance)

#store the characters length of names of all members
memName1L = len(gname1)
memName2L = len(gname2)
memName3L = len(gname3)

#prints out the result
print("Member 1 consist of", memName1L, "characters") #22 characters
print("Member 2 consist of", memName2L, "characters") #20 characters
print("Member 3 consist of", memName3L, "characters") #31 characters

#Add and Subtract the ege of all members
addMem = (ageMem1 + ageMem2 + ageMem3) 
subMem = (ageMem1 - ageMem2 - ageMem3) 
print (addMem) #20+22+20=62
print (subMem) #20-22-20=-22

#multiply the age of all members to their allowance per week
multiplyMem1Allo = ageMem1 * mem1Allowance
multiplyMem2Allo = ageMem2 * mem2Allowance
multiplyMem3Allo = ageMem3 * mem3Allowance
print(multiplyMem1Allo) #20*1,000.0=20,000.0
print(multiplyMem2Allo) #22*1,000.0=22,000.0
print(multiplyMem3Allo) #20*1,000.0=20,000.0

#compare the age of members to thier groupmates
Com1 = (ageMem1 - ageMem2)
Com2 = (ageMem2 - ageMem3)
print(Com1) #20-22=-2
print(Com2) #22-20=2

#compare the name length of members to their groupmates
NameLength1 = (memName1L - memName2L)
NameLength2 = (memName2L - memName3L)
print(NameLength1) #22-20=2
print(NameLength2) #20-31=-11