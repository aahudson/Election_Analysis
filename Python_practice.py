print("Hello World")
print("Rise and Shine")

num_candidates = 3
winning_percentage = 73.81
candidate = "Diane"
won_election = True
help("keywords")
print((5 + 2) * 3)
print((8 // 5) - 3)
counties = ["Araphoe","Denver","Jefferson"]
print(counties)
my_list = [ ]
list()
my_list = list()
print(my_list)
print(counties[0])
print(counties[-1])
print(len(counties))
print(counties[0:2])
print(counties[0:1])
print(counties[:1])
counties.insert(2, "El Paso")
print(counties)
counties.remove("El Paso")
print(counties)
print(counties)
counties[2] = "El Paso"
print(counties)
counties_tuple = ("Arapahoe","Denver","Jefferson")
print(counties_tuple)
print(len(counties_tuple))
print(counties_tuple[1])
print(counties_tuple[:-2])
print(counties_tuple[:2])
print(counties_tuple[:-1])
print(counties_tuple[1:2])
my_dictionary = dict()
counties_dict = {}
print(counties_dict)
counties_dict["Arapahoe"] = 422829
print(counties_dict)
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)
print(len(counties_dict))
print(counties_dict.items())
print(counties_dict.keys())
print(counties_dict.values())
print(counties_dict.get("Denver"))
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
print(voting_data)
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data)
# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")

#What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')

# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

x = 0
while x <= 5:
    print(x)
    x = x + 1

count = 7

while count < 1:

    print("Hello World")

for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

for voters in counties_dict.values():
    print(voters)
