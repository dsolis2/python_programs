# This program uses recursion to solve the puzzle.
  
def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    #print(n)
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
  
# Numer of disks
disks = 4
  
# A, C, B are the name of rods
TowerOfHanoi(disks, 'A', 'C', 'B')

#Adding some text
