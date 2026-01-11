import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery

class BigQueryRepository:
    def __init__(self):
        self.credentials = service_account.Credentials.from_service_account_info(
            st.secrets["gcp_service_account"]
        )
        self.client = bigquery.Client(credentials=self.credentials, project='celestial-feat-360315')
    
    # Perform query.
    # # Cache a same query for about 10 min
    # @st.cache_data(ttl=600)
    def run_query(self, query):
        query_job = self.client.query(query)
        rows_raw = query_job.result()
        # Convert to list of dicts. Required for st.cache_data to hash the return value.
        rows = [dict(row) for row in rows_raw]
        return rows