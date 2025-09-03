import random
nu = int(input("Enter number of random points: "))
n = 0
count = 0
while count < nu:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        n += 1

    count += 1

pi_approx = 4 * n / nu
print("Approximation of pi:", pi_approx)