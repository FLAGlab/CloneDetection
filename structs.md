# Structure and Enumeration Definition

[back to main results](./index.md)

## Enumerations

We begin with the definition of enumerations taking the prototypical example of playing cards for both Dart and Kotlin. In this case, we define the enumerations (card rank and suit) and an accompanying description function for each of them.
The following shows an extract of the definition in both Dart and Kotlin

**Snippet 1.** Dart enumeration declaration and use
```
enum Rank {
    ACE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN,
    JACK, QUEEN, KING
}

rankDescription(Rank r) {
  switch(r) {
      case Rank.ACE:
          return "ace";
      case Rank.JACK:
          return "jack";
      case Rank.QUEEN:
          return "queen";
      case Rank.KING:
          return "king";
      default:
          return (r.index + 1).toString();
  }
} 
```

**Snippet 2.** Kotlin enumeration definition and use
```
enum class Rank {
    ACE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN,
    JACK, QUEEN, KING
}

fun rankDescription(r : Rank) : String {
    return when(r) {
        Rank.ACE ->  "ace"
        Rank.JACK ->  "jack"
        Rank.QUEEN ->  "queen"
        Rank.KING ->  "king"
        else -> (r.ordinal + 1).toString()
    }
}
```

### Single language evaluation

The clone evaluation returns a large number of clones given the size of the files, and the repetitive structure of the two enumeration definitions correctly detecting all Type 1 clones in all different locations in the Dart code.
The large number of Type 2 clones in Dart corresponds to the identification of the enumeration members as clones of each other, which is correct, as they have the same node type, but different values. However, the algorithms also detects, incorrectly, nodes corresponding to the enumeration definition (e.g., `Rank`) with nodes of their values (e.g., `ACE`) or function definition nodes, generating 21 FPs.
The detected Type 3 clones in Dart correspond to Universal nodes detected on across the tree. From the detection algorithm it is not clear whether these nodes are in different locations of the tree, and therefore we classifythem as FPs. 

A similar situation takes place in the analysis of Kotlin code. All Type clones are correctly detected. Type 2 clones are present in large numbers due to the crossing values of the enumerations with 10 FPs given by the confusion of enumeration declarations with their values and function definitions, as before. However, note that there are far less detected clones due to the additional typing information existing in Kotlin. FInally, Type 3 clones are detected between the same types of universal nodes in 6 cases.

**Language** | **Total** | **Type 1** | **Type 2** | **Type 3** | **FP** | **FN** | **Precision** | **Recall**|
---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----
Dart | 178 | 110 | 50 | 18 | 39 | 0 | 0.78 | 1 |
Kotlin | 156 | 102 | 36 | 18 | 16 | 0 | 0.89 | 1 |

### Cross-language evaluation

In the cross-language case, comparing the Dart and Kotlin versions of the program we identify a larger set of Type 2 and Type 3 clones. Type 1 clones correspond to teh correct identification of the functions defined to manage the enums, the enum definitions and their use, as well as the identification of most of the enum literals, although some appear missing explicitly (12 FNs). The large number of Type 2 clones corresponds to the crossing between the functions. However, many of the identify clones, 26, are missclasified as they are detecting the enum literal to be a clone of other literals (e.g., suit names, vars, that do not correspond). Type 3 clones, identify many (21) of the same universal nodes as clones, which could be Type 1 clones, though no information about their content is provided so is not possible to verify.


**Language** | **Total** | **Type 1** | **Type 2** | **Type 3** | **FP** | **FN** | **Precision** | **Recall**|
---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----
Dart v. Kotlin| 103 | 22 | 53 | 28 | 47 | 12 | 0.49 | 0.79 |


## Structure evalluation

With respect to the definition of structures, we take into account the language that do provide an explicit definition of structures as C++ or Swift. The following snippet shows the structure definition example in Swift for a `Card`, using the enumerations from the previous section.

**Snippet 3.** Swift definition of structures
```
struct Card {
    var rank: Rank
    var suit: Suit
    func simpleDescription() -> String {
        return "The \(rank.simpleDescription()) of \(suit.simpleDescription())"
    }
}
let threeOfSpades = Card(rank: .three, suit: .spades)
let threeOfSpadesDescription = threeOfSpades.simpleDescription()
```

### Single language evaluation

As structures are not presente in every language, and in particular not present in Dart or Kotlin. We omit the results for this language feature.


