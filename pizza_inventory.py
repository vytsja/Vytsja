import pandas as pd
import numpy as np

# 1. СТВОРЕННЯ ДАНИХ (Відтворення вашої структури)
# ---------------------------------------------------------

# Дані про інгредієнти (Master Data)
ingredients_data = {
    'ID': [f'ING{i:03d}' for i in range(1, 21)],
    'Název': [
        'Sugo Solana', 'Smetana 20%', 'Mozzarella La Giusta', 'Šunka Vršovka',
        'Žampiony konzerv.', 'Ananas konzerv.', 'Kukuřice', 'Špenát mražený',
        'Salám Paprikáš', 'Feferonky', 'Slanina', 'Cibule', 'Sušená rajčata',
        'Olivy černé', 'Gouda uzená', 'Niva', 'Kuřecí pečené', 'Pórek',
        'Camembert', 'Brusinky'
    ],
    'Dodavatel': ['Fany'] * 20, # Спрощено
    'Jedn.': ['kg', 'l', 'kg', 'kg', 'kg', 'kg', 'kg', 'kg', 'kg', 'kg', 'kg', 'kg', 'kg', 'kg', 'kg', 'kg', 'kg', 'kg', 'kg', 'kg'],
    'Cena': [27.2, 50, 139, 90, 24, 35.6, 18, 13.6, 179, 87, 130, 20, 80, 45.8, 119.9, 184, 120, 25, 250, 140],
    'MIN': [5, 2, 8, 3, 1, 1, 1, 1, 2, 0.5, 1, 1, 0.5, 1, 1, 1, 1, 0.5, 0.5, 0.5],
    'MAX': [15, 6, 20, 8, 4, 3, 4, 4, 5, 2, 4, 4, 2, 3, 3, 4, 3, 2, 2, 2],
    'Aktuální': [0] * 20  # Поки що нуль, як у вашому файлі
}
df_ingredience = pd.DataFrame(ingredients_data)

# Дані про рецепти (Normy) - зі старими "поганими" назвами
normy_data = {
    'Pizza': ['Margherita', 'Olivová', 'Šunková', 'Capricciosa', 'Hawai', 'Americana', 'Bobo', 'Salámová', 'Ďábelská', 'Farmářská', 'Sedlácká', 'Špenátová', 'Sýrová', 'Kuřecí', 'Pollo', 'Brusinková'],
    'Sugo': [90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, np.nan, 90, np.nan, np.nan],
    'Smeta': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 40, np.nan, 40, 40],
    'Mozza': [120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120],
    'Šunka': [np.nan, np.nan, 60, 60, 60, 60, 60, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    'Žampi': [np.nan, np.nan, np.nan, 40, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 20, np.nan, np.nan],
    'Anana': [np.nan, np.nan, np.nan, np.nan, 50, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    'Kukuř': [np.nan, np.nan, np.nan, np.nan, np.nan, 30, 30, np.nan, np.nan, np.nan, 30, np.nan, np.nan, np.nan, 40, np.nan],
    'Špená': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 30, np.nan, np.nan, np.nan, np.nan, 40, np.nan, np.nan, np.nan, np.nan],
    'Salám': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 40, 40, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    'Fefer': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 15, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    'Slani': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 60, 60, np.nan, np.nan, np.nan, np.nan, np.nan],
    'Cibul': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 30, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    'Sušen': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 30, np.nan, np.nan, np.nan],
    'Olivy': [np.nan, 40, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    'Gouda': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 30, np.nan, np.nan, np.nan],
    'Niva': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 30, np.nan, 30, 30],
    'Kuřec': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 50, 50, np.nan],
    'Pórek': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 30, np.nan, 10, np.nan, np.nan],
    'Camem': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 40],
    'Brusi': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 30],
}
df_normy = pd.DataFrame(normy_data).fillna(0)

# Ціни продажу піци (з вашого файлу)
pizza_prices = {
    'Margherita': 215, 'Olivová': 225, 'Šunková': 225, 'Capricciosa': 225, 'Hawai': 225,
    'Americana': 225, 'Bobo': 225, 'Salámová': 225, 'Ďábelská': 225, 'Farmářská': 225,
    'Sedlácká': 225, 'Špenátová': 225, 'Sýrová': 225, 'Kuřecí': 235, 'Pollo': 235,
    'Brusinková': 245
}

# 2. ВИПРАВЛЕННЯ ТА ОБРОБКА
# ---------------------------------------------------------

# А. СЛОВНИК ВІДПОВІДНОСТІ (Mapping Dictionary)
# Це ключ до вирішення проблеми!
col_mapping = {
    'Sugo': 'Sugo Solana', 'Smeta': 'Smetana 20%', 'Mozza': 'Mozzarella La Giusta',
    'Šunka': 'Šunka Vršovka', 'Žampi': 'Žampiony konzerv.', 'Anana': 'Ananas konzerv.',
    'Kukuř': 'Kukuřice', 'Špená': 'Špenát mražený', 'Salám': 'Salám Paprikáš',
    'Fefer': 'Feferonky', 'Slani': 'Slanina', 'Cibul': 'Cibule',
    'Sušen': 'Sušená rajčata', 'Olivy': 'Olivy černé', 'Gouda': 'Gouda uzená',
    'Niva': 'Niva', 'Kuřec': 'Kuřecí pečené', 'Pórek': 'Pórek',
    'Camem': 'Camembert', 'Brusi': 'Brusinky'
}

# Б. Перейменування стовпців у Normy
df_normy_fixed = df_normy.rename(columns=col_mapping)

# В. Розрахунок Food Cost
# 1. Розгортаємо таблицю рецептів (Melt)
df_melted = df_normy_fixed.melt(id_vars=['Pizza'], var_name='Ingredience', value_name='Gramy')
df_melted = df_melted[df_melted['Gramy'] > 0] # Прибираємо нульові значення

# 2. Додаємо ціну за кг з таблиці Ingredience
df_merged = df_melted.merge(df_ingredience[['Název', 'Cena']], left_on='Ingredience', right_on='Název', how='left')

# 3. Рахуємо вартість інгредієнта в піці: (грами / 1000) * ціна_за_кг
# Для 'l' (літрів) припускаємо, що 1000мл (г) = 1л, логіка та сама
df_merged['Cost_Component'] = (df_merged['Gramy'] / 1000) * df_merged['Cena']

# 4. Групуємо по піці, щоб отримати повну собівартість
df_food_cost = df_merged.groupby('Pizza')['Cost_Component'].sum().reset_index()
df_food_cost.columns = ['Pizza', 'Calculated_FC']
df_food_cost['Calculated_FC'] = df_food_cost['Calculated_FC'].round(2)

# Г. Оновлення таблиці продажів (Denní prodej)
df_sales = pd.DataFrame(list(pizza_prices.items()), columns=['Pizza', 'Cena'])
df_sales = df_sales.merge(df_food_cost, on='Pizza', how='left')
df_sales['Počet'] = 0 # Початковий стан
df_sales['Tržba'] = df_sales['Počet'] * df_sales['Cena']
df_sales['FC_Total'] = df_sales['Počet'] * df_sales['Calculated_FC']
df_sales['Zisk'] = df_sales['Tržba'] - df_sales['FC_Total']
# Додаємо маржу у відсотках (для аналітики)
df_sales['Marže_%'] = round(((df_sales['Cena'] - df_sales['Calculated_FC']) / df_sales['Cena']) * 100, 1)

# Перейменування для краси
df_sales_final = df_sales[['Pizza', 'Počet', 'Cena', 'Tržba', 'Calculated_FC', 'Zisk', 'Marže_%']]
df_sales_final.columns = ['Pizza', 'Počet', 'Cena (CZK)', 'Tržba', 'Food Cost (1ks)', 'Zisk', 'Marže %']

# 3. ЗБЕРЕЖЕННЯ В EXCEL
# ---------------------------------------------------------
output_file = 'PizzaBobo_Inventura_FIXED.xlsx'

with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
    # Записуємо вкладки
    df_sales_final.to_excel(writer, sheet_name='Denní prodej', index=False)
    df_normy_fixed.to_excel(writer, sheet_name='Normy (Fixed)', index=False)
    df_ingredience.to_excel(writer, sheet_name='Ingredience', index=False)

    # Форматування (для краси)
    workbook = writer.book
    worksheet_sales = writer.sheets['Denní prodej']

    # Формат грошей
    money_fmt = workbook.add_format({'num_format': '#,##0.00 Kč'})
    worksheet_sales.set_column('C:F', 15, money_fmt)
    worksheet_sales.set_column('A:A', 20)

    print(f"Файл '{output_file}' успішно створено!")
    print("\n--- ПРИКЛАД РОЗРАХУНКУ (Margherita) ---")
    m_cost = df_food_cost[df_food_cost['Pizza'] == 'Margherita']['Calculated_FC'].values[0]
    print(f"Собівартість Margherita: {m_cost} Kč")
    print("(90г соусу * 27.2 + 120г моцарели * 139)")
