# What is the difference between NULL and nullptr?
## nullptr has type std::nullptr_t. It's implicitly convertible to any pointer type. Thus, it'll match std::nullptr_t or pointer types in overload resolution, but not other types such as int.
## NULL just an Integer 0
```
void fun(int* x) { std::cout << "fun(int*) called\n"; }
```
```
void fun(int x) { std::cout << "fun(int) called\n"; }
```

```
int main() {
  fun(nullptr); // this works fine becuase it will call fun(int*)

  fun(NULL); // this is ambiguous call because  NULL (aka 0) can call any func of them

  return 0;
}
```

[reference](https://stackoverflow.com/questions/20509734/null-vs-nullptr-why-was-it-replaced)
