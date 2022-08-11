def solution(deposit, rate, threshold):
    
    def calculate_yearly_increase(amount):
        return amount * ((rate/100) + 1)
        
    amount = deposit
    years = 0
    while True:
        amount = calculate_yearly_increase(amount)
        years += 1
        print(amount)
        if amount >= threshold:
            return years