import streamlit as st
import requests

st.title('DSP Report Finder')

# Text input for the user question
user_input = st.text_input("Type your question here:")

# Button to send the input to the API
if st.button('Ask'):
    if user_input:
        # API URL
        url = 'https://483u3stv5c.execute-api.us-east-1.amazonaws.com/prod/query'
        
        # Headers required by the API
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer goamc2024!'
        }
        
        # Data to be sent to API
        data = {'question': user_input}
        
        # Sending a POST request to the API
        response = requests.post(url, json=data, headers=headers)
        
        if response.status_code == 200:
            # Extract the list of queries from the response
            queries = response.json().get('queries', [])
            
            # Check if the list is not empty
            if queries:
                for query in queries:
                    # Display each query name and instruction
                    st.subheader("Response")
                    st.write(f"Report Type: {query['query_name']}")
                    st.write(query['instruction'])
            else:
                st.write("No details available for this query.")
        else:
            st.error(f"Failed to get response from the API. Status code: {response.status_code}")
    else:
        st.error("Please enter some text to ask.")
