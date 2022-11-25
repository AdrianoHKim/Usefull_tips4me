#  5. days left in the year (one line)

import datetime

print((datetime.date(2022, 12, 31) - datetime.date.today()).days)

# in one line:
import datetime; print((datetime.date(2022, 12, 31) - datetime.date.today()).days)  # what about the pep...
