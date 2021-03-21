const fib = (n) =>{
    if (n <= 2) return 1;
    return fib(n-1) + fib(n-2);
}

const fibm = (n,memo={}) =>{
    if (n in memo) return memo[n];
    if (n <= 2) return 1;
    memo[n] = fibm(n-1, memo) + fibm(n-2, memo);
    return memo[n]
}

console.log(fibm(40));