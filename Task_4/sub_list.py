# Step 1: Given list
nums = [4, 2, -3, 1, 6]

# Step 2: Loop through each starting point
for i in range(len(nums)):
    
    total = 0   # reset sum for each new start
    
    # Step 3: Check sub-list from i to end
    for j in range(i, len(nums)):
        total = total + nums[j]   # add elements
        
        # Step 4: Check if sum becomes 0
        if total == 0:
            print("Sub-list with sum 0 found")