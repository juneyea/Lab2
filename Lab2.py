def main():
    p = 0
    while p < 1000 :

        print ("ET0735 (DevOps for AIoT)- Lab 2 - Introduction to Python")
        display_main_menu()
        num_list = get_user_input()
        maxi = find_min_max(num_list)
        avg = calc_average(num_list)
        skib = calc_median_temperature(num_list)
        print ("These are the Maximum and Minimum values respectively " + str(maxi))
        print ("This is the average of all the values " + str(avg))
        print ("This is the Median value " + str(skib))
        p = p + 1
    

def display_main_menu():
    print ("Enter values separated by commmas, E.g 1, 2, 3, 4")

def get_user_input():
    x = input()
    values = x.split(",")
    y = list(map(float, values))
    return (y)

def calc_average(y):
    
    average = sum(y)/len(y)
    return average

def find_min_max(y):
    large = y[0]
    for i in y:
        if i>large:
            large = i
    small = y[0]
    for s in y:
        if small>=s:
            small = s
    value = [large,small]
    return value

def calc_median_temperature(y):
    t = int(len(y))
    new = (t+1)/2
    if t%2 == 0:
        new = int(new)
        valuenew = (y[new-1] + y[new])/2
    else:
        new = int(new)
        valuenew = y[new-1]
    
    return valuenew

if __name__ == "__main__":
    main()