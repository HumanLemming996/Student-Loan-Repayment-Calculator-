import streamlit as st
col1, col2 = st.columns(2, gap='medium')

with col1:
    global salary, growth_factor, hike, income_percent, interest, base, maxterm, initial_loan, loan_amount, years
    st.title("Student Loan Repayment Calculator")
    st.warning("Calculations will appear on the right")
    salary = st.number_input("Salary (£)", value=None, min_value=0, max_value=1_000_000, placeholder="Expected Starting Salary")
    growth_factor = st.number_input("Wage Growth (Percentage %)", value=None, min_value=0, max_value=100, placeholder="Expected Salary Growth (Percentage)")
    hike = st.number_input("Wage Increase (£)", value=None, min_value=0, max_value=1_000_000, placeholder="Expected Salary Growth (Amount)")
    st.info("Recommended that only one of the growth factors is chosen and the other is set to 0")

    interest = st.number_input("Interest Rate (%)", value=7.8, min_value=0.0, max_value=100.0)
    income_percent = 9
    base = 25_000
    maxterm = 40
    initial_loan = 9250 * 3
    loan_amount = initial_loan * (1 + interest / 100)
    years = 40

def runner():
    global salary, growth_factor, hike, income_percent, interest, base, maxterm, initial_loan, loan_amount, years
    total = 0
    for k in range(0, maxterm):
        if loan_amount <= 0:
            years = k
            break
        else:
            if salary > base:
                threshold = salary - base
                payperyear = threshold * (income_percent / 100)

                total += payperyear
                loan_amount -= payperyear
        
        salary *= (1 + growth_factor / 100)
        salary += hike
        loan_amount *= (1 + interest / 100)


    st.header("You will be repaying approximately:")
    st.subheader(f":blue[£{round(total):,}] in total")
    if years == 40:
        st.subheader("Loan is written off after :blue[40] years")
    else:
        st.subheader(f"Paid in :blue[{years}] years")
    st.subheader("On average:")
    st.markdown(f" :orange[£{round(total / years):,}] per year")
    st.markdown(f" :orange[£{round(total / (years * 12)):,}] per month")
    st.markdown(f":orange[{round((total / initial_loan) * 100)}%] of the loan amount")

if st.button("Calculate"):
    with col2:
        with st.expander("Your Results", expanded=True):
            runner()
