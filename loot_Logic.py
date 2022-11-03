import random

master_Loot = {
  1: '1H Sword',
  2: 'Shield',
  3: '2H Sword',
  4: 'Staff',
  5: 'Short Bow',
  6: 'Long Bow',
  7: 'Damascus'
}

# Get random loot from a chest
# Start with an empty loot list
def get_Loot(loot_Result=[]):
  #Get a random integer number up to the length of the Loot Chest
  rand_Num = random.randint(1, len(master_Loot))
  print(f'Loot Size {rand_Num}')
  # Pick out the random items from the Loot Chest and add them to the Loot
  # Results list if they dont already exist in the table
  for i in master_Loot:
    # Get a second random number to randomize the order of the items
    # being picked out
    rand_Num2 = random.randint(1, len(master_Loot))
    print(f'{i}.Selected Item #{rand_Num2}')
    # If the item picked out is already on the Results list, skip it
    if master_Loot[rand_Num2] in loot_Result:
      continue
    # If the item in NOT on the Results, append it to the list
    else:
      loot_Result.append(master_Loot[rand_Num2])
    # Once 'i' reaches the length of rand_Num, stop the loop
    if i >= rand_Num:
      break

  # The function ends with a new list of loot randomly picked out from the chest
  return loot_Result