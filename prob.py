#Problem: Quality check in a candy factory 

total_candies = 100
red_candies = 70

p_first_red = red_candies / total_candies

p_second_red = (red_candies - 1) / (total_candies - 1)
probability = p_first_red * p_second_red

print(f"the probability is {probability}")