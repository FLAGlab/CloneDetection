# Out of Step

## Cross-language Clone Detection for Mobile Apps

This online appendix presents the complete evaluation results for our work on cross-language clone detection for mobile device programming languages: Dart, Kortlin, and Swift.

The experiment evaluation is structured in three parts.

1. Clone detection for the basic language features.
2. Clone detection using algorithms from a known (i.e., sorting algorithms) domain.
3. Clone detection on a corpus of mobile app repositories.

## Clone detection: Language Features

The first part of our evaluation consists on assuring Out of Step is able to detect clones effectively across the different language features and abstractions. To demonstrate this, we provide implementations demonstrating each of the features and manually translate them to the other languages, generating a high rate of Type-1 and Type-2 clones.

The first part of the evaluation in all cases conisders the comparison of programs using the same languagee base (comparing two versions of a program, or a version with itself) to evaluate the correctness of the algorithm in detecting clones for the specific language feature at hand.

### Data set description

The language features datasets consists of 7 categories as shown in the following table. For each of the categories we show the different files and clones to test.

Note that, while we define the programs for different programming languages, we focus the result and analysis to the mobile app programming languages Dart and Kotlin.

Feature | Cases | Evaluation | Languages
------ | -------------- | -------------- | --------------
[Variable declaration](./vars.md) | 1 | integer variable declaration | C++, Dart, Java, kotlin, Swift
[Function declaration](./funcs.md) | 1 | Stats calculation | C++, Dart, Java, Kotlin, Swift
[Conditionals](./conditionals.md) | 1 | Test variable and return | C++, Dart, Java, Kotlin, Swift
[Loops](./loops.md) | 2 | `for` loop <br><br> `while` loop | C++, Dart, Java, Kotlin, Swift
[Structures](./structs.md) | 2 | Structures <br> Enumerations | C++ Swift <br> C++, Dart, Java, Kotlin, Swift
[Classes](./classes.md) | 2 | 1-to-1 definition <br> Crossed definition | C++, Dart, Java, Kotlin, Swift <br> C++, Dart, Java, Kotlin, Swift

## Clone detection: Sorting Algorithms

Our second dataset is composed by different algorithms from the known domain of sorting. The objective of this evaluation is to assess the effectiveness of Out of Step to detect clones in small programs found in the wild.

Using a known domain enables us to validate the algorithms correctness, and to easily detect if the clones detected are true clones or false positives. This assessment is important to move forward to larger application domains with confidence about the validity of our results.

### Data set description

The implementation of the algorithms is taken from the [rosettacode.org](https://rosettacode.org/wiki/Rosetta_Code) website to eliminate any implementation bias. The implementations on RosettaCode are standard implementations submitted by different users and curated by the community.

<table>
<td> Algorithm </td> <td colspan=5> Languages (with LoC) </td>
<tr>
  <td>Bubble</td> <td> C++ </td> <td> Dart </td><td> Java </td> <td> Kotlin </td> <td> Swift </td>
</tr>
<tr>
  <td>Heap</td> <td> C++ </td> <td> Dart </td><td> Java </td> <td> Kotlin </td> <td> Swift </td>
</tr>
<tr>
  <td>Insertion</td> <td> C++ </td> <td> Dart </td><td> Java </td> <td> Kotlin </td> <td> Swift </td>
</tr>
<tr>
  <td>Quick</td> <td> C++ </td> <td> Dart </td><td> Java <br> Java </td> <td> Kotlin <br> Kotlin </td> <td> Swift </td>
</tr>
<tr>
  <td>Selection</td> <td> C++ </td> <td> Dart </td><td> Java </td> <td> Kotlin </td> <td> Swift </td>
</tr>
<tr>
  <td>Shell</td> <td> C++ </td> <td> Dart </td><td> Java </td> <td> Kotlin </td> <td> Swift </td>
</tr>
</table>

Evaluation [results](./sorting.md)

## Clone detection: Mobile Apps

The final set in our evaluation uses full fletch mobile apps of mid and large size

### Data set description

Our evalution data set consists of 116 mobile apps mined from GitHub and collected from student projects from a mobile app development (capstone) course. The following table shows the app distribution across language pairs.

**type** | **quantity** | **source of the repositories**
---- | ---- | ----
kotlin-dart | 50 | GitHub (4 Dart, 4 Kotlin), Students (21 Dart, 21 Kotlin)
kotlin-swift | 52 | GitHub (12 Kotlin, 12 Swift), Students (14 Kotlin, 14 Swift)
dart-swift | 14 | GitHub (3 Dart, 3 Swift), Students (4 Dart, 4 Swift)

We focus the evaluation on the 50 apps for Dart and Kotlin, as shown in the results section.

Evaluation [results](./mobile_apps.md) for Dart and Kotlin repositories.
