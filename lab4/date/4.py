from datetime import *

date1 = datetime(2024, 3, 15, 21, 20, 15)
date2 = datetime(2024, 2, 15, 21, 20, 10)
diff = date1 - date2
ans = diff.total_seconds()

print(ans)

