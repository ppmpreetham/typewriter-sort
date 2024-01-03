# typewriter-sort
A sorting algorithm has a time complexity of $`O(n)`$ and in the worst case, it has a time complexity of $`O( \infty )`$.
Yes, it's worse than Bogosort, Bozosort and Bogobogosort.

The algorithm was made as a joke on a search to make the worst algorithm of all time.
The usage of two ```while``` loops makes it impossible to give the desired output in time.

## Usage
### Python
```python
import {typewriter_sort} from '@Preetham-ai/typewriter-sort'
test_array = [7,5,338,46,21,2,9]
print(typewriter_sort(test_array))
```
### Rust
```rust
fn main() {
    let input_list = vec![/*Array goes here*/];
    let result = typewriter_sort(&input_list);
    println!("{:?}", result);
}```