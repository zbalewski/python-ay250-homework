"""CalCalc: evaluate strings as numeric expressions. If simple (i.e., no 
alpha characters), will try to evaluate locally with numexpr. If more 
complex, will try to query wolfram alpha.
"""

import argparse
import numexpr as ne
import urllib.request


def calculate(str_input, return_float=True):
    """Evaluate any string, limited to numerical expressions.

    Parameters
    ----------
    str_input : str
        String expression to evaluate.
    return_float : bool
        If output should be float (default = True)

    Returns
    -------
    answer : float
        Numeric output of evaluated string.

    """
    
    # first, are you string?
    if type(str_input) != str:
        raise ValueError("You are not a string. Try again.")
    
    # let's see if numexpr can solve you
    try: 
        answer = ne.evaluate(str_input)
        return answer 
    except (KeyError, SyntaxError) as e: 
        
        # ok, let's send you to wolfram
        try: 
            answer = query_wolfram(str_input, return_float)
            return answer
        except (ValueError, SyntaxError) as e:
            print("Wolfram could not solve query.")
        
        
    
def query_wolfram(str_input, return_float):
    """Send off query to wolfram...
    
    Parameters
    ----------
    str_input : str
        String expression to evaluate, e.g. 'mass of moon in kg'
    return_float : bool
        If output should be float (default = True)

    Returns
    -------
    query_output : str or float
        Full text restult or just float, depending on 'return_float'

    """

    # get query url
    url_prefix = 'http://api.wolframalpha.com/v2/query?input=' 
    query = str_input.replace('+', '%2B').replace(' ','+') # replace numeric '+'; use '+' as space;
    return_opts = '&appid=9TLK2V-8T9H43UY82&format=plaintext&includepodid=Result' # reduce output to just results as text

    full_url = url_prefix + query + return_opts

    # set off to wolfram!
    output = urllib.request.urlopen(full_url) # request for url
    output_as_text = output.read().decode('utf-8') # turn it into English...

    # extract answer, assuming it's in the plaintext section of the results pod...
    idx_plaintext = output_as_text.find('<plaintext>')
    
    if idx_plaintext == -1:
        raise ValueError("Don't know how to parse result from wolfram.")
    
    idx_start = idx_plaintext + 11
    idx_start = output_as_text.find('<plaintext>')+11
    idx_stop = output_as_text.find('</plaintext>',idx_start)
    query_output = output_as_text[idx_start:idx_stop]
    
    if query_output == '(data not available)':
        return ValueError('Wolfram does not know the answer.')
    
    if return_float:
        number = query_output.split(' ')[0]
        number_simple = number.replace('×','*').replace('^','**')
        return ne.evaluate(number_simple)
    
    else: 
        return query_output
    
    
if __name__ == '__main__':
    # parse command line arguements
    parser = argparse.ArgumentParser(description='CalCal Module')
    parser.add_argument('-s', action='store', dest='str_input',
                        help='String to parse') # use the same flag for all inputs! 
    results = parser.parse_args()

    # TODO: try using click instead to make cuter!

    # check you got an arg
    if results.str_input == None:
        raise ValueError('feed me a string with -s')
    
    # execute function
    print(calculate(results.str_input))
