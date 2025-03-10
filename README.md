# studytime

## Overview
When I first started college, I needed to find a way to organize my time; I needed some sort of planner. I discovered an app that I liked called
[Structured](https://structured.app/). It had a feature called the inbox to list task that needed to be done, and also a timeline where you could
assign the tasks and time-block your day. I made use of both of these features to organize my time.

After my freshman year, I had learned quite a lot about doing data science in python. Since I had recorded literally all the time I spent on schoolwork
into structured, I had a good source of data available to me. There was no way to export data, so I manually went through and copied the data into
a csv file. Then I used python to make some visualizations with pandas, matplotlib, and seaborn.

Eventually, I realized structured had added functions to be used in Apple's Shortcuts app, and I took advantage of them to export all the data 
for me automatically.

## Repository Structure
* `notebooks`: contains scratch work for data exploration and visualization
* `src`: contains python scripts used to produce results
* `results`: contains visualizations illustrating the data

## Reproducibility

### Environment
All packages used are listed in `requirements.txt`. A detailed document on the computing environment can be found in `environment.md`

### Workflow Automation
I used snakemake to create a reproducible workflow. See `Snakefile` in the root directory.


## Results
![Alt text](/results/stackplot_by_class.png?raw=true "Stackplot By Class")

The above stack plot shows how much time I spent studying on a weekly basis per class per semester. So far my fall semesters are typically lighter 
and Spring 2025 is proving to be especially tough.



![Alt text](/results/barplot_by_weekday.png?raw=true "Day of Week Barplot")

The above barplot shows how much time I spent studying on average each weekday per semester. My study habits can vary day to day, and I see that
I typically don't do much at all on Fridays.

![Alt text](/results/heatmap_by_weekday.png?raw=true "Day of Week Barplot")

The above heatmap shows at which times during the week I most frequently spend studying.

## Future Work
* Explore new visualizations to expand my knowledge of data visualization.
* Analyze additional variables available to look at, such as assignment due dates and assignment names.
* Draw conclusions to improve my study habits in the future.

<a href="https://trackgit.com">
<img src="https://us-central1-trackgit-analytics.cloudfunctions.net/token/ping/m7pcv9r3loyldc8cb1m7" alt="trackgit-views" />
</a>
