import pandas as pd

def prepare_data(filename, term):
    due_dates = []
    courses = []
    titles = []
    pcts = []

    df = pd.read_json(filename)

    # parse titles
    for title in df['title']:
        # Has a due date
        if str(title).startswith(('Sun', 'Mon', 'Tue', "Wed", "Thu", "Fri", "Sat")):
            subs = str(title).split(' ')
            due_dates.append(subs[1])
            courses.append(subs[2])
            # Has a progress pct
            if str(title).__contains__('%'):
                titles.append(" ".join(subs[3:-1]))
                pcts.append(subs[-1].strip('[').strip(']').strip('%'))
            else:
                titles.append(" ".join(subs[3::]))
                pcts.append(None)
        # Does not have a due date
        else:
            subs = str(title).split(' ')
            due_dates.append(None)
            courses.append(subs[0])
            # Has a progress pct
            if str(title).__contains__('%'):
                titles.append(" ".join(subs[1:-1]))
                pcts.append(subs[-1].strip('[').strip(']').strip('%'))
            else:
                titles.append(" ".join(subs[1::]))
                pcts.append(None)
    df['due_date'] = due_dates
    df['course'] = courses
    df['title'] = titles
    df['progress'] = pcts

    # interpret type
    is_study = df['title'].str.contains('study', case=False) | df['title'].str.contains('review', case=False)
    df.loc[is_study, 'type'] = 'study'
    df.loc[~is_study, 'type'] = 'assignment'

    # interpret date format
    df['start_date'] = pd.to_datetime(df['start_date'])
    df['end_date'] = pd.to_datetime(df['end_date'])
    year = df.iloc[0]['start_date'].year
    df['due_date'] = pd.to_datetime(df['due_date'] + f"/{year}")

    # interpret duration format
    df['duration'] = pd.to_numeric(df['duration'].apply(lambda x: x.split(" ")[0]))

    # set term
    df['term'] = term

    # extract day of week
    df["day of week"] = df["start_date"].apply(lambda x: x.day_name())
    df["day of week"] = pd.Categorical(df["day of week"], categories=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], ordered=True)

    # extract week
    if term != 'fa23':
        df["week"] = df["start_date"].apply(lambda x: x.week - df.iloc[0]['start_date'].week + 1)
    else:
        print("fa23")
        df["week"] = df["start_date"].apply(lambda x: x.week - 34 + 1)

    # order dataframe
    df = df[["term", "week", "day of week", "course", "duration", 'type', "start_date", "end_date", 'due_date', 'title', 'progress']]

    return df

# prepare semester data and apply correct course names
fa23 = prepare_data("data/raw/fa23.json", 'fa23')
fa23['course'] = fa23['course'].replace({"Hist": "HIST 164", "Math": "MATH 241", "Phys": "PHYS 213/214", "Stat": "STAT 107"})
fa23 = fa23[fa23['course'] != 'AIS']

sp24 = prepare_data("data/raw/sp24.json", 'sp24')
sp24['course'] = sp24['course'].replace({"Math": "MATH 257", "Anth": "ANTH 103", "Stat": "STAT 207", "Geol": "GEOL 107", "Astro": "ASTR 210"})

fa24 = prepare_data("data/raw/fa24.json", 'fa24')
fa24['course'] = fa24['course'].replace({"Chem": "CHEM 102/103", "Aces": "ACES 179", "IS": "IS 477", "Geol": "GEOL 208", "Astro": "ASTR 310"})
fa24 = fa24[fa24['course'] != 'Research']

sp25 = prepare_data("data/raw/sp25.json", 'sp25')
sp25['course'] = sp25['course'].replace({"Chem": "CHEM 104/105", "CS": "CS 307", "Astro": "ASTR 405", "Geol": "GEOL 432", "RST": "RST 100"})

fa25 = prepare_data("data/raw/fa25.json", 'fa25')
fa25['course'] = fa25['course'].replace({"Math": "MATH 285", "436": "GEOL 436", "497": "GEOL 497", "IS": "IS 467", "Phys": "PHYS 225"})

# combine all semesters
master = pd.concat([fa23, sp24, fa24, sp25, fa25])

# add course group column
ds_group = ['STAT 107', 'STAT 207', 'IS 477', 'CS 307', 'IS 467']
astro_group = ['ASTR 210', 'ASTR 310', 'ASTR 405']
gened_group = ['HIST 164', 'ANTH 103', 'ACES 179', 'RST 100']
geol_group = ['GEOL 107', 'GEOL 208', 'GEOL 432', 'GEOL 436', 'GEOL 497']
stem_foundations = ['MATH 241', 'MATH 257', 'PHYS 213/214', 'CHEM 102/103', 'CHEM 104/105', 'MATH 285', 'PHYS 225']

def find_group(course: str):
    if course in ds_group:
        return 'ds'
    elif course in astro_group:
        return 'astro'
    elif course in gened_group:
        return 'gened'
    elif course in geol_group:
        return 'geol'
    elif course in stem_foundations:
        return 'stem'
    elif course == 'Research':
        return 'research'
    else:
        return 'other'

master['group'] = master['course'].apply(lambda x: find_group(x))
master = master[["term", "week", "day of week", 'group', "course", "duration", 'type', "start_date", "end_date", 'due_date', 'title', 'progress']]

# save to csv
master.to_csv("data/master/studytime.csv", index=False)