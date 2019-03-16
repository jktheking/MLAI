# Set Operations Description
# In a school, there are total 20 students numbered from 1 to 20. You’re given
# three lists named ‘C’, ‘F’, and ‘H’, representing students who play cricket, football, and hockey, respectively.
# Based on this information, find out and print the following:
# Students who play all the three sports
# Students who play both cricket and football but don’t play hockey
# Students who play exactly two of the sports
# Students who don’t play any of the three sports
from builtins import set

C = [2, 5, 9, 12, 13, 15, 16, 17, 18, 19]
F = [2, 4, 5, 6, 7, 9, 13, 16]
H = [1, 2, 5, 9, 10, 11, 12, 13, 15]

setC = set(C)
setF = set(F)
setH = set(H)
# Students who play all the three sports
whoPlayAllTheGames = (setC.intersection(setF).intersection(setH))
print(sorted(list(whoPlayAllTheGames)))
# Students who play both cricket and football but don’t play hockey
whoPlayCandFnotH = (setC.intersection(setF)).difference(setH)
print(sorted(list(whoPlayCandFnotH)))

# Students who play exactly two of the sports
whoPlayCandHnotF = (setC.intersection(setH)).difference(setF)
whoPlayFandHnotC = (setF.intersection(setH)).difference(setC)
whoPlayExactly2Games = whoPlayCandFnotH.union(whoPlayCandHnotF).union(whoPlayFandHnotC)
print(sorted(list(whoPlayExactly2Games)))

# Students who don’t play any of the three sports
universalSet = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
notAplayer = universalSet.difference(setC.union(setF).union(setH))
print(sorted(list(notAplayer)))