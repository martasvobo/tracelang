// TraceLang - Practical Trace History Example
// Demonstrates the @ operator for accessing variable history

print("=== Price Change Analysis ===\n");

trace float price = 100.0;
print("Day 1 - Starting price: $" + price);

price = 110.0;
print("Day 2 - Price increased to: $" + price);

price = 105.0;
print("Day 3 - Price decreased to: $" + price);

price = 115.0;
print("Day 4 - Price increased to: $" + price);

price = 120.0;
print("Day 5 - Price increased to: $" + price);

// Analyze the price history
print("\n=== Historical Analysis ===");
print("Day 1 price: $" + price@0);
print("Day 2 price: $" + price@1);
print("Day 3 price: $" + price@2);
print("Day 4 price: $" + price@3);
print("Day 5 price: $" + price@4);

// Calculate statistics
float totalChange = price@4 - price@0;
print("\nTotal change: $" + totalChange);

float avgPrice = (price@0 + price@1 + price@2 + price@3 + price@4) / 5.0;
print("Average price: $" + avgPrice);

// Find biggest single-day change
float change1 = price@1 - price@0;
float change2 = price@2 - price@1;
float change3 = price@3 - price@2;
float change4 = price@4 - price@3;

print("\nDaily changes:");
print("Day 1->2: $" + change1);
print("Day 2->3: $" + change2);
print("Day 3->4: $" + change3);
print("Day 4->5: $" + change4);

print("\n=== Counter Example ===\n");

trace int steps = 0;
print("Starting counter at: " + steps);

int i = 0;
while (i < 5) {
    steps = steps + (i + 1);
    print("Step " + (i + 1) + ": counter = " + steps);
    i++;
}

print("\n=== Counter History ===");
print("steps@0 = " + steps@0);
print("steps@1 = " + steps@1);
print("steps@2 = " + steps@2);
print("steps@3 = " + steps@3);
print("steps@4 = " + steps@4);
print("steps@5 = " + steps@5);

// Calculate increments from history
int inc1 = steps@1 - steps@0;
int inc2 = steps@2 - steps@1;
int inc3 = steps@3 - steps@2;
int inc4 = steps@4 - steps@3;
int inc5 = steps@5 - steps@4;

print("\nIncrements:");
print("Increment 1: " + inc1);
print("Increment 2: " + inc2);
print("Increment 3: " + inc3);
print("Increment 4: " + inc4);
print("Increment 5: " + inc5);

print("\n=== All Examples Complete! ===");
