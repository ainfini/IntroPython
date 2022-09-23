def get_magnitude(number):

    mag = float(input(f"Please enter the magnitude for earthquake {number} : \n"))
    while mag < 0:
        mag = float(input(f"Please enter the magnitude for earthquake {number} : \n"))
    return mag 
    
def compare_magnitudes(magnitude1, magnitude2):
    return ( 10 **  (1.5*(magnitude1-magnitude2)  ))
        
def get_run_again():
    
    try_again = input("Try again?  Type 1 for yes: ")
    print()
    if try_again == '1':
        return True 
    else:
        return False

if __name__ == "__main__":
    again = True
    while again == True:
        mag1 = get_magnitude(1)
        mag2 = get_magnitude(2)
        
        if mag1 > mag2 :
            sol = compare_magnitudes(mag1, mag2)
            print(f"An earthquake of magnitude {mag1} is {sol:.1f} times more powerful than an earthquake of magnitude {mag2} .")
        elif mag2 > mag1:
            sol = compare_magnitudes(mag2,mag1)
            print(f"An earthquake of magnitude {mag2} is {sol:.1f} times more powerful than an earthquake of magnitude {mag1} .")
            
        again = get_run_again()
    print('Bye!')
    
       
        
            
