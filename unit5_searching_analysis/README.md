# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compared linear search and binary search by implementing both
algorithms in Python and testing them against small, large, and edge-case
datasets.

## Learning Objectives

- Implemented linear search
- Implemented binary search
- Compared performance
- Analyzed algorithm efficiency

## Requirements

1. Tested both algorithms on a small sorted dataset.
2. Tested both algorithms on a large sorted dataset with 500,000 values.
3. Demonstrated edge cases including an empty list, a single-element list, a
   first-position match, and a last-position match.
4. Analyzed performance using comparison counts and elapsed time.
5. Created a real-world interpretation for searching course records.

## Implementation Summary

I implemented `linear_search` so it inspected each list value from beginning to
end and returned the matching index or `-1` when the target was missing. I
implemented `binary_search` so it worked on sorted lists by checking the middle
value, then removing either the left half or the right half of the remaining
search range.

I also added helper functions that counted comparisons and printed clearer
results for each test case. The output showed the dataset size, target value,
result index, comparison count, and elapsed time for each algorithm.

## Performance Analysis

The small dataset confirmed that both algorithms found existing values and
returned `-1` for missing values. The large dataset showed the efficiency
difference more clearly. Linear search checked values one at a time, so it
needed 499,001 comparisons to find `998000` near the end of the list and
500,000 comparisons for the missing value `999999`. Binary search found or
rejected those same values in 19 comparisons because each step cut the remaining
search range approximately in half.

## Edge Case Results

The empty-list test returned `-1` for both algorithms because there were no
values to inspect. The single-element test returned index `0` when the only
value matched the target. The first-position and last-position tests showed how
linear search performed best when the target appeared early and worst when the
target appeared near the end.

## Real-World Search Scenario

This behavior matched a course-registration search scenario. A small unsorted
list of recently viewed courses could have been searched with linear search
because the setup was simple and the list was short. A large sorted course
catalog would have benefited from binary search because students could locate a
course number with far fewer comparisons, as long as the catalog had already
been sorted.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial
discussion post in LEO.

Your reflection should be approximately 150-200 words and address the following
questions:

I learned how linear search and binary search solved the same problem with very
different strategies. Linear search checked each item in order, so its logic was
simple and worked even when the data was not sorted. Binary search required
sorted data, but it reduced the search range by half after each comparison, which
made it much faster on larger datasets. The main challenge was making the
performance difference visible in the output because small lists completed too
quickly for timing alone to explain much. I overcame that by adding comparison
counts along with elapsed time, which made the efficiency difference easier to
interpret. In real-world scenarios, I would have used linear search for short,
temporary, or unsorted data where setup time mattered more than speed. I would
have used binary search for large sorted collections, such as course catalogs,
student ID lists, or inventory records. The tradeoff was that binary search was
more efficient only when the data had already been sorted, while linear search
was more flexible but slower as the list grew.
