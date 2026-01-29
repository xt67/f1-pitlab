# 🏎️ F1 Pitstop Analyzer

A Python data analysis project that fetches and analyzes real Formula 1 pit stop data.

## 📊 Features

- Select and analyze any race from any season (2018–2025)
- Fetches real F1 race data using the FastF1 API
- Analyzes pit stop durations by driver and team
- Detailed summary and statistics for each race
- Unified, scrollable chart with all visualizations in one figure
- User prompt to save charts to the `charts/` folder
- Caching for fast repeated analysis
- Pre-cache all races in a season for speed

## 🛠️ Technologies Used

- **Python 3.x**
- **FastF1** - F1 data API
- **Pandas** - Data manipulation
- **Matplotlib & Seaborn** - Data visualization

## 📈 Sample Output

```
🏁 PIT STOP ANALYSIS: Monaco Grand Prix 2024
...existing code...
🏆 PIT STOP RECORDS:
   🥇 Fastest: VER (Red Bull Racing) - 23.67s on Lap 18
   🥈 2nd: HAM (Mercedes) - 24.09s on Lap 22
   🥉 3rd: NOR (McLaren) - 24.36s on Lap 25

🐢 Slowest: STR (Aston Martin) - 28.12s on Lap 41

👨‍✈️ DRIVER PIT STOP SUMMARY:
   Driver   Team                 Avg      Best   Stops Pit Laps
   VER      Red Bull Racing     23.67s   23.67s     1 [18]
   HAM      Mercedes            24.09s   24.09s     1 [22]
   ...

📊 After analysis, a unified chart with all visualizations will be shown. You will be prompted:
💾 Do you want to save this chart to the charts/ folder? (y/n):
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/xt67/F1-pitstop-analyzer.git
   cd F1-pitstop-analyzer
   ```

2. Create a virtual environment
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

4. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

5. Create a cache folder
   ```bash
   mkdir cache
   ```

6. Run the analyzer
   ```bash
   python main.py
   ```

## 🕹️ Usage

1. **Select a season and race**: The program will prompt you to choose any available season and race.
2. **View analysis and charts**: After analysis, a single scrollable chart with all visualizations will be displayed.
3. **Save charts**: When prompted, enter `y` to save the chart to the `charts/` folder, or `n` to skip saving.
4. **Pre-cache races**: Use the menu to pre-cache all races in a season for faster future analysis.

## 📁 Project Structure

```
f1-pitstop-analyzer/
├── main.py           # Main analysis script
├── requirements.txt  # Python dependencies
├── cache/            # Cached F1 data (gitignored)
├── charts/           # Saved chart images (auto-created)
├── venv/             # Virtual environment (gitignored)
├── .gitignore        # Git ignore file
└── README.md         # This file
```

## 🔮 Future Improvements

- [ ] Analyze multiple races/seasons at once
- [ ] Build ML model to predict pit stop times
- [ ] Add interactive dashboard
- [ ] Compare pit strategies

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- [FastF1](https://github.com/theOehrly/Fast-F1) for the amazing F1 data API
- Formula 1 for the exciting sport!

