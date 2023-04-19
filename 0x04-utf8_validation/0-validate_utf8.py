#!/usr/bin/python3
""" utf-8 validation
"""

def validUTF8(data):
    """ 
    used to determine the validity of data using utf-8
    """
    
    number_bytes = 0
    
    """ mask_1 = 1 << 7
    mask_2 = 1 << 6
      """
    for i in data:
        
        mask_1 = 1 << 7
        
        if not number_bytes:
        
            while mask_1 & i:
                number_bytes += 1
                mask_1 >> 1
                
        if not number_bytes:
            continue
        
        if number_bytes == 1 or number_bytes > 4:
                return False
    else:
        if i >> 6 != 0b10:
            return False
        
    number_bytes -= 1
    return number_bytes == 0
