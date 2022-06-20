import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime, timedelta
from collections import defaultdict

# Status
dev = 'Development'
done = 'Done'

# Artifacts
dc = 'D&C'
hltp = 'HLTP'
hltc = 'HLTC'
lltc = 'LLTC'
lltp = 'LLTP'

# Features
approach = 'Approach'
airport = 'Airport'
arrival = 'Arrival'
con = 'Constraints'
dept = 'Departure'

# plot set up
plt.style.use('seaborn-whitegrid')
plt.rcParams["figure.autolayout"] = True

path = r'C:\Users\223050503\Downloads\Mission 3.xlsx'

# variable set up
x = []
y = []
late_list = []
ontime_list = []
done_dict = {}
dev_dict = {}
due_done_dict = {}
due_date_dict = {}
ontime_tasks_by_week = defaultdict(int)
late_tasks_by_week = defaultdict(int)

# Teams Excel Data
df = pd.read_excel(path, header=0)
df2 = df.dropna(subset=['Labels'])
df3 = df.dropna(subset=['Due Date'])
df4 = df.dropna(subset=['Due Date', 'Labels'])

task_name = list(df2.iloc[:, 0])
bucket_name = list(df2.iloc[:, 2])
current_date = pd.to_datetime(list(df2.iloc[:, 17])).strftime('%m/%d/%y')

# CYCLE TIME
current_task = ''

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and task_name[i] == task_name[j]:
            found = True
            break
    if found and current_task != task_name[i]:
        done_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

current_task = ''

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if dev in bucket_name[i] and task_name[i] == task_name[j] and task_name[i] in done_dict:
            found = True
            break
    if found and current_task != task_name[i]:
        dev_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

current_task = ''
done_dict = {}

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and task_name[i] == task_name[j] and task_name[i] in dev_dict:
            found = True
            break
    if found and current_task != task_name[i]:
        done_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

for task_name in done_dict:
    a = done_dict[task_name]
    b = dev_dict[task_name]
    c = datetime.strptime(a, '%m/%d/%y')
    d = datetime.strptime(b, '%m/%d/%y')
    cycle_time = c - d
    cycle_time = cycle_time.days
    x.append(a)
    x = sorted(x)
    y.append(cycle_time)

ax = plt.subplot()

plt.plot(x, y, 'o')

n = len(y)
y.sort()

if n % 2 == 0:
    median1 = y[n//2]
    median2 = y[n//2-1]
    median = (median1 + median2)//2
else:
    median = y[n//2]

ax.axhline(median, label='Median Cycle Time', linestyle='--')

plt.legend(loc='upper right')
plt.title('Cycle Time of Done Items')
plt.xlabel('Completion Date')
plt.xticks(rotation=90, fontsize='medium')
plt.ylabel('Cycle Time Days')

plt.savefig('mission3_overall_cycle.png')
plt.clf()

print("Our overall cycle time median is: " + str(median) + " days")

# reset data
done_dict = {}
dev_dict = {}
x = []
y = []
n = ''
median1 = ''
median2 = ''
median = ''

task_name = list(df2.iloc[:, 0])
bucket_name = list(df2.iloc[:, 2])
label_name = list(df2.iloc[:, 16])
current_date = pd.to_datetime(list(df2.iloc[:, 17])).strftime('%m/%d/%y')

# D&C
current_task = ''

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and dc in label_name[i] and task_name[i] == task_name[j]:
            found = True
            break
    if found and current_task != task_name[i]:
        done_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

current_task = ''

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if dev in bucket_name[i] and dc in label_name[i] and task_name[i] == task_name[j] and task_name[i] in done_dict:
            found = True
            break
    if found and current_task != task_name[i]:
        dev_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

current_task = ''
done_dict = {}

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and dc in label_name[i] and task_name[i] == task_name[j] and task_name[i] in dev_dict:
            found = True
            break
    if found and current_task != task_name[i]:
        done_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

for task_name in done_dict:
    a = done_dict[task_name]
    b = dev_dict[task_name]
    c = datetime.strptime(a, '%m/%d/%y')
    d = datetime.strptime(b, '%m/%d/%y')
    cycle_time = c - d
    cycle_time = cycle_time.days
    x.append(a)
    x = sorted(x)
    y.append(cycle_time)

ax = plt.subplot()

plt.plot(x, y, 'o')

n = len(y)
y.sort()

if n % 2 == 0:
    median1 = y[n//2]
    median2 = y[n//2-1]
    median = (median1 + median2)//2
else:
    median = y[n//2]

ax.axhline(median, label='Median Cycle Time', linestyle='--')

plt.legend(loc='upper right')
plt.title('Cycle Time of D&C Items')
plt.xlabel('Completion Date')
plt.xticks(rotation=90, fontsize='medium')
plt.ylabel('Cycle Time Days')

plt.savefig('mission3_D&C_cycle.png')
plt.clf()

print("Our D&C cycle time median is: " + str(median) + " days")

done_dict = {}
dev_dict = {}
x = []
y = []
n = ''
median1 = ''
median2 = ''
median = ''

task_name = list(df2.iloc[:, 0])
bucket_name = list(df2.iloc[:, 2])
label_name = list(df2.iloc[:, 16])
current_date = pd.to_datetime(list(df2.iloc[:, 17])).strftime('%m/%d/%y')

# HLTP
current_task = ''

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and hltp in label_name[i] and task_name[i] == task_name[j]:
            found = True
            break
    if found and current_task != task_name[i]:
        done_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

current_task = ''

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if dev in bucket_name[i] and hltp in label_name[i] and task_name[i] == task_name[j] and task_name[i] in done_dict:
            found = True
            break
    if found and current_task != task_name[i]:
        dev_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

current_task = ''
done_dict = {}

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and hltp in label_name[i] and task_name[i] == task_name[j] and task_name[i] in dev_dict:
            found = True
            break
    if found and current_task != task_name[i]:
        done_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

for task_name in done_dict:
    a = done_dict[task_name]
    b = dev_dict[task_name]
    c = datetime.strptime(a, '%m/%d/%y')
    d = datetime.strptime(b, '%m/%d/%y')
    cycle_time = c - d
    cycle_time = cycle_time.days
    x.append(a)
    x = sorted(x)
    y.append(cycle_time)

ax = plt.subplot()

plt.plot(x, y, 'o')

n = len(y)
y.sort()

if n % 2 == 0:
    median1 = y[n//2]
    median2 = y[n//2-1]
    median = (median1 + median2)//2
else:
    median = y[n//2]

ax.axhline(median, label='Median Cycle Time', linestyle='--')

plt.legend(loc='upper right')
plt.title('Cycle Time of HLTP Items')
plt.xlabel('Completion Date')
plt.xticks(rotation=90, fontsize='medium')
plt.ylabel('Cycle Time Days')

plt.savefig('mission3_HLTP_cycle.png')
plt.clf()

print("Our HLTP cycle time median is: " + str(median) + " days")

done_dict = {}
dev_dict = {}
x = []
y = []
n = ''
median1 = ''
median2 = ''
median = ''

task_name = list(df2.iloc[:, 0])
bucket_name = list(df2.iloc[:, 2])
label_name = list(df2.iloc[:, 16])
current_date = pd.to_datetime(list(df2.iloc[:, 17])).strftime('%m/%d/%y')

# HLTC
current_task = ''

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and hltc in label_name[i] and task_name[i] == task_name[j]:
            found = True
            break
    if found and current_task != task_name[i]:
        done_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

current_task = ''

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if dev in bucket_name[i] and hltc in label_name[i] and task_name[i] == task_name[j] and task_name[i] in done_dict:
            found = True
            break
    if found and current_task != task_name[i]:
        dev_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

current_task = ''
done_dict = {}

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and hltc in label_name[i] and task_name[i] == task_name[j] and task_name[i] in dev_dict:
            found = True
            break
    if found and current_task != task_name[i]:
        done_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

for task_name in done_dict:
    a = done_dict[task_name]
    b = dev_dict[task_name]
    c = datetime.strptime(a, '%m/%d/%y')
    d = datetime.strptime(b, '%m/%d/%y')
    cycle_time = c - d
    cycle_time = cycle_time.days
    x.append(a)
    x = sorted(x)
    y.append(cycle_time)

ax = plt.subplot()

plt.plot(x, y, 'o')

n = len(y)
y.sort()

if n % 2 == 0:
    median1 = y[n//2]
    median2 = y[n//2-1]
    median = (median1 + median2)//2
else:
    median = y[n//2]

ax.axhline(median, label='Median Cycle Time', linestyle='--')

plt.legend(loc='upper right')
plt.title('Cycle Time of HLTC Items')
plt.xlabel('Completion Date')
plt.xticks(rotation=90, fontsize='medium')
plt.ylabel('Cycle Time Days')

plt.savefig('mission3_HLTC_cycle.png')
plt.clf()

print("Our HLTC cycle time median is: " + str(median) + " days")

done_dict = {}
dev_dict = {}
x = []
y = []
n = ''
median1 = ''
median2 = ''
median = ''

task_name = list(df2.iloc[:, 0])
bucket_name = list(df2.iloc[:, 2])
label_name = list(df2.iloc[:, 16])
current_date = pd.to_datetime(list(df2.iloc[:, 17])).strftime('%m/%d/%y')

# LLTP
current_task = ''

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and lltp in label_name[i] and task_name[i] == task_name[j]:
            found = True
            break
    if found and current_task != task_name[i]:
        done_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

current_task = ''

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if dev in bucket_name[i] and lltp in label_name[i] and task_name[i] == task_name[j] and task_name[i] in done_dict:
            found = True
            break
    if found and current_task != task_name[i]:
        dev_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

current_task = ''
done_dict = {}

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and lltp in label_name[i] and task_name[i] == task_name[j] and task_name[i] in dev_dict:
            found = True
            break
    if found and current_task != task_name[i]:
        done_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

for task_name in done_dict:
    a = done_dict[task_name]
    b = dev_dict[task_name]
    c = datetime.strptime(a, '%m/%d/%y')
    d = datetime.strptime(b, '%m/%d/%y')
    cycle_time = c - d
    cycle_time = cycle_time.days
    x.append(a)
    x = sorted(x)
    y.append(cycle_time)

ax = plt.subplot()

plt.plot(x, y, 'o')

n = len(y)
y.sort()

if n % 2 == 0:
    median1 = y[n//2]
    median2 = y[n//2-1]
    median = (median1 + median2)//2
else:
    median = y[n//2]

ax.axhline(median, label='Median Cycle Time', linestyle='--')

plt.legend(loc='upper right')
plt.title('Cycle Time of LLTP Items')
plt.xlabel('Completion Date')
plt.xticks(rotation=90, fontsize='medium')
plt.ylabel('Cycle Time Days')

plt.savefig('mission3_LLTP_cycle.png')
plt.clf()

print("Our LLTP cycle time median is: " + str(median) + " days")

done_dict = {}
dev_dict = {}
x = []
y = []
n = ''
median1 = ''
median2 = ''
median = ''

task_name = list(df2.iloc[:, 0])
bucket_name = list(df2.iloc[:, 2])
label_name = list(df2.iloc[:, 16])
current_date = pd.to_datetime(list(df2.iloc[:, 17])).strftime('%m/%d/%y')

# LLTC
current_task = ''

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and lltc in label_name[i] and task_name[i] == task_name[j]:
            found = True
            break
    if found and current_task != task_name[i]:
        done_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

current_task = ''

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if dev in bucket_name[i] and lltc in label_name[i] and task_name[i] == task_name[j] and task_name[i] in done_dict:
            found = True
            break
    if found and current_task != task_name[i]:
        dev_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

current_task = ''
done_dict = {}

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and lltc in label_name[i] and task_name[i] == task_name[j] and task_name[i] in dev_dict:
            found = True
            break
    if found and current_task != task_name[i]:
        done_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

for task_name in done_dict:
    a = done_dict[task_name]
    b = dev_dict[task_name]
    c = datetime.strptime(a, '%m/%d/%y')
    d = datetime.strptime(b, '%m/%d/%y')
    cycle_time = c - d
    cycle_time = cycle_time.days
    x.append(a)
    x = sorted(x)
    y.append(cycle_time)

ax = plt.subplot()

plt.plot(x, y, 'o')

n = len(y)
y.sort()

if n % 2 == 0:
    median1 = y[n//2]
    median2 = y[n//2-1]
    median = (median1 + median2)//2
else:
    median = y[n//2]

ax.axhline(median, label='Median Cycle Time', linestyle='--')

plt.legend(loc='upper right')
plt.title('Cycle Time of LLTC Items')
plt.xlabel('Completion Date')
plt.xticks(rotation=90, fontsize='medium')
plt.ylabel('Cycle Time Days')

plt.savefig('mission3_LLTC_cycle.png')
plt.clf()

print("Our LLTC cycle time median is: " + str(median) + " days")

done_dict = {}
dev_dict = {}
x = []
y = []
n = ''
median1 = ''
median2 = ''
median = ''

task_name = list(df2.iloc[:, 0])
bucket_name = list(df2.iloc[:, 2])
label_name = list(df2.iloc[:, 16])
current_date = pd.to_datetime(list(df2.iloc[:, 17])).strftime('%m/%d/%y')

# approach
current_task = ''

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and approach in label_name[i] and task_name[i] == task_name[j]:
            found = True
            break
    if found and current_task != task_name[i]:
        done_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

current_task = ''

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if dev in bucket_name[i] and approach in label_name[i] and task_name[i] == task_name[j] and task_name[i] in done_dict:
            found = True
            break
    if found and current_task != task_name[i]:
        dev_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

current_task = ''
done_dict = {}

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and approach in label_name[i] and task_name[i] == task_name[j] and task_name[i] in dev_dict:
            found = True
            break
    if found and current_task != task_name[i]:
        done_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

for task_name in done_dict:
    a = done_dict[task_name]
    b = dev_dict[task_name]
    c = datetime.strptime(a, '%m/%d/%y')
    d = datetime.strptime(b, '%m/%d/%y')
    cycle_time = c - d
    cycle_time = cycle_time.days
    x.append(a)
    x = sorted(x)
    y.append(cycle_time)

ax = plt.subplot()

plt.plot(x, y, 'o')

n = len(y)
y.sort()

if n % 2 == 0:
    median1 = y[n//2]
    median2 = y[n//2-1]
    median = (median1 + median2)//2
else:
    median = y[n//2]

ax.axhline(median, label='Median Cycle Time', linestyle='--')

plt.legend(loc='upper right')
plt.title('Cycle Time of Approach Items')
plt.xlabel('Completion Date')
plt.xticks(rotation=90, fontsize='medium')
plt.ylabel('Cycle Time Days')

plt.savefig('mission3_approach_cycle.png')
plt.clf()

print("Our Approach Verf Entry cycle time median is: " + str(median) + " days")

done_dict = {}
dev_dict = {}
x = []
y = []
n = ''
median1 = ''
median2 = ''
median = ''

task_name = list(df2.iloc[:, 0])
bucket_name = list(df2.iloc[:, 2])
label_name = list(df2.iloc[:, 16])
current_date = pd.to_datetime(list(df2.iloc[:, 17])).strftime('%m/%d/%y')

# airport
current_task = ''

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and airport in label_name[i] and task_name[i] == task_name[j]:
            found = True
            break
    if found and current_task != task_name[i]:
        done_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

current_task = ''

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if dev in bucket_name[i] and airport in label_name[i] and task_name[i] == task_name[j] and task_name[i] in done_dict:
            found = True
            break
    if found and current_task != task_name[i]:
        dev_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

current_task = ''
done_dict = {}

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and airport in label_name[i] and task_name[i] == task_name[j] and task_name[i] in dev_dict:
            found = True
            break
    if found and current_task != task_name[i]:
        done_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

for task_name in done_dict:
    a = done_dict[task_name]
    b = dev_dict[task_name]
    c = datetime.strptime(a, '%m/%d/%y')
    d = datetime.strptime(b, '%m/%d/%y')
    cycle_time = c - d
    cycle_time = cycle_time.days
    x.append(a)
    x = sorted(x)
    y.append(cycle_time)

ax = plt.subplot()

plt.plot(x, y, 'o')

n = len(y)
y.sort()

if n % 2 == 0:
    median1 = y[n//2]
    median2 = y[n//2-1]
    median = (median1 + median2)//2
else:
    median = y[n//2]

ax.axhline(median, label='Median Cycle Time', linestyle='--')

plt.legend(loc='upper right')
plt.title('Cycle Time of Airport Entries Items')
plt.xlabel('Completion Date')
plt.xticks(rotation=90, fontsize='medium')
plt.ylabel('Cycle Time Days')

plt.savefig('mission3_airport_cycle.png')
plt.clf()

print("Our Airport Entries cycle time median is: " + str(median) + " days")

done_dict = {}
dev_dict = {}
x = []
y = []
n = ''
median1 = ''
median2 = ''
median = ''

task_name = list(df2.iloc[:, 0])
bucket_name = list(df2.iloc[:, 2])
label_name = list(df2.iloc[:, 16])
current_date = pd.to_datetime(list(df2.iloc[:, 17])).strftime('%m/%d/%y')

# arrival
current_task = ''

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and arrival in label_name[i] and task_name[i] == task_name[j]:
            found = True
            break
    if found and current_task != task_name[i]:
        done_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

current_task = ''

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if dev in bucket_name[i] and arrival in label_name[i] and task_name[i] == task_name[j] and task_name[i] in done_dict:
            found = True
            break
    if found and current_task != task_name[i]:
        dev_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

current_task = ''
done_dict = {}

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and arrival in label_name[i] and task_name[i] == task_name[j] and task_name[i] in dev_dict:
            found = True
            break
    if found and current_task != task_name[i]:
        done_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

for task_name in done_dict:
    a = done_dict[task_name]
    b = dev_dict[task_name]
    c = datetime.strptime(a, '%m/%d/%y')
    d = datetime.strptime(b, '%m/%d/%y')
    cycle_time = c - d
    cycle_time = cycle_time.days
    x.append(a)
    x = sorted(x)
    y.append(cycle_time)

ax = plt.subplot()

plt.plot(x, y, 'o')

n = len(y)
y.sort()

if n % 2 == 0:
    median1 = y[n//2]
    median2 = y[n//2-1]
    median = (median1 + median2)//2
else:
    median = y[n//2]

ax.axhline(median, label='Median Cycle Time', linestyle='--')

plt.legend(loc='upper right')
plt.title('Cycle Time of Arrival Entries Items')
plt.xlabel('Completion Date')
plt.xticks(rotation=90, fontsize='medium')
plt.ylabel('Cycle Time Days')

plt.savefig('mission3_arrival_cycle.png')
plt.clf()

print("Our Arrival Entries cycle time median is: " + str(median) + " days")

done_dict = {}
dev_dict = {}
x = []
y = []
n = ''
median1 = ''
median2 = ''
median = ''

task_name = list(df2.iloc[:, 0])
bucket_name = list(df2.iloc[:, 2])
label_name = list(df2.iloc[:, 16])
current_date = pd.to_datetime(list(df2.iloc[:, 17])).strftime('%m/%d/%y')

# constraints

# dept
current_task = ''

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and dept in label_name[i] and task_name[i] == task_name[j]:
            found = True
            break
    if found and current_task != task_name[i]:
        done_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

current_task = ''

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if dev in bucket_name[i] and dept in label_name[i] and task_name[i] == task_name[j] and task_name[i] in done_dict:
            found = True
            break
    if found and current_task != task_name[i]:
        dev_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

current_task = ''
done_dict = {}

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and dept in label_name[i] and task_name[i] == task_name[j] and task_name[i] in dev_dict:
            found = True
            break
    if found and current_task != task_name[i]:
        done_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

for task_name in done_dict:
    a = done_dict[task_name]
    b = dev_dict[task_name]
    c = datetime.strptime(a, '%m/%d/%y')
    d = datetime.strptime(b, '%m/%d/%y')
    cycle_time = c - d
    cycle_time = cycle_time.days
    x.append(a)
    x = sorted(x)
    y.append(cycle_time)

ax = plt.subplot()

plt.plot(x, y, 'o')

n = len(y)
y.sort()

if n % 2 == 0:
    median1 = y[n//2]
    median2 = y[n//2-1]
    median = (median1 + median2)//2
else:
    median = y[n//2]

ax.axhline(median, label='Median Cycle Time', linestyle='--')

plt.legend(loc='upper right')
plt.title('Cycle Time of Departure Items')
plt.xlabel('Completion Date')
plt.xticks(rotation=90, fontsize='medium')
plt.ylabel('Cycle Time Days')

plt.savefig('mission3_dept_cycle.png')
plt.clf()

print("Our Departure cycle time median is: " + str(median) + " days")

done_dict = {}
dev_dict = {}
x = []
y = []
n = ''
median1 = ''
median2 = ''
median = ''

task_name = list(df3.iloc[:, 0])
bucket_name = list(df3.iloc[:, 2])
due_date = pd.to_datetime(list(df3.iloc[:, 9])).strftime('%m/%d/%y')
current_date = pd.to_datetime(list(df3.iloc[:, 17])).strftime('%m/%d/%y')

# due date graph
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
    if delta_time <= 3:
        ontime_list.append(delta_time)
    elif delta_time > 3:
        late_list.append(delta_time)
    x.append(a)
    x = sorted(x)
    y.append(delta_time)

ax = plt.subplot()

plt.plot(x, y, 'o')

n = len(y)
y.sort()
if n % 2 == 0:
    median1 = y[n//2]
    median2 = y[n//2-1]
    median = (median1 + median2)//2
else:
    median = y[n//2]

ax.axhline(median, label='Median Arrival Time', linestyle='--')

plt.legend(loc='upper right')
plt.title('On Time Delivery')
plt.xlabel('Completion Date')
plt.xticks(rotation=90, fontsize='medium')
plt.ylabel('On Time Delta')

plt.savefig('mission3_overall_delivery.png')
plt.clf()

num_of_due_items = len(due_done_dict)
num_of_ontime = len(ontime_list)
num_of_late = len(late_list)

percent_ontime = round(num_of_ontime/num_of_due_items * 100, 1)
percent_late = round(num_of_late/num_of_due_items * 100, 1)

print("Our overall arrival time median is: " + str(median) + " days")
print("Number of early or on time items: " + str(num_of_ontime) + " items")
print("Number of late items: " + str(num_of_late) + " items")
print("Percentage of early or on time items is: " + str(percent_ontime) + "%")
print("Percentage of late items is: " + str(percent_late) + "%")

due_done_dict = {}
due_date_dict = {}
ontime_list = []
late_list = []
x = []
y = []
n = ''
median1 = ''
median2 = ''
median = ''

task_name = list(df4.iloc[:, 0])
bucket_name = list(df4.iloc[:, 2])
label_name = list(df4.iloc[:, 16])
due_date = pd.to_datetime(list(df4.iloc[:, 9])).strftime('%m/%d/%y')
current_date = pd.to_datetime(list(df4.iloc[:, 17])).strftime('%m/%d/%y')

# D&C due date graph
current_task = ''

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and dc in label_name[i] and task_name[i] == task_name[j]:
            found = True
            break
    if found and current_task != task_name[i]:
        due_done_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and dc in label_name[i] and task_name[i] == task_name[j] and task_name[i] in due_done_dict:
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
        if done in bucket_name[i] and dc in label_name[i] and task_name[i] == task_name[j] and task_name[i] in due_date_dict:
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
    if delta_time <= 3:
        ontime_list.append(delta_time)
    elif delta_time > 3:
        late_list.append(delta_time)
    x.append(a)
    x = sorted(x)
    y.append(delta_time)

ax = plt.subplot()

plt.plot(x, y, 'o')

n = len(y)
y.sort()
if n % 2 == 0:
    median1 = y[n//2]
    median2 = y[n//2-1]
    median = (median1 + median2)//2
else:
    median = y[n//2]

ax.axhline(median, label='Median Arrival Time', linestyle='--')

plt.legend(loc='upper right')
plt.title('D&C On Time Delivery')
plt.xlabel('Completion Date')
plt.xticks(rotation=90, fontsize='medium')
plt.ylabel('On Time Delta')

plt.savefig('mission3_D&C_delivery.png')
plt.clf()

num_of_due_items = len(due_done_dict)
num_of_ontime = len(ontime_list)
num_of_late = len(late_list)

percent_ontime = round(num_of_ontime/num_of_due_items * 100, 1)
percent_late = round(num_of_late/num_of_due_items * 100, 1)

print("Our D&C arrival time median is: " + str(median) + " days")
print("Number of D&C early or on time items: " + str(num_of_ontime) + " items")
print("Number of D&C late items: " + str(num_of_late) + " items")
print("Percentage of D&C early or on time items is: " + str(percent_ontime) + "%")
print("Percentage of D&C late items is: " + str(percent_late) + "%")

due_done_dict = {}
due_date_dict = {}
ontime_list = []
late_list = []
x = []
y = []
n = ''
median1 = ''
median2 = ''
median = ''

task_name = list(df4.iloc[:, 0])
bucket_name = list(df4.iloc[:, 2])
label_name = list(df4.iloc[:, 16])
due_date = pd.to_datetime(list(df4.iloc[:, 9])).strftime('%m/%d/%y')
current_date = pd.to_datetime(list(df4.iloc[:, 17])).strftime('%m/%d/%y')

# hltp due date graph
current_task = ''

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and hltp in label_name[i] and task_name[i] == task_name[j]:
            found = True
            break
    if found and current_task != task_name[i]:
        due_done_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and hltp in label_name[i] and task_name[i] == task_name[j] and task_name[i] in due_done_dict:
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
        if done in bucket_name[i] and hltp in label_name[i] and task_name[i] == task_name[j] and task_name[i] in due_date_dict:
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
    if delta_time <= 3:
        ontime_list.append(delta_time)
    elif delta_time > 3:
        late_list.append(delta_time)
    x.append(a)
    x = sorted(x)
    y.append(delta_time)

ax = plt.subplot()

plt.plot(x, y, 'o')

n = len(y)
y.sort()
if n % 2 == 0:
    median1 = y[n//2]
    median2 = y[n//2-1]
    median = (median1 + median2)//2
else:
    median = y[n//2]

ax.axhline(median, label='Median Arrival Time', linestyle='--')

plt.legend(loc='upper right')
plt.title('HLTP On Time Delivery')
plt.xlabel('Completion Date')
plt.xticks(rotation=90, fontsize='medium')
plt.ylabel('On Time Delta')

plt.savefig('mission3_HLTP_delivery.png')
plt.clf()

num_of_due_items = len(due_done_dict)
num_of_ontime = len(ontime_list)
num_of_late = len(late_list)

percent_ontime = round(num_of_ontime/num_of_due_items * 100, 1)
percent_late = round(num_of_late/num_of_due_items * 100, 1)

print("Our HLTP arrival time median is: " + str(median) + " days")
print("Number of HLTP early or on time items: " + str(num_of_ontime) + " items")
print("Number of HLTP late items: " + str(num_of_late) + " items")
print("Percentage of HLTP early or on time items is: " + str(percent_ontime) + "%")
print("Percentage of HLTP late items is: " + str(percent_late) + "%")

due_done_dict = {}
due_date_dict = {}
ontime_list = []
late_list = []
x = []
y = []
n = ''
median1 = ''
median2 = ''
median = ''

task_name = list(df4.iloc[:, 0])
bucket_name = list(df4.iloc[:, 2])
label_name = list(df4.iloc[:, 16])
due_date = pd.to_datetime(list(df4.iloc[:, 9])).strftime('%m/%d/%y')
current_date = pd.to_datetime(list(df4.iloc[:, 17])).strftime('%m/%d/%y')

# hltC due date graph
current_task = ''

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and hltc in label_name[i] and task_name[i] == task_name[j]:
            found = True
            break
    if found and current_task != task_name[i]:
        due_done_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and hltc in label_name[i] and task_name[i] == task_name[j] and task_name[i] in due_done_dict:
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
        if done in bucket_name[i] and hltc in label_name[i] and task_name[i] == task_name[j] and task_name[i] in due_date_dict:
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
    if delta_time <= 3:
        ontime_list.append(delta_time)
    elif delta_time > 3:
        late_list.append(delta_time)
    x.append(a)
    x = sorted(x)
    y.append(delta_time)

ax = plt.subplot()

plt.plot(x, y, 'o')

n = len(y)
y.sort()
if n % 2 == 0:
    median1 = y[n//2]
    median2 = y[n//2-1]
    median = (median1 + median2)//2
else:
    median = y[n//2]

ax.axhline(median, label='Median Arrival Time', linestyle='--')

plt.legend(loc='upper right')
plt.title('HLTC On Time Delivery')
plt.xlabel('Completion Date')
plt.xticks(rotation=90, fontsize='medium')
plt.ylabel('On Time Delta')

plt.savefig('mission3_HLTC_delivery.png')
plt.clf()

num_of_due_items = len(due_done_dict)
num_of_ontime = len(ontime_list)
num_of_late = len(late_list)

percent_ontime = round(num_of_ontime/num_of_due_items * 100, 1)
percent_late = round(num_of_late/num_of_due_items * 100, 1)

print("Our HLTC arrival time median is: " + str(median) + " days")
print("Number of HLTC early or on time items: " + str(num_of_ontime) + " items")
print("Number of HLTC late items: " + str(num_of_late) + " items")
print("Percentage of HLTC early or on time items is: " + str(percent_ontime) + "%")
print("Percentage of HLTC late items is: " + str(percent_late) + "%")

due_done_dict = {}
due_date_dict = {}
ontime_list = []
late_list = []
x = []
y = []
n = ''
median1 = ''
median2 = ''
median = ''

task_name = list(df4.iloc[:, 0])
bucket_name = list(df4.iloc[:, 2])
label_name = list(df4.iloc[:, 16])
due_date = pd.to_datetime(list(df4.iloc[:, 9])).strftime('%m/%d/%y')
current_date = pd.to_datetime(list(df4.iloc[:, 17])).strftime('%m/%d/%y')

# lltc due date graph
current_task = ''

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and lltc in label_name[i] and task_name[i] == task_name[j]:
            found = True
            break
    if found and current_task != task_name[i]:
        due_done_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and lltc in label_name[i] and task_name[i] == task_name[j] and task_name[i] in due_done_dict:
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
        if done in bucket_name[i] and lltc in label_name[i] and task_name[i] == task_name[j] and task_name[i] in due_date_dict:
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
    if delta_time <= 3:
        ontime_list.append(delta_time)
    elif delta_time > 3:
        late_list.append(delta_time)
    x.append(a)
    x = sorted(x)
    y.append(delta_time)

ax = plt.subplot()

plt.plot(x, y, 'o')

n = len(y)
y.sort()
if n % 2 == 0:
    median1 = y[n//2]
    median2 = y[n//2-1]
    median = (median1 + median2)//2
else:
    median = y[n//2]

ax.axhline(median, label='Median Arrival Time', linestyle='--')

plt.legend(loc='upper right')
plt.title('LLTC On Time Delivery')
plt.xlabel('Completion Date')
plt.xticks(rotation=90, fontsize='medium')
plt.ylabel('On Time Delta')

plt.savefig('mission3_LLTC_delivery.png')
plt.clf()

num_of_due_items = len(due_done_dict)
num_of_ontime = len(ontime_list)
num_of_late = len(late_list)

percent_ontime = round(num_of_ontime/num_of_due_items * 100, 1)
percent_late = round(num_of_late/num_of_due_items * 100, 1)

print("Our LLTC arrival time median is: " + str(median) + " days")
print("Number of LLTC early or on time items: " + str(num_of_ontime) + " items")
print("Number of LLTC late items: " + str(num_of_late) + " items")
print("Percentage of LLTC early or on time items is: " + str(percent_ontime) + "%")
print("Percentage of LLTC late items is: " + str(percent_late) + "%")

due_done_dict = {}
due_date_dict = {}
ontime_list = []
late_list = []
x = []
y = []
n = ''
median1 = ''
median2 = ''
median = ''

task_name = list(df4.iloc[:, 0])
bucket_name = list(df4.iloc[:, 2])
label_name = list(df4.iloc[:, 16])
due_date = pd.to_datetime(list(df4.iloc[:, 9])).strftime('%m/%d/%y')
current_date = pd.to_datetime(list(df4.iloc[:, 17])).strftime('%m/%d/%y')

# lltp due date graph
current_task = ''

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and lltp in label_name[i] and task_name[i] == task_name[j]:
            found = True
            break
    if found and current_task != task_name[i]:
        due_done_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and lltp in label_name[i] and task_name[i] == task_name[j] and task_name[i] in due_done_dict:
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
        if done in bucket_name[i] and lltp in label_name[i] and task_name[i] == task_name[j] and task_name[i] in due_date_dict:
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
    if delta_time <= 3:
        ontime_list.append(delta_time)
    elif delta_time > 3:
        late_list.append(delta_time)
    x.append(a)
    x = sorted(x)
    y.append(delta_time)

ax = plt.subplot()

plt.plot(x, y, 'o')

n = len(y)
y.sort()
if n % 2 == 0:
    median1 = y[n//2]
    median2 = y[n//2-1]
    median = (median1 + median2)//2
else:
    median = y[n//2]

ax.axhline(median, label='Median Arrival Time', linestyle='--')

plt.legend(loc='upper right')
plt.title('LLTP On Time Delivery')
plt.xlabel('Completion Date')
plt.xticks(rotation=90, fontsize='medium')
plt.ylabel('On Time Delta')

plt.savefig('mission3_LLTP_delivery.png')
plt.clf()

num_of_due_items = len(due_done_dict)
num_of_ontime = len(ontime_list)
num_of_late = len(late_list)

percent_ontime = round(num_of_ontime/num_of_due_items * 100, 1)
percent_late = round(num_of_late/num_of_due_items * 100, 1)

print("Our LLTP arrival time median is: " + str(median) + " days")
print("Number of LLTP early or on time items: " + str(num_of_ontime) + " items")
print("Number of LLTP late items: " + str(num_of_late) + " items")
print("Percentage of LLTP early or on time items is: " + str(percent_ontime) + "%")
print("Percentage of LLTP late items is: " + str(percent_late) + "%")

due_done_dict = {}
due_date_dict = {}
ontime_list = []
late_list = []
x = []
y = []
n = ''
median1 = ''
median2 = ''
median = ''

task_name = list(df4.iloc[:, 0])
bucket_name = list(df4.iloc[:, 2])
label_name = list(df4.iloc[:, 16])
due_date = pd.to_datetime(list(df4.iloc[:, 9])).strftime('%m/%d/%y')
current_date = pd.to_datetime(list(df4.iloc[:, 17])).strftime('%m/%d/%y')

# approach due date graph
current_task = ''

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and approach in label_name[i] and task_name[i] == task_name[j]:
            found = True
            break
    if found and current_task != task_name[i]:
        due_done_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and approach in label_name[i] and task_name[i] == task_name[j] and task_name[i] in due_done_dict:
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
        if done in bucket_name[i] and approach in label_name[i] and task_name[i] == task_name[j] and task_name[i] in due_date_dict:
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
    if delta_time <= 3:
        ontime_list.append(delta_time)
    elif delta_time > 3:
        late_list.append(delta_time)
    x.append(a)
    x = sorted(x)
    y.append(delta_time)

ax = plt.subplot()

plt.plot(x, y, 'o')

n = len(y)
y.sort()
if n % 2 == 0:
    median1 = y[n//2]
    median2 = y[n//2-1]
    median = (median1 + median2)//2
else:
    median = y[n//2]

ax.axhline(median, label='Median Arrival Time', linestyle='--')

plt.legend(loc='upper right')
plt.title('Approach Entries On Time Delivery')
plt.xlabel('Completion Date')
plt.xticks(rotation=90, fontsize='medium')
plt.ylabel('On Time Delta')

plt.savefig('mission3_approach_delivery.png')
plt.clf()

num_of_due_items = len(due_done_dict)
num_of_ontime = len(ontime_list)
num_of_late = len(late_list)

percent_ontime = round(num_of_ontime/num_of_due_items * 100, 1)
percent_late = round(num_of_late/num_of_due_items * 100, 1)

print("Our Approach Entries arrival time median is: " + str(median) + " days")
print("Number of Approach Entries early or on time items: " +
      str(num_of_ontime) + " items")
print("Number of Approach Entries late items: " + str(num_of_late) + " items")
print("Percentage of Approach Entries early or on time items is: " +
      str(percent_ontime) + "%")
print("Percentage of Approach Entries late items is: " + str(percent_late) + "%")

due_done_dict = {}
due_date_dict = {}
ontime_list = []
late_list = []
x = []
y = []
n = ''
median1 = ''
median2 = ''
median = ''

task_name = list(df4.iloc[:, 0])
bucket_name = list(df4.iloc[:, 2])
label_name = list(df4.iloc[:, 16])
due_date = pd.to_datetime(list(df4.iloc[:, 9])).strftime('%m/%d/%y')
current_date = pd.to_datetime(list(df4.iloc[:, 17])).strftime('%m/%d/%y')

# airport due date graph
current_task = ''

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and airport in label_name[i] and task_name[i] == task_name[j]:
            found = True
            break
    if found and current_task != task_name[i]:
        due_done_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and airport in label_name[i] and task_name[i] == task_name[j] and task_name[i] in due_done_dict:
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
        if done in bucket_name[i] and airport in label_name[i] and task_name[i] == task_name[j] and task_name[i] in due_date_dict:
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
    if delta_time <= 3:
        ontime_list.append(delta_time)
    elif delta_time > 3:
        late_list.append(delta_time)
    x.append(a)
    x = sorted(x)
    y.append(delta_time)

ax = plt.subplot()

plt.plot(x, y, 'o')

n = len(y)
y.sort()
if n % 2 == 0:
    median1 = y[n//2]
    median2 = y[n//2-1]
    median = (median1 + median2)//2
else:
    median = y[n//2]

ax.axhline(median, label='Median Arrival Time', linestyle='--')

plt.legend(loc='upper right')
plt.title('Airport Entries On Time Delivery')
plt.xlabel('Completion Date')
plt.xticks(rotation=90, fontsize='medium')
plt.ylabel('On Time Delta')

plt.savefig('mission3_airport_delivery.png')
plt.clf()

num_of_due_items = len(due_done_dict)
num_of_ontime = len(ontime_list)
num_of_late = len(late_list)

percent_ontime = round(num_of_ontime/num_of_due_items * 100, 1)
percent_late = round(num_of_late/num_of_due_items * 100, 1)

print("Our Airport Entries arrival time median is: " + str(median) + " days")
print("Number of Airport Entries early or on time items: " +
      str(num_of_ontime) + " items")
print("Number of Airport Entries late items: " + str(num_of_late) + " items")
print("Percentage of Airport Entries early or on time items is: " +
      str(percent_ontime) + "%")
print("Percentage of Airport Entries late items is: " + str(percent_late) + "%")

due_done_dict = {}
due_date_dict = {}
ontime_list = []
late_list = []
x = []
y = []
n = ''
median1 = ''
median2 = ''
median = ''

task_name = list(df4.iloc[:, 0])
bucket_name = list(df4.iloc[:, 2])
label_name = list(df4.iloc[:, 16])
due_date = pd.to_datetime(list(df4.iloc[:, 9])).strftime('%m/%d/%y')
current_date = pd.to_datetime(list(df4.iloc[:, 17])).strftime('%m/%d/%y')

# arrival due date graph
current_task = ''

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and arrival in label_name[i] and task_name[i] == task_name[j]:
            found = True
            break
    if found and current_task != task_name[i]:
        due_done_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and arrival in label_name[i] and task_name[i] == task_name[j] and task_name[i] in due_done_dict:
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
        if done in bucket_name[i] and arrival in label_name[i] and task_name[i] == task_name[j] and task_name[i] in due_date_dict:
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
    if delta_time <= 3:
        ontime_list.append(delta_time)
    elif delta_time > 3:
        late_list.append(delta_time)
    x.append(a)
    x = sorted(x)
    y.append(delta_time)

ax = plt.subplot()

plt.plot(x, y, 'o')

n = len(y)
y.sort()
if n % 2 == 0:
    median1 = y[n//2]
    median2 = y[n//2-1]
    median = (median1 + median2)//2
else:
    median = y[n//2]

ax.axhline(median, label='Median Arrival Time', linestyle='--')

plt.legend(loc='upper right')
plt.title('Arrival Entries On Time Delivery')
plt.xlabel('Completion Date')
plt.xticks(rotation=90, fontsize='medium')
plt.ylabel('On Time Delta')

plt.savefig('mission3_arrival_delivery.png')
plt.clf()

num_of_due_items = len(due_done_dict)
num_of_ontime = len(ontime_list)
num_of_late = len(late_list)

percent_ontime = round(num_of_ontime/num_of_due_items * 100, 1)
percent_late = round(num_of_late/num_of_due_items * 100, 1)

print("Our Arrival Entries arrival time median is: " + str(median) + " days")
print("Number of Arrival Entries early or on time items: " +
      str(num_of_ontime) + " items")
print("Number of Arrival Entries late items: " + str(num_of_late) + " items")
print("Percentage of Arrival Entries early or on time items is: " +
      str(percent_ontime) + "%")
print("Percentage of Arrival Entries late items is: " + str(percent_late) + "%")

due_done_dict = {}
due_date_dict = {}
ontime_list = []
late_list = []
x = []
y = []
n = ''
median1 = ''
median2 = ''
median = ''

task_name = list(df4.iloc[:, 0])
bucket_name = list(df4.iloc[:, 2])
label_name = list(df4.iloc[:, 16])
due_date = pd.to_datetime(list(df4.iloc[:, 9])).strftime('%m/%d/%y')
current_date = pd.to_datetime(list(df4.iloc[:, 17])).strftime('%m/%d/%y')

# dept due date graph
current_task = ''

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and dept in label_name[i] and task_name[i] == task_name[j]:
            found = True
            break
    if found and current_task != task_name[i]:
        due_done_dict[task_name[i]] = current_date[i]
        current_task = task_name[i]

for j in range(len(task_name)):
    found = False
    for i in range(len(task_name)):
        if done in bucket_name[i] and dept in label_name[i] and task_name[i] == task_name[j] and task_name[i] in due_done_dict:
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
        if done in bucket_name[i] and dept in label_name[i] and task_name[i] == task_name[j] and task_name[i] in due_date_dict:
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
    if delta_time <= 3:
        ontime_list.append(delta_time)
    elif delta_time > 3:
        late_list.append(delta_time)
    x.append(a)
    x = sorted(x)
    y.append(delta_time)

ax = plt.subplot()

plt.plot(x, y, 'o')

n = len(y)
y.sort()
if n % 2 == 0:
    median1 = y[n//2]
    median2 = y[n//2-1]
    median = (median1 + median2)//2
else:
    median = y[n//2]

ax.axhline(median, label='Median Arrival Time', linestyle='--')

plt.legend(loc='upper right')
plt.title('Departure On Time Delivery')
plt.xlabel('Completion Date')
plt.xticks(rotation=90, fontsize='medium')
plt.ylabel('On Time Delta')

plt.savefig('mission3_dept_delivery.png')
plt.clf()

num_of_due_items = len(due_done_dict)
num_of_ontime = len(ontime_list)
num_of_late = len(late_list)

percent_ontime = round(num_of_ontime/num_of_due_items * 100, 1)
percent_late = round(num_of_late/num_of_due_items * 100, 1)

print("Our Departure arrival time median is: " + str(median) + " days")
print("Number of Departure early or on time items: " +
      str(num_of_ontime) + " items")
print("Number of Departure late items: " + str(num_of_late) + " items")
print("Percentage of Departure early or on time items is: " +
      str(percent_ontime) + "%")
print("Percentage of Departure late items is: " + str(percent_late) + "%")
