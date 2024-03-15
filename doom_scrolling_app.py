import streamlit as st 
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder
import pandas as pd

st.sidebar.success("Select Pages") 
st.markdown("# Doom Scrolling Solutions") 
st.sidebar.header("Doom Scrolling Solutions")

def main_page():
    """
    Function: 
        -Gets creates the main page of the web application. 
    """

    st.markdown("# Rotten Database:")
    #Creates 
    st.sidebar.markdown("# Page 1 ")
    #Displays title of page. 
    st.title("Rotten Tomatoe Database Best Movies:") 

    #Reads in web scraped data as csv. 
    df = pd.read_csv("page_1_rt2023_web_scraping.csv") 
    #Creates a search window and displays search movies by title or year
    text_search = st.text_input("Search movies by title or year", value="")
    #Applies the table search functionality of the column Name 
    movie_title_search = df["Name"].str.contains(text_search)
    #Applies the table search functionality of the column Year
    movie_year_search = df["Year"].str.contains(text_search)

    #Taking the max value of the rating column.
    #also need to convert to float to change type 
    max_score = float(df["Rating"].max())
    #also need to convert to float to change type
    #Taking the min value of the rating column. 
    min_score = float(df["Rating"].min())
    #Creates a rating scale based on the range of minimum rating and maximum rating found in the table. 
    rating_sort = st.slider('Rating Scale:', min_value=min_score, max_value=min_score, value=[min_score, max_score])
    #Further filters the range of the slider 
    df_filtered = df[(df["Rating"] >= rating_sort[0]) & (df["Rating"] <= rating_sort[1])]
    #Applies the search functionality for the user to use (either searching title or yeaer)
    df_search = df[movie_title_search | movie_year_search]

    #Control flow of search engine.
    #If user decides to search...
    if text_search:
        #Allows search capabilities
        st.write(df_search)
    #Otherwise if rating sort is active. 
    elif rating_sort:
        #Allows sorting capabilities.
        st.write(df_filtered)
    #Else...
    else:
        #Continues search capabilitiles. 
        st.write(df_search)
    
    #Creates a table that allows user to select checkboxes.
    save_for_later = GridOptionsBuilder.from_dataframe(df)
    #Configures the table further to allow mutliple checkbox widgets to be selected.
    save_for_later.configure_selection(selection_mode='multiple', use_checkbox=True)
    #Creates the table. 
    gridoptions = save_for_later.build()
    #Displays the table dynamically that can be saved as a csv. 
    grid_table = AgGrid(df, height=250, gridOptions=gridoptions,
                    update_mode=GridUpdateMode.SELECTION_CHANGED)
    #Displays save for later above created table. 
    st.write('Save for later')
    #Makes the table a dataframe that can be save. 
    checked_row = grid_table["selected_rows"]
    st.dataframe(checked_row)


#page formatting continues the same....
    
def page2():
    """
    Function: 
        -Gets creates the second page of the web application. 
    """
    st.markdown("# RT: Page 2")
    st.sidebar.markdown("# Page 2 ")
    st.title("Rotten Tomatoe Database TV Shows: Past 25 Years") 

    df = pd.read_csv("page2_rt25_tv_web_scraping.csv") 
    text_search = st.text_input("Search movies by title or year", value="")
    movie_title_search = df["Name"].str.contains(text_search)
    movie_year_search = df["Year"].str.contains(text_search)

    max_score = float(df["Rating"].max())
    min_score = float(df["Rating"].min())
    rating_sort = st.slider('Rating Scale:', min_value=min_score, max_value=min_score, value=[min_score, max_score])
    df_filtered = df[(df["Rating"] >= rating_sort[0]) & (df["Rating"] <= rating_sort[1])]
    df_search = df[movie_title_search | movie_year_search]

    if text_search:
        st.write(df_search)
    elif rating_sort:
        st.write(df_filtered)
    else:
        st.write(df_search)
    

    gd = GridOptionsBuilder.from_dataframe(df)
    gd.configure_selection(selection_mode='multiple', use_checkbox=True)
    gridoptions = gd.build()

    grid_table = AgGrid(df, height=250, gridOptions=gridoptions,
                    update_mode=GridUpdateMode.SELECTION_CHANGED)

    st.write('Save for later')
    selected_row = grid_table["selected_rows"]
    st.dataframe(selected_row)

def page3():
    """
    Function: 
        -Gets creates the third page of the web application. 
    """
    st.markdown("# RT: Page 3 ")
    st.sidebar.markdown("# Page 3")
    st.title("RT: Best Movies Past 25 Years") 

    df = pd.read_csv("page3_movie_web_scraping25.csv") 
    text_search = st.text_input("Search movies by title or year", value="")
    movie_title_search = df["Name"].str.contains(text_search)
    movie_year_search = df["Year"].str.contains(text_search)

    max_score = float(df["Rating"].max())
    min_score = float(df["Rating"].min())
    rating_sort = st.slider('Rating Scale:', min_value=min_score, max_value=min_score, value=[min_score, max_score])
    df_filtered = df[(df["Rating"] >= rating_sort[0]) & (df["Rating"] <= rating_sort[1])]
    df_search = df[movie_title_search | movie_year_search]

    if text_search:
        st.write(df_search)
    elif rating_sort:
        st.write(df_filtered)
    else:
        st.write(df_search)
    

    gd = GridOptionsBuilder.from_dataframe(df)
    gd.configure_selection(selection_mode='multiple', use_checkbox=True)
    gridoptions = gd.build()

    grid_table = AgGrid(df, height=250, gridOptions=gridoptions,
                    update_mode=GridUpdateMode.SELECTION_CHANGED)

    st.write('Save for later')
    selected_row = grid_table["selected_rows"]
    st.dataframe(selected_row)

def page4():
    """
    Function: 
        -Gets creates the fourth page of the web application. 
    """
    st.markdown("# RT : Page 4 ")
    st.sidebar.markdown("# Page 4 ")
    st.title("RT: Best TV Shows of 2023") 

    df = pd.read_csv("page4_rttv2023_web_scraping.csv") 
    text_search = st.text_input("Search movies by title or year", value="")
    movie_title_search = df["Name"].str.contains(text_search)
    movie_year_search = df["Year"].str.contains(text_search)

    max_score = float(df["Rating"].max())
    min_score = float(df["Rating"].min())
    rating_sort = st.slider('Rating Scale:', min_value=min_score, max_value=min_score, value=[min_score, max_score])
    df_filtered = df[(df["Rating"] >= rating_sort[0]) & (df["Rating"] <= rating_sort[1])]
    df_search = df[movie_title_search | movie_year_search]

    if text_search:
        st.write(df_search)
    elif rating_sort:
        st.write(df_filtered)
    else:
        st.write(df_search)
    

    gd = GridOptionsBuilder.from_dataframe(df)
    gd.configure_selection(selection_mode='multiple', use_checkbox=True)
    gridoptions = gd.build()

    grid_table = AgGrid(df, height=250, gridOptions=gridoptions,
                    update_mode=GridUpdateMode.SELECTION_CHANGED)

    st.write('Save for later')
    selected_row = grid_table["selected_rows"]
    st.dataframe(selected_row)

def page5():
    """
    Function: 
        -Gets creates the fifth page of the web application. 
    """
    st.markdown("# RT: Page 5 ")
    st.sidebar.markdown("# Page 5 ")
    st.title("RT: Best TV Shows of 2024") 

    df = pd.read_csv("page5_RT_2024_tvscraping.csv") 
    text_search = st.text_input("Search movies by title or year", value="")
    movie_title_search = df["Name"].str.contains(text_search)
    movie_year_search = df["Year"].str.contains(text_search)

    max_score = float(df["Rating"].max())
    min_score = float(df["Rating"].min())
    rating_sort = st.slider('Rating Scale:', min_value=min_score, max_value=min_score, value=[min_score, max_score])
    df_filtered = df[(df["Rating"] >= rating_sort[0]) & (df["Rating"] <= rating_sort[1])]
    df_search = df[movie_title_search | movie_year_search]

    if text_search:
        st.write(df_search)
    elif rating_sort:
        st.write(df_filtered)
    else:
        st.write(df_search)
    

    gd = GridOptionsBuilder.from_dataframe(df)
    gd.configure_selection(selection_mode='multiple', use_checkbox=True)
    gridoptions = gd.build()

    grid_table = AgGrid(df, height=250, gridOptions=gridoptions,
                    update_mode=GridUpdateMode.SELECTION_CHANGED)

    st.write('Save for later')
    selected_row = grid_table["selected_rows"]
    st.dataframe(selected_row)

def page6():
    """
    Function: 
        -Gets creates the sixth page of the web application. 
    """
    st.markdown("# IMDV Database: Page 6 ")
    st.sidebar.markdown("# Page 6 ")
    st.title("IMDB: Best Movies") 

    df = pd.read_csv("page5_imdb_web_scraping.csv") 
    text_search = st.text_input("Search movies by title or year", value="")
    movie_title_search = df["Name"].str.contains(text_search)
    movie_year_search = df["Year"].str.contains(text_search)

    max_score = float(df["Rating"].max())
    min_score = float(df["Rating"].min())
    rating_sort = st.slider('Rating Scale:', min_value=min_score, max_value=min_score, value=[min_score, max_score])
    df_filtered = df[(df["Rating"] >= rating_sort[0]) & (df["Rating"] <= rating_sort[1])]
    df_search = df[movie_title_search | movie_year_search]

    if text_search:
        st.write(df_search)
    elif rating_sort:
        st.write(df_filtered)
    else:
        st.write(df_search)
    

    gd = GridOptionsBuilder.from_dataframe(df)
    gd.configure_selection(selection_mode='multiple', use_checkbox=True)
    gridoptions = gd.build()

    grid_table = AgGrid(df, height=250, gridOptions=gridoptions,
                    update_mode=GridUpdateMode.SELECTION_CHANGED)

    st.write('Save for later')
    selected_row = grid_table["selected_rows"]
    st.dataframe(selected_row)


#Creates multi-page functionality from pages functions
page_names_to_funcs = {
    "Home Page": main_page,
    "Page 2": page2,
    "Page 3": page3,
    "Page 4": page4,
    "Page 5": page5,
    "Page 6": page6
}

#Allows users to select specific pages. 
selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

#References: 
#https://docs.streamlit.io/library/api-reference/widgets/st.selectbox
#https://blog.streamlit.io/create-a-search-engine-with-streamlit-and-google-sheets/
#https://docs.streamlit.io/library/api-reference/widgets/st.slider
#https://discuss.streamlit.io/t/get-min-max-values-of-a-slider-based-on-min-and-max-values-of-a-given-dataframe-column/2698
#https://snyk.io/advisor/python/streamlit/functions/streamlit.selectbox
#https://docs.streamlit.io/get-started/tutorials/create-a-multipage-app
#https://stackoverflow.com/questions/72633449/add-checkbox-in-dataframe
#https://blog.streamlit.io/introducing-multipage-apps/

