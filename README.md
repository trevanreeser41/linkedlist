# Assignment: LinkedLists

Write a dynamic linked list class that has the following features:

1. Track its own size using a class variable, independent of the actual memory allocated.
1. Initialize with a null head.

The API for your class is provided in `linkedlist_api.py`.  Please translate this API to your language, and maintain the public names and parameters wherever possible.

To give you additional help, I've also left private methods in the API class; these can be deleted or modified as you wish.



## Getting Started

I suggest that you create and test one method at a time as you work through `add`, `insert`, `set`, `get`, `delete`, and `swap`.  Test your linked list class in a separate file named `main.py` (alter for your language).

For example, as your program the `insert` function, ensure it handles the following:

* Inserting when your head is null.
* Inserting when your list has data.
* Inserting with an invalid index (< 0 or >= the current size).

Regarding this last point, your class should throw an exception when the index is out of bounds.  This exception will be caught in your main program.


## Printing the Structure

In order to grade your assignment, we need to be able to see the internal state of your linked list class.  Add a `debug_print` method to your class that prints the following line:

`11 >>> a, e, r, o, I, o, d, u, s, a, u`

In the line above:

* 11 is the current (logical) size of the linked list.
* a, e, r, o, and so on are the values in the linked list nodes.


## The File of Instructions

The assignment comes with a CSV file named `data.csv`.  This file contains the instructions you should run on your LinkedList class.  It will assist in grading your work.

In your `main.py` file, read `data.csv` and interate through the commands.  You can either use a CSV library in your language, or you can simply split each line by comma (there are no commas in the values).  On each line, call the appropriate method in your LinkedList class.   The commands are as follows:

* `CREATE` creates an instance of your linked list class.
* `DEBUG` prints the debug line to the console.
* `ADD` adds a value to the end of the linked list.
* `SET` sets a value at a given index in the linked list.
* `GET` retrieves a value at a given index in the linked list.  Your main program should print this value to the console.
* `DELETE` removes a value at the given index in the linked list.  Be sure to shift all elements down to fill the empty slot.
* `INSERT` inserts a value at the given index in the linked list.  Be sure to shift all elements up to make an empty slot.
* `SWAP` swaps two values at the given indices in the linked list.

Each time you run a command, print the zero-based file line number followed by the command, in this format:

`LineNum:FileLine`

Note that some commands in the file are meant to fail, such as trying to insert a value beyond the bounds of the linked list.  You need to wrap each call in a try/catch exception block and print the following when this occurs:

`Error: <msg from your class here>`

See the example output below for a comprehensive list of what your output should look like.

## Example

The `data_example.csv` file contains an example set of instructions you can work with.  I suggest you cut this file down to one or two instructions at a time as you develop rather than try to run the entire file at once.

I've included the output of my assignment in the `output_example.txt` file so you can see exactly how your output should look.  Note the following in the file:

* Line 1 shows an empty, initial linked list with no nodes.
* Line 18 is a `GET`, so it has an 's' on the next line.
* Line 19 caused an error, so we see the exception text on the next line.



## Submitting the Assignment

Zip the following files and submit on https://caplearning.net

```
main.py
linked list.py
data.csv
output.txt
(add any additional files needed to run your program)
```
