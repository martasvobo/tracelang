// TraceLang - Array Operations Demo

print("=== Array Creation ===");
array<int> numbers = [10, 20, 30, 40, 50];
array<string> names = ["Alice", "Bob", "Charlie"];
array<float> prices = [9.99, 19.99, 29.99];

print("Numbers: " + numbers[0] + ", " + numbers[1] + ", " + numbers[2]);
print("Names: " + names[0] + ", " + names[1] + ", " + names[2]);

print("\n=== Array Length ===");
print("Numbers length: " + length(numbers));
print("Names length: " + length(names));

print("\n=== Array Iteration ===");
int i = 0;
while (i < length(numbers)) {
    print("numbers[" + i + "] = " + numbers[i]);
    i++;
}

print("\n=== Array Modification ===");
numbers[0] = 100;
numbers[2] = 300;
print("Modified array:");
for (int j = 0; j < length(numbers); j++) {
    print("numbers[" + j + "] = " + numbers[j]);
}

print("\n=== Sum Array Elements ===");
array<int> values = [5, 10, 15, 20, 25];
int total = 0;
for (int k = 0; k < length(values); k++) {
    total = total + values[k];
}
print("Sum of array: " + total);

print("\n=== Find Maximum ===");
array<int> nums = [3, 7, 2, 9, 1, 5];
int max = nums[0];
for (int m = 1; m < length(nums); m++) {
    if (nums[m] > max) {
        max = nums[m];
    }
}
print("Maximum value: " + max);
