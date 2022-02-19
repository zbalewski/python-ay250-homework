from random import uniform


def hit_target(n_darts): 
    """Throw a dart at a square; check if (x, y) coords 
    hit inscribed circle 
    
    Parameters
    ----------
    None
        
    Returns
    -------
    in_circle : bool
        True if dart hit circle
        
    """
    
    # define square inscribed circle
    len_square = 1
    rad_circle = len_square / 2
    
    # throw a uniform dart!
    x = uniform(0, len_square)
    y = uniform(0, len_square)
    
    # check if hit circle
    in_circle = (x - rad_circle)**2 + (y - rad_circle)**2 <= rad_circle**2
    
    return int(in_circle)


def throw_darts_serial(n_darts):
    """Throw darts at a square. Execute serially! Count 
    how many end up in an inscribed circle. Approximate pi. 

    Parameters
    ----------
    n_darts : int
        Number of darts to throw

    Returns
    -------
    pi_approx : float
        Approximation of pi
        
    """
    
    n_success = 0
    
    for dart in range(n_darts):
        if hit_target(dart):
            n_success += 1

    pi_approx = 4 * n_success / n_darts
    
    return pi_approx
