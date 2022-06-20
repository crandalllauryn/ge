import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime, timedelta
from collections import defaultdict
import collections
import numpy as np

dev = 'Development'
done = 'Done'

#Artifacts 
dc = 'D&C'
hltp = 'HLTP'
lltc = 'LLTC'
lltp = 'LLTP'
#Features
approach = 'Approach Vref Entry'
airport = 'Airport entries'
arrival = 'Arrival entries'
con = 'Constraints'
departure = 'Departure entries'

# plot set up

plt.style.use('seaborn-whitegrid')
plt.rcParams["figure.autolayout"] = True

path = r'C:\Users\223050503\Downloads\Mission 3.xlsx'

# variable set up

done_dict = {}
dev_dict = {}
due_done_dict = {}
due_date_dict = {}
ontime_tasks_by_week = defaultdict(int)
late_tasks_by_week = defaultdict(int)

# pull Teams Excel Data
df = pd.read_excel(path, index_col=0, header=0)
df2 = df.dropna(subset=['Due Date'])

task_name = list(df2.iloc[:, 0])
bucket_name = list(df2.iloc[:, 1])
due_date = pd.to_datetime(list(df2.iloc[:, 8])).strftime('%m/%d/%y')
current_date = pd.to_datetime(list(df2.iloc[:, 16])).strftime('%m/%d/%y')

#Delivery DeltaTime
current_task = ''

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and task_name[i] == task_name[j]:
            found = True
            break
    if found and current_task != task_name[i]:
        due_done_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]
    

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and task_name[i] == task_name[j] and task_name[i] in due_done_dict:
            found = True
            break
    if found and current_task != task_name[i]:
        due_date_dict[task_name[i]] = due_date[i]
        current_task = task_name[i]

current_task = ''
due_done_dict = {}

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and task_name[i] == task_name[j] and task_name[i] in due_date_dict:
            found = True
            break
    if found and current_task != task_name[i]:
        due_done_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

for task_name in due_done_dict:
    a = due_done_dict[task_name]
    b = due_date_dict[task_name]
    c = datetime.strptime(a, '%m/%d/%y')
    d = datetime.strptime(b, '%m/%d/%y')
    delta_time = c - d
    delta_time = delta_time.days
    week_num = c - timedelta(days = c.weekday())
    week_num = week_num.strftime('%m/%d/%y')
    if delta_time <= 3:
        ontime_tasks_by_week[week_num] += 1
    elif delta_time > 3:
        late_tasks_by_week[week_num] += 1

ontime_tasks_by_week = collections.OrderedDict(sorted(ontime_tasks_by_week.items()))
ontime_tasks_by_week = dict(ontime_tasks_by_week)
late_tasks_by_week = collections.OrderedDict(sorted(late_tasks_by_week.items()))
late_tasks_by_week = dict(late_tasks_by_week)

weeks = list(ontime_tasks_by_week.keys())
weeks.sort()
ontime_items = list(ontime_tasks_by_week.values())
late_items = list(late_tasks_by_week.values())

pos = np.arange(len(ontime_tasks_by_week))
bar_width = 0.35
legend = ['Ontime', 'Late']

plt.bar(pos, ontime_items, bar_width, tick_label = weeks, color = 'green', edgecolor='black')
plt.bar(pos+bar_width, late_items, bar_width, tick_label = weeks, color = 'red', edgecolor='black')

plt.legend(legend, loc = 2)
plt.title('Weekly Delivery Delta')
plt.xlabel('Completion Week')
plt.xticks(rotation=90, fontsize='medium')
plt.ylabel('Items Completed')

plt.savefig('overall_late_bar.png')

plt.show()