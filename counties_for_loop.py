counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, voters in counties_dict.items():
    print(county,voters,sep=' county has ',end=' registered voters.\n')


for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")