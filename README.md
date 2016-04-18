# GPA-Convert
This script calculates the score 0-100 scale and generates CSV file with the scores based in the transformation of scores [ESPOL](http://www.espol.edu.ec).  Also, it allow calculate the score 0-100 to GPA EEUU

## Format

- **-h**: Help
- **-s**: score file or source file **(Required)**
- **-t**: Type to convert (ESPOL transformation or U.S)
- **-o**: Output filename

When the parameter **-o** is not written, it is taken as the output file name, the same name of the source file preceded by **gpa.scv**.

## Input

### Example 1
```
score100_to_gpa -h
```

### Example 2
```
score100_to_gpa -s scores.csv
```

### Example 2
```
score100_to_gpa -s scores.csv -o newScores.csv
```

## Output

Show the results calculated from source file
- **Sum total Score**: Sum total score from source file (qualifications)
- **Sum total credits**: Sum all credits by subject from source file
- **Sum total GPAs**: Sum all GPA determined in each subject according to the type
- **Total points**: Sum total of each GPA by subject multiplied multiplied by the number of credits of the myself
- **U.S GPA**: It is the grade earned by the total points
- ** GPA score**: Final score obtained in scale 4

### Example
```
Sum total Score: 4690.6
Sum total credits: 241
Sum total GPAs: 149.6
Total Points: 585.8
U.S. GPA: D-
GPA score: 2.43070539419 / 4.0
```
