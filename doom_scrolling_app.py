import streamlit as st 
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder
import pandas as pd

st.sidebar.success("Select Pages") 

st.markdown("# Doom Scrolling Solutions") 
st.sidebar.header("Doom Scrolling Solutions")

def main_page():
    st.markdown("# Rotten Database:")
    st.sidebar.markdown("# Page 1 ")
    st.title("Rotten Tomatoe Database Best Movies:") 

    df = pd.read_csv("page_1_rt2023_web_scraping.csv") 
    text_search = st.text_input("Search movies by title or year", value="")
    m1 = df["Name"].str.contains(text_search)
    m2 = df["Year"].str.contains(text_search)

    maxValue = float(df["Rating"].max())
    minValue = float(df["Rating"].min())
    rating_sort = st.slider('Rating Scale:', min_value=minValue, max_value=maxValue, value=[minValue, maxValue])
    df_filtered = df[(df["Rating"] >= rating_sort[0]) & (df["Rating"] <= rating_sort[1])]
    df_search = df[m1 | m2]

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
        

def page2():
    st.markdown("# RT: Page 2")
    st.sidebar.markdown("# Page 2 ")
    st.title("Rotten Tomatoe Database TV Shows: Past 25 Years") 

    df = pd.read_csv("page2_rt25_tv_web_scraping.csv") 
    text_search = st.text_input("Search movies by title or year", value="")
    m1 = df["Name"].str.contains(text_search)
    m2 = df["Year"].str.contains(text_search)

    maxValue = float(df["Rating"].max())
    minValue = float(df["Rating"].min())
    rating_sort = st.slider('Rating Scale:', min_value=minValue, max_value=maxValue, value=[minValue, maxValue])
    df_filtered = df[(df["Rating"] >= rating_sort[0]) & (df["Rating"] <= rating_sort[1])]
    df_search = df[m1 | m2]

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
    st.markdown("# RT: Page 3 ")
    st.sidebar.markdown("# Page 3")
    st.title("RT: Best Movies Past 25 Years") 

    df = pd.read_csv("page3_movie_web_scraping25.csv") 
    text_search = st.text_input("Search movies by title or year", value="")
    m1 = df["Name"].str.contains(text_search)
    m2 = df["Year"].str.contains(text_search)

    maxValue = float(df["Rating"].max())
    minValue = float(df["Rating"].min())
    rating_sort = st.slider('Rating Scale:', min_value=minValue, max_value=maxValue, value=[minValue, maxValue])
    df_filtered = df[(df["Rating"] >= rating_sort[0]) & (df["Rating"] <= rating_sort[1])]
    df_search = df[m1 | m2]

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
    st.markdown("# RT : Page 4 ")
    st.sidebar.markdown("# Page 4 ")
    st.title("RT: Best TV Shows of 2023") 

    df = pd.read_csv("page4_rttv2023_web_scraping.csv") 
    text_search = st.text_input("Search movies by title or year", value="")
    m1 = df["Name"].str.contains(text_search)
    m2 = df["Year"].str.contains(text_search)

    maxValue = float(df["Rating"].max())
    minValue = float(df["Rating"].min())
    rating_sort = st.slider('Rating Scale:', min_value=minValue, max_value=maxValue, value=[minValue, maxValue])
    df_filtered = df[(df["Rating"] >= rating_sort[0]) & (df["Rating"] <= rating_sort[1])]
    df_search = df[m1 | m2]

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
    st.markdown("# RT: Page 5 ")
    st.sidebar.markdown("# Page 5 ")
    st.title("RT: Best TV Shows of 2024") 

    df = pd.read_csv("page5_RT_2024_tvscraping.csv") 
    text_search = st.text_input("Search movies by title or year", value="")
    m1 = df["Name"].str.contains(text_search)
    m2 = df["Year"].str.contains(text_search)

    maxValue = float(df["Rating"].max())
    minValue = float(df["Rating"].min())
    rating_sort = st.slider('Rating Scale:', min_value=minValue, max_value=maxValue, value=[minValue, maxValue])
    df_filtered = df[(df["Rating"] >= rating_sort[0]) & (df["Rating"] <= rating_sort[1])]
    df_search = df[m1 | m2]

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
    st.markdown("# IMDV Database: Page 6 ")
    st.sidebar.markdown("# Page 6 ")
    st.title("IMDB: Best Movies") 

    df = pd.read_csv("page5_imdb_web_scraping.csv") 
    text_search = st.text_input("Search movies by title or year", value="")
    m1 = df["Name"].str.contains(text_search)
    m2 = df["Year"].str.contains(text_search)

    maxValue = float(df["Rating"].max())
    minValue = float(df["Rating"].min())
    rating_sort = st.slider('Rating Scale:', min_value=minValue, max_value=maxValue, value=[minValue, maxValue])
    df_filtered = df[(df["Rating"] >= rating_sort[0]) & (df["Rating"] <= rating_sort[1])]
    df_search = df[m1 | m2]

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

page_names_to_funcs = {
    "Home Page": main_page,
    "Page 2": page2,
    "Page 3": page3,
    "Page 4": page4,
    "Page 5": page5,
    "Page 6": page6
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()