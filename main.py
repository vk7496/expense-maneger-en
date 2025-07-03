import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Expense Manager", page_icon="💰")
st.title("💰 Expense Manager App")

if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Category", "Amount"])

category = st.text_input("Category (e.g., Food, Transport)")
amount = st.number_input("Amount", min_value=0.0, step=1.0)

if st.button("Add Expense"):
    if category and amount:
        st.session_state.data = pd.concat([
            st.session_state.data,
            pd.DataFrame([[category, amount]], columns=["Category", "Amount"])
        ], ignore_index=True)
        st.success(f"Added {amount} to {category}")

st.subheader("📋 Expense List")
st.dataframe(st.session_state.data)

total = st.session_state.data["Amount"].sum()
st.info(f"💰 Total Expenses: {total:.2f} units")

if not st.session_state.data.empty:
    fig, ax = plt.subplots()
    st.session_state.data.groupby("Category").sum().plot.pie(
        y="Amount", ax=ax, autopct="%1.1f%%", legend=False
    )
    st.pyplot(fig)

csv = st.session_state.data.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Download CSV File",
    data=csv,
    file_name='expenses.csv',
    mime='text/csv',
)
