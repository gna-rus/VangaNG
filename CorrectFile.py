import os
import pandas as pd

count = 1

it_sector_tickers = [
    "AAPL", "MSFT", "GOOG"
]


# it_sector_tickers = [
#     "AAPL", "MSFT", "GOOG", "AMZN", "INTC",
#     "NVDA", "CRM", "ORCL", "QCOM", "PYPL",
#     "IBM", "VRSN", "SNAP", "UBER", "TWTR",
#     "NFLX", "YELP", "ROKU", "SQ", "ZS"
# ]

mining_sector_tickers = [
    "XOM", "CVX", "COP", "BP", "SLB",
    "HAL", "EOG", "OXY", "BHP", "FCX",
    "KGC", "ABX", "GD", "TCK", "MRO",
    "NOV", "ANDE", "WMB", "CLR", "AR"
]

# Укажем путь к папке с исходными файлами
folder_path = r'D:\Анализ\Базы данных\Финансы\USA top 900+ Companies stock historic dataset2'

# Список для сбора таблиц
dfs = []

# Проходим по каждому файлу в папке
for filename in os.listdir(folder_path):
    print('Step: ', count)
    count += 1 
    # Проверяем расширение файла (.csv) и наличие любого тикера в имени файла
    if filename.endswith('.csv') and any(ticker in filename for ticker in it_sector_tickers):
        # Чтение CSV-файла
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)

        # Добавление новой колонки с именем файла
        df['filename'] = filename

        # Добавляем в общий список
        dfs.append(df)

# Объединяем все DataFrames в один
if dfs:
    merged_df = pd.concat(dfs, ignore_index=True)

    # Путь для сохранения объединенного файла
    output_file = 'merged_it_data.csv'

    # Сохраняем объединённый файл
    merged_df.to_csv(output_file, index=False)
else:
    print("Нет подходящих файлов.")


