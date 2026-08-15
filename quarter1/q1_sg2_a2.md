# Annex C
## Code Quality Assessment Worksheet

### Section: 9 - Pinatubo                                 Score:____________
### C# / Name: #16 Umayan, #17 Aguilar, #18 Atencio       Date: 08/15/2026


Instructions:

The problem: Finding the highest (Maximum) number from a given list of numbers.


| PseudoCode 1 | PseudoCode 2 |

| Algorithm FindMax1(numbers) | Algorithm FindMax2(numbers) |

|  max ← numbers[0] |    For i from 0 to length(numbers)-1bigger ← true |

|  For i from 1 to length(numbers)-1 |       For j from 0 to length(numbers)-1 |

|     If numbers[i] > max Then |          If numbers[j] > numbers[i] Then |

|        max ← numbers[i] |           bigger ← false |

|     EndIf |          EndIf |

|  EndFor |       EndFor |

|   Return max |       If bigger = true Then |

| EndAlgorithm |        Return numbers[i] |
|  |     EndIf |
|  |    EndFor |
|  | EndAlgorithm |

Algorithm FindMax2(numbers)

   For i from 0 to length(numbers)-1bigger ← true

      For j from 0 to length(numbers)-1

         If numbers[j] > numbers[i] Then

            bigger ← false

         EndIf

      EndFor

      If bigger = true Then

         Return numbers[i]

      EndIf

   EndFor

EndAlgorithm

Questions with Checklists
1. Efficiency
Which algorithm is faster when the list of numbers is very large? Why?

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________


PseudoCode 1

PseudoCode 2

walang check Does the algorithm use one loop or two nested loops?

walang check Does the algorithm repeat work unnecessarily?

walang check Which algorithm finishes in fewer steps?

walang check Does the algorithm use one loop or two nested loops?

walang check Does the algorithm repeat work unnecessarily?

walang check Which algorithm finishes in fewer steps?

Checklist to guide your answer:
2. Readability

Which algorithm is easier to understand at first glance? What makes it clearer?

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

Checklist to guide your answer:

PseudoCode 1

PseudoCode 2

walang check Are variable names meaningful (e.g., max vs. bigger)?

walang check Is the logic simple or complicated?

walang check Are there fewer lines of code?

walang check Are variable names meaningful (e.g., max vs. bigger)?

walang check Is the logic simple or complicated?

walang checkAre there fewer lines of code?

3. Maintainability
If you had to add a new feature (like finding both max and min), which algorithm would be easier to update? Why?

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

Checklist to guide your answer:

PseudoCode 1

PseudoCode 2

walang check Is the structure straightforward?

walang check Would adding new steps break the code easily?

walang check Is there less chance of errors when updating?

walang check Is the structure straightforward?

walang check Would adding new steps break the code easily?

walang check Is there less chance of errors when updating?

4. Testability
Which algorithm is easier to test with different inputs? Why?

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

Checklist to guide your answer:


PseudoCode 1

PseudoCode 2

walang check Can you test with small lists easily?

walang check Does the algorithm have fewer conditions to check?

walang check Is the output predictable and clear?

walang check Can you test with small lists easily?

walang check Does the algorithm have fewer conditions to check?

walang check Is the output predictable and clear?


5. Security
Imagine the input list comes from a user. What should the algorithm check to avoid errors or misuse?

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

Checklist to guide your answer:

PseudoCode 1

PseudoCode 2

walang check Does the algorithm check if the list is empty?

walang check Does it handle invalid inputs (like letters instead of numbers)?

walang check Does it avoid crashing when inputs are unusual?

walang check Does the algorithm check if the list is empty?

walang check Does it handle invalid inputs (like letters instead of numbers)?

walang check Does it avoid crashing when inputs are unusual?

 

6. Final Answer
Based on your answers from 1 to 5, which one is the better algorithm that you will use to solve the problem of finding the highest number? Why? Summarize your answer

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________
