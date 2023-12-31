# --------------------------------------------------------------
# 3rd party imports
# --------------------------------------------------------------
from enumfields import Enum



class UserTitle(Enum):
    mr = 'mr'
    mrs = 'mrs'
    miss = 'miss'
    ms = 'ms'
    other = 'other'

    class Labels:
        mr = 'Mr'
        mrs = 'Mrs'
        miss = 'Miss'
        ms = 'Ms'
        other = 'Other'

    def __repr__(self):
        return self.value


class Gender(Enum):
    female = 'female'
    male = 'male'
    other = 'other'

    class Labels:
        female = 'Female'
        male = 'Male'
        other = 'Other'

    def __repr__(self):
        return self.value
