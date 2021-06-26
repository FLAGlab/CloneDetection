insertionsort(List items){
    int len = items.size
    if (len==0||len<2){
        return items;
    }
    for (count in 1..len-1){
        int it = items[count];
        int i = count;
        while(i>0&&it<items[i-1]){
            items[i] = items[i-1];
            i = i-1;
        }
        items[i] = item;
    }
    return items;
}