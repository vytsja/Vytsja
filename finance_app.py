import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Фінансовий трекер", layout="centered")
st.title("Фінансовий трекер")

# --- Файл CSV
st.sidebar.header("🔄 Імпорт / експорт даних")
uploaded_file = st.sidebar.file_uploader("Завантаж CSV з фінансами", type=["csv"])

@st.cache_data
def load_data(file):
    df = pd.read_csv(file, parse_dates=["Дата"], dayfirst=True)
    return df

# --- Додавання нової транзакції
def add_transaction(df):
    st.subheader("➕ Додати нову транзакцію")
    with st.form("new_txn"):
        col1, col2, col3 = st.columns(3)
        date = col1.date_input("Дата", value=datetime.now())
        category = col2.text_input("Категорія", value="Інше")
        typ = col3.selectbox("Тип", ["Дохід", "Витрата"])
        amount = st.number_input("Сума (CZK)", min_value=0.0, step=1.0)
        comment = st.text_input("Коментар")
        debt = st.selectbox("Борг", ["ні", "так"])
        debt_status = st.text_input("Статус боргу", value="-")
        submitted = st.form_submit_button("Додати")
    if submitted and amount > 0:
        new_row = {
            "Дата": pd.to_datetime(date),
            "Категорія": category,
            "Тип (дохід/витрата)": typ,
            "Сума, CZK": amount,
            "Коментар": comment,
            "Борг (так/ні)": debt,
            "Статус боргу": debt_status,
        }
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        st.success("Транзакцію додано!")
    return df

# --- Основна логіка
if uploaded_file:
    df = load_data(uploaded_file)
    st.success("Дані завантажено!")
    df = add_transaction(df)
else:
    st.info("Завантаж CSV або додай першу транзакцію")
    # Створити пусту таблицю якщо файл не завантажено
    df = pd.DataFrame(columns=[
        "Дата", "Категорія", "Тип (дохід/витрата)", "Сума, CZK", "Коментар", "Борг (так/ні)", "Статус боргу"
    ])
    df = add_transaction(df)

# --- Показати таблицю
st.subheader("📋 Таблиця транзакцій")
df = df.sort_values(by="Дата", ascending=False)
st.dataframe(df, use_container_width=True)

# --- KPI
st.subheader("📊 Статистика")
total_income = df[df["Тип (дохід/витрата)"] == "Дохід"]["Сума, CZK"].sum()
total_expense = df[df["Тип (дохід/витрата)"] == "Витрата"]["Сума, CZK"].sum()
balance = total_income - total_expense

col1, col2, col3 = st.columns(3)
col1.metric("Дохід (CZK)", f"{total_income:,.2f}")
col2.metric("Витрати (CZK)", f"{total_expense:,.2f}")
col3.metric("Баланс (CZK)", f"{balance:,.2f}")

# --- Графік по тижнях
df["Week"] = df["Дата"].dt.strftime("%Y-%U")
weekly = df.groupby(["Week", "Тип (дохід/витрата)"])["Сума, CZK"].sum().unstack(fill_value=0)
st.subheader("📈 Тижневий аудит")
st.line_chart(weekly)

# --- Експорт
st.sidebar.markdown("---")
st.sidebar.download_button(
    label="⬇️ Завантаж CSV зі змінами",
    data=df.to_csv(index=False).encode('utf-8'),
    file_name="finansy_updated.csv",
    mime="text/csv"
)
