fun sum_range(start: Int, end: Int) -> Int {
    var sum : Int
    sum = 0
    var current = start
    while current < end {
        sum += current
        current++
    }
    return sum
}

fun main() {
    print("\(sum_range(0,10))")
}