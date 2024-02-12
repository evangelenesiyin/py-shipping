import locale

locale.setlocale(locale.LC_ALL, '')

while True:
    weight_input = input(
        "Enter the weight of the package (lb), or type 'quit' to exit: ")

    if weight_input.lower() == 'quit':
        response = input(
            "The script is now stopped. Type 'start' to restart the script: ")
        if response.lower() == 'start':
            continue

    try:
        weight = float(weight_input)

        # Ground Shipping
        if weight <= 2:
            ground_cost = round((weight * 1.50) + 20.00, 2)
            print(
                f"Ground Shipping Cost: ${locale.format_string('%.2f', ground_cost, grouping=True)}")
        elif 2 < weight <= 6:
            ground_cost = round((weight * 3.00) + 20.00, 2)
            print(
                f"Ground Shipping Cost: ${locale.format_string('%.2f', ground_cost, grouping=True)}")
        elif 6 < weight <= 10:
            ground_cost = round((weight * 4.00) + 20.00, 2)
            print(
                f"Ground Shipping Cost: ${locale.format_string('%.2f', ground_cost, grouping=True)}")
        else:
            ground_cost = round((weight * 4.75) + 20.00, 2)
            print(
                f"Ground Shipping Cost: ${locale.format_string('%.2f', ground_cost, grouping=True)}")

        # Ground Shipping Premium
        ground_premium_cost = 125.00
        print(
            f"Ground Shipping Premium Cost: ${locale.format_string('%.2f', ground_premium_cost, grouping=True)}")

        # Drone Shipping
        if weight <= 2:
            drone_cost = round(weight * 4.50, 2)
            print(
                f"Drone Shipping Cost: ${locale.format_string('%.2f', drone_cost, grouping=True)}")
        elif 2 < weight <= 6:
            drone_cost = round(weight * 9.00, 2)
            print(
                f"Drone Shipping Cost: ${locale.format_string('%.2f', drone_cost, grouping=True)}")
        elif 6 < weight <= 10:
            drone_cost = round(weight * 12.00, 2)
            print(
                f"Drone Shipping Cost: ${locale.format_string('%.2f', drone_cost, grouping=True)}")
        else:
            drone_cost = round(weight * 14.25, 2)
            print(
                f"Drone Shipping Cost: ${locale.format_string('%.2f', drone_cost, grouping=True)}")

        cheapest = min(ground_cost, ground_premium_cost, drone_cost)
        if cheapest == ground_cost:
            print(
                f"The cheapest option is Ground Shipping with a cost of ${locale.format_string('%.2f', ground_cost, grouping=True)}.")
            print("==================================")
        elif cheapest == ground_premium_cost:
            print(
                f"The cheapest option is Ground Shipping Premium with a cost of ${locale.format_string('%.2f', ground_premium_cost, grouping=True)}.")
            print("==================================")
        else:
            print(
                f"The cheapest option is Drone Shipping with a cost of ${locale.format_string('%.2f', drone_cost, grouping=True)}.")
            print("==================================")
    except ValueError:
        response = input(
            "The input is invalid. Type 'start' to restart the script: ")
        if response.lower() == 'start':
            continue
        else:
            break
