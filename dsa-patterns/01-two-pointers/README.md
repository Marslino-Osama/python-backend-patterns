# Two Pointers

## Core Idea

Two Pointers means using two indexes to move through an array or string in a controlled way.

Instead of checking every possible pair or repeatedly scanning the same data, you keep two positions and move one or both of them based on a rule.

The goal is usually to reduce an `O(n²)` brute-force solution into `O(n)` or `O(n log n)` if sorting is required first.

## The Brute-Force Problem

Many problems ask you to compare pairs, remove items, check symmetry, or find a valid combination.

The naive solution often looks like this:

```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        # check pair
```

This checks too many combinations. If `n = 100,000`, `O(n²)` is too slow.

Two Pointers avoids unnecessary checks by using information from the input, usually sorted order, symmetry, or in-place movement.

## What This Pattern Optimizes

Two Pointers removes repeated work.

Examples:

- In a sorted array, if the sum is too small, moving the right pointer left will not help. Move `left` right.
- In a palindrome check, compare both ends once and move inward.
- In in-place filtering, use one pointer to scan and one pointer to write valid values.

## Main Types

### 1. Opposite Direction Pointers

Use when working from both ends toward the middle.

Common uses:

- Palindrome checks
- Pair sum in a sorted array
- Container/water problems
- Reversing arrays/strings

Template shape:

```python
left = 0
right = len(nums) - 1

while left < right:
    # inspect nums[left] and nums[right]

    if condition_is_met:
        return result
    elif need_larger_value:
        left += 1
    else:
        right -= 1
```

### 2. Same Direction Pointers

Use when both pointers move left to right, usually at different speeds.

Common uses:

- Remove duplicates
- Filter values in-place
- Fast/slow pointer logic
- Merging-like scans

Template shape:

```python
slow = 0

for fast in range(len(nums)):
    if should_keep(nums[fast]):
        nums[slow] = nums[fast]
        slow += 1
```

### 3. Multiple Pointers After Sorting

Use when a problem asks for pairs/triples and sorting makes movement predictable.

Common uses:

- 3Sum
- 4Sum
- Closest sum problems

Template shape:

```python
nums.sort()

for i in range(len(nums)):
    left = i + 1
    right = len(nums) - 1

    while left < right:
        current = nums[i] + nums[left] + nums[right]

        if current == target:
            # record answer
            left += 1
            right -= 1
        elif current < target:
            left += 1
        else:
            right -= 1
```

## When to Use

Use Two Pointers when:

- The input is sorted or can be sorted.
- You need to find a pair/triple.
- You compare both ends of an array/string.
- You need in-place modification.
- You need to remove duplicates.
- You need to reverse or partition data.
- A nested loop seems obvious but too slow.

## LeetCode Recognition Signs

Look for phrases like:

- “sorted array”
- “in-place”
- “remove duplicates”
- “palindrome”
- “two numbers”
- “pair”
- “triplets”
- “subsequence”
- “container”
- “reverse”
- “move zeroes”

## Core Invariants

Different Two Pointer problems have different invariants.

### Opposite Direction

```text
The answer, if it exists, is still inside the range [left, right].
```

### In-Place Filtering

```text
Everything before slow is already valid.
fast scans every element exactly once.
```

### Palindrome

```text
All characters outside [left, right] have already matched.
```

## Complexity

| Approach | Time | Space |
|----------|------|-------|
| Brute force pair checking | O(n²) | O(1) |
| Two pointers on sorted input | O(n) | O(1) |
| Sort + two pointers | O(n log n) | Depends on sorting |
| In-place fast/slow | O(n) | O(1) |

## Common Mistakes

### Moving the Wrong Pointer

In sorted pair-sum problems:

```text
sum too small  -> move left right
sum too large  -> move right left
```

Do not move both pointers unless you have found a valid pair or the problem logic requires it.

### Forgetting Sorting Requirement

Two Pointers for pair sums usually depends on sorted order. If the array is unsorted, either sort it or use a hash map depending on the problem.

### Wrong Loop Condition

Use:

```python
while left < right:
```

for pair/symmetric problems.

Using `<=` can compare the same element with itself by mistake.

### Skipping Duplicates Incorrectly

For problems like 3Sum, skip duplicates carefully after sorting. Skipping too early can remove valid answers.

### Returning the Wrong Thing

Some problems ask for:

- indices
- values
- count
- modified array length
- boolean

Read the output requirement carefully.

## Reflection Questions

After solving a Two Pointers problem, answer:

1. Was the input sorted? If not, did I sort it?
2. What did each pointer represent?
3. What was the invariant?
4. Why was it safe to move that pointer?
5. What edge case broke my first attempt?
6. What is the time and space complexity?
