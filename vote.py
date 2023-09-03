#check if a person is applicable to vote or not.
age = int(input("Enter your age :"))
n  = age>=18
vote = "yes,you can vote"*n + "no you can not vote"*(1-n)
print(vote)
