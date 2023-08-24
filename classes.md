# Class definition

[back to main results](./index.md)

To evaluate the definition of classes we create a simple definition of a person class with its constructure and two methods.
For each class definition we create two versions, exchanging the position of the class definition and its use. 
The Dart snippet shows the first version, while the Kotlin snippet the second version. Aside from the ordering, the classes are identical.

**Snippet 1.** Dart class declaration and object creation
```
main(){
    Person A = Person("A");
    Person B = Person("B");
}

class Person {
    var name;

    Person(String name) {
      this.name = name;
    }

    String present(){
        return "Yes";
    }

    String great(String other){
        return "Both ${name} and ${other}";
    }
}
```

**Snippet 2.** Kotlin class declaration, version B
```
class Person(private val name: String){
    fun present() : String = "Yes"
    fun greet(other: String) : String {
        return "Both $name and $other"
    }
}

fun main(args: Array<String>) {
    val A = Person("A")
    val B = Person("B")
}
```

## Single language evaluation

In the single version of the programs we evaluate the program with itself, and with the version exchanging the class definition location.

**Language** | **Total** | **Type 1** | **Type 2** | **Type 3** | **FP** | **FN** | **Precision** | **Recall**|
---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----
Dart A|  |  |  |  |  |  |  |  |
Dart B|  |  |  |  |  |  |  |  |
Dart A v. B|  |  |  |  |  |  |  |  |
Dart A|  |  |  |  |  |  |  |  |
Dart B|  |  |  |  |  |  |  |  |
Dart A v. B|  |  |  |  |  |  |  |  |



## Cross-language evaluation

In the cross language analysis, we cross the Dart and Kotlin implementations of the same version of the program and its crossed versions.

**Language** | **Total** | **Type 1** | **Type 2** | **Type 3** | **FP** | **FN** | **Precision** | **Recall**|
---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----
Dart v. Kotlin A|  |  |  |  |  |  |  |  |
Dart v. Kotlin B|  |  |  |  |  |  |  |  |
Dart A v. Kotlin B|  |  |  |  |  |  |  |  |
Dart B v. Kotlin A|  |  |  |  |  |  |  |  |
