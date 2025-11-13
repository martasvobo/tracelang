// Test trace history access with @ operator

trace int counter = 0;
print("Initial counter: " + counter);

counter = 5;
print("Counter after first update: " + counter);

counter = 10;
print("Counter after second update: " + counter);

counter = 15;
print("Counter after third update: " + counter);

// Access historical values
print("\n=== Accessing History ===");
print("counter@0 (initial): " + counter@0);
print("counter@1 (first update): " + counter@1);
print("counter@2 (second update): " + counter@2);
print("counter@3 (third update): " + counter@3);

// Use history in calculations
int sum = counter@0 + counter@1 + counter@2 + counter@3;
print("\nSum of all history: " + sum);
