# Out of Step
Out of Step is a clone detection tool for cross-language settings focused on modern programming languages (e.g., Dart, Kotlin, Swift) and new application domains (i.e., mobile apps).

The documentation about Out of Step, its features, and node description is available on the project's wiki pages

## Quick Usage

To generate the Parser, Lexer and Visitor classes please use ANTLR4,
```
conda create -n test python=3.8
pip install antlr4-python3-runtime
```

Download any grammar defined in ANTLR4 and run the following command,
```
java -cp antlr-4.9-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 -visitor ../clone_detection/grammars/XXX/XXX.g4
```

```
python -m clone_detection --f examples/sort/bubble_sort.kt examples/sort/bubble_sort.dart
```
