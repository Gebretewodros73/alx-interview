# alx-interview - 0x08-making_change

## Tasks

### 0. Change comes from within
**Mandatory**

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

#### Prototype
```python
def makeChange(coins, total)
```

#### Return

* Fewest number of coins needed to meet total
* If total is 0 or less, return 0
* If total cannot be met by any number of coins you have, return -1

#### Arguments

* `coins`: A list of the values of the coins in your possession
* `total`: The target total amount

#### Additional Information

* The value of a coin will always be an integer greater than 0
* You can assume you have an infinite number of each denomination of coin in the list
* Your solution’s runtime will be evaluated in this task

## Example

```bash
makeChange([1, 2, 25], 37)  # Output: 7
makeChange([1256, 54, 48, 16, 102], 1453)  # Output: -1
```

## Repo:

* GitHub repository: [alx-interview](./https://github.com/Gebretewodros73/alx-interview.git)
* Directory: 0x08-making_change
* File: [0-making_change.py](./0-making_change.py)
