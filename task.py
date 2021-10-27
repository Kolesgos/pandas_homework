import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def Ep1():
    data = pd.read_csv('transactions.csv')
    max_money = data[data.STATUS == 'OK'].nlargest(3, ['SUM'])
    print("Три наибольшие транзакции на счета Umbrella Inc:")
    print(max_money)
    Umbrella = data[(data.STATUS == 'OK') & (data.CONTRACTOR == 'Umbrella, Inc')]
    print("На счета Umbrella Inc за все время было переведено:", Umbrella.SUM.sum(), "USD.")
    
def Ep2():
    data = pd.read_csv('flights.csv')
    fig, axs = plt.subplots(1, 3, figsize=(11, 11), sharey=True)
    companies = data.CARGO.unique()
    AMOUNT = []
    PRICE = []
    WEIGHT = []
    for i in companies:
        AMOUNT.append(len(data[data.CARGO == i]))
        PRICE.append(data[data.CARGO == i].PRICE.sum())
        WEIGHT.append(data[data.CARGO == i].WEIGHT.sum())
        
    print("Данные по авиакомпаниям:")
    for i in range(len(companies)):
        print(f"{companies[i]}. Рейсов: {AMOUNT[i]}, полная стоимость: {PRICE[i]}, полная масса грузов: {WEIGHT[i]}.")
        
    axs[0].pie(AMOUNT, labels = companies)
    axs[0].set_title("Number of flights")
    axs[1].pie(PRICE, labels = companies)
    axs[1].set_title("Full cost of flights")
    axs[2].pie(WEIGHT, labels = companies)
    axs[2].set_title("Weight of transported goods")
    fig.savefig('Flights.pdf')

def Ep3():
    result = pd.read_html("results_ejudge.html")[0].sort_values(by = 'User')
    students = pd.read_excel("students_info.xlsx").sort_values(by ='login')
    data = students.merge(result, left_on='login', right_on='User')
    
    group_faculty = students.group_faculty.unique()
    avg_group_faculty = []
    group_out = students.group_out.unique()
    avg_group_out = []
    
    for i in group_faculty:
        this_group = data[data.group_faculty == i].Solved
        avg_group_faculty.append(this_group.sum() / len(this_group))
    for i in group_out:
        this_group = data[data.group_out == i].Solved
        avg_group_out.append(this_group.sum() / len(this_group))
        
    fig, axs = plt.subplots(1, 2, figsize=(11, 11), sharey=True)
    axs[0].bar(group_faculty, avg_group_faculty)
    axs[0].set_title('Averange tasks in faculty groups')
    axs[1].bar(group_out, avg_group_out)
    axs[1].set_title('Averange tasks in out groups')
    fig.savefig('Groups_avg.pdf')
    
    lucky = data[(data.G > 10) | (data.H > 10)]
    lucky_group_faculty = lucky.group_faculty.unique()
    lucky_group_out = lucky.group_out.unique()
    amt_group_faculty = []
    amt_group_out = []
    for i in lucky_group_faculty:
        amt_group_faculty.append(len(lucky[lucky.group_faculty == i]))
    for i in lucky_group_out:
        amt_group_out.append(len(lucky[lucky.group_out == i]))
        
    fig, axs = plt.subplots(1, 2, figsize=(11, 11), sharey=True)
    axs[0].pie(amt_group_faculty, labels = lucky_group_faculty)
    axs[0].set_title('Powerful students in faculty groups')
    axs[1].pie(amt_group_out, labels = lucky_group_out)
    axs[1].set_title('Powerful students in out groups')
    fig.savefig('Powerful_students.pdf')
    
    print("Студенты, решения которых прошли больше одного теста в заданиях G и H, состояли в факультетских группах: ", end = '')
    print(*lucky_group_faculty, sep = ', ', end = '\n')
    print('Они были распределены в группы: ', end = '')
    print(*lucky_group_out, sep = ', ')
 
 
def main():
    n = int(input("Enter the number of Ep.: "))
    if (0 < n < 4):
        exec(f"Ep{n}()")
        print()
        print()
        main()         
    elif (n == 0):
        pass
    else:
        print("Please do it carfully...")
        main()    
main()