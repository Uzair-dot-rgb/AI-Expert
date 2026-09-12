n = int(input("Enter any n (try, 5, 10, or 50): "))
input("One Loop - runs once per item.  Press Enter to run ")
for i in range(n):
    pass
print("  n =", n, "  steps =", n, "  ->  0(n)  linear time")
input("Two nested loops - runs once per item.  Press Enter to run ")
for i in range(n):
    for j in range(n):
        pass
print("  n =", n, "  steps =", n * n, "  ->  0(n^2)  quadratic time")
input("Rule: count loops.  Press Enter ")
print("  0 loops -> 0(1)  1 loop -> 0(n)  2 nested -> 0(n^2)")
