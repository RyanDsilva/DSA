# Arrays

## Time Complexity Of Common Operations

| Operation             | Big-O     | Note                                                                                                 |
| --------------------- | --------- | ---------------------------------------------------------------------------------------------------- |
| Access                | O(1)      |                                                                                                      |
| Search                | O(n)      |                                                                                                      |
| Search (sorted array) | O(log(n)) |                                                                                                      |
| Insert                | O(n)      | Insertion would require shifting all the subsequent elements to the right by one and that takes O(n) |
| Insert (at the end)   | O(1)      | Special case of insertion where no other element needs to be shifted                                 |
| Remove                | O(n)      | Removal would require shifting all the subsequent elements to the left by one and that takes O(n)    |
| Remove (at the end)   | O(1)      | Special case of removal where no other element needs to be shifted                                   |

## Things To Look Out For

- Clarify if there are duplicate values in the array. Would the presence of duplicate values affect the answer? Does it make the question simpler or harder?
- When using an index to iterate through array elements, be careful not to go out of bounds.
- Be mindful about slicing or concatenating arrays in your code. Typically, slicing and concatenating arrays would take O(n) time. Use start and end indices to demarcate a subarray/range where possible.

## Corner Cases

- Empty sequence
- Sequence with 1 or 2 elements
- Sequence with repeated elements
- Duplicated values in the sequence

## Common Terms

- **Subarray** - A range of contiguous values within an array.
  - Example: given an array `[2, 3, 6, 1, 5, 4]`, `[3, 6, 1]` is a subarray while `[3, 1, 5]` is not a subarray.
- **Subsequence** - A sequence that can be derived from the given sequence by deleting some or no elements without changing the order of the remaining elements.
  - Example: given an array `[2, 3, 6, 1, 5, 4]`, `[3, 1, 5]` is a subsequence but `[3, 5, 1]` is not a subsequence.

## Techniques

- **Sliding Window** - In the sliding window technique, two pointers usually move in the same direction and never overtake each other. Each element is visited at most twice. Keep increasing the window from the right till the condition is met, then reduce the window from the left to check whether the condition is still met. If yes, decrease further, else, increase from the right again.
