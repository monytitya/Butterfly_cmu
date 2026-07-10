#Pizza Party / Goal: Division
total_slices = 20
num_friends = 6

slices_per_friend = total_slices // num_friends

leftover_slices = total_slices % num_friends

print(f"Each friend gets {slices_per_friend} whole slices.")
print(f"There are {leftover_slices} slices left over.")