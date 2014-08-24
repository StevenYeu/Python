__author__ = 'stevenyeu'
# This an implementation of the Lunh algorithm
# THe algorithm is used to validate identification numbers
# such as credit cards


def check_credit_type(credit_card):
    """
    This function determines the type of
    credit card based on the card number
    The amount of card types this function is
    limited as now.
    :param credit_card: type String
    :return: a String
    """

    # stores the credit card number in a list
    numbers = []
    for digit in credit_card:
        numbers.append(digit)

    # Determines the card type by checking the first few digits
    if int(numbers[0]) == 4:
        return "It is a Visa Card"
    elif int(numbers[0]) == 3 and int(numbers[1] == 4) or int(numbers[0]) == 3 and int(numbers[1]) == 7:
        return "It is an American Express Card"
    elif int(numbers[0]) == 6 and int(numbers[1]) == 0 and int(numbers[2]) == 1 and int(numbers[3]) == 1:
        return "It is a Discover Card"
    elif int(numbers[0]) == 6 and int(numbers[1]) == 4 and int(numbers[2]) == 4:
        return "It is a Discover Card"
    elif int(numbers[0]) == 5 and int(numbers[1]) == 5:
        return "It is a Discover Card"
    elif int(numbers[0] == 5 and (int(numbers[1]) == 1 or int(numbers[1]) == 2 or int(numbers[1]) == 3 or int(numbers[1]) == 4) or int(numbers[1]) == 4):
        return "It is a MasterCard"




def luhn_check_card(credit_card):
    """
    This function checks if the credit card
    numbers are valid.
    :param credit_card: Type String
    :return:
    """
    numbers = [0] * 16

    # Store digits into list
    for digit in credit_card:
        numbers.append(digit)

    # store every even placed digit
    num = numbers[::2]

    # store evey odd placed digit
    odd_num = numbers[1:len(numbers):2]
    doubles = [0] * 8

    #double every even placed digit
    for ch in num:
        n = int(num.pop()) * 2
        doubles.append(n)

    even_digits = [0] * 8
    # for evey digit doubled
    # if the result is a two digit number
    # sum the two digits to make a one digit number
    for y in doubles:
        check_digit = doubles.pop()
        string_digit = str(check_digit)
        if int(check_digit) >= 10:
            two_digits = [0] * 2
            for nums in string_digit:
                two_digits.append(nums)

            first_digit = int(two_digits.pop())
            second_digit = int(two_digits.pop())
            summed_digit = first_digit + second_digit
            even_digits.append(summed_digit)
        else:
            even_digits.append(check_digit)

    # Sum the even and odd placed digits
    even_digits = [int(m) for m in even_digits]
    odd_num = [int(j) for j in odd_num]
    total = sum(odd_num) + sum(even_digits)

    # Take the remainder of the total
    # divided by 10
    return total % 10


def luhn_driver():
    """
    This is the driver for
    the application.
    """
    q = False
    while not q:
        print "Please Enter Credit Card Number (no spaces)."
        credit_number = raw_input()
        if int(credit_number) == 0:
            print "Please Enter A 16 Digit Credit Card Number."
        else:
            card = luhn_check_card(credit_number)
            if card == 0 :
                print "Credit Card Number Is Valid."
                print check_credit_type(credit_number)

            else:
                print "Credit Card Number Is Not Valid."

            print "1. Enter New Card Number"
            print "2. Quit"
            user_input = raw_input()
            if user_input == "1" :
                q = False
            else:
                q = True


luhn_driver()