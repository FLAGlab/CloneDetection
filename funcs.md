# Function Definition Results

[back to main results](./index.md)

In the case of function definition we evaluate multiple function interacting with each other as part of a program  to check  declaration and the call to a print function. The Snippet exemoplars for Dart and Kotlin are as follows

**Snippet 1.** Dart multiple function definitions and calls
``` 
List<int> calculateStatistics(List<int> scores) {
    var min = scores[0];
    var max = scores[0];
    var sum = 0;

    for(int score in scores) {
        if(score > max) {
            max = score;
        } else if (score < min) {
            min = score;
        }
        sum += score;
    }

    return [min, max, sum];
}

bool hasAnyMatches(List<int> list,  Function(int) condition) {
    for (int item in list) {
        if (condition(item)) {
            return true;
        }
    }
    return false;
}
bool lessThanTen(int number) {
    return number < 10;
}

void main() {
  var numbers = [20, 19, 7, 12];
  hasAnyMatches(numbers, lessThanTen);
  var statistics = calculateStatistics([5, 3, 100, 3, 9]);
  print(statistics[2]);
  print(statistics[1]);
}
```

**Snippet 2.** Kotlin multiple function definitions and calls
```
fun calculateStatistics(scores: Array<Int>) : Triple(Int, Int, Int) {
    var min = scores[0]
    var max = scores[0]
    var sum = 0

    for(score in scores) {
        if(score > max) {
            max = score
        } else if (score < min) {
            min = score
        }
        sum += score
    }

    return Triple(min, max, sum)
}

fun hasAnyMatches(list: List<Int>, condition: (Int) -> Bool) : Bool {
    for (item in list) {
        if (condition(item)) {
            return true
        }
    }
    return false
}
func lessThanTen(number: Int) : Bool {
    return number < 10
}

fun main() {
	var numbers = listOf(20, 19, 7, 12)
	hasAnyMatches(numbers, lessThanTen)
	val statistics = calculateStatistics(arrayOf(5, 3, 100, 3, 9))
	println(statistics.sum)
	println(statistics.2)
}
```
## Same-language evaluation

In this case we have a single version of the application for each language, effectively generating a Type 1 clone between the applications. The table beelow hows the summay of theobtain results fort each language, comparing the program ith itself.

**Language** | **Total** | **Type 1** | **Type 2** | **Type 3** | **FP** | **FN** | **Precision** | **Recall**|
---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----
Kotlin | 195 | 135 | 50 | 10 | - | - | - | - |
Dart| 156 | 114 | 36 | 6 | 5 | 0 | 0.96 | 1 |


Two things come to mind when evaluating the single language cases for Dart.
First, the amount of detected clones is far larger than that of Kotlin; this is due to two main reasons. On the one hand the comparison in Dart is more fine-grained, detecting the clone type for each pair of code elements twice, yielding the double of clones than those present. For example, the function identifier `calculateStatistics` is detected as a clone of Type 1 with the identifier of function `lessThanTen`. However, when evaluating the identifier of function `lessThanTen`, this will be detected as a clone of identifier `calculateStatistics`, even though they are technically the same clone.
On the other hand, the clone evaluation occurs for every node on teh generated eCST, which for example, processes a clone for each element of the declaration of the `func lessThanTen(number: Int) : Bool ...` statement, but also for each of its parts, the parameters (variable types, and identifiers) for the function itself, yielding a larger nnumber of identified clones.

Second, the dart code detects a larger number of False Positives (FP). These occur by the miss classification of Type 3 clones, for example detecting 


## Cross-language evaluation

The analysis for Dart and Kotlin results in 4 correct Type 1 clones identifying the variables `main` function name, the number literal, and the `main` functions' parameter lists. A Type 2 clone is detected between the type declaration of the Dart code and the val declaration in the Kotlin case. FInally, a Type 3 clone is detected between . However, this clone is not of Type 3 as, contituing a False Positive.

The table below shows the summary of the results.

**Language** | **Total** | **Type 1** | **Type 2** | **Type 3** | **FP** | **FN** | **Precision** | **Recall**|
---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----
Dart v. Kotlin| 6 | 4 | 1 | 1 | 1 | 0 | 0.83 | 1 |
