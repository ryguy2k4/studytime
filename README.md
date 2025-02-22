# studytime

## Overview
When I first started college, I needed to find a way to organize my time; I needed some sort of planner. I discovered an app called
[Structured](https://structured.app/) which I really liked. It had a feature called the inbox where you could put a list of tasks that 
needed to be done, and also a timeline where you could assign the tasks and time-block your day. I would add all of my outstanding assignments 
to my inbox and then when I did a task, I assigned it to a time.

After my freshman year, I had learned quite a bit about how to do data science in python, so I decided to do some data science on my study habits, 
since I had recorded literally every assignment and time spent studying into structured. There was no way to export data, so I manually went through 
created a spreadsheet with the data. Then I opened it with pandas in python and used matplotlib and seaborn to make some plots.

Eventually, I realized structured had added functions to be used in Apple's Shortcuts app, and I took advantage of them to export all the data 
for me automatically.

## Results
![Alt text](/results/stackplot_by_class.png?raw=true "Stackplot By Class")

The above stack plot shows how much time I spent studying on a weekly basis per class per semester. So far my fall semesters are typically lighter 
and Spring 2025 is proving to be especially tough.



![Alt text](/results/day_of_week_barplot.png?raw=true "Day of Week Barplot")

The above barplot shows how much time I spent studying on average each weekday per semester. My study habits can vary day to day, and I see that
I typically don't do much at all on Fridays.

## Future Work
I want to fully automate the process of adding new data by using Apple Shortcuts and making a workflow with snakemake.
