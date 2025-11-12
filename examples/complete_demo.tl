// TraceLang - Complete Features Demo
// Demonstrates all language features

// 1. Variable declarations with different types
int age = 25;
float pi = 3.14159;
string name = "TraceLang";
bool isActive = true;

print("=== Data Types Demo ===");
print("Age: " + age);
print("Pi: " + pi);
print("Name: " + name);
print("Active: " + isActive);

// 2. Arithmetic operations
int a = 10;
int b = 3;
print("\n=== Arithmetic Operations ===");
print("10 + 3 = " + (a + b));
print("10 - 3 = " + (a - b));
print("10 * 3 = " + (a * b));
print("10 / 3 = " + (a / b));
print("10 % 3 = " + (a % b));

// 3. Comparison operators
print("\n=== Comparison Operations ===");
print("10 == 3: " + (a == b));
print("10 != 3: " + (a != b));
print("10 > 3: " + (a > b));
print("10 < 3: " + (a < b));
print("10 >= 3: " + (a >= b));
print("10 <= 3: " + (a <= b));

// 4. Logical operators
bool x = true;
bool y = false;
print("\n=== Logical Operations ===");
print("true && false: " + (x && y));
print("true || false: " + (x || y));
print("!true: " + (!x));

// 5. If/Else statement
print("\n=== If/Else Demo ===");
int score = 85;
if (score >= 90) {
    print("Grade: A");
} else {
    if (score >= 80) {
        print("Grade: B");
    } else {
        print("Grade: C");
    }
}

// 6. While loop
print("\n=== While Loop Demo ===");
int count = 0;
while (count < 5) {
    print("Count: " + count);
    count++;
}

// 7. For loop
print("\n=== For Loop Demo ===");
for (int i = 0; i < 5; i++) {
    print("i = " + i);
}

// 8. Arrays
print("\n=== Array Demo ===");
array<int> numbers = [1, 2, 3, 4, 5];
print("First element: " + numbers[0]);
print("Array length: " + length(numbers));

int idx = 0;
while (idx < length(numbers)) {
    print("numbers[" + idx + "] = " + numbers[idx]);
    idx++;
}

// 9. Array modification
numbers[2] = 10;
print("After modification, numbers[2] = " + numbers[2]);

// 10. Functions
print("\n=== Function Demo ===");

function int add(int x, int y) {
    return x + y;
}

function int multiply(int x, int y) {
    return x * y;
}

int sum = add(5, 3);
int product = multiply(4, 7);
print("5 + 3 = " + sum);
print("4 * 7 = " + product);

// 11. Compound assignments
print("\n=== Compound Assignments ===");
int num = 10;
print("Initial: " + num);
num += 5;
print("After += 5: " + num);
num -= 3;
print("After -= 3: " + num);
num *= 2;
print("After *= 2: " + num);
num /= 4;
print("After /= 4: " + num);

// 12. Increment/Decrement
print("\n=== Increment/Decrement ===");
int counter = 5;
print("Initial: " + counter);
counter++;
print("After ++: " + counter);
counter--;
print("After --: " + counter);

print("\n=== All Features Tested Successfully! ===");
