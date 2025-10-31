import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import interp1d
import numpy as np

### DATA
master = pd.read_csv("data/master/studytime.csv")
master["day of week"] = pd.Categorical(master["day of week"], categories=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], ordered=True)

classes_and_colors = {
    'fa23': {
        'order' : ["STAT 107", "PHYS 213/214", "MATH 241", "HIST 164"],
        'colors' : ['orange', 'purple', 'red', 'tan']
    },
    'sp24': {
        'order' : ["STAT 207","MATH 257", "GEOL 107", "ASTR 210", "ANTH 103"],
        'colors' : ['orange', 'red', 'green', 'blue', 'tan']
    },
    'fa24': {
        'order' : ["IS 477", "CHEM 102/103", "GEOL 208", "ASTR 310", "ACES 179"],
        'colors' : ['orange', 'yellow', 'green', 'blue', 'tan']
    },
    'sp25': {
        'order' : ["CS 307", "CHEM 104/105", "GEOL 432", "ASTR 405", "ASTR Research", "RST 100"],
        'colors' : ['orange', 'yellow', 'green', 'blue', 'royalblue', 'tan']
    },
    'fa25': {
        'order' : ["IS 467", "PHYS 225", "MATH 285", "GEOL 436", "GEOL 497", "ASTR Research"],
        'colors' : ['orange', 'purple', 'red', 'green', 'lime', 'royalblue']
    },
}

def to_stack_plot_data(master, term, order=[]):
    df = master[master["term"] == term]
    df = df.groupby(['term', 'week', 'day of week', 'course']).agg('sum')[['duration']].reset_index()
    df = df.pivot(index=['term', "week", 'day of week'], columns='course', values='duration')
    df = df.groupby(['week']).agg('sum')
    if order != []:
        df = df[order]
    # Ensure all weeks (1 to 17) are present, filling missing weeks with 0
    all_weeks = pd.Index(range(1, 18), name='week')  # Define the full range of weeks
    df = df.reindex(all_weeks, fill_value=0)
    
    return df

### PLOT

fig, ax = plt.subplots(3,2, figsize=[8,11], sharey=True, sharex=True)

for i, term in enumerate(['fa23', 'sp24', 'fa24', 'sp25', 'fa25']):
    if i == 0:
        x=0
        y=0
    if i == 1:
        x=0
        y=1
    if i == 2:
        x=1
        y=0
    if i == 3:
        x=1
        y=1
    if i == 4:
        x=2
        y=0

    df1 = to_stack_plot_data(master, term, classes_and_colors[term]['order'])
    df1.plot(kind='bar', stacked=True, color=classes_and_colors[term]['colors'], width=1, ax=ax[x,y])
    ax[x,y].grid(axis='y', ls='dotted')
    ax[x,y].legend(df1.columns)
    if (x == 1):
        ax[x,y].set_xlabel("Week")
    if (y == 0):
        ax[x,y].set_ylabel("Duration (min)")

    ax[x,y].set_xlim(-0.5, 17)
    ax[x,y].set_ylim(0, 3000)


# FIGURE
# Subplot Titles
ax[0,0].set_title("Fall 2023")
ax[0,1].set_title("Spring 2024")
ax[1,0].set_title("Fall 2024")
ax[1,1].set_title("Spring 2025")
ax[2,0].set_title("Fall 2025")

# Axis Limit
plt.xlim(-0.5, 17)
plt.ylim(0, 2000)

plt.tight_layout()
fig.savefig('results/stackplot_by_class.png')