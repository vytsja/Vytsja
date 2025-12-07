# Pizza Bobo - Inventory Management System

A comprehensive Python-based inventory and cost management system for pizza restaurant operations.

## Overview

This system helps manage pizza restaurant operations by:
- Tracking ingredient inventory levels
- Calculating food costs per pizza type
- Managing daily sales and profit margins
- Generating detailed Excel reports

## Features

### Ingredient Management
- Master database of 20 ingredients with:
  - Unique IDs (ING001-ING020)
  - Supplier information
  - Unit prices (CZK)
  - Min/Max stock levels
  - Current inventory tracking

### Recipe Management (Normy)
- Standardized recipes for 16 pizza types:
  - Margherita, Olivová, Šunková, Capricciosa
  - Hawai, Americana, Bobo, Salámová
  - Ďábelská, Farmářská, Sedlácká, Špenátová
  - Sýrová, Kuřecí, Pollo, Brusinková
- Precise ingredient quantities in grams per pizza

### Cost Analysis
- Automated food cost calculation
- Profit margin analysis
- Sales tracking with revenue calculations
- Price optimization insights

## Requirements

- Python 3.11+
- pandas
- numpy
- openpyxl
- xlsxwriter

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Vytsja
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script to generate the inventory Excel file:

```bash
python3 pizza_inventory.py
```

This will create `PizzaBobo_Inventura_FIXED.xlsx` with three worksheets:

1. **Denní prodej** - Daily sales tracking with:
   - Pizza type and quantity sold
   - Sale price and total revenue
   - Food cost per unit
   - Profit and margin percentage

2. **Normy (Fixed)** - Complete recipe specifications with full ingredient names

3. **Ingredience** - Master ingredient database

## Example Output

```
Файл 'PizzaBobo_Inventura_FIXED.xlsx' успішно створено!

--- ПРИКЛАД РОЗРАХУНКУ (Margherita) ---
Собівартість Margherita: 19.13 Kč
(90г соусу * 27.2 + 120г моцарели * 139)
```

### Sample Calculations

**Margherita Pizza:**
- 90g Sugo Solana @ 27.2 Kč/kg = 2.45 Kč
- 120g Mozzarella @ 139 Kč/kg = 16.68 Kč
- **Total Food Cost: 19.13 Kč**
- Sale Price: 215 Kč
- **Profit Margin: 91.1%**

## Data Structure

### Ingredients Table
| Field | Description |
|-------|-------------|
| ID | Unique identifier (ING001-ING020) |
| Název | Ingredient name (Czech) |
| Dodavatel | Supplier name |
| Jedn. | Unit of measurement (kg/l) |
| Cena | Price per unit (CZK) |
| MIN | Minimum stock level |
| MAX | Maximum stock level |
| Aktuální | Current stock level |

### Recipe Mapping
The system uses a smart mapping dictionary to convert abbreviated ingredient names to full names:
- `Sugo` → `Sugo Solana`
- `Smeta` → `Smetana 20%`
- `Mozza` → `Mozzarella La Giusta`
- And more...

## Customization

To modify the system:

1. **Update ingredients**: Edit `ingredients_data` dictionary
2. **Add new pizzas**: Add entries to `normy_data` and `pizza_prices`
3. **Adjust recipes**: Modify ingredient quantities in `normy_data`
4. **Change formatting**: Update Excel formatting in the writer section

## License

This project is provided as-is for restaurant inventory management purposes.

## Author

Created for Pizza Bobo restaurant operations.
