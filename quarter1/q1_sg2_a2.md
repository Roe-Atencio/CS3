# Annex C
## Code Quality Assessment Worksheet

### Section: Pinatubo                                         Score:____________
### C# / Name: #16 Umayan, #17 Aguilar, #19 Atencio Date:     August 16, 2026


Instructions:

The problem: Finding the highest (Maximum) number from a given list of numbers.
| PseudoCode 1                        | Pseudocode 2                           |
| ----------------------------------- | -------------------------------------- |
| Algorithm FindMax1(numbers)         | Algorithm FindMax2(numbers)            |
|   max ← numbers[0]                  |   For i from 1 to length(numbers)-1    |
|   For i from 1 to length(numbers)-1 |     For j from 0 to length(number)-1   |
|     If numbers[i] > max Then        |       If numbers[j] > numbers [i] Then |
|       max ← numbers[i]              |         bigger ← false                 |
|     EndIf                           |       EndIf                            |
|   EndFor                            |     EndFor                             |
|   Return max                        |     If bigger = true Then              |
| EndAlgorithm                        |       Return numbers [i]               |
|                                     |     EndIf                              |
|                                     |   EndFor                               |
|                                     | EndAlgorithm                           |

Questions with Checklists

1. Efficiency
Which algorithm is faster when the list of numbers is very large? Why?

Algorithm 1 is significantly faster when dealing with lists that contain large numbers because it only uses one loop and has fewer lines of code as compared to algorithm 2.

| PseudoCode 1                                             | Pseudocode 2                                             |
| -------------------------------------------------------- | -------------------------------------------------------- |
| [/] Does the algorithm use one loop or two nested loops? | [ ] Does the algorithm use one loop or two nested loops? |
|                                                          |                                                          |
| [ ] Does the algorithm repeat work unnecessarily?        | [/] Does the algorithm repeat work unnecessarily?        |
|                                                          |                                                          |
| [/] Which algorithm finishes in fewer steps?             | [ ] Which algorithm finishes in fewer steps?             |
Checklist to guide your answer:

2. Readability

Which algorithm is easier to understand at first glance? What makes it clearer?

Algorithm 1 does not require much thinking to understand the code. It is much shorter and the logic used is simple.

| PseudoCode 1                                              | Pseudocode 2                                              |
| --------------------------------------------------------- | --------------------------------------------------------- |
| [/] Are variable names meaningful (e.g., max vs. bigger)? | [ ] Are variable names meaningful (e.g., max vs. bigger)? |
|                                                           |                                                           |
| [Simple] Is the logic simple or complicated?              | [Complicated] Is the logic simple or complicated?         |
|                                                           |                                                           |
| [/] Are there fewer lines of code?                        | [ ] Are there fewer lines of code?                        |
Checklist to guide your answer:

3. Maintainability
If you had to add a new feature (like finding both max and min), which algorithm would be easier to update? Why?

Algorithm 1 

| PseudoCode 1                                       | Pseudocode 2                                       |
| -------------------------------------------------- | -------------------------------------------------- |
| [ ] Is the structure straightforward?              | [ ] Is the structure straightforward?              |
|                                                    |                                                    |
| [ ] Would adding new steps break the code easily?  | [ ] Would adding new steps break the code easily?  |
|                                                    |                                                    |
| [ ]  Is there less chance of errors when updating? | [ ]  Is there less chance of errors when updating? |
Checklist to guide your answer:
