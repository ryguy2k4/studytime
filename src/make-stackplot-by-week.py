import matplotlib.pyplot as plt
import pandas as pd

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
        'order' : ["CS 307", "CHEM 104/105", "GEOL 432", "ASTR 405", "Research"],
        'colors' : ['orange', 'yellow', 'green', 'blue', 'pink']
    },
}

def to_stack_plot_data(master, term, order=[]):
    df = master[master["term"] == term]
    df = df.groupby(['term', 'week', 'day of week', 'course']).agg('sum')[['duration']].reset_index()
    df = df.pivot(index=['term', "week", 'day of week'], columns='course', values='duration')
    df = df.groupby(['week']).agg('sum')
    if order != []:
        df = df[order]
    return df

### PLOT

fig, ax = plt.subplots(2,2, figsize=[7.5,7.5], sharey=True, sharex=True)

for i, term in enumerate(['fa23', 'sp24', 'fa24', 'sp25']):
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

    df1 = to_stack_plot_data(master, term, classes_and_colors[term]['order'])
    ax[x,y].stackplot(df1.index, [df1[col]/60 for col in df1.columns], labels=df1.columns, colors=classes_and_colors[term]['colors'])
    ax[x,y].grid(axis='y', ls='dotted')
    ax[x,y].legend(df1.columns)
    if (x == 1):
        ax[x,y].set_xlabel("Week")
    if (y == 0):
        ax[x,y].set_ylabel("Duration (hrs)")


# FIGURE
# Subplot Titles
ax[0,0].set_title("Fall 2023")
ax[0,1].set_title("Spring 2024")
ax[1,0].set_title("Fall 2024")
ax[1,1].set_title("Spring 2025")

# Axis Limit
plt.xlim(1, 17)

plt.tight_layout()
fig.savefig('results/stackplot_by_class.png')