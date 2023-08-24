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
Dart A| 65 | 53 | 8 | 4 | 4 | 0 | 0.93 | 1 |
Dart B| 65 | 53 | 8 | 4 | 4 | 0 | 0.93 | 1 |
Dart A v. B| 65 | 53 | 8 | 4 | 4 | 0 | 0.93 | 1 |
Kotlin A| 50 | 40 | 6 | 4 | 4 | 0 | 0.92 | 1 |
Kotlin B| 50 | 40 | 6 | 4 | 4 | 0 | 0.92 | 1 |
Kotlin A v. B| 50 | 40 | 6 | 4 | 4 | 0 | 0.92 | 1 |

We observe from the Dart evaluation, that regardles of the location of the class definition and its use, the exact same clones are detected. Type 1 clones correspond to the matches of literal variables, class, and function names, while Type 2 clones correspond to the names of different elements in the program (independent of their type). Type 3 clones make the FPs, as they refer to the same universal nodes; these should be Type 1 clones.
The case for the Kotlin code, presents the same behavior as in Dart.

## Cross-language evaluation

In the cross language analysis, we cross the Dart and Kotlin implementations of the same version of the program and its crossed versions.

**Language** | **Total** | **Type 1** | **Type 2** | **Type 3** | **FP** | **FN** | **Precision** | **Recall**|
---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----
Dart v. Kotlin A| 34 | 12 | 12 | 10 | 15 | 2 | 0.55 | 0.91 |
Dart v. Kotlin B| 34 | 12 | 12 | 10 | 15 | 2 | 0.55 | 0.91 |
Dart A v. Kotlin B| 34 | 12 | 12 | 10 | 15 | 2 | 0.55 | 0.91 |
Dart B v. Kotlin A| 34 | 12 | 12 | 10 | 15 | 2 | 0.55 | 0.91 |

In the cross evaluation we notice a larger number of errors in the identification of clones. First, we notice that there are two FNs, failing to identify as clones the `A` variable declarations and the `greet` function definitions. Furthermore, the `greet` functions are incorrectly identified as Type 2 clones of each other. Finally, we get a large number of FPs in the identification of Type 3 clones of the same universal node types.
