# DSA-Assignment:Stack and Queue Implementation Using Linked List
This project implements Stack and Queue data structures using a Linked List in Python. It provides hands-on practice with fundamental data structures and demonstrates the advantages of dynamic memory management.
How to Run the Program

Steps to Run
1. ### Clone the Repository: ###
Download the project files from GitHub by running:
```bash
git clone https://github.com/your-username/stack-queue-linked-list.git
cd stack-queue-linked-list
 ```
2. ### Run the Program: ###
Execute the specific scripts to test the implementations:

 #### Stack Implementation:###
```bash
python stack.py
```
#### Queue Implementation:
bash
python queue.py

Purpose of the Code
The goal of this project is to:

.Implement Stack and Queue using Linked Lists, providing a dynamic alternative to array-based implementations.

.Reinforce concepts of linked lists, including node creation, pointer manipulation, and efficient memory usage.

.Demonstrate efficient handling of key operations such as insertion and deletion.

## Definitions:
## Stack: 
     A data structure that operates on the LIFO (Last In, First Out) principle. Operations include:
##### .`Push `:  Add an element to the top.
 
##### .`Pop`: Remove the top element.
 
##### .`Peek`: View the top element without removing it.
 
## Queue:
     A data structure that operates on the FIFO (First In, First Out) principle. Operations include:
 ##### `.Enqueue`  : Add an element to the rear.
 
##### ` .Dequeue`: Remove an element from the front.
 
##### `.Peek`: View the front element without removing it.
 
## Time Complexity ##
#### Operation	 Stack  Queue	 Explanation
   `.Insertion`	O(1) (Push)	O(1) (Enqueue)	Insertions are performed at the head for Stack and at the rear for Queue, making it constant time.
   
   `.Deletion`	O(1) (Pop)	O(1) (Dequeue)	Deletions are performed at the head in both structures, ensuring efficient removal.
   
  `.Access (Peek)`	O(1)	O(1)	Peek operations directly access the top (Stack) or front (Queue) element without traversing the list.
  
The use of Linked List ensures that all operations are performed in constant time by maintaining pointers to the head (and tail for Queue).
