import array as arr
n = int(input())
# check if the input integer is between 2 and 10
while n < 2 or n > 10:
    print("number must be between 2 and 10")
    n = int(input())

# creating dictionary called record to store the information
records = {}

for i in range(0, n):

    # input the record as a string

    record = input()

    info = record.split()  # split the string entered in order to store name and marks
    name = info[0]        # store the name of the student
    name = name.capitalize()  # capitalize the name in order to store it in proper way
    marks = info[1:]          # store the marks as list
    mark = [eval(j) for j in marks]  # convert the marks list from the string to integer
    res1 = arr.array('i', mark)      # convert the marks as list  into an array where 'i' is the typecode
    for k in res1:
        if k < 0 or k > 100:            # check if the entered marks is between 0 and 100
            print("marks should be between 0 and 100")
            exit()
    if len(res1) > 3:                    # check if the length of the array of marks is not greater than 3
        print("length must not be greater than 3")
        exit()
    records.update({name: res1})       # store the name and marks into the dictionary

sch = input()               # input the query_name the name of a student to query
if sch.capitalize() in records:  # to check if the entered name is in the dictionary
    for names, marks in records.items():   # read the element of the dictionary
        if names.lower() == sch.lower():     # check where the name is equal to the query name
            print(names, "Average:", end=" ")
            sums = 0
            avg = 0
            for i in marks:       # read the array of the marks in order to calculate sum and average
                sums = sums+i         # calculate the sum
            avg = sums/3           # calculate the average
            print("%.2f" % avg)    # print the average with 2 decimal places
else:
    print("No Record found for ", sch)
