
/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */
 function createCounter(start) {
  let count = start;
  return function() {
    return count++;
  }
}