# roamer contains the Roamer class
from Roamer import Roamer
# init.py contains package imports and one-time assigned variables
from init import (current_month,
                  current_month_name,
                  next_month,
                  next_month_name,
                  use_next_month)


# Region name strings
kanto  = "Kanto"
johto  = "Johto"
hoenn  = "Hoenn"
sinnoh = "Sinnoh"
unova  = "Unova"

# Available locations
avail_grass       = ["Grass"]
avail_grass_water = ["Grass", "Water (Surfing)"]

# Avaialble month "sector" (3-month based)
jan_apr_jul_oct = [1, 4, 7, 10]
feb_may_aug_nov = [2, 5, 8, 11]
mar_jun_sep_dec = [3, 6, 9, 12]

# Available month "sector" (2-month based)
odd_months  = [1, 3, 5, 7, 9, 11]
even_months = [2, 4, 6, 8, 10, 12]

# Roamer definitions
## kanto
zapdos = Roamer("Zapdos",
                kanto,
                jan_apr_jul_oct,
                avail_grass_water)

moltres = Roamer("Moltres",
                 kanto,
                 feb_may_aug_nov,
                 avail_grass_water)

articuno = Roamer("Articuno",
                  kanto,
                  mar_jun_sep_dec,
                  avail_grass_water)

## Johto
entei = Roamer("Entei",
               johto,
               jan_apr_jul_oct,
               avail_grass)

suicune = Roamer("Suicune",
                 johto,
                 feb_may_aug_nov,
                 avail_grass_water)

raikou = Roamer("Raikou",
                johto,
                mar_jun_sep_dec,
                avail_grass)


# Hoenn
#latias = Roamer("Latias",
#                hoenn,
#                N/A,
#                avail_grass_water)

#latios = Roamer("Latios",
#                hoenn,
#                N/A,
#                avail_grass_water)


kanto_roamers  = [zapdos, moltres, articuno]
johto_roamers  = [suicune, raikou, entei]
hoenn_roamers  = []
sinnoh_roamers = []
unova_roamers  = []

all_roamers = [kanto_roamers,
               johto_roamers,
               hoenn_roamers,
               sinnoh_roamers,
               unova_roamers]



def get_avail_roamer_in_region(roamers:list[Roamer],
                                          month:int
                                          ) -> Roamer:
    '''
    Gets the available roamer from a given month from a list of region roamers.

    ### Parameters:
    - roamers (list[Roamer]):
        All the roamers in a region.
    
    - month (int):
        The month to get the corresponding available roamer of.
    
    ### Returns:
        The available roamer from a region, corresponding to a given month.
    '''
    for roamer in roamers:
        if roamer.is_available(month):
            return roamer


def get_avail_roamers_in_month(all_roamers:list[list[Roamer]],
                                month:int
                                )-> list[Roamer]:
    '''
    Gets all available roamers for a given month.

    ### Parameters:
    - all_roamers (list[list[Roamer]]):
        List of list of every roamer in each region.
        Outer list is the region, inner list is the roamers in said region.
    
    month (int):
        The month to get corresponding roamers of.
    
    ### Returns:
        A list of all the roamers available in a given month.
    '''
    currently_avail_roamers = []

    for region_roamers in all_roamers:
        currently_avail_roamers.append(get_avail_roamer_in_region(region_roamers, month))

    return currently_avail_roamers

def get_avail_roamers_str(roamers:list[Roamer],
                          prefix_str:str = None
                          ) -> str:
    '''
    Gets a nice string of all given roamers.

    ### Parameters:
    - roamers (list[Roamer]):
        A list of roamers to construct a string of.
    
    - prefix_str (str):
        A prefix string to concat into the beginning of the final string.
    
    ### Returns:
        A pretty string with roamers, their name, region, and where they can be found.
    '''
    final_str_list = []

    # If prefix_str is given, concat it at the beginning
    if prefix_str != None:
        final_str_list.append("## " + prefix_str + "\n")
    
    for roamer in roamers:
        # Placeholder null check until every region has a set of roamers
        if roamer == None:
            continue
        
        # Construct all lines into a list
        final_str_list.append(f"## {roamer.region}:\n")
        final_str_list.append(f"- {roamer.name}\n")
        final_str_list.append(f"- Can be found outdoors in: {roamer.get_avail_locations()}\n\n")

    # Return a concatenated string of all lines in the list
    return ''.join(final_str_list)

def print_avail_roamers(roamers:list[Roamer],
                        prefix_str:str = None):
    '''
    Nicely prints all the currently available roamers in each region.
    Wrapper for the function 'get_avail_roamers_str()'

    ### Parameters:
    - roamers (list[Roamer]):
        The given roamers to print.
    
    - prefix_str (str):
        The string to print before printing roamer info.
    '''
    print(get_avail_roamers_str(roamers, prefix_str))



# Current roamers
curr_roamers = get_avail_roamers_in_month(all_roamers, current_month)
print_avail_roamers(curr_roamers, prefix_str=f"Currently available roamers ({current_month_name})")

# Roamers next month
if use_next_month:
    next_roamers = get_avail_roamers_in_month(all_roamers, next_month)
    print_avail_roamers(next_roamers, prefix_str=f"Next available roamers ({next_month_name})")