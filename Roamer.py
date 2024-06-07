from init import month_names
from init import current_month

class Roamer:
    def __init__(self,
                 name:str,
                 region:str,
                 avail_months:list[int],
                 avail_locations:list[str]):
        self.name = name
        self.region = region
        self.avail_months = avail_months
        self.avail_locations = avail_locations
    

    def is_currently_available(self,
                               current_month:int
                               ) -> bool:
        return current_month in self.avail_months
    

    def get_avail_months(self,
                         months:list[str]
                         )-> str:
        ret_str = ''

        for month in self.avail_months:
            ret_str += months[month]

            if month != self.avail_months[-1]:
                ret_str += ", "
        
        return ret_str
    

    def get_avail_locations(self)-> str:
        ret_str = ''

        for location in self.avail_locations:
            ret_str += location

            if location is not self.avail_locations[-1]:
                ret_str += ", "
        
        return ret_str


    def __str__(self
                ) -> str:

        return ''.join([
               f"## {self.name}:\n",
               f"Region: {self.region}\n",
               f"Can be found outdoors in: {self.get_avail_locations()}\n",
               f"Available months: {self.get_avail_months(month_names)}\n",
               f"Currently available: {self.is_currently_available(current_month)}\n"])
