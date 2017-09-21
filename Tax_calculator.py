#TODO: add rest of tax codes
#TODO: add error checking
#TODO: build front end
#TODO: add NI
#TODO: convert to class
tax_rate = 0.2, 0.4, 0.45
tax_allow = 11500
tax_codes = {
    '1000L': 10000,
    '1100L': 11000,
}

wage = input('Enter you yearly wage: ')
check = input('Enter tax code: ')


def net_income(n,e):
    if n <= tax_allow:
        print('You dont need to pay tax when you only make ' + str(wage))
    elif n > tax_allow <= 45000:
        r = tax_calc(n,e)
        w = tax_rate[0] * r
        net_wage(w, n)
    elif n > 45000 <= 150000:
        r = tax_calc(n,e)
        w = tax_rate[1] * r
        net_wage(w, n)
    else:
        r = tax_calc(n,e)
        w = tax_rate[2] * r
        net_wage(w, n)


def net_wage(w,n):
    x = monthly_wage(n) - tax_month(w, n)
    print('Net wage is ' + str(x))
    return x


def tax_month(w, n):
    x = monthly(w)
    print('Total tax payable is per month: %s' % x)
    return x


def monthly(n):
    r = n / 12
    return r


def tax_calc(n, e):
    r = n - check_code(e)
    print('Total amount of taxable pay is: %s per year. This equals up to %s per month' % (str(r), str(monthly(r))))
    return r


def monthly_wage(w):
    x = monthly(w)
    print('total month pay is %s' % ((x)))
    return x


def check_code(n):
    try:
        r = tax_codes[n]
    except Exception:
        print("Please enter correct tax code")
    return r

net_income(int(wage),check)