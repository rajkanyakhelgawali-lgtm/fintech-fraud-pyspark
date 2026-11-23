import streamlit as st
import pandas as pd
from databricks import sql
from google import genai

st.set_page_config(page_title="FinTech Fraud Intelligence", page_icon="🛡️", layout="wide")

st.title("🛡️ Real-Time FinTech Fraud & GenAI Investigation Dashboard")
st.markdown("**Backend:** PySpark + Delta Lake + MLlib (6.36M Transactions) | **AI:** Random Forest (0.9890 ROC-AUC) + Google GenAI")

# --- 1. LOAD DATA DIRECTLY FROM DATABRICKS (WITH CSV FALLBACK) ---
@st.cache_data(ttl=600)
def load_alerts():
    try:
        with sql.connect(
            server_hostname=st.secrets["DATABRICKS_HOST"],
            http_path=st.secrets["DATABRICKS_HTTP_PATH"],
            access_token=st.secrets["DATABRICKS_TOKEN"]
        ) as conn:
            df = pd.read_sql("SELECT * FROM workspace.default.critical_fraud_alerts ORDER BY fraud_prob DESC", conn)
            return df, "🟢 Connected Live to Databricks Delta Table"
    except Exception:
        df = pd.read_csv("critical_alerts.csv")
        return df, "🟡 Loaded from Cached Backup (Databricks Serverless Sleeping)"

alerts_df, connection_status = load_alerts()
st.caption(connection_status)

# --- 2. EXECUTIVE KPI CARDS ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Txns Scanned", "6,362,620")
col2.metric("Model Accuracy (ROC-AUC)", "98.90%")
col3.metric("Critical Alerts (>90%)", len(alerts_df))
col4.metric("Total Flagged Value", f"${alerts_df['amount'].sum():,.0f}")

st.divider()

# --- 3. INTERACTIVE RISK THRESHOLD FILTER ---
st.sidebar.header("🎛️ Risk Controls")
threshold = st.sidebar.slider("Minimum Fraud Probability Threshold", 0.90, 0.99, 0.90, 0.01)
txn_type = st.sidebar.multiselect("Transaction Type", options=alerts_df["type"].unique(), default=alerts_df["type"].unique())

filtered_df = alerts_df[(alerts_df["fraud_prob"] >= threshold) & (alerts_df["type"].isin(txn_type))]

left_col, right_col = st.columns([2, 1])

with left_col:
    st.subheader(f"🚨 High-Risk Transactions ({len(filtered_df)} Alerts)")
    st.dataframe(filtered_df, use_container_width=True, height=350)

with right_col:
    st.subheader("📊 Alerts by Payment Type")
    st.bar_chart(filtered_df["type"].value_counts())

st.divider()

# --- 4. LIVE GENAI FRAUD INVESTIGATOR ---
st.subheader("🤖 GenAI Suspicious Activity Report (SAR) Generator")
selected_sender = st.selectbox("Select a Flagged Sender Account to Investigate:", filtered_df["nameOrig"].head(25))

if st.button("Generate AI Investigation Report"):
    txn = filtered_df[filtered_df["nameOrig"] == selected_sender].iloc[0].to_dict()
    
    with st.spinner("Analyzing transaction patterns with GenAI..."):
        client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
        prompt = f"""
        You are a senior bank fraud compliance analyst. Write a concise 3-bullet Suspicious Activity Report (SAR) explaining why this transaction is high risk and what action to take:
        - Type: {txn['type']}
        - Amount: ${txn['amount']:,.2f}
        - Old Balance: ${txn['oldbalanceOrg']:,.2f}
        - New Balance: ${txn['newbalanceOrig']:,.2f}
        - Account Emptied: {txn['is_account_emptied']}
        - ML Fraud Probability: {txn['fraud_prob']*100:.2f}%
        """
        for model_name in ["gemma-4-26b-a4b-it", "gemini-3.8-flash"]:
            try:
                response = client.models.generate_content(model=model_name, contents=prompt)
                st.success(f"Investigation Report for Account **{selected_sender}**")
                st.write(response.text)
                break
            except Exception:
                continue
