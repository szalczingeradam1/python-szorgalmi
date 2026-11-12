import os
import pandas as pd

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, "players.csv")
df = pd.read_csv(csv_path)

df["player_name"] = (
    df["common_name"]
    .fillna(df["first_name"].fillna("") + " " + df["last_name"].fillna(""))
    .str.strip()
)

df["birthdate"] = pd.to_datetime(df["birthdate"], errors="coerce")
df["age"] = (pd.to_datetime("today") - df["birthdate"]).dt.days // 365.25

skill_cols = [
    "pace",
    "shooting",
    "passing",
    "dribbling",
    "defending",
    "physicality",
]

df_field = df.dropna(subset=skill_cols).copy()
df_field = df_field[df_field["position"] != "GK"].copy()

# =========================================================================
# 1. KÉRDÉS: A legsokoldalúbb játékosok (Alacsony szórás, magas képességátlag)
# =========================================================================
df_field["skill_mean"] = df_field[skill_cols].mean(axis=1)
df_field["skill_std"] = df_field[skill_cols].std(axis=1)

versatile_players = (
    df_field[df_field["skill_mean"] >= 75]
    .sort_values(by="skill_std", ascending=True)[
        ["player_name", "position", "overall_rating", "skill_mean", "skill_std"]
    ]
    .head(5)
    .rename(
        columns={
            "player_name": "Játékos",
            "position": "Poszt",
            "overall_rating": "Overall",
            "skill_mean": "Átlagos_képesség",
            "skill_std": "Szórás_(kiegyensúlyozottság)",
        }
    )
)
print("--- 1. Legkiegyensúlyozottabb játékosok (legkisebb szórás) ---")
print(versatile_players.round(2).to_string(index=False), "\n")

# =========================================================================
# 2. KÉRDÉS: Leginkább specializált és legsokoldalúbb poszt (szórás alapján)
# =========================================================================
pos_specialization = (
    df_field.groupby("position")[skill_cols]
    .mean()
    .std(axis=1)
    .sort_values(ascending=False)
)

print(
    "--- 2. Leginkább specializált / egyoldalú poszt (legnagyobb szórás) ---"
)
print(pos_specialization.head(1).round(2), "\n")

print(
    "--- 2. Legsokoldalúbb / legkiegyensúlyozottabb poszt (legkisebb szórás) ---"
)
print(pos_specialization.tail(1).round(2), "\n")

# =========================================================================
# 3. KÉRDÉS: Top futballnemzetek relatív eltérése a világátlagtól
# =========================================================================
top_nations = df_field["nationality"].value_counts().head(5).index
nation_diff = (
    df_field[df_field["nationality"].isin(top_nations)]
    .groupby("nationality")[skill_cols]
    .mean()
    - df_field[skill_cols].mean()
)
print("--- 3. Top 5 nemzet átlagos eltérése a globális átlagtól ---")
print(nation_diff.round(2), "\n")

# =========================================================================
# 4. KÉRDÉS: Fizikai sebesség vs. Mentális játéklátás kor szerinti alakulása
# =========================================================================
age_trends = (
    df_field[(df_field["age"] >= 20) & (df_field["age"] <= 35)]
    .groupby("age")[["movement_sprint_speed", "mentality_vision"]]
    .mean()
    .rename(
        columns={
            "movement_sprint_speed": "Átlagos_sprintsebesség",
            "mentality_vision": "Átlagos_játéklátás",
        }
    )
)
age_trends.index.name = "Életkor"

print("--- 4. Sprintsebesség és játéklátás változása 20 és 35 év között ---")
print(age_trends.round(1), "\n")

# =========================================================================
# 5. KÉRDÉS: Miben emelkednek ki leginkább az elit csatárok az átlagból?
# =========================================================================
st_players = df_field[df_field["position"] == "ST"]

elite_st = st_players[st_players["overall_rating"] >= 85][skill_cols].mean()
avg_st = st_players[
    (st_players["overall_rating"] >= 70) & (st_players["overall_rating"] < 75)
][skill_cols].mean()

# Különbségképzés: mely képességnél a legnagyobb a különbség?
skill_gap = (elite_st - avg_st).sort_values(ascending=False)

print("--- 5. Pontkülönbség az elit (85+) és átlagos csatárok között (ST) ---")
print(skill_gap.round(1))