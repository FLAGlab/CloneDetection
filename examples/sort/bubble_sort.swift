class VideoMode {
    var resolution = Resolution()
    var interlaced = false
    var frameRate = 0.0
    var name: String?
}
struct Resolution {
    var width = 0
    var height = 0
}
func bubbleSort(_ arr: [Int]) -> [Int] {
    var dataSet = arr
    let last_position = dataSet.count - 1
    var swap = true
    while swap == true {
        swap = false
        for i in 0..<last_position {
            if dataSet[i] > dataSet[i + 1] {
                let temp = dataSet [i + 1]
                dataSet [i + 1] = dataSet[i]
                dataSet[i] = temp

                swap = true
            }
        }
    }
    return dataSet
}