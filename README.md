# 📊 Dataset Analyzer CLI

A lightweight command-line tool for analyzing **CSV** and **Excel** datasets.

The tool provides a quick overview of a dataset's structure, data quality, and basic statistics by simply passing the dataset path as a command-line argument. s

---

## ✨ Features

- Load CSV (`.csv`) files
- Load Excel (`.xlsx`) files
- Display dataset dimensions
- Show column data types
- Count missing values
- Count zero values
- Detect duplicate rows
- Display dataset statistics
- Show memory usage
- Analyze datasets from **any location** on your computer

---

## 📁 Project Structure

```text
dataset-analyzer/
│
├── data/
│   ├── sample.csv
│   └── sample.xlsx
│
├── src/
│   ├── __init__.py
│   ├── analyze_dataset.py
│   └── load_data.py
│
├── tests/
│   └── test_analyze_dataset.py
│
├── main.py
├── pyproject.toml
├── pytest.ini
├── README.md
└── uv.lock
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Hanan-Nawaz/dataset-analyzer.git
```

Navigate to the project directory:

```bash
cd dataset-analyzer
```

Install dependencies using **uv**:

```bash
uv sync
```

---

## 💻 Usage

Run the analyzer by providing the path to any CSV or Excel dataset.

### Basic Syntax

```bash
uv run main.py <path_to_dataset>
```

### Examples

Analyze a CSV file:

```bash
uv run main.py data/sample.csv
```

Analyze an Excel file:

```bash
uv run main.py data/sample.xlsx
```

Analyze a dataset from your Downloads folder:

```bash
uv run main.py ~/Downloads/obesity.csv
```

Analyze a dataset using an absolute path:

```bash
uv run main.py /Users/username/Desktop/customers.xlsx
```

---

## 📄 Supported File Types

Currently supported:

- CSV (`.csv`)
- Excel (`.xlsx`)

The dataset can be located anywhere on your computer. Simply provide its file path when running the program.

---

## 📊 Example Output

```text
============================================================
Dataset Analysis Report
============================================================

Basic Information
Rows      : 10
Columns   : 4

Column Types
----------------------------------------
id      int64
name    object
age     int64
city    object

Missing Values
----------------------------------------
Column     Null     Zero
id          0        0
name        1        0
age         0        1
city        0        0

Duplicate Rows : 1

Dataset Statistics
----------------------------------------
...

Memory Usage : 1376 bytes
```

---

## 🧪 Running Tests

Run all tests:

```bash
pytest
```

Or using **uv**:

```bash
uv run pytest
```

---

## 🛠️ Technologies Used

- Python
- Pandas
- uv
- pytest

---

## 🎯 Learning Objectives

This project was built to strengthen my understanding of:

- Python project structure
- Command-Line Interfaces (CLI)
- Working with CSV and Excel files
- Exploratory Data Analysis (EDA)
- Data quality assessment
- Writing reusable Python functions
- Unit testing with pytest
- Dependency management using uv

---

## 🚀 Future Improvements

Planned features include:

- Summary statistics using `describe()`
- Correlation analysis
- Outlier detection
- Data visualization
- Export reports to CSV, JSON, or HTML
- Interactive terminal output using Rich
- Support for additional file formats
- Package the project as an installable CLI

---

## 👨‍💻 Author

**Abdul Hanan Nawaz**

- Master's Student in Germany
- Software Engineer (Werkstudent)

---

## 📜 License

This project is licensed under the MIT License.