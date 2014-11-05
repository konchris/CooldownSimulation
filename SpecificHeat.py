import numpy as np

def spec_heat_apiezon_n(T, echo=False):
    """Return the specific heat for Apiezon N at temperature 'T' in Kelvin
    
    Parameters
    ----------
    T : float, int, list, numpy.ndarray
        Temperature in Kelvin at which the specific heat should be calculated.
    echo : boolean, optional
        When true, the function prints a sentence with the values to the command line.
        
    Returns
    -------
    C : numpy.ndarray
        The specific heat of Apiezon N at tempterature T in uTg^(-1)K^(-1)
        
    Reference
    ---------
    [1] Pobell, Frank. "Matter and Methods at Low Temperatures, 3rd Edition". Springer-Verlag, 2007.
    
    """
    # Convert whatever the input is into a numpy array.
    if isinstance(T, (list, float, int)):
        T = np.asarray(T)
    elif isinstance(T, np.ndarray):
        pass
    else:
        raise TypeError('Invalid temperature type. Type a float, int, list or numpy array.')
        
    C = np.ndarray(T.shape)
        
    for i, t in enumerate(T):
        if t >= 0.1 and t <= 2.5:
            C[i] = 1.32 * t + 25.8 * t**3 + 0.0044 * t**(-2)
        else:
            C[i] = np.NaN
    
    # Print the results to the commant line
    if echo:
        try:
            for i, t in enumerate(T):
                # print(i, t)
                print('The specific heat of Apiezon N at {} K is {:.1f} uJg^(-1)K^(-1)'.format(t, C[i]))
        except IndexError:
            print('The specific heat of Apiezon N at {} K is {:.1f} uJg^(-1)K^(-1)'.format(T, C))
    
    # Return the resutling array
    return C