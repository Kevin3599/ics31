def driving_cost(miles_per_gallon,dollars_per_gallon,miles_driven):
    gas_used = miles_driven / miles_per_gallon
    cost = gas_used * dollars_per_gallon
    return cost
def main():
    mpg = float(input())
    price = float(input())
    cost10 = driving_cost(mpg,price,10)
    cost50 = driving_cost(mpg,price,50)
    cost100 = driving_cost(mpg,price,400)
    print(f'{cost10:.2f}')
    print(f'{cost50:.2f}')
    print(f'{cost100:.2f}')
if __name__ == '__main__':
    main()