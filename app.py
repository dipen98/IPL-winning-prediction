import streamlit as st
import pickle
import base64
import pandas as pd



pipe = pickle.load(open('pipe.pkl','rb'))
st.title('IPL win Predictor')
st.markdown(
    """
    <style>
    .reportview-container {
        background: linear-gradient( rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7) ), url('https://images.unsplash.com/photo-1594470117722-de4b9a02ebed?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1729&q=80');
        background-position:center top;
        font-weight:600;
        font-family : Lucida Console;
    }
   .sidebar .sidebar-content {
        background: url("https://images.unsplash.com/photo-1607734834519-d8576ae60ea6?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1657&q=80")
    }
    </style>
    """,
    unsafe_allow_html=True
)

teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Mohali', 'Bengaluru']

col1,col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select the batting team :', sorted(teams))
    
with col2:
    bowling_team = st.selectbox('Select the bowling team :', sorted(teams))
    
selected_city = st.selectbox('Select host city', sorted(cities))
target = st.number_input('Target')

col3,col4,col5 = st.columns(3)

with col3:
    score = st.number_input('Score')

with col4:
    overs = st.number_input('Overs Completed')
    
with col5:
    wickets = st.number_input('Wickets Out',)
    
if st.button('Predict Probablility'):
    if batting_team == bowling_team:
        st.header('Same Teams cannot play with each other')
    else:
         runs_left = target -score
         balls_left = 120 - (overs*6)
         wickets = 10-wickets
         crr = score/overs
         rrr = (runs_left * 6)/balls_left
         input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})
    
         result = pipe.predict_proba(input_df)
         loss = result[0][0]
         win = result[0][1]
         st.header(batting_team + "- " + str(round(win*100)) + "%")
         st.header(bowling_team + "- " + str(round(loss*100)) + "%")
   
    
   
