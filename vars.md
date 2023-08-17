# Variable Declaraion Results

[back to main results](./index.md)

We start the evaluation of languages features with a simple variable declaration to check variables are correctly identified across the languages. In particular we are interested in verifying that type declarations and constants and variables are correctly map to variables. For this purpose we create exact clones of the variable declaration in both languages, modulo type declarations (left out of the Kotlin version in Snippet 2).

**Snippet 1.** Dart single variable declaration
``` 
 void main(){
     int lengthOfArray = 10;
 }
```

**Snippet 2.** Kotlin single variable declaration
```
 fun main(){
    val lengthOfArray = 10
 }
```
## Same-language evaluation

In this case we have a single version of the application for each language, effectively generating a Type 1 clone between the applications. The table beelow hows the summay of theobtain results fort each language, comparing the program ith itself.

**Language** | **Total** | **Type 1** | **Type 2** | **Type 3** | **FP** | **FN** | **Precision** | **Recall**|
---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----
Kotlin| 7 | 7 | 0 | 0 | - | - | - | - |
Dart|  |  |  |  | - | - | - | - |

## Cross-language evaluation

The analysis for Dart and Kotlin results in 4 correct Type 1 clones identifying the variables `main` function name, the number literal, and the `main` functions' parameter lists. A Type 2 clone is detected between the type declaration of the Dart code and the val declaration in the Kotlin case. FInally, a Type 3 clone is detected between . However, this clone is not of Type 3 as, contituing a False Positive.

The table below shows the summary of the results.

**Language** | **Total** | **Type 1** | **Type 2** | **Type 3** | **FP** | **FN** | **Precision** | **Recall**|
---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----
Dart v. Kotlin| 6 | 4 | 1 | 1 | 1 | 0 | 0.83 | 1 |
