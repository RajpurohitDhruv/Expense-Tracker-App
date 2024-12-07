import streamlit as st
import pandas as pd
import datetime

# Set the title of the app
st.title("Expense Tracker App 📊")

# Initialize session state for storing expenses data
if "expenses" not in st.session_state:
    st.session_state.expenses = []

# Function to add expense
def add_expense(category, amount, description, date):
    expense = {
        "Category": category,
        "Amount": amount,
        "Description": description,
        "Date": date,
    }
    st.session_state.expenses.append(expense)

# Input fields for adding a new expense
st.subheader("Add a New Expense")
category = st.selectbox("Category", ["Food", "Transport", "Entertainment", "Utilities", "Other"])
amount = st.number_input("Amount", min_value=0.0, step=0.1)
description = st.text_input("Description")
date = st.date_input("Date", value=datetime.date.today())

if st.button("Add Expense"):
    if amount > 0:
        add_expense(category, amount, description, date)
        st.success("Expense added successfully!")
    else:
        st.error("Please enter a valid amount.")

# Display the list of expenses
if st.session_state.expenses:
    st.subheader("Your Expenses")
    expenses_df = pd.DataFrame(st.session_state.expenses)
    expenses_df["Date"] = pd.to_datetime(expenses_df["Date"])
    st.dataframe(expenses_df)

    # Calculate total expenses
    total_expense = expenses_df["Amount"].sum()
    st.write(f"**Total Expenses:** ${total_expense:.2f}")

    # Category-wise summary
    st.subheader("Category Summary")
    category_summary = expenses_df.groupby("Category")["Amount"].sum().reset_index()
    st.bar_chart(category_summary.set_index("Category")["Amount"])

else:
    st.info("No expenses added yet. Add your first expense!")

# Add a footer
st.markdown("---")
st.markdown("Built with Streamlit")
