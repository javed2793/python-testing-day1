ways = 0

for c1 in range(11):      # ₹1 coins
    for c2 in range(6):   # ₹2 coins
        for c5 in range(3):   # ₹5 coins
            for c10 in range(2):  # ₹10 coins
                
                if c1*1 + c2*2 + c5*5 + c10*10 == 10:
                    ways = ways + 1

print("Total ways:", ways)
ways = 0

for c1 in range(11):
    for c2 in range(6):
        for c5 in range(3):
            for c10 in range(2):
                
                if c1 + 2*c2 + 5*c5 + 10*c10 == 10:
                    print(c1, c2, c5, c10)
                    ways = ways + 1

print("Total ways:", ways)