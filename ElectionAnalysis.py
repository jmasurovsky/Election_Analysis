#!/usr/bin/env python
# coding: utf-8

# ## Election Analysis

# In[1]:


num_candidates = 3
winning_percentage = 73.81
candidate = "Diane"
won_election = True


# In[2]:


counties = ["Arapahoe","Denver","Jefferson"]
counties.append("El Paso")
counties.insert(2, "El Paso")
counties.remove("El Paso")
counties.pop(-1)
counties


# In[3]:


counties = ['El Paso','Jefferson','Denver','Arapahoe']


# In[4]:


def printname(counties):
    for name in counties[::-1]:
        print("hello " + name)
        
printname(counties)


# In[7]:


counties_dict = {}

counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438


# In[10]:


counties_dict.items()


# In[13]:


voting_data = []

voting_data.append({"county":"El Paso", "registered_voters": 461149})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({'county': 'Arapahoe', 'registered_voters': 422829})
voting_data


# In[14]:


# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")


# In[15]:


counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])


# In[16]:


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


# In[17]:


counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")


# In[19]:


if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")


# In[20]:


x = 0
while x <= 5:
    print(x)
    x = x + 1


# In[21]:


for county in counties:
    print(county)


# In[22]:


for i in range(len(counties)):
    print(counties[i])
    


# In[26]:


#Get keys in dict
for county in counties_dict:
    print(county)
print("---------")
#Get values in dict
for voters in counties_dict.values():
    print(voters)


# In[27]:


for county in counties_dict:
    print(counties_dict[county])


# In[28]:


for county in counties_dict:
    print(counties_dict.get(county))


# In[ ]:


#Syntax
for key, value in dictionary_name.items():
    print(key, value)


# In[30]:


for county, voters in counties_dict.items():
    print(county, voters)


# In[31]:


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)


# In[32]:


for county_dict in voting_data:
    for value in county_dict.values():
        print(value)


# In[33]:


for county_dict in voting_data:

     print(county_dict['registered_voters'])


# In[34]:


counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")


# In[35]:


for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")


# In[37]:


candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)


# In[ ]:




