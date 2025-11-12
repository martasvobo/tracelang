print("=== Simple Trace Demo ===");
trace int x = 0;
x = 5;
x = 10;
x = 15;
print("Final x: " + x);

print("\n=== Trace in Loop ===");
trace int sum = 0;
int i = 1;
while (i <= 5) {
    sum = sum + i;
    i++;
}
print("Sum of 1-5: " + sum);

print("\n=== Trace with Function ===");
function int factorial(int n) {
    if (n <= 1) {
        return 1;
    }
    trace int result = 1;
    int i = 2;
    while (i <= n) {
        result = result * i;
        i++;
    }
    return result;
}

trace int fact5 = factorial(5);
print("5! = " + fact5);

print("\n=== Multiple Traced Variables ===");
trace int a = 1;
trace int b = 2;
trace int c = 0;

c = a + b;
a = a * 2;
b = b + 3;
c = a + b;

print("Final values: a=" + a + ", b=" + b + ", c=" + c);
