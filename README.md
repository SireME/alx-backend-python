# ALX Backend Python Project

Welcome to the ALX Python Backend project! This repository contains solutions and implementations for various Python tasks related to variable annotations and complex types asyncronous programming and more. The project is structured into different directories, each corresponding to a specific task.

## Project Structure

- **0x00-python_variable_annotations**: Directory containing the Python scripts for the tasks related to variable annotations.
- **0x01-python_async_function**: Directory containing the Python scripts for tasks related to asynchronous programming.

## Table of Contents

1. [Variable Annotations Tasks Overview](#variable-annotations-tasks-overview)
    - [Task 0 - Basic annotations - add](#task-0---basic-annotations---add)
    - [Task 1 - Basic annotations - concat](#task-1---basic-annotations---concat)
    - [Task 2 - Basic annotations - floor](#task-2---basic-annotations---floor)
    - [Task 3 - Basic annotations - to string](#task-3---basic-annotations---to-string)
    - [Task 4 - Define variables](#task-4---define-variables)
    - [Task 5 - Complex types - list of floats](#task-5---complex-types---list-of-floats)
    - [Task 6 - Complex types - mixed list](#task-6---complex-types---mixed-list)
    - [Task 7 - Complex types - string and int/float to tuple](#task-7---complex-types---string-and-int-float-to-tuple)
    - [Task 8 - Complex types - functions](#task-8---complex-types---functions)
    - [Task 9 - Let's duck type an iterable object](#task-9---lets-duck-type-an-iterable-object)

2. [Async Function Tasks Overview](#async-function-tasks-overview)
    - [Task 0 - The basics of async](#task-0---the-basics-of-async)
    - [Task 1 - Let's execute multiple coroutines at the same time with async](#task-1---lets-execute-multiple-coroutines-at-the-same-time-with-async)
    - [Task 2 - Measure the runtime](#task-2---measure-the-runtime)
    - [Task 3 - Tasks](#task-3---tasks)
    - [Task 4 - Tasks](#task-4---tasks)

3. [Directory Structure](#directory-structure)
4. [Getting Started](#getting-started)
5. [Usage](#usage)
6. [Contributing](#contributing)
7. [License](#license)

## Variable Annotations Tasks Overview

1. **Task 0 - Basic annotations - add**
   - File: `0-add.py`
   - Write a type-annotated function `add` that takes two float arguments and returns their sum as a float.

2. **Task 1 - Basic annotations - concat**
   - File: `1-concat.py`
   - Write a type-annotated function `concat` that concatenates two strings.

3. **Task 2 - Basic annotations - floor**
   - File: `2-floor.py`
   - Write a type-annotated function `floor` that takes a float as an argument and returns its floor as an integer.

4. **Task 3 - Basic annotations - to string**
   - File: `3-to_str.py`
   - Write a type-annotated function `to_str` that converts a float to its string representation.

5. **Task 4 - Define variables**
   - File: `4-define_variables.py`
   - Define and annotate specific variables with specified values.

6. **Task 5 - Complex types - list of floats**
   - File: `5-sum_list.py`
   - Write a type-annotated function `sum_list` that takes a list of floats as an argument and returns their sum as a float.

7. **Task 6 - Complex types - mixed list**
   - File: `6-sum_mixed_list.py`
   - Write a type-annotated function `sum_mixed_list` that takes a list of integers and floats and returns their sum as a float.

8. **Task 7 - Complex types - string and int/float to tuple**
   - File: `7-to_kv.py`
   - Write a type-annotated function `to_kv` that takes a string and an int or float and returns a tuple.

9. **Task 8 - Complex types - functions**
   - File: `8-make_multiplier.py`
   - Write a type-annotated function `make_multiplier` that takes a float as an argument and returns a function that multiplies a float by the given multiplier.

10. **Task 9 - Let's duck type an iterable object**
    - File: `9-element_length.py`
    - Annotate the parameters and return values of the function `element_length`.

## Async Function Tasks Overview

### Task 0 - The basics of async
- File: `0-basic_async_syntax.py`
- Write an asynchronous coroutine that takes in an integer argument (`max_delay`, with a default value of 10) named `wait_random` that waits for a random delay between 0 and `max_delay` (inclusive) seconds and eventually returns it.

### Task 1 - Let's execute multiple coroutines at the same time with async
- File: `1-concurrent_coroutines.py`
- Import `wait_random` from the previous python file and write an async routine called `wait_n` that takes in 2 int arguments (`n` and `max_delay`). You will spawn `wait_random` `n` times with the specified `max_delay`. `wait_n` should return the list of all the delays (float values) in ascending order.

### Task 2 - Measure the runtime
- File: `2-measure_runtime.py`
- Import `wait_n` from the previous file and create a `measure_time` function that measures the total execution time for `wait_n(n, max_delay)` and returns `total_time / n`.

### Task 3 - Tasks
- File: `3-tasks.py`
- Import `wait_random` from `0-basic_async_syntax` and write a function `task_wait_random` that takes an integer `max_delay` and returns an `asyncio.Task`.

### Task 4 - Tasks
- File: `4-tasks.py`
- Take the code from `wait_n` and alter it into a new function `task_wait_n`. The code is nearly identical to `wait_n` except `task_wait_random` is being called.
