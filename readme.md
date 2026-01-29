# 🏎️ F1 Pitstop Analyzer

A Python data analysis project that fetches and analyzes real Formula 1 pit stop data.

## 📊 Features

- Fetches real F1 race data using the FastF1 API
- Analyzes pit stop durations by driver and team
- Visualizes pit stop performance with charts
- Identifies fastest and slowest pit stops

## 🛠️ Technologies Used

- **Python 3.x**
- **FastF1** - F1 data API
- **Pandas** - Data manipulation
- **Matplotlib & Seaborn** - Data visualization
- **Scikit-learn** - Machine Learning

## 📈 Sample Output

```
🏆 FASTEST PIT STOP:
   VER (Red Bull Racing) - 23.67 seconds

🐢 SLOWEST PIT STOP:
   STR (Aston Martin) - 28.12 seconds

📊 AVERAGE PIT STOP TIME BY TEAM:
   Red Bull Racing: 23.67 seconds
   Mercedes: 24.09 seconds
   Kick Sauber: 24.36 seconds
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

## 📁 Project Structure

```
f1-pitstop-analyzer/
├── main.py           # Main analysis script
├── requirements.txt  # Python dependencies
├── cache/            # Cached F1 data (gitignored)
├── venv/             # Virtual environment (gitignored)
├── .gitignore        # Git ignore file
└── README.md         # This file
```

## 🔮 Future Improvements

- [ ] Analyze multiple races/seasons
- [ ] Build ML model to predict pit stop times
- [ ] Add interactive dashboard
- [ ] Compare pit strategies

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- [FastF1](https://github.com/theOehrly/Fast-F1) for the amazing F1 data API
- Formula 1 for the exciting sport!

