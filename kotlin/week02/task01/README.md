## Comparison

Read about [operator overloading][1] to learn how
different conventions for operations like `==`, `<`, `+`
work in Kotlin. Add the function `compareTo` to the
`class MyDate` to make it comparable. After that the code
below `date1 < date2` will start to compile.

In Kotlin when you override a member, the modifier [`override`][2] is mandatory.

[1]: https://kotlinlang.org/docs/reference/operator-overloading.html
[2]: https://kotlinlang.org/docs/reference/classes.html#overriding-members