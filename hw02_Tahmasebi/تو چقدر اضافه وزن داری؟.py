#mitratsb
n=int(input())
m=float(input())

if 1<=n<=200 and 1<=m<=10 :
    
    BMI=n/(m**2)
    print(f'{BMI:.2f}')

    if BMI<18.5 :
        print("Underweight")
    elif 18.5<=BMI<25 :
        print("Normal")
    elif 25<=BMI<30 :
        print("Overweight")
    elif 30<=BMI :
        print("Obese")
    

