from pkg.calculator import Calculator

calc = Calculator()
result = calc.evaluate("3 + 7 * 2")
print(f"3 + 7 * 2 = {result}")
assert result == 17, f"Expected 17, got {result}"

result2 = calc.evaluate("3 * 4 + 5")
print(f"3 * 4 + 5 = {result2}")
assert result2 == 17, f"Expected 17, got {result2}"

print("All manual checks passed!")
