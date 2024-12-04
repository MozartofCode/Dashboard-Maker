import pandas as pd

def analyze_excel(file_path):

    data = pd.read_excel(file_path)
    correlations = data.corr()
    return correlations.to_dict()

if __name__ == "__main__":
    file_path = "excel_file.xlsx"
    results = analyze_excel(file_path)
    print(results)
