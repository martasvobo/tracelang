// TraceLang - Fibonacci with Trace History Access Example
// This demonstrates the unique trace feature with @ operator

function int fibonacci(int n) {
    if (n <= 1) {
        return n;
    }
    
    trace int prev = 0;
    trace int curr = 1;
    
    int i = 2;
    while (i <= n) {
        trace int temp = curr + prev;
        prev = curr;
        curr = temp;
        i++;
    }
    
    return curr;
}

trace int result = fibonacci(6);
print("Fibonacci(6) = " + result);

// Access the history of traced variables
print("\n=== Accessing Variable History ===");
print("result@0 (final): " + result@0);
