from nada_dsl import *

def nada_main():
    # Define the party
    party1 = Party(name="Party1")
    
    # Define the inputs from the party
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))
    
    # Compute the product of the inputs
    product = my_int1 * my_int2
    
    # Output the result to the party
    return [Output(product, "product_output", party1)]