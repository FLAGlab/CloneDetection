bubbleSort(List array){
    bool swap = true;
    int len = arr.size;
    while(swap){
        swap = false;
        for(i in 0...len-1){
            if(array[i] > array[i+1]){
                int temp = array[i];
                array[i] = array[i+1];
                array[i + 1] = temp;
                swap = true;
            }
        }
    }
    return arr;
}