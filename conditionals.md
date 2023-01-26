# Conditional nodes

[back to main results](./index.md)

To evaluate conditional nodes we provide two variations of the `if-else` statement in both Dart (in Snippets \ref{lst:ifdA} \ref{lst:ifdB}), and Kotlin (in Snippets \ref{lst:ifkA} and \ref{lst:ifkB}). These code snippets are defined to exhibit Type 1 clones in the `else` branch, and Type 2 clones in the `if` condition.

**Snippet 1.** Dart `if` example with Type-2 (with Snippet 2) clone in conditional variable.
```
 if (i > 10) { return "Hi"; }
 else { return "Bye"; }
```

**Snippet 2.** Dart `if` example with Type-2 (with Snippet 1) clone in conditional variable.
```
 if (j > 10) { return "Hi"; }
 else { return "Bye"; }
```

**Snippet 3.** Kotlin `if` example with Type-2 (with Snippet 4) clone in conditional variable
```
if (i > 10) { return "Hi" }
else { return "Bye" }
```

**Snippet 4.** Kotlin `if` example with Type-2 (with Snippet 3) clone in conditional variable
```
if (j > 10) { return "Hi" }
else { return "Bye" }
```

Analyzing the snippets for a single language, our algorithm is able to detect both, the Type-1 and Type-2 clones. In the case of the Kotlin snippets, a Type-2 clone was found in the first line for the variable definitions, `i` and `j`, while Type-1 clones were found across the rest of the snippet. The same exact analysis applies for the Dart snippets.

Given the nature of the examples and the similarity of the `if` abstraction in both programming languages, when versions A are analyzed across languages, we detect Type 1 clones in the complete snippet. The same result ie yield when analyzing versions B of the `if` abstraction. Finally, the outcome of comparing any A vs any B versions across languages will find the inserted Type 2 clone for the variables `i` and `j` in the condition.

## Experiment results
