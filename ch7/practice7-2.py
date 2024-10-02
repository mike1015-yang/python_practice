# 使⽤者輸入:
# 借書⽇期：格式為「年-⽉-⽇」 
# 可借幾⽇：例如 7 ⽇
# ---------------------------- 
# 顯⽰ 
# 還書⽇期 
# 顯⽰今天是否逾期  
# 未逾期，顯⽰還有幾天才需還書 
# 若逾期，顯⽰逾期天數 
# ------------------------------
# 借書⽇期 (年-⽉-⽇): 2023-4-28 
# 可借幾⽇: 7 
# 2023-05-05 前歸還 
# 今天是 2023-04-29 
# 您必須在 6 天內歸還
# ------------------------------
# 借書⽇期 (年-⽉-⽇): 2023-4-20 
# 可借幾⽇: 7 
# 2023-04-27 前歸還 
# 今天是 2023-04-29 
# 逾期天數: 2

from datetime import date
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta

borrow_date = input(f"借書日期(年-月-日): ")
borrow_day = int(input(f"可借幾日: "))
pmt = "%Y-%m-%d"
borrow_p = datetime.strptime(borrow_date, pmt)
return_date = borrow_p + timedelta(days=borrow_day)
fmt = "%Y/%m/%d"
print(f"{return_date.strftime(fmt)} 前歸還")
print(f"今天是 {date.today()}")
now = datetime.now()
if now > return_date:
    rDelta = relativedelta(dt1=now, dt2=return_date)
    print(f"逾期天數: {rDelta.days}")
else:
    rDelta = relativedelta(dt1=return_date, dt2=now)
    print(f"您必須在{rDelta.days}天內歸還")

