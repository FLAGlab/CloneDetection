func sum_range(_ start: Int, _ end: Int) -> Int {
    var sum : Int
    sum = 0
    var current = start
    while current < end {
        sum += current
        current += 1
    }
    return sum
}

print("\(sum_range(0,10))")