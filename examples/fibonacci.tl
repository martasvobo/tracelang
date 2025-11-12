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
