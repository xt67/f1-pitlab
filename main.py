import fastf1
import pandas as pd

fastf1.Cache.enable_cache('cache')
session = fastf1.get_session(2024, 'Monaco', 'R')
session.load()

laps = session.laps

# Get laps where car EXITED the pit (PitOutTime exists = this is an "out lap")
out_laps = laps[laps['PitOutTime'].notna()][['Driver', 'Team', 'LapNumber', 'PitOutTime', 'Compound', 'Stint']].copy()

# Get laps where car ENTERED the pit (PitInTime exists = this is an "in lap")
# IMPORTANT: Exclude Lap 1 - those aren't real pit stops, just race start data
in_laps = laps[(laps['PitInTime'].notna()) & (laps['LapNumber'] > 1)][['Driver', 'LapNumber', 'PitInTime']].copy()
in_laps['NextLap'] = in_laps['LapNumber'] + 1  # The out lap is the next lap

# Merge: match each pit entry with its pit exit
pit_data = pd.merge(
    in_laps,
    out_laps,
    left_on=['Driver', 'NextLap'],
    right_on=['Driver', 'LapNumber'],
    suffixes=('_in', '_out')
)

# Calculate pit stop duration
pit_data['PitDuration'] = pit_data['PitOutTime'] - pit_data['PitInTime']
pit_data['PitDuration_Seconds'] = pit_data['PitDuration'].dt.total_seconds()

# Clean up columns
pit_data = pit_data[['Driver', 'Team', 'LapNumber_in', 'PitInTime', 'PitOutTime', 'PitDuration_Seconds', 'Compound', 'Stint']]
pit_data = pit_data.rename(columns={'LapNumber_in': 'PitLap'})

print("=== PIT STOPS: Monaco 2024 ===")
print(pit_data.to_string())
print(f"\nTotal pit stops: {len(pit_data)}")

# === ANALYSIS ===
valid_pits = pit_data[pit_data['PitDuration_Seconds'].notna()]

# 1. Fastest pit stop
fastest = valid_pits.loc[valid_pits['PitDuration_Seconds'].idxmin()]
print(f"\n🏆 FASTEST PIT STOP:")
print(f"   {fastest['Driver']} ({fastest['Team']}) - {fastest['PitDuration_Seconds']:.2f} seconds on Lap {int(fastest['PitLap'])}")

# 2. Slowest pit stop
slowest = valid_pits.loc[valid_pits['PitDuration_Seconds'].idxmax()]
print(f"\n🐢 SLOWEST PIT STOP:")
print(f"   {slowest['Driver']} ({slowest['Team']}) - {slowest['PitDuration_Seconds']:.2f} seconds on Lap {int(slowest['PitLap'])}")

# 3. Average pit stop time per team
print(f"\n📊 AVERAGE PIT STOP TIME BY TEAM:")
team_avg = valid_pits.groupby('Team')['PitDuration_Seconds'].mean().sort_values()
for team, avg_time in team_avg.items():
    print(f"   {team}: {avg_time:.2f} seconds")

# === VISUALIZATION ===
import matplotlib.pyplot as plt 
import seaborn as sns
sns.set_style("darkgrid")
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
# Chart 1: Bar chart - Pit stop duration by driver
ax1 = axes[0]
colors = sns.color_palette("husl", len(valid_pits))
bars = ax1.bar(valid_pits['Driver'], valid_pits['PitDuration_Seconds'], color=colors)
ax1.set_xlabel("Driver")
ax1.set_ylabel("Pit Stop Duration (seconds)")
ax1.set_title("Pit Stop Durations - Monaco 2024")
ax1.axhline(y=valid_pits['PitDuration_Seconds'].mean(), color='red', linestyle='--', label='Average')
ax1.legend()
# Chart 2: Bar chart - Average pit stop by team
ax2 = axes[1]
team_colors = {'Red Bull Racing': 'darkblue', 'Mercedes': 'cyan', 'Kick Sauber': 'green', 
               'Williams': 'blue', 'Aston Martin': 'darkgreen'}
team_avg_sorted = valid_pits.groupby('Team')['PitDuration_Seconds'].mean().sort_values()
bars2 = ax2.barh(team_avg_sorted.index, team_avg_sorted.values, color=[team_colors.get(t, 'gray') for t in team_avg_sorted.index])
ax2.set_xlabel("Average Pit Stop Duration (seconds)")
ax2.set_title("Average Pit Stop Time By Team")
# Adjust layout and show plot
plt.tight_layout()
plt.savefig('pit_stops_monaco_2024.png', dpi=150)
plt.show()
print("\n Chart saved as 'pit_stops_monaco_2024.png'")
