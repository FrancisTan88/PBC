import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime
from scipy.stats import norm

ASS = ["HW0", "HW1", "HW2", "HW3", "HW4", "HW5", "HW6", "HW7 ",
       "Quiz", "Midterm1", "Midterm 1 bonus", "Midterm2"]
DDL = ["2023-02-28 12:00", "2023-03-07 12:00", "2023-03-14 12:00",
        "2023-03-25 12:00", "2023-04-01 12:00", "2023-04-11 12:00",
          "2023-04-18 12:00", "2023-05-02 23:59", "2023-03-20 21:05",
            "2023-03-27 21:05", "2023-04-04 12:00", "2023-05-01 21:15"]
DDL = [datetime.strptime(i, '%Y-%m-%d %H:%M') for i in DDL]
COMB = [(ASS[i], DDL[i]) for i in range(len(ASS))]
# "HW1", "HW2", "HW5", "HW6"

def del_columns(df, del_cols):
    df.drop(columns=del_cols, axis=1, inplace=True)
    return df

def del_after_ddl(df):
    dfs = []
    for hw, ddl in COMB:
        curr_df = df[df["challenge_title"] == hw]
        curr_df = curr_df[curr_df["submission_submit_time"] <= ddl]
        dfs.append(curr_df)
    new_df = pd.concat(dfs)
    return new_df

def write_csv(df):
    df.to_csv("./tmp.csv")

def calculate_mean(group):
    latest_score = group.tail(1)
    mus_stds = []
    for hw in ASS:
        curr_hw = latest_score[latest_score["challenge_title"] == hw]
        scores = curr_hw.groupby("anonymous_account")["submission_result_score"].sum()
        if hw == "HW0":
            scores = scores.multiply(other=2.5)
        elif hw == "HW1" or hw == "HW2" or hw == "HW3" or\
                hw == "HW4" or hw == "HW6":
            scores = scores.multiply(other=1.25)
        elif hw == "Midterm 1 bonus":
            scores = scores.multiply(other=5)
        elif hw == "Midterm2":
            scores = scores.multiply(other=0.8333)        
        mus_stds.append([np.mean(scores), np.std(scores)])
    return mus_stds

def analyze_tns(df):
    subs_byhw = []
    for hw in ASS:
        curr_df = df[df["challenge_title"] == hw]
        subs = curr_df.groupby(curr_df["submission_submit_time"].dt.date)["anonymous_account"].count().values
        subs_byhw.append(subs)
    return subs_byhw

def codelen_score(group):
    df = group.tail(1)
    new_df = df.groupby("anonymous_account")
    write_csv(df)
    scores = new_df["submission_result_score"].sum()
    codelen = new_df["submission_code_length"].sum()
    print(len(scores), len(codelen))
    comb = list(zip(scores, codelen))
    comb.sort(key=lambda x: x[1])
    return comb

    
def plot_CI(mus_and_stds):
    for i in range(len(ASS)):
        mean, std = mus_and_stds[i][0], mus_and_stds[i][1]
        x = np.linspace(mean - 4*std, mean + 4*std, 1000)
        y = norm.pdf(x, loc=mean, scale=std)
        plt.plot(x, y, label=ASS[i], linewidth=1.5)
    plt.legend()
    plt.xlabel('score')
    plt.ylabel('pdf')
    plt.title('95% Confidence Interval')
    # plt.show()
    plt.savefig("./plots/score_CI.png")
    plt.close()

def plot_tns(subs):
    x = [j for j in range(1, 8)]
    x = [f"day{str(j)}" for j in x]
    x.append("ddl")
    # for sub in subs:
    for i in range(len(ASS)):
        if len(subs[i]) == 8:
            y = subs[i]
            plt.plot(x, y, label=ASS[i], linewidth=1.5)
            # plt.hist([x, y], bins="auto")
    plt.legend()
    plt.xlabel('Days')
    plt.ylabel('Times')
    plt.title('Submission Times')
    # plt.show()
    plt.savefig("./plots/subtimes_ddl.png")   
    plt.close()

def plot_codelen(comb):
    scores, codelens = [], []
    for score, codelen in comb:
        scores.append(score)
        codelens.append(codelen)
    scores.pop()
    scores.pop()
    codelens.pop()
    codelens.pop()
    plt.scatter(codelens, scores, s=5)
    # plt.legend()
    # plt.xticks(np.arange(min(codelens), max(codelens)+1, 10000))
    plt.xlabel('Length of code')
    plt.ylabel('Scores')
    plt.title('Relationship of Score and CodeLen')
    # plt.show()
    plt.savefig("./plots/score_codelen.png")   
    plt.close()


file_path = "/Users/francistan/Downloads/github_FrancisTan88/PBC/submission_complete.csv"
df = pd.read_csv(file_path)
df = del_columns(df, ["class_name", "submission_id"])
df["submission_submit_time"] = pd.to_datetime(df["submission_submit_time"])
df = del_after_ddl(df)
# print(df.head(10))
# write_csv(df)
########################################################################

df_gp = df.groupby(["anonymous_account", "challenge_title", "problem_label"])
# mus_stds = calculate_mean(df_gp)
# plot_CI(mus_stds)

subs_byhw = analyze_tns(df)
plot_tns(subs_byhw)

# comb = codelen_score(df_gp)
# plot_codelen(comb)


