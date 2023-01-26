# Out of Step

## Cross-language Clone Detection for Mobile Apps

This online appendix presents the complete evaluation results for our work on cross-language clone detection for mobile device programming languages: Dart, Kortlin, and Swift.

The experiment evaluation is structured in three parts.

1. Clone detection for the basic language features.
2. Clone detection using algorithms from a known (i.e., sorting algorithms) domain.
3. Clone detection on a corpus of mobile app repositories.

## Clone detection: Language Features

Teh first part of our evaluation consists on assuring Out of Step is able to detect clones effectively across the different language features and abstractions. To demonstrate this, we provide implementations demonstrating each of the features and manually translate them to the other languages, generating a high rate of Type-1 and Type-2 clones.

### Dataset description

The language features datasets consists of 7 categories as shown in the following table. For each of the categories we show the different files and clones to test.

Note that, while we define the programs for different programming languages, we focus the result and analysis to the mobile app programming languages Dart and Kotlin.

Feature | Cases | Evaluation | Languages
------ | -------------- | -------------- | --------------
Variable declaration | 1 | integer variable declaration | C++, Dart, Java, kotlin, Swift
Function declaration | 1 | Stats calculation | C++, Dart, Java, Kotlin, Swift
Conditionals | 1 | Test variable and return | C++, Dart, Java, Kotlin, Swift
Loops | 2 | `for` loop <br><br> `while` loop | C++, Dart, Java, Kotlin, Swift
Structures | 2 | Structures <br> Enumerations | C++ Swift <br> C++, Dart, Java, Kotlin, Swift
Classes | 2 | 1-to-1 definition <br> Crossed definition | C++, Dart, Java, Kotlin, Swift <br> C++, Dart, Java, Kotlin, Swift

#### Variable declaration

#### Conditional nodes

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

### Experiment results
