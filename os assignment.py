#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Define sets of tuples
set1 = {(1, 3), (2, 4), (5, 6)}
set2 = {(2, 4), (3, 5), (7, 8)}

# Union of sets
union_set = set1.union(set2)
print("Union:", union_set)

# Intersection of sets
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

# Finding maximum and minimum values
max_value = max(set1.union(set2), key=lambda x: x[1])
min_value = min(set1.union(set2), key=lambda x: x[0])
print("Maximum value:", max_value)
print("Minimum value:", min_value)


# In[ ]:




