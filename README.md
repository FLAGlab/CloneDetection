# CloneDetection
Detect clones in a cross-language setting

To generate the Parser, Lexer and Visitor classes please use ANTLR4,
```
conda create -n test python=3.8
pip install antlr4-python3-runtime
```

Download any grammar defined in ANTLR4 and run the following command,
```
java -cp antlr-4.7.1-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 -visitor ../clone_detection/grammars/XXX
```
