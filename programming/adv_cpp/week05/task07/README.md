Воспользуйтесь `IntList` и метафункцией `Generate` для того, чтобы научиться "раскрывать" кортежи.
От вас потребуется написать функцию apply, которая принимает функтор и кортеж с аргументами для вызова этого функтора и вызывает функтор от этих аргументов.

### Пример:

```cpp
auto f = [](int x, double y, double z) { return x + y + z; };
auto t = std::make_tuple(30, 5.0, 1.6);  // std::tuple<int, double, double>
auto res = apply(f, t);                // res = 36.6
```

**Указание:** в решении этой задачи вам потребуется воспользоваться оператором "...", который позволяет раскрывать параметры в шаблонах с переменным числом аргументов. Пример использования этого оператора можно посмотреть в уроке про [perfect forwarding](https://stepik.org/lesson/53374/step/9?unit=31466).