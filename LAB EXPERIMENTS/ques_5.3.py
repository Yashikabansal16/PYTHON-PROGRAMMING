'''3.WAP to input a list of scores for N students in a list data type. Find the score of the 
runner-up and print the output.
Sample Input
N = 5
Scores= 2 3 6 6 5
Sample output
5
Note: Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second maximum is 5. Hence,
we print 5 as the runner-up score.'''

n = int(input("Enter number of students: "))

values = []
for x in input().split():
    values.append(int(x))

# Remove duplicate values
unique_scores = list(set(values))

# Remove the maximum score
unique_scores.remove(max(unique_scores))

# Runner-up is now the maximum of remaining values
runner_up = max(unique_scores)

print("Runner-up score is:", runner_up)
