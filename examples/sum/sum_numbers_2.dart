int sumRange(int start, int end) {
    var sum = 0;
    for(int i = start; i < end; i++) {
        sum += i;
    }
    return sum;
}
void main() {
    print('${sumRange(0, 10)}');
}