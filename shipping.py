weight = float(input("Enter the weight of the package (lb): "))

# Ground Shipping
if weight <= 2:
    ground_cost = round((weight * 1.50) + 20.00, 2)
    print(f"Ground Shipping Cost: ${ground_cost}")
elif 2 < weight <= 6:
    ground_cost = round((weight * 3.00) + 20.00, 2)
    print(f"Ground Shipping Cost: ${ground_cost}")
elif 6 < weight <= 10:
    ground_cost = round((weight * 4.00) + 20.00, 2)
    print(f"Ground Shipping Cost: ${ground_cost}")
else:
    ground_cost = round((weight * 4.75) + 20.00, 2)
    print(f"Ground Shipping Cost: ${ground_cost}")

# Ground Shipping Premium
ground_premium_cost = 125.00
print(f"Ground Shipping Premium Cost: ${ground_premium_cost}")

# Drone Shipping
if weight <= 2:
    drone_cost = round(weight * 4.50, 2)
    print(f"Drone Shipping Cost: ${drone_cost}")
elif 2 < weight <= 6:
    drone_cost = round(weight * 9.00, 2)
    print(f"Drone Shipping Cost: ${drone_cost}")
elif 6 < weight <= 10:
    drone_cost = round(weight * 12.00, 2)
    print(f"Drone Shipping Cost: ${drone_cost}")
else:
    drone_cost = round(weight * 14.25, 2)
    print(f"Drone Shipping Cost: ${drone_cost}")

cheapest = min(ground_cost, ground_premium_cost, drone_cost)
if cheapest == ground_cost:
    print(
        f"The cheapest option is Ground Shipping with a cost of ${ground_cost}.")
elif cheapest == ground_premium_cost:
    print(
        f"The cheapest option is Ground Shipping Premium with a cost of ${ground_premium_cost}.")
else:
    print(
        f"The cheapest option is Drone Shipping with a cost of ${drone_cost}.")
