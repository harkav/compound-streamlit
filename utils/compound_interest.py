from numbers import Number

def calculate_compound(principal : Number, assumed_yearly_profit : Number, num_years : Number ) -> float: 
    """
    Returns the assumed profit for an investment based on assumed yearly profit and number of years.
    
    Args: 
        principal (Number): The investment as a number.
        assumed_yearly_profit(Number): the assumed growth rate (if you care about inflation, just deduct that)
        num_years (Number): years of investment.
        
    Returns: 
        The sum (float).
    
    """
    
    return principal * ((1 + assumed_yearly_profit / 100) ** num_years)
    