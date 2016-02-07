def input_number_between(prompt, lower_bound, upper_bound):
    while True:
        number = input(prompt)
        if lower_bound <= number <= upper_bound:
            return number
        print "This number should be between %s and %s!" % (lower_bound, upper_bound)

