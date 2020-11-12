function abs(x) {
    console.log('in abs');
    console.log(x);
    if (x >= 0) {
        return x;
    } else {
        return -x;
    }
}


console.log(abs(-10));