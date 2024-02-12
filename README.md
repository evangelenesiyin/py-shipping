## 🛳️ Shipping Calculator

A Python script to calculate shipping prices according to weight. Type the weight in lbs and the system will print the calculated prices based on dummy information set for Ground, Ground Premium, and Drone shipping methods.

## 📝 Learnings

- Data types (`float`): Accepts integer input with decimals.
- Loops (`while`): Keeps the script going until the conditions are met.
- Conditional Statements (`if`, `elif`, `else`): Checks if the input satisfies the stated conditions and run the script accordingly.
- Python's `try... except ValueError` is similar to JavaScript's `try... catch(error)` which I am familiar with.
- Python's `locale` library: Specifies how numbers should be formatted e.g. two decimal places, with thousands separators.

I spent some time figuring out the logic to validate inputs and used a nested `while` loop to check the input for its validity before checking against the conditionals. 

As nested loops are generally `O(n^2)` in terms of time complexity, the usage of nested loops for this case turns out to be `O(n)`. The following is happening:
- The outer loop runs indefinitely until the script is manually terminated.
- The inner loop repeatedly prompts the user for input until a valid input is provided or the script is terminated. This is executed each time the outer loop iterates.

The inner loop is dependent on the user's input and that the number of iterations of the inner loop is not strictly bound by the number of iterations of the outer loop. Considering the worst case scenario when the user provides an invalid input repeatedly, this is linear in terms of the number of invalid input attempts and is not quadratic (`O(n^2)`).

## 💻 Try It Out

Download the `shipping.py` file and open it in a Python program like IDLE, or on VS Code and run `python3 shipping.py`.
  
## 📷 Demo Image

<img src="https://github.com/evangelenesiyin/py-shipping/assets/108106809/f5dc50ce-48e2-403e-9103-f787e42d9432" width="50%" />
