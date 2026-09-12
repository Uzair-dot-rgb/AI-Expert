n = 10
guess = input("Double Loop at n = 10 checks n x n pairs. How many?  ")
input("Formula: one calculation, done. Press Enter to run ")
steps = 1
print("  steps=", steps, "  ->  0(n)  constant time  ->  steps never change")

input("Loop: one step per item.  Press Enter to run ")
steps = 0
for i in range(n):
    steps += 1
print("  steps=", steps, "  ->  0(n)  linear time  ->  steps increase with n")

input("Double Loop: checks every pair.  Press Enter to run ")
steps = 0
for i in range(n):
    for j in range(n):
        steps += 1
print("  steps=", steps, "  your guess:", guess, "  ->  0(n^2)  quadratic time")
input("Two more notations.  Press Enter ")
print("  Big Omega  Ω  -> best case lower bound")
print("  Big Theta  Θ  -> exact bound (worst = best)")
