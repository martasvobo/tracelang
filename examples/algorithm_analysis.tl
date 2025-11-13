// TraceLang - Algorithm Analysis with Trace History
// Shows how trace history helps understand algorithm behavior

print("=== Bubble Sort Step Analysis ===\n");

// Simple bubble sort demonstration with trace
trace int swapCount = 0;
array<int> arr = [5, 2, 8, 1, 9];

print("Initial array: [5, 2, 8, 1, 9]");
print("Sorting...\n");

// Manual bubble sort steps (simplified for demo)
bool swapped = true;
int temp = 0;

// First pass
if (arr[0] > arr[1]) {
    temp = arr[0];
    arr[0] = arr[1];
    arr[1] = temp;
    swapCount++;
}

if (arr[1] > arr[2]) {
    temp = arr[1];
    arr[1] = arr[2];
    arr[2] = temp;
    swapCount++;
}

if (arr[2] > arr[3]) {
    temp = arr[2];
    arr[2] = arr[3];
    arr[3] = temp;
    swapCount++;
}

if (arr[3] > arr[4]) {
    temp = arr[3];
    arr[3] = arr[4];
    arr[4] = temp;
    swapCount++;
}

print("After first pass:");
print("Array: [" + arr[0] + ", " + arr[1] + ", " + arr[2] + ", " + arr[3] + ", " + arr[4] + "]");
print("Swaps so far: " + swapCount);

// View swap history
print("\n=== Swap History ===");
int maxIndex = swapCount@0;
int i = 0;
while (i <= maxIndex) {
    int swapAtI = 0;
    if (i == 0) { swapAtI = swapCount@0; }
    if (i == 1) { swapAtI = swapCount@1; }
    if (i == 2) { swapAtI = swapCount@2; }
    if (i == 3) { swapAtI = swapCount@3; }
    if (i == 4) { swapAtI = swapCount@4; }
    print("After swap " + i + ": " + swapAtI + " total swaps");
    i++;
}

// Example: Algorithm convergence tracking
print("\n\n=== Newton's Method Convergence ===");
trace float estimate = 2.0;
float target = 4.0;

// Simulate a few iterations of square root approximation
estimate = (estimate + target / estimate) / 2.0;
estimate = (estimate + target / estimate) / 2.0;
estimate = (estimate + target / estimate) / 2.0;

print("Final estimate: " + estimate);
print("\nConvergence path:");
print("estimate@0 (initial): " + estimate@0);
print("estimate@1 (iter 1): " + estimate@1);
print("estimate@2 (iter 2): " + estimate@2);
print("estimate@3 (iter 3): " + estimate@3);

// Calculate convergence rate
float error0 = estimate@0 - 2.0;
float error1 = estimate@1 - 2.0;
float error2 = estimate@2 - 2.0;
float error3 = estimate@3 - 2.0;

print("\nError reduction:");
print("Error at iter 0: " + error0);
print("Error at iter 1: " + error1);
print("Error at iter 2: " + error2);
print("Error at iter 3: " + error3);

print("\n=== Analysis Complete! ===");
