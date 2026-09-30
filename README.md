# Hostel Roommate Compatibility System

A console-based Python program that helps allot hostel rooms by measuring how compatible two students are as roommates.

## Why this project?

Sharing a room is hard when two people have very different routines. One sleeps at 10 pm and studies seriously, the other plays music till 2 am. This program compares students' habits, gives every pair a compatibility score out of 100, and suggests room pairs with the least friction.

## Features

- Add and remove students with an eight-question habit questionnaire
- Compare any two students and get a compatibility % with a rating (Excellent / Good / Average / Poor)
- Find the top 3 best matches for any student
- Allot rooms automatically, best pairs first (greedy algorithm)
- Detects the leftover student when the count is odd
- Input validation, so wrong or out-of-range answers are asked again
- Five sample students preloaded so you can try it instantly

## Requirements

- Python 3.6 or above
- No external libraries needed

## How to run

```bash
git clone https://github.com/<your-username>/hostel-roommate-compatibility.git
cd hostel-roommate-compatibility
python roommate_simple.py
```

On some systems use `python3` instead of `python`.

## Usage

The program shows this menu:

```
===== HOSTEL ROOMMATE SYSTEM =====
1. Add student
2. Show all students
3. Compare two students
4. Best matches for a student
5. Remove student
6. Allot rooms
7. Show room list
0. Exit
```

### Example: compare two students

```
Enter your choice: 3
First student: Aman
Second student: Karan
Aman and Karan -> 81 % Good
```

### Example: allot rooms

```
Enter your choice: 6
Karan has no partner, needs a single room
Room 101 : Aman + Sameer -> 93 %
Room 102 : Ravi + Dev -> 54 %
Average compatibility: 73.5 %
```

## Questions asked for each student

| Question | Values |
|---|---|
| Sleeping hour | 0–23 (24-hour clock) |
| Waking hour | 0–23 |
| Cleanliness | 1 (messy) – 5 (very neat) |
| Noise level | 1 (quiet) – 5 (loud) |
| Study seriousness | 1 (chill) – 5 (topper) |
| Friends visiting | 1 (never) – 5 (always) |
| Smoker | y / n |
| Vegetarian | y / n |

## How the score works

Every pair starts at **100 points**. Points are subtracted for each difference:

| Factor | Penalty |
|---|---|
| Sleeping hour | 4 per hour of difference |
| Waking hour | 3 per hour of difference |
| Cleanliness | 7 per level |
| Noise level | 5 per level |
| Study seriousness | 4 per level |
| Friends visiting | 3 per level |
| Smoking mismatch | 20 |
| Food habit mismatch | 5 |
| Loud person + serious studier | 10 (extra) |

The score never goes below 0. Ratings: **85+** Excellent, **70–84** Good, **50–69** Average, **below 50** Poor.

Clock hours wrap around midnight, so 11 pm and 1 am are 2 hours apart, not 22.

You can change any weight inside the `compatibility()` function.

## How room allotment works

1. Make every possible pair of students and calculate its score.
2. Sort the pairs from highest score to lowest.
3. Go down the list and give a room to a pair only if neither student already has one.

This is a *greedy* method. It is fast and simple, but it does not always give the best total score.

## Project structure

```
hostel-roommate-compatibility/
├── roommate_simple.py   # complete program
└── README.md
```

## Concepts used
- Variables, expressions, functions, parameters and return values
- `if / elif / else`, `while` and `for` loops, `break`, `continue`
- Lists, tuples and dictionaries
- Sorting and searching
- Top-down design and algorithm analysis

## Limitations

- Data is kept in memory only and is lost when the program closes
- Rooms hold exactly two students
- Weights are chosen by judgement, not survey data
- Greedy allotment may not be globally optimal

## Future improvements

- Save and load data using files
- Rooms for three or four students
- A better allotment algorithm that maximises the total score
- Let students choose how important each habit is
- Graphical or web interface

## Author

Shivaansh Srivastava – B.Tech CSE (First Year), VIT Bhopal University

## License

This project is for educational purposes. Licensed under the [MIT License](LICENSE) if you add one to the repository.
