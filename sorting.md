# Sorting Algorithms Results

[back to main results](./index.md)

As an example of the different situations that may take place, we show the detailed results for bubble sort (Snippets \ref{lst:kotlin-bubblea} and \ref{lst:dart-bubblea} for Kotlin and Dart respectively), and insertion sort (Snippets \ref{lst:kotlin-insertionb} and 2 for Dart and Kotlin respectively). All clone types are present for these two algorithms.

**Snippet 1.** Bubble sort in Dart.
```
bubbleSort(List arr){
    bool swap = true;
    int len = arr.size;
    while(swap){
        swap = false;
        for(i in 0...len-1){
            if(arr[i] > arr[i+1]){
                int temp = arr[i];
                arr[i] = arr[i+1];
                arr[i + 1] = temp;
                swap = true;
            }
        }
    }
    return arr;
}
```

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

When comparing the sort algorithms (e.g., bubble sort), Out of Step is able to detect the function declarations as Type 1 clones. That is, the same similarities are found across the complete functions, given that the code and structure is the same, even if the programming language differs. This means, that a perfect transcription from one language to another results in exact clones.

**Snippet 3.** Insertion sort in Dart
```
insertionsort(List items){
    int len = items.size
    if (len==0 || len<2)
        return items;
    for (count in 1..len-1){
        int it = items[count];
        int i = count;
        while(i>0 && it<items[i-1]){
            items[i] = items[i-1];
            i = i-1;
        }
        items[i] = item;
    }
    return items;
}
```

**Snippet 4.** Insertion sort in Kotlin
```
fun insertionsort(items:List):List{
    val len = items.size
    if (len==0 || len<2)
        return items
    for (count in 1..len-1){
        val it = items[count]
        var i = count
        while(i>0 && it<items[i-1]){
            items[i] = items[i-1]
            i = i-1
        }
        items[i] = item
    }
    return items
}
```

The observed results from the execution of Out of Step effectively detects a Type 3 clone between `bubbleSort` and `insertionSort` functions including the parameter list `arr` and `items` from the function declaration. This is working as expected given that the structure and type of both functions coincides. Additionally, the auxiliary variables used in bubble sort, `swap` and `len`, are seen as clones for the `len` variable in insertion sort. This is a limitation given than they have the same structure and type nodes in the eCST.

**Algorithm** | **Total** | **Type 1** | **Type-2** | **Type 3** | **FPs**
---- | ---- | ---- | ---- | ---- | ----  
Bubble | 23 | 3 | 9 | 3 | 8
Insertion | 16 | 3 | 6 | 2 | 5
Heap | 129 | 33 | 39 | 16 | 41
Selection | 2 | 0 | 0 | 2 | 0
Quick | 25 | 1 | 10 | 4 | 10
Quick (functional) | 1 | 0 | 0 | 1 | 0  
Merge | 25 | 10 | 4 | 7 | 4

From the table, we can also note two interesting examples. The first relates to the two implementations of quick sort provided in Kotlin. The first implementation uses a recursive approach based on the pivot element, similar to the idea in the implementation in Dart. In this case we are able to identify the sort functions as Type 1, and find Type 2 and 3 clones in the implementation for the pivot definition and the recursive calls. However, when comparing the same Dart implementation to a Kotlin implementation that relies heavily on functional programming and higher-order functions, we note that only a Type 3 clone is found for the complete quick sort function. The other interesting case is that of the heap sort algorithm. In this case, we note Out of Step detects almost four times more clones than for the other sorting algorithms. This is due to two main reasons. First, the code base of the algorithm is at least twice as large of any of the other algorithms, opening the possibility to detect more clones. Additionally the code of the heap sort for both the Kotlin and Dart codebases is structured in 3 different functions (clones of each other). This causes Out of Step to analyze all 9 combinations between the defined functions, generating more clones between the two code versions. %of the sorting algorithm.

The single language case, in this example, tests that the structures are similar, detecting Type 3 clones among the different implementations of sorting.
