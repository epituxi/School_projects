def linearSearch(table, x):
  for i in range(len(table)):
    if (table[i] == x):
      return i
  return -1

def binarySearch(table, x):
  low = 0
  high = len(table) - 1

  while (low <= high):
    mid = (low + high) // 2
    print(low, mid, high)
    if (table[mid] < x):
      low = mid + 1
    elif (table[mid] > x):
      high = mid - 1
    else:
      return mid
  return -1