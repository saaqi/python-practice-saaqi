import time
start_time = time.time()

# outer loop
for i in range(100):
  # inner loop
  for j in range(50):
    print (j, end= ", ")
    j += 1
  print(i)
  i += 1

print("\n\n\n in")
print(round(time.time() - start_time, 5), "Seconds")