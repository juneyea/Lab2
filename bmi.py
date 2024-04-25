def calculate_bmi(height,weight):
    print ("Height = " + str(height))
    print ("Weight = " + str(weight))
    bmi = weight/(height * height)
    print ("BMI = " + str(bmi))
    if bmi < 18.5 :
        print ("You are Under Weight")
    elif 18.5 <= bmi <= 25.0:
        print ("You are Normal Weight")
    else: 
        print ("You are Over Weight")
        



calculate_bmi(height = 1.73, weight = 57)