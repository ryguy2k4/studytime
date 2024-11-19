import pandas as pd

def clean(filename: str, term: str):
    df = pd.read_csv(filename)
    df.rename(columns={"Date": "date"}, inplace=True)
    df = df.melt(id_vars=["date"], value_vars=df.columns[1::], var_name="class", value_name="time spent (min)")
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date", ascending=True)
    df["term"] = term
    df["day of week"] = df["date"].apply(lambda x: x.day_name())
    df["day of week"] = pd.Categorical(df["day of week"], categories=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], ordered=True)
    df["week"] = df["date"].apply(lambda x: x.week - df.iloc[0]['date'].week + 1)
    df = df[["term", "week", "day of week", "class", "time spent (min)"]]
    return df

fa23 = clean("../data/raw/StudyTimeFa23.csv", 'fa23')
sp24 = clean("../data/raw/StudyTimeSp24.csv", 'sp24')
fa24 = clean("../data/raw/StudyTimeFa24.csv", 'fa24')
master = pd.concat([fa23, sp24, fa24]).dropna()
master.to_csv("../data/master/studytime.csv", index=False)