#Get five numerical grades, show letter grade, then average test score.
#4/18/2018
#CTI-110 P5HW1 - Test Average and Grade
#Bradley Legge

NUM_OF_GRADES = 5

def main():
    num = 0
    total = 0

    while num < NUM_OF_GRADES:
        testScore = int(input('Enter a test score: '))
        total = total + testScore
        print('Your letter grade is: ', determine_grade(testScore), '.')
        num = num + 1

    print('Your average test score is: ', calc_average(total), '.')
    
def calc_average(total):
    return total / NUM_OF_GRADES

def determine_grade(grade):
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
 
    if grade >= A_score:
        return 'A'
    elif grade >= B_score and grade < A_score:
        return 'B'
    elif grade >= C_score and grade < B_score:
        return 'C'
    elif grade >= D_score and grade < C_score:
        return 'D'
    else:
        return 'F'
main()
