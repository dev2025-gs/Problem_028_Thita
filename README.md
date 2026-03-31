# Minimum Number of Swaps to Make the String Balanced

## 📌 Problem Description

You are given a **0-indexed string `s`** of even length `n`. The string consists of exactly:

- `n / 2` opening brackets `'['`
- `n / 2` closing brackets `']'`

A string is considered **balanced** if:

1. It is an empty string, OR  
2. It can be written as `AB`, where both `A` and `B` are balanced, OR  
3. It can be written as `[C]`, where `C` is balanced  

You may swap the brackets at **any two indices** any number of times.

### 🎯 Goal

Return the **minimum number of swaps** required to make the string balanced.
Link: https://thita.ai/problems/minimum-number-of-swaps-to-make-the-string-balanced

---

## 🧠 Approach

### Key Idea

We track imbalance while iterating through the string:

- Maintain a counter `balance`:
  - Increment for `'['`
  - Decrement for `']'`
- If `balance` becomes negative, it means we have more closing brackets than opening ones at that point → imbalance

### Insight

Each time imbalance occurs, we need a swap to fix it.  
The number of swaps required is:
