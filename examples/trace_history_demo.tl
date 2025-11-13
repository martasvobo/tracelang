// TraceLang - Comprehensive Trace History Demo
// Demonstrates accessing previous values with @ operator

print("=== Basic Counter Example ===");
trace int counter = 0;
print("counter = " + counter);

counter = 10;
print("counter = " + counter);

counter = 20;
print("counter = " + counter);

counter = 30;
print("counter = " + counter);

print("\nAccessing history:");
print("counter@0 = " + counter@0);
print("counter@1 = " + counter@1);
print("counter@2 = " + counter@2);
print("counter@3 = " + counter@3);

// Example: Calculate differences between successive values
print("\n=== Calculating Differences ===");
int diff1 = counter@1 - counter@0;
int diff2 = counter@2 - counter@1;
int diff3 = counter@3 - counter@2;
print("Diff between @1 and @0: " + diff1);
print("Diff between @2 and @1: " + diff2);
print("Diff between @3 and @2: " + diff3);

// Example: Loop with trace
print("\n=== Loop with Trace ===");
trace int loopVar = 1;
int count = 0;
while (count < 4) {
    loopVar = loopVar * 2;
    count++;
}

print("Final loopVar = " + loopVar);
print("\nLoop history:");
print("loopVar@0 = " + loopVar@0);
print("loopVar@1 = " + loopVar@1);
print("loopVar@2 = " + loopVar@2);
print("loopVar@3 = " + loopVar@3);
print("loopVar@4 = " + loopVar@4);

// Example: Using history in expressions
print("\n=== Using History in Calculations ===");
trace float price = 100.0;
print("Initial price: " + price);

price = price * 1.1;
print("After 10% increase: " + price);

price = price * 0.9;
print("After 10% decrease: " + price);

float avgPrice = (price@0 + price@1 + price@2) / 3.0;
print("Average price across history: " + avgPrice);

print("\n=== All Tests Completed! ===");
