#!/usr/bin/env python3

import sys
import math

# Function to check if a value is numeric
def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Function to perform calculations and return results
def calculate(a, b, c):
    # Check if inputs are numeric
    if not all(is_numeric(x) for x in [a, b, c]):
        return "<p style='color:red;'>Error: All inputs must be numeric.</p>"
    
    # Convert inputs to float
    a = float(a)
    b = float(b)
    c = float(c)
    
    # Conditional checks and calculations
    if a < 1:
        return "<p style='color:red;'>Error: Input 'a' is too small (must be >= 1).</p>"
    
    if b == 0:
        result_message = "<p>Note: 'b' is 0, so it will not affect the result.</p>"
    else:
        result_message = ""
    
    if c < 0:
        return "<p style='color:red;'>Error: Input 'c' cannot be negative.</p>"
    
    # Compute c^3
    c_cubed = c ** 3
    
    # Perform calculations based on c^3
    if c_cubed > 1000:
        final_result = math.sqrt(c_cubed) * 10
    else:
        final_result = math.sqrt(c_cubed) / a
    
    # Add b to the final result
    final_result += b
    
    # Generate HTML output
    output = f"""
    <h2>Calculation Results</h2>
    <p>Input values:</p>
    <ul>
        <li>a = {a}</li>
        <li>b = {b}</li>
        <li>c = {c}</li>
    </ul>
    {result_message}
    <p>Final Result: <strong>{final_result:.2f}</strong></p>
    """
    return output

# Main script execution
if __name__ == "__main__":
    # Retrieve input values from command-line arguments
    if len(sys.argv) != 4:
        print("<p style='color:red;'>Error: Invalid number of arguments. Expected 3 inputs (a, b, c).</p>")
        sys.exit(1)
    
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
    
    # Perform calculations and print the result
    result = calculate(a, b, c)
    print(result)