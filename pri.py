# init.py contains package imports and one-time assigned variables
from init import current_month, current_month_name, next_month, next_month_name
# roamer contains the Roamer class
from Roamer import Roamer


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



