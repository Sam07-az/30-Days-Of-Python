# 1. names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. Unpack the first five countries and 
# store them in a variable nordic_countries, 
# store Estonia and Russia in es, and ru respectively.

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']

*nordic_countries , es , ru = names
print(nordic_countries, es , ru)
#output
# ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland'] Estonia Russia
*n, s , f , t , u = names
print(n,s,f,t,u)