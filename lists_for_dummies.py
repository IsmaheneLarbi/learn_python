#doubling values in a list
prizes = [5, 10, 50, 100, 1000]
dbl_prizes = []
for prize in prizes:
    dbl_prizes.append(prize * 2)
print(dbl_prizes)

#comprehension method
dbl_prizes = [prize * 2 for prize in prizes]
print(dbl_prizes)

#square even numbers of a list
nums = [1,2,3,4,5,6,7,8,9,10]
squared_even_numbers = []
for num in nums:
    if (num ** 2) % 2 == 0:
        squared_even_numbers.append(num ** 2)
print(squared_even_numbers)

#comprehension
squared_even_numbers = [num ** 2 for num in nums if (num ** 2) % 2 == 0]
print(squared_even_numbers)