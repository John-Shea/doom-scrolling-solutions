import streamlit as st 
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder
import pandas as pd

st.sidebar.success("Select Pages") 
st.markdown("# Doom Scrolling Solutions") 
st.sidebar.header("Doom Scrolling Solutions")
st.text('')

def main_page():
    """
    Function: 
        -Gets creates the main page of the web application. 
    """

    # st.markdown("# Rotten Database:")
    #Creates 
    st.sidebar.markdown("# Page 1 ")
    #Displays title of page. 
    st.title("Best Movies of 2023:")
    st.subheader(":gray[Rotten Tomato Database]")
    st.divider()  

    st.caption('First read throught the provided table and search for interesting movies/tv show by name or year from the provided table. Information on the movie can be seen either in a summary format or a critic consensus for the particular medium. Then please go on to create your own table to watch later from the list that you have searched over. Also use the provided rating slider to hone in on a range of movies or tv shows. ')

    #Reads in web scraped data as csv. 
    df = pd.read_csv("page1_web_scraping.csv") 
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
    st.caption('Want to filter the movies further. Please use the slider to a range of your liking to filter and display movies / tv shows. ')
    rating_sort = st.slider('Rating Scale:', min_value=min_score, max_value=min_score, value=[min_score, max_score])
    #Further filters the range of the slider 
    df_filtered = df[(df["Rating"] >= rating_sort[0]) & (df["Rating"] <= rating_sort[1])]
    #Applies the search functionality for the user to use (either searching title or yeaer)
    df_search = df[movie_title_search | movie_year_search]

    st.caption('No time to search the table? Set the sort box to rating in order to see a table with only the top five rated movies / tv shows.  ')
# Select column to sort by
    sort_column = st.selectbox('Sort table by Rating:', df.columns[2:4])
# Sort DataFrame based on selected column
    df_sorted = df.sort_values(by=sort_column, ascending=False)

# Display top 5 movies based on the selected column
    if sort_column == 'Rating':
        st.write('Top 5 Movies based on Rating:')
        top_5_movies = df_sorted.head(5)
        st.dataframe(top_5_movies)

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
    elif sort_column == 'Rating':
        st.write('Top 5 based on Rating:')
        top_5_movies = df_sorted.head(5)
        st.dataframe(top_5_movies)
        #Continues search capabilitiles. 
        st.write(df_search)
    else:
        # Display top 5 movies based on the selected column
        st.write(df_search)

    st.divider()
    st.caption('Having search the above table, please check the indicated row of the movie you are interested in watching later. Checking the rows will create a table of movies or tv shows you want to save for later. ')
    
    #Creates a table that allows user to select checkboxes.
    save_for_later = GridOptionsBuilder.from_dataframe(df)
    #Configures the table further to allow mutliple checkbox widgets to be selected.
    save_for_later.configure_selection(selection_mode='multiple', use_checkbox=True)
    #Creates the table. 
    gridoptions = save_for_later.build()
    #Displays the table dynamically that can be saved as a csv. 
    grid_table = AgGrid(df, height=250, gridOptions=gridoptions,
                    update_mode=GridUpdateMode.SELECTION_CHANGED)
    
    st.divider() 
    #Displays save for later above created table. 
    st.write('Save for later')
    #Makes the table a dataframe that can be saved. 
    checked_row = grid_table["selected_rows"]
    st.dataframe(checked_row)

    st.caption('Once you are satisified with your selection please press the save button to save your created table. The table of movies and tv shows will be saved as a csv formated table. Enjoy the rest of the pages to find more highly rated movies and tv shows. ')

# Download button to save the selected rows as a CSV file
    if st.button('Download Selected Rows as CSV'):
    # Convert selected rows to DataFrame
        selected_df = pd.DataFrame(checked_row)
    # Save DataFrame as CSV file
        csv = selected_df.to_csv(index=False)
    # Offer the CSV file as a download link
        st.download_button(label='Save Table', data=csv, file_name='selected_rows.csv', mime='text/csv')

#page formatting continues the same....
    
def page2():
    """
    Function: 
        -Gets creates the second page of the web application. 
    """
    st.sidebar.markdown("# Page 2 ")
    st.title("Best TV Shows of Past 25 Years:")
    st.subheader(":gray[Rotten Tomato Database]")
    st.divider()

    st.caption('First read throught the provided table and search for interesting movies/tv show by name or year from the provided table. Information on the movie can be seen either in a summary format or a critic consensus for the particular medium. Then please go on to create your own table to watch later from the list that you have searched over. Also use the provided rating slider to hone in on a range of movies or tv shows. ')

    df = pd.read_csv("page2_web_scraping.csv") 
    text_search = st.text_input("Search movies by title or year", value="")
    movie_title_search = df["Name"].str.contains(text_search)
    movie_year_search = df["Year"].str.contains(text_search)

    max_score = float(df["Rating"].max())
    min_score = float(df["Rating"].min())
    rating_sort = st.slider('Rating Scale:', min_value=min_score, max_value=min_score, value=[min_score, max_score])
    df_filtered = df[(df["Rating"] >= rating_sort[0]) & (df["Rating"] <= rating_sort[1])]
    df_search = df[movie_title_search | movie_year_search]

    st.caption('No time to search the table? Set the sort box to rating in order to see a table with only the top five rated movies / tv shows.  ')
# Select column to sort by
    sort_column = st.selectbox('Sort table by Rating:', df.columns[2:4])
# Sort DataFrame based on selected column
    df_sorted = df.sort_values(by=sort_column, ascending=False)

# Display top 5 movies based on the selected column
    if sort_column == 'Rating':
        st.write('Top 5 Movies based on Rating:')
        top_5_movies = df_sorted.head(5)
        st.dataframe(top_5_movies)

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
    elif sort_column == 'Rating':
        st.write('Top 5 based on Rating:')
        top_5_movies = df_sorted.head(5)
        st.dataframe(top_5_movies)
        #Continues search capabilitiles. 
        st.write(df_search)
    else:
        # Display top 5 movies based on the selected column
        st.write(df_search)

    st.divider()
    st.caption('Having search the above table, please check the indicated row of the movie you are interested in watching later. Checking the rows will create a table of movies or tv shows you want to save for later. ')
    gd = GridOptionsBuilder.from_dataframe(df)
    gd.configure_selection(selection_mode='multiple', use_checkbox=True)
    gridoptions = gd.build()

    grid_table = AgGrid(df, height=250, gridOptions=gridoptions,
                    update_mode=GridUpdateMode.SELECTION_CHANGED)

    st.write('Save for later')
    selected_row = grid_table["selected_rows"]
    st.dataframe(selected_row)


    st.caption('Once you are satisified with your selection please press the save button to save your created table. The table of movies and tv shows will be saved as a csv formated table. Enjoy the rest of the pages to find more highly rated movies and tv shows. ')

# Download button to save the selected rows as a CSV file
    if st.button('Download Selected Rows as CSV'):
    # Convert selected rows to DataFrame
        selected_df = pd.DataFrame(selected_row)
    # Save DataFrame as CSV file
        csv = selected_df.to_csv(index=False)
    # Offer the CSV file as a download link
        st.download_button(label='Save Table', data=csv, file_name='selected_rows.csv', mime='text/csv')

def page3():
    """
    Function: 
        -Gets creates the third page of the web application. 
    """
    st.sidebar.markdown("# Page 3")
    st.title("Best Movies of Past 25 Years:")
    st.subheader(":gray[Rotten Tomato Database]")
    st.divider()

    st.caption('First read throught the provided table and search for interesting movies/tv show by name or year from the provided table. Information on the movie can be seen either in a summary format or a critic consensus for the particular medium. Then please go on to create your own table to watch later from the list that you have searched over. Also use the provided rating slider to hone in on a range of movies or tv shows. ')

    df = pd.read_csv("page3_web_scraping.csv") 
    text_search = st.text_input("Search movies by title or year", value="")
    movie_title_search = df["Name"].str.contains(text_search)
    movie_year_search = df["Year"].str.contains(text_search)

    max_score = float(df["Rating"].max())
    min_score = float(df["Rating"].min())
    rating_sort = st.slider('Rating Scale:', min_value=min_score, max_value=min_score, value=[min_score, max_score])
    df_filtered = df[(df["Rating"] >= rating_sort[0]) & (df["Rating"] <= rating_sort[1])]
    df_search = df[movie_title_search | movie_year_search]

    st.caption('No time to search the table? Set the sort box to rating in order to see a table with only the top five rated movies / tv shows.  ')
# Select column to sort by
    sort_column = st.selectbox('Sort table by Rating:', df.columns[2:4])
# Sort DataFrame based on selected column
    df_sorted = df.sort_values(by=sort_column, ascending=False)

# Display top 5 movies based on the selected column
    if sort_column == 'Rating':
        st.write('Top 5 Movies based on Rating:')
        top_5_movies = df_sorted.head(5)
        st.dataframe(top_5_movies)

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
    elif sort_column == 'Rating':
        st.write('Top 5 based on Rating:')
        top_5_movies = df_sorted.head(5)
        st.dataframe(top_5_movies)
        #Continues search capabilitiles. 
        st.write(df_search)
    else:
        # Display top 5 movies based on the selected column
        st.write(df_search)

    st.divider()
    st.caption('Having search the above table, please check the indicated row of the movie you are interested in watching later. Checking the rows will create a table of movies or tv shows you want to save for later. ')
    gd = GridOptionsBuilder.from_dataframe(df)
    gd.configure_selection(selection_mode='multiple', use_checkbox=True)
    gridoptions = gd.build()

    grid_table = AgGrid(df, height=250, gridOptions=gridoptions,
                    update_mode=GridUpdateMode.SELECTION_CHANGED)

    st.write('Save for later')
    selected_row = grid_table["selected_rows"]
    st.dataframe(selected_row)

    st.caption('Once you are satisified with your selection please press the save button to save your created table. The table of movies and tv shows will be saved as a csv formated table. Enjoy the rest of the pages to find more highly rated movies and tv shows. ')
# Download button to save the selected rows as a CSV file
    if st.button('Download Selected Rows as CSV'):
    # Convert selected rows to DataFrame
        selected_df = pd.DataFrame(selected_row)
    # Save DataFrame as CSV file
        csv = selected_df.to_csv(index=False)
    # Offer the CSV file as a download link
        st.download_button(label='Save Table', data=csv, file_name='selected_rows.csv', mime='text/csv')


def page4():
    """
    Function: 
        -Gets creates the fourth page of the web application. 
    """
    st.sidebar.markdown("# Page 4 ")
    st.title("Best TV Shows of 2023:")
    st.subheader(":gray[Rotten Tomato Database]")
    st.divider()

    st.caption('First read throught the provided table and search for interesting movies/tv show by name or year from the provided table. Information on the movie can be seen either in a summary format or a critic consensus for the particular medium. Then please go on to create your own table to watch later from the list that you have searched over. Also use the provided rating slider to hone in on a range of movies or tv shows. ')

    df = pd.read_csv("page4_web_scraping.csv") 
    text_search = st.text_input("Search movies by title or year", value="")
    movie_title_search = df["Name"].str.contains(text_search)
    movie_year_search = df["Year"].str.contains(text_search)

    max_score = float(df["Rating"].max())
    min_score = float(df["Rating"].min())
    rating_sort = st.slider('Rating Scale:', min_value=min_score, max_value=min_score, value=[min_score, max_score])
    df_filtered = df[(df["Rating"] >= rating_sort[0]) & (df["Rating"] <= rating_sort[1])]
    df_search = df[movie_title_search | movie_year_search]

    st.caption('No time to search the table? Set the sort box to rating in order to see a table with only the top five rated movies / tv shows.  ')
# Select column to sort by
    sort_column = st.selectbox('Sort table by Rating:', df.columns[2:4])
# Sort DataFrame based on selected column
    df_sorted = df.sort_values(by=sort_column, ascending=False)

# Display top 5 movies based on the selected column
    if sort_column == 'Rating':
        st.write('Top 5 Movies based on Rating:')
        top_5_movies = df_sorted.head(5)
        st.dataframe(top_5_movies)

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
    elif sort_column == 'Rating':
        st.write('Top 5 based on Rating:')
        top_5_movies = df_sorted.head(5)
        st.dataframe(top_5_movies)
        #Continues search capabilitiles. 
        st.write(df_search)
    else:
        # Display top 5 movies based on the selected column
        st.write(df_search)

    st.divider()
    st.caption('Having search the above table, please check the indicated row of the movie you are interested in watching later. Checking the rows will create a table of movies or tv shows you want to save for later. ')
    gd = GridOptionsBuilder.from_dataframe(df)
    gd.configure_selection(selection_mode='multiple', use_checkbox=True)
    gridoptions = gd.build()

    grid_table = AgGrid(df, height=250, gridOptions=gridoptions,
                    update_mode=GridUpdateMode.SELECTION_CHANGED)

    st.write('Save for later')
    selected_row = grid_table["selected_rows"]
    st.dataframe(selected_row)

    st.caption('Once you are satisified with your selection please press the save button to save your created table. The table of movies and tv shows will be saved as a csv formated table. Enjoy the rest of the pages to find more highly rated movies and tv shows. ')
# Download button to save the selected rows as a CSV file
    if st.button('Download Selected Rows as CSV'):
    # Convert selected rows to DataFrame
        selected_df = pd.DataFrame(selected_row)
    # Save DataFrame as CSV file
        csv = selected_df.to_csv(index=False)
    # Offer the CSV file as a download link
        st.download_button(label='Save Table', data=csv, file_name='selected_rows.csv', mime='text/csv')


def page5():
    """
    Function: 
        -Gets creates the fifth page of the web application. 
    """
    st.sidebar.markdown("# Page 5 ")
    st.title("Best TV Shows of 2024:")
    st.subheader(":gray[Rotten Tomato Database]")
    st.divider()

    st.caption('First read throught the provided table and search for interesting movies/tv show by name or year from the provided table. Information on the movie can be seen either in a summary format or a critic consensus for the particular medium. Then please go on to create your own table to watch later from the list that you have searched over. Also use the provided rating slider to hone in on a range of movies or tv shows. ')

    df = pd.read_csv("page5_web_scraping.csv") 
    text_search = st.text_input("Search movies by title or year", value="")
    movie_title_search = df["Name"].str.contains(text_search)
    movie_year_search = df["Year"].str.contains(text_search)

    max_score = float(df["Rating"].max())
    min_score = float(df["Rating"].min())
    rating_sort = st.slider('Rating Scale:', min_value=min_score, max_value=min_score, value=[min_score, max_score])
    df_filtered = df[(df["Rating"] >= rating_sort[0]) & (df["Rating"] <= rating_sort[1])]
    df_search = df[movie_title_search | movie_year_search]

    st.caption('No time to search the table? Set the sort box to rating in order to see a table with only the top five rated movies / tv shows.  ')
# Select column to sort by
    sort_column = st.selectbox('Sort table by Rating:', df.columns[2:4])
# Sort DataFrame based on selected column
    df_sorted = df.sort_values(by=sort_column, ascending=False)

# Display top 5 movies based on the selected column
    if sort_column == 'Rating':
        st.write('Top 5 Movies based on Rating:')
        top_5_movies = df_sorted.head(5)
        st.dataframe(top_5_movies)

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
    elif sort_column == 'Rating':
        st.write('Top 5 based on Rating:')
        top_5_movies = df_sorted.head(5)
        st.dataframe(top_5_movies)
        #Continues search capabilitiles. 
        st.write(df_search)
    else:
        # Display top 5 movies based on the selected column
        st.write(df_search)

    st.divider()
    st.caption('Having search the above table, please check the indicated row of the movie you are interested in watching later. Checking the rows will create a table of movies or tv shows you want to save for later. ')
    gd = GridOptionsBuilder.from_dataframe(df)
    gd.configure_selection(selection_mode='multiple', use_checkbox=True)
    gridoptions = gd.build()

    grid_table = AgGrid(df, height=250, gridOptions=gridoptions,
                    update_mode=GridUpdateMode.SELECTION_CHANGED)

    st.write('Save for later')
    selected_row = grid_table["selected_rows"]
    st.dataframe(selected_row)

    @st.cache_data
    def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

    saved_csv = convert_df(df)
    st.caption('Once you are satisified with your selection please press the save button to save your created table. The table of movies and tv shows will be saved as a csv formated table. Enjoy the rest of the pages to find more highly rated movies and tv shows. ')
# Download button to save the selected rows as a CSV file
    if st.button('Download Selected Rows as CSV'):
    # Convert selected rows to DataFrame
        selected_df = pd.DataFrame(selected_row)
    # Save DataFrame as CSV file
        csv = selected_df.to_csv(index=False)
    # Offer the CSV file as a download link
        st.download_button(label='Save Table', data=csv, file_name='selected_rows.csv', mime='text/csv')

def page6():
    """
    Function: 
        -Gets creates the sixth page of the web application. 
    """
    st.sidebar.markdown("# Page 6 ")
    st.title("Best Movies:")
    st.subheader(":gray[IMDB Database]")
    st.divider()

    st.caption('First read throught the provided table and search for interesting movies/tv show by name or year from the provided table. Information on the movie can be seen either in a summary format or a critic consensus for the particular medium. Then please go on to create your own table to watch later from the list that you have searched over. Also use the provided rating slider to hone in on a range of movies or tv shows. ')

    df = pd.read_csv("page6_web_scrapingIMDB.csv") 
    text_search = st.text_input("Search movies by title or year", value="")
    movie_title_search = df["Name"].str.contains(text_search)
    movie_year_search = df["Year"].str.contains(text_search)

    max_score = float(df["Rating"].max())
    min_score = float(df["Rating"].min())
    rating_sort = st.slider('Rating Scale:', min_value=min_score, max_value=min_score, value=[min_score, max_score])
    df_filtered = df[(df["Rating"] >= rating_sort[0]) & (df["Rating"] <= rating_sort[1])]
    df_search = df[movie_title_search | movie_year_search]


    st.caption('No time to search the table? Set the sort box to rating in order to see a table with only the top five rated movies / tv shows.  ')
# Select column to sort by
    sort_column = st.selectbox('Sort table by Rating:', df.columns[3:5])
# Sort DataFrame based on selected column
    df_sorted = df.sort_values(by=sort_column, ascending=False)

# Display top 5 movies based on the selected column
    if sort_column == 'Rating':
        st.write('Top 5 Movies based on Rating:')
        top_5_movies = df_sorted.head(5)
        st.dataframe(top_5_movies)

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
    elif sort_column == 'Rating':
        st.write('Top 5 based on Rating:')
        top_5_movies = df_sorted.head(5)
        st.dataframe(top_5_movies)
        #Continues search capabilitiles. 
        st.write(df_search)
    else:
        # Display top 5 movies based on the selected column
        st.write(df_search)

    st.divider()
    st.caption('Having search the above table, please check the indicated row of the movie you are interested in watching later. Checking the rows will create a table of movies or tv shows you want to save for later. ')
    gd = GridOptionsBuilder.from_dataframe(df)
    gd.configure_selection(selection_mode='multiple', use_checkbox=True)
    gridoptions = gd.build()

    grid_table = AgGrid(df, height=250, gridOptions=gridoptions,
                    update_mode=GridUpdateMode.SELECTION_CHANGED)

    st.write('Save for later')
    selected_row = grid_table["selected_rows"]
    st.dataframe(selected_row)

    st.caption('Once you are satisified with your selection please press the save button to save your created table. The table of movies and tv shows will be saved as a csv formated table. Enjoy the rest of the pages to find more highly rated movies and tv shows. ')
# Download button to save the selected rows as a CSV file
    if st.button('Download Selected Rows as CSV'):
    # Convert selected rows to DataFrame
        selected_df = pd.DataFrame(selected_row)
    # Save DataFrame as CSV file
        csv = selected_df.to_csv(index=False)
    # Offer the CSV file as a download link
        st.download_button(label='Save Table', data=csv, file_name='selected_rows.csv', mime='text/csv')

def page7():
    """
    Function: 
        -Gets creates the sixth page of the web application. 
    """
    st.sidebar.markdown("# Page 7 ")
    st.title("Best TV Shows:")
    st.subheader(":gray[IMDB Database]")
    st.divider()

    st.caption('First read throught the provided table and search for interesting movies/tv show by name or year from the provided table. Information on the movie can be seen either in a summary format or a critic consensus for the particular medium. Then please go on to create your own table to watch later from the list that you have searched over. Also use the provided rating slider to hone in on a range of movies or tv shows. ')

    df = pd.read_csv("page7_web_scrapingIMDB.csv") 
    text_search = st.text_input("Search movies by title or year", value="")
    movie_title_search = df["Name"].str.contains(text_search)
    movie_year_search = df["Year"].str.contains(text_search)

    max_score = float(df["Rating"].max())
    min_score = float(df["Rating"].min())
    rating_sort = st.slider('Rating Scale:', min_value=min_score, max_value=min_score, value=[min_score, max_score])
    df_filtered = df[(df["Rating"] >= rating_sort[0]) & (df["Rating"] <= rating_sort[1])]
    df_search = df[movie_title_search | movie_year_search]


    st.caption('No time to search the table? Set the sort box to rating in order to see a table with only the top five rated movies / tv shows.  ')
# Select column to sort by
    sort_column = st.selectbox('Sort table by Rating:', df.columns[3:5])
# Sort DataFrame based on selected column
    df_sorted = df.sort_values(by=sort_column, ascending=False)

# Display top 5 movies based on the selected column
    if sort_column == 'Rating':
        st.write('Top 5 Movies based on Rating:')
        top_5_movies = df_sorted.head(5)
        st.dataframe(top_5_movies)

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
    elif sort_column == 'Rating':
        st.write('Top 5 based on Rating:')
        top_5_movies = df_sorted.head(5)
        st.dataframe(top_5_movies)
        #Continues search capabilitiles. 
        st.write(df_search)
    else:
        # Display top 5 movies based on the selected column
        st.write(df_search)

    st.divider()
    st.caption('Having search the above table, please check the indicated row of the movie you are interested in watching later. Checking the rows will create a table of movies or tv shows you want to save for later. ')
    gd = GridOptionsBuilder.from_dataframe(df)
    gd.configure_selection(selection_mode='multiple', use_checkbox=True)
    gridoptions = gd.build()

    grid_table = AgGrid(df, height=250, gridOptions=gridoptions,
                    update_mode=GridUpdateMode.SELECTION_CHANGED)

    st.write('Save for later')
    selected_row = grid_table["selected_rows"]
    st.dataframe(selected_row)

    st.caption('Once you are satisified with your selection please press the save button to save your created table. The table of movies and tv shows will be saved as a csv formated table. Enjoy the rest of the pages to find more highly rated movies and tv shows. ')
# Download button to save the selected rows as a CSV file
    if st.button('Download Selected Rows as CSV'):
    # Convert selected rows to DataFrame
        selected_df = pd.DataFrame(selected_row)
    # Save DataFrame as CSV file
        csv = selected_df.to_csv(index=False)
    # Offer the CSV file as a download link
        st.download_button(label='Save Table', data=csv, file_name='selected_rows.csv', mime='text/csv')


#Creates multi-page functionality from pages functions
page_names_to_funcs = {
    "Home Page": main_page,
    "Page 2": page2,
    "Page 3": page3,
    "Page 4": page4,
    "Page 5": page5,
    "Page 6": page6,
    "Page 7": page7
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

