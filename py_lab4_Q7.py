n=int(input("Enter the value:"))
def sum_series(n):
  if n < 1:
    return 0
  else:
    return n + sum_series(n - 2)

print("The sum of the positive integers:",sum_series(n))
