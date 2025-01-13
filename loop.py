# for Loop
# while loop

# str = "Saqib Islam, Front-End Web Developer"
# num = 0

# for i in str:
#   print(i)

# while num < 5:
#   num = num + 1
#   print(num)

food = ["Biryani", "Karahi", "Nihari", "Pulao", "Kabab", "Kofta", "Korma", "Haleem", "Qorma", "Kheer"]

# for item in food:
#   print(item, end=", ")

count = 0
while count < len(food):
  print(food[count], end=", ")
  count += 1