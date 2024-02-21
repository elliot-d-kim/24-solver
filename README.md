# 24-solver

Given 4 numbers, get 24 using only basic arithmetic! (or in this case, an algorithm.)

**Keywords: Recursion, Decision Trees, Algorithm design**

## Table of Contents
- [Introduction](#introduction)
- [Rules of 24](#rules-of-24)
- [The Naive Approach](#the-naive-approach)
- [The Algorithm: Grouping and Decision Trees](#the-algorithm-grouping-and-decision-trees)
- [Implementation](#implementation)
- [Future considerations](#future-considerations)

## Introduction

Where I work as a part-time coding instructor, there is a daily "24" to solve. It's a fun brain teaser, but I wanted to take it a step further and write an algorithm that would find solutions in a robust manner. Coming up with a theoretical algorithm reminded me of my Algorithms course in college and long evenings with friends sketching flow networks and DAGs on whiteboards -- though this algorithm may not be as complex in concept, implementing it proved to have its own fun challenges.

## Rules of 24

* Given: 4 natural numbers (integers > 0)
* Each number must be used _exactly_ once
* Use only arithmetic operations: +, -, ×, ÷

## The Naive Approach

It may seem straightforward enough to do something like this: 

Given the numbers `[2, 3, 4, 6]`, arrange all possible orderings of the numbers ...

```
2 _ 3 _ 4 _ 6
3 _ 2 _ 4 _ 6
3 _ 4 _ 2 _ 6
...
```

... and assign all possible arrangements of operations between the numbers. For the first ordering:

```
2 + 3 + 4 + 6
2 * 3 + 4 + 6
2 * 3 * 4 + 6
...
```

The issue here is that some solutions are only possible with grouping. For example, `[1, 3, 4, 8]` can only be solved via grouping: (8 - 4) * (3 - 1) = 24 (credit to [BGR360](https://github.com/BGR360) for this example).

## The Algorithm: Grouping and Decision Trees

My grouping approach is, at least in concept, a robust and relatively simple way to find all possible solutions.

The construction of any possible expression given _n_ numbers can be thought of as a **sequence of decisions**:
* Which two of the available values are you combining?
    * Which operation are you using to combine them?
* Repeat until you have a final expression (hopefully 24).

> ### Example: Understanding the Decision Space
>
> Ignoring for now the sub-decision of which operation to use, here is an example given `[a, b, c]` (just 3 numbers for simplicity):
> * Combine a and b: `[ab, c]`
>    * Combine ab and c: `[abc]` (Outcome 1)
> * Combine a and c: `[ac, b]`
>    * Combine ac and b: `[acb]` (Outcome 2)
> * Combine b and c: `[bc, a]`
>    * Combine bc and a: `[bca]` (Outcome 3)
>
> Notice when 3 values are available (`[a, b, c]`), there are 3 choices of combinations: this is 3 choose 2, if you are familiar with combinatorics. After 2 of the 3 values are combined (e.g., combining `a` and `b`), there are 2 values available (`[ab, c]`). When 2 values are available, there is only 1 (i.e., 2 choose 2) way to combine them (`[abc]`). As we can see, there are 3 * 1 = 3 possible outcomes
>
> When there are 4 values available to start, as is the case in classic 24, there are 4 choose 2 (i.e., 6) possible combinations. 6 choices that will leave you with 3 available values, which (as we saw previously) each have their own 3 choices, which each have 1 choice, means that there are 6 * 3 * 1 = 18 possible ways to combine the values. With the 4 arithmetic operations, there are 18 * 4 = **72 possible outcomes**. 
>

To solve 24, the outcomes as well as the construction of their expressions are necessary to evaluate whether each expression is equal to 24 and, if it is, reproduce the expression as a solution. A tree is an appropriate data structure here: not only can it hold the 72 possible outcomes at its leaves but also it retains all paths to the outcomes in its branches.

Finally, while in many cases there will be some equivalent expressions and repeated outcomes, this is a robust approach that will discover all possible solutions.

## Implementation

As I assessed various implementation approaches, I found that these were key considerations:
* Separating (a) building the solution space and (b) searching it
* Storing the various distinct aspects of solutions -- sequence of decisions, operands, operations, outcome of expression -- in a coherent data structure

Separating the building and searching of the solution space helped with "separation of concerns": once the solution space could be reliably built, focusing on ways to evaluate solutions within it came far more naturally.

Two main ways to store solutions were considered: a tree data structure and a multi-dimensional matrix. The appeal of a multidimensional matrix would be a simpler extraction of complete solution statements, where each "row" is a complete solution statement. On the other hand, extracting a complete solution statement from a tree requires tree traversal. Ultimately, the custom tree data structure turned out to be superior for storing the necessary information and representing the solution space intuitively.

Other implementation details:
* Sorting operands in descending order prior to applying arithmetic to prevent subtracting or dividing a smaller number by a larger number (but avoid dividing by 0)
* Removing any instances of non-integer quotients from solution space to prevent int-float bugs (which I later learned actually means this current implementation misses some edge cases)

## Future considerations

* Better visual representation of the solution tree
* Easier access to solver
    * No requirement to download file
    * GUI instead of CLI
* Edge cases: fractional expressions (refer to [@auntyellow's documentation](https://github.com/auntyellow/24) for examples)
* Cleaner, more principled implementation
* Eliminate similar expressions