# Conditional nodes

[back to main results](./index.md)

To evaluate conditional nodes we provide two variations of the `if-else` statement in both Dart (in Snippets \ref{lst:ifdA} \ref{lst:ifdB}), and Kotlin (in Snippets \ref{lst:ifkA} and \ref{lst:ifkB}). These code snippets are defined to exhibit Type 1 clones in the `else` branch, and Type 2 clones in the `if` condition.

**Snippet 1.** Dart version A `if` example with Type-2 (with Snippet 2) clone in conditional variable.
```
 String conditional() {
  var i;

  if (i > 10) { return "Hi"; }
  else { return "Bye"; }
  
 }
```

**Snippet 2.** Dart version B `if` example with Type-2 (with Snippet 1) clone in conditional variable.
```
String conditional() {
  var j;
  
  if (j > 10) { 
    return "Hi"; 
  }
  else { 
    return "Bye"; 
  }
}
```

**Snippet 3.** Kotlin version A `if` example with Type-2 (with Snippet 4) clone in conditional variable
```
fun conditional() : String {
    val i : Int

    if (i > 10) {
        return "Hi"
    } else {
        return "Bye"
    }
}
```

**Snippet 4.** Kotlin version B `if` example with Type-2 (with Snippet 3) clone in conditional variable
```
fun conditional() : String {
    val j : Int
    if (j > 10) { return "Hi" }
    else { return "Bye" }
}
```

Analyzing the snippets for a single language, our algorithm is able to detect both, the Type-1 and Type-2 clones. In the case of the Kotlin snippets, a Type-2 clone was found in the first line for the variable definitions, `i` and `j`, while Type-1 clones were found across the rest of the snippet. The same exact analysis applies for the Dart snippets.

Given the nature of the examples and the similarity of the `if` abstraction in both programming languages, when versions A are analyzed across languages, we detect Type 1 clones in the complete snippet. The same result ie yield when analyzing versions B of the `if` abstraction. Finally, the outcome of comparing any A vs any B versions across languages will find the inserted Type 2 clone for the variables `i` and `j` in the condition.

## Same-language evaluation

In teh case of conditionals we purpusly add two version of the same program, with the existence of two Type 2 clones (the var defition) as shown in the previous snippets. For the comparison of the same langauge experiments, we compare both version A, version B, and version A v. version B for each language.

**Language** | **Total** | **Type 1** | **Type 2** | **Type 3** | **FP** | **FN** | **Precision** | **Recall**|
---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----
Dart A| 15 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
Dart B| 15 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
Dart A v. B | 15 | 13 | 2 | 0 | 0 | 0 | 1 | 1 |
Kotlin A| 16 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
Kotlin B| 16 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
Kotlin A v. B | 16 | 14 | 2 | 0 | 0 | 0 | 1 | 1 |


## Cross-language evaluation

The results of the cross-language comparison take into account the `A v. A`, `B v. B` and `A v. B` versions of the program.
The table below shows the summary of the results.

**Language** | **Total** | **Type 1** | **Type 2** | **Type 3** | **FP** | **FN** | **Precision** | **Recall**|
---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----
Dart v. Kotlin A |  |  |  |  |  |  |  |  |
Dart v. Kotlin A |  |  |  |  |  |  |  |  |
Dart A v. Kotlin B |  |  |  |  |  |  |  |  |
Dart B v. Kotlin a |  |  |  |  |  |  |  |  |
