import streamlit as st
from src.analyze_dataset import (
    show_basic_info,
    show_columns_types,
    show_missing_values,
    show_duplicate_values,
    show_stats,
)

st.set_page_config(page_title="Overview", layout="wide")

st.subheader("Overview Dataset")
st.markdown("---")

if "df" not in st.session_state:
    st.warning("Please upload the dataset first")
else:
    col1, col2 = st.columns([1,1 ], gap="large")
    df = st.session_state["df"]
    
    with col1:
        st.write("Dataframe")
        st.dataframe(df.head(), hide_index=True)
        
    with col2:
        st.write("Basic Information")
        df_basic = show_basic_info(df)
        st.dataframe(df_basic, hide_index=True)
        
        st.write("Columns Informatoin")
        df_cols = show_columns_types(df)
        st.dataframe(df_cols, hide_index=True)
