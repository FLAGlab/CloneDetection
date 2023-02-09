# Loop evaluation Results

[back to main results](./index.md)

Managing loops is an interesting case for universal nodes. Loop abstractions are defined using different keywords in the programming languages (e.g., `for`, `while`). In Out of Step we process loop abstractions as semantically equivalent, and define them as Type 3 clones. To evaluate this, we manually inject Type 1 and Type 3 clones in our tests.

**Snippet 1.** Dart for loop - version A
``` 
 int sum = 0;
 for (int i = 1; i <= 100; i++) 
    sum = sum + i;
```

**Snippet 2.** Dart while loop - version B
```
 int sum = 0;
 int i = 1;
 while ( i <= 100) {
    sum = sum + i;
    i = i + 1;
 }
```

**Snippet 3.** Kotlin for loop - version A.
```
 var sum = 0;
 for (i in 1..100) 
    sum = sum + i
```

**Snippet 4.** Kotlin while loop - version B
```
 var sum = 0
 var i = 1
 while (i <= 100) {
    sum = sum + i
    i = i + 1
 }
```

The analysis for Dart (Snippets 1 and 2), and Kotlin (Snippets 3 and 4) in the same language results in two Type 3 clones. These match the `for` and `while` statements and the `i` variable declaration. The clone for the postfix statement `i++` and the variable assignment `i = i + 1` is not correctly detected as a Type 3 clone due to their node representations in the eCST, an `assignment_operator` unary node, and a binary node respectively. Nonetheless, we identify the complete `for` and `while` blocks as clones of each other, as the algorithm broadcasts clones inside the body of blocks. Additionally, Out of Step identifies the declarations and assignment of variables as Type 1 clones in Line 1 of both snippets, and Line 3 of version A with Line 4 of version B.

The cross-language comparison between code versions A and B is also successful in detecting the corresponding clones. This is because the node information and the eCST structure are the same for the two code snippets. Every node is matched to its corresponding node on the other eCST, even though the programming languages differ. When comparing any A vs any B versions, we find that there are Type 3 clones for the `for` and `while` statements, and the definition of variable `i`. Additionally, we can find the Type 1 clones for the declaration and assignment of the `sum` variable, as before.

In the loop analysis, Out of Step finds a couple of Type 2 false positives, due to the two assignments that are present in versions B of the code. In this case, the detection algorithm points to the body of the `for` and `while` statements to be clones. This happens because the intermediate type node for both of them is the same. The exact same behavior takes place with the assignment before the `loop` statement in both cases.

**Snippet 2.** Bubble sort in Kotlin.
```
fun bubbleSort(arr){
    var swap = true
    var len = arr.size
    while(swap){
        swap = false;
        for(i in 0 until len-1){
            if(arr[i]>arr[i+1]){
                val temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                swap = true
            }
        }
    }
    return arr
}
```

**Algorithm** | **Total** | **Type 1** | **Type-2** | **Type 3** | **FPs** | **Precision**
---- | ---- | ---- | ---- | ---- | ---- | ---- 
Dart-A v. Dart-B|  |  |  |  | 
Kotlin-A v. Kotlin-B|  |  |  |  | 
Dart-A v. Kotlin-A|  |  |  |  | 
Dart-B v. Kotlin-B|  |  |  |  | 
Dart-A v. Kotlin-B|  |  |  |  | 
Dart-B v. Kotlin-A|  |  |  |  | 
