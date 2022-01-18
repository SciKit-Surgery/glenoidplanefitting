"""
A colour palette based on Bang's colour pallette
Wong, B. Points of view: Color blindness. Nat Methods 8, 441 (2011).
https://doi.org/10.1038/nmeth.1618
"""

bang_palette={ 'black' : [0,0,0],
               'orange' : [230./255., 159./255., 0],
               'sky blue' : [86./255., 180./255., 233./255.],
               'bluish green' : [0./255., 158./255., 115./255.],
               'yellow' : [240./255., 228./255., 66./255.],
               'blue' : [0./255., 114./255., 178./255.],
               'vermillion' : [213./255., 94./255., 0./255.],
               'reddish purple' : [204./255., 121./255., 167./255.]
             }

weiss_light_blue = [0.0, 0.384, 0.490]


def bang_list():
    """
    Returns the bang palette as a list
    """
    bp_list = []
    for _key, value in bang_palette.items():
        bp_list.append(value)
    return bp_list
