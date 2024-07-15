#UNDERSTANDING IN PROGRESS IF SOMEONE COULD EXPLAIN IT WOULD BE GREATLY APPRECIATED
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
 #https://youtu.be/RKr9yw1LPNk?si=QESE2iE0CC0-kG8h
 #https://youtu.be/LUm2ABqAs1w?si=a8f22HdcZD8N68Ej
 #https://youtu.be/PvrxZaH_eZ4?si=pIAJOCH3HujxnjQ8
def is_circular(head):
    fast=head
    slow=head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

#head = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
node10 = Node(10)
node9 = Node(9, node10)
node8 = Node(8, node9)
node7 = Node(7, node8)
node6 = Node(6, node7)
node10.next = node8
#is_circular(head)
is_circular(node6)

'''
**Floyd's Cycle Finding Algorithm**

This code implements Floyd's algorithm to detect a cycle (loop) in a linked list.

**Explanation:**
6->7->8(loop starts)->9-10 )

1. **Initializing variables:**
   - `L`: Length of the loop (unknown initially). length of loop 8(loop starts)->9-10 ) so 3 for the three nodes in the loop or perimeter of the circle
                                                                 ^--------------------
   - `M`: Distance from the beginning of the list to the start of the loop (unknown initially). before loop starts so 6->7 so 2 for the two nodes before the start of the loop
   - `K`: Distance from the start of the loop to the point where the slow and fast pointers meet or meetng point (unknown initially). there is a simulation below but after you find out it is 1
   - `fast`: Fast pointer that moves two steps at a time (`fast.next.next`).
   - `slow`: Slow pointer that moves one step at a time (`slow.next`).

2. **Finding the meeting point:**
   - We iterate while both `fast` and `fast.next` are not `None`.
   - In each iteration:
      - `slow` moves one step forward.
      - `fast` moves two steps forward.

**Explanation for K:**

   - When a cycle exists, `fast` will eventually "lap" `slow` inside the loop. At this point, `fast` and `slow` will point to the same node (denoted as the meeting point).
   - **K** represents the distance from the **start of the loop** to the **meeting point**.

**Let's do a simulation to see when each pointer enters and leaves the loop:**

   - `fast=6, slow=6`: Both pointers start at the beginning (outside the loop).
   - `while fast and fast.next are true`: This loop continues as long as `fast` and `fast.next` are not `None`.
      - `slow=7, fast=8`: `slow` moves to the next node (still outside the loop), and `fast` jumps two nodes ahead, entering the loop for the first time (**here fast entered the loop**).
      - `if fast==slow is false`: Since they are not at the same node yet, the loop continues.
      - `slow=8, fast=10`: `slow` moves into the loop, and `fast` jumps two nodes further (still inside the loop).
      - `if fast==slow is false`: They haven't met yet, so the loop continues.
      - `slow=9, fast=9`: `slow` moves further inside the loop, and `fast` jumps two nodes, "lapping" `slow` and landing on the same node as `slow` (node 9) fast finished one round of the loop and entered the loop again a second time 
            -you could enter it many times; it's just that in our linked list, we entered it twice with fast and once with slow.
      - `if fast==slow is true`: Since they point to the same node (the meeting point), the loop breaks and we know a cycle exists. **Here, K is the distance from node 8 (start of the loop) to node 9 (meeting point), which is 1.**

3. **Calculating loop length:**
   - Once `fast` and `slow` meet, we can calculate the loop length (`L`).
   - `C1`: Number of times `slow` entered the loop. (In this example, it's 1)
   - `C2`: Number of times `fast` entered the loop. (This will be greater than `C1` in this example it is 2)
   - We know:
      - `fast_`: Total distance traveled by `fast` (including outside and inside the loop).
      - the distance it traveled outside the loop (it always visits this exactly once because it has to reach the loop from the start) + the distance it travels in the loop * however many times it does this plus the distance it travels before meeting slow which is how many nodes till the meeting point in the loop
      - `slow_`: Total distance traveled by `slow` (including outside and inside the loop).
   - We set `fast_` equal to 2 * `slow_` because `fast` moves twice as fast as `slow`. it allows it to be equal because fast travels twice the distance that slow travels. This ensures they meet at the same point in the loop.
   - We can express `fast_` and `slow_` as:
      ```
      fast_ = M + L * C2 + K  # Distance traveled by fast
      slow_ = M + L * C1 + K  # Distance traveled by slow
      ```
   - Solving the equation `fast_ = 2 * slow_`, we get:
      ```
      M + L*C2 + K = 2*M + 2*L*C1 + 2*K
      Move everything to one side because we want to isolate the loop length and other terms.
    
      0 = (2*M - M) + 2*L*C1 - L*C2 + (2*K - K)
      0 = M + 2L*C1 - L*C2 + K
      Factor out L because it simplifies the equation and reveals the relationship between the terms.
    
      0 = M + K + L(2*C1 - C2)
      Set L(2*C1 - C2) to the other side because we want to isolate the loop length and simplify the equation.
    
      0 - L(2*C1 - C2) = M + K
      L(C2 - 2*C1) = M + K
      
      from Sam

      M + L*C2 + K = 2(M + L * C1 + K)
      M + K = 2M + 2(L*C1) + 2K - L*C2
      M + K = 2(M + K) + 2(L*C1) - L*C2
      (M+K) = 2L*C1 -L*C2
      M + K = L*C2 - 2L*C1
      M + K = L * (C2 - 2C1)
    
      Gonna do a bit of a leap here so let me know tmrw if this doesnt make sense:
      M + K is an integer.
      L is also an integer.
      They're all integers because they're discrete # of steps in the list
    
      That means because M + K = L * (C2 - 2C1)
      C2 - 2C1 is an integer which I'll rename C
      M + K = L * C
      M + K / L = C
      And because we proved earlier C is an integer, M+K is a multiple of L
      and knowing that m+k is a multiple of L means you will always land in the loop or within the confines of L
      ```
   - This tells us that `M + K` is a multiple of the loop length `L`. 

**Explanation of M + K being an integer multiple of L:**

   - An integer multiple means that when `M + K` is divided by `L`, there is no remainder. This shows that `M + K` is exactly `L`, `2L`, `3L`, etc. 

**How this ensures we reach the start of the loop:**

   - Consider that `M` is the distance from the head of the list to the start of the loop, and `K` is the distance from the start of the loop to the meeting point.
   - If `M + K` is a multiple of `L` (let's call it `nL` where `n` is an integer), it means that starting from the head and moving `M` steps will land the slow pointer at the start of the loop, and then moving `nL` steps will take the slow pointer exactly `n` laps around the loop, landing it again at the start of the loop.
   - Therefore, when `M + K` is a multiple of `L`, it ensures that both pointers will meet at the start of the loop after `M` steps.

4. **Finding the start of the loop:**
   - Since `M + K` is a multiple of `L`, moving `slow` from the beginning and `fast` from the meeting point by `M` steps each will bring them both to the start of the loop.

**Key Points:**

- The algorithm relies on the fact that the fast pointer will eventually lap the slow pointer inside the loop.
- The difference between the number of times `fast` and `slow` enter the loop determines the distance `K` from the meeting point to the loop start.
- By ensuring `M + K` is a multiple of `L`, we guarantee that moving both pointers `M` steps will bring them to the loop start.

**In essence:**

- The loop length `L` is the "perimeter" of the cycle (3 in the example).
- The difference `C2 - 2 * C1` represents the number of extra laps `fast` takes compared to `slow` (1 in the example).
- This difference, multiplied by `L` (loop length), ensures we land at the beginning of the loop when both pointers move `M` steps.

'''
