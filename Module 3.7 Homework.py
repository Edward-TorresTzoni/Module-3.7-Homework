# Excercise 1 - Copy and paste the code from the question, and run it both on the console and the text box.

def main():
    scores = get_scores()
    total = get_total(scores)
    lowest = min(scores)
    
    total -= lowest

    average = total / (len(scores) - 1)
    
    print(f'Average with lowest score dropped: {average}')

def get_scores():
    test_scores = []
    again = 'y'
        
    while again == 'y':
        value = float(input('Enter a test score: '))
        test_scores.append(value)
            
        print('Do you want to add another score?')
        again = input('y = yes, other buttons = no: ')
        print()
            
    return test_scores
        
def get_total(value_list):
    total = 0.0
                
    for num in value_list:
        total += num
                    
    return total
    
if __name__ == '__main__':
    main()
    
print('-----')

# Excercise 2

Max = 20
totalNum = 0.0
numList = []
num = len(numList)

for counter in range (Max):
    Number = int(float(input('Enter 20 numbers: ')))
    
    totalNum = totalNum + Number
    averageNum = sum(numList) / Max
    
    numList.append(Number)
    numList.sort()
    
    if len(numList) == 20:
        print('Your lowest number: ', numList[0])
        print('Your highest number: ', numList[-1])
        print('Total of all numbers: ', sum(numList))
        print(f'Average of all 20 numbers: {averageNum:,.2f}')

