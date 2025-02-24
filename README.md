# studytime

## Overview
When I first started college, I needed to find a way to organize my time; I needed some sort of planner. I discovered an app called
[Structured](https://structured.app/), which I really liked. It had a feature called the inbox where you could put a list of tasks that 
needed to be done, and also a timeline where you could assign the tasks and time-block your day. I would add all of my outstanding assignments 
to my inbox assigned them a time when I did them.

After my freshman year, I had learned quite a bit about how to do data science in python. Since I had recorded literally every assignment or 
time spent studying into structured, I had a good source of data available to me. There was no way to export data, so I manually went through 
and copied the data into a csv file. Then I used python to make some visualizations with pandas, matplotlib, and seaborn.

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
