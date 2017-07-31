nums = range(0, 100)
def is_even(n):
    return n % 2 == 0

#we don't have to specify if is_even(n) = true because it's implied by the meaning of if.
#the below syntax is called list comprehension; if we make it a set, it's set comprehension
even_numbers = [ n for n in nums if is_even(n) ]
print even_numbers
