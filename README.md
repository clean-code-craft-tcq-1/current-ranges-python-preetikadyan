# Test Driven Ranges

This exercise extends the [Battery Monitoring] use-case.

The charging current varies during the process of charging.
We need to capture the range of current measurements -
what range of currents are most often encountered while charging.

> **DO NOT** jump into implementation! Read the example and the starting task below.

## Example

### Input

Consider a set of periodic current samples from a charging session to be:
`3, 3, 5, 4, 10, 11, 12`

### Functionality

The continuous ranges in there are: `3,4,5` and `10,11,12`.

The task is to detect the ranges and
output the number of readings in each range.

In this example,

- the `3-5` range has `4` readings
- the `10-12` range has `3` readings.

### Output

The expected output would be:

```
Range, Readings
3-5, 4
10-12, 3
```

## Tasks

Start test-driven development:

1. Establish quality parameters for your project: What is the maximum complexity you would allow? How much duplication would you consider unacceptable? What is the coverage you'll aim for?
Adapt/adopt/extend the `yml` files from one of your workflow folders.

  - I have limited the complexity to 4 CCN and for this I have added **limit-complexity.yml** file to the workflow
  - Duplication is covered beyond 3 lines and for this I have added **no-dups.yml** file to the workflow
  - I have added **main-workflow.yml** file to start the workflow from the file **current_range.test.py**
  - As of now I have not provided code coverage
  
![image](https://user-images.githubusercontent.com/13776900/116265257-96b14680-a798-11eb-8ee8-d33d971b91b4.png)

1. Write the smallest possible failing test.

1. Write the minimum amount of code that'll make it pass.

**Flow chart of the logic implemented**

![image](https://user-images.githubusercontent.com/13776900/116407945-e7d04180-a84f-11eb-8065-aafb3463d62d.png)


1. Write the next failing test.

Implement one failing test and at least one passing test:

-  **passing_test_range_and_count()** is the function having the **passing** test
-  **passing_test_range_and_count** is the function having the *failing** test

![image](https://user-images.githubusercontent.com/13776900/116265664-f0b20c00-a798-11eb-9af0-1aa814c9cdc5.png)

