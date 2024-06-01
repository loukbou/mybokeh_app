from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Select
from bokeh.layouts import column
import pandas as pd
from bokeh.io import curdoc
from bokeh.transform import factor_cmap
from bokeh.palettes import Spectral6

def create_help_source_visualization():
    # Load the dataset
    df = pd.read_csv('survey_result_cleaned.csv')

    # Drop unnecessary columns
    columns_to_drop = ['lastSubmit', 'userId', 'Fav_Coding_Drink', 'Covid_Productivity']
    data = df.drop(columns=columns_to_drop, errors='ignore')

    # Drop rows with NaN values in significant columns
    columns_to_check = ['Wanted_Programming_Languages', 'Teaching_Problems_POV', 'Open_Source_Participation',
                        'Daily_Web_Frameworks', 'Continuous_Learning_Frequency', 'Immigration_Plans', 'Employment_Status']
    data = data.dropna(subset=columns_to_check)

    # Flatten the array of help sources for each respondent
    help_data = data[['Coding_Experience', 'Help_Sources']].dropna()
    help_data['Help_Sources'] = help_data['Help_Sources'].str.strip('[]').str.replace("'", "").str.split(', ')
    help_data_expanded = help_data.explode('Help_Sources')

    # Count the occurrences of each help source by coding experience
    help_counts = help_data_expanded.groupby(['Coding_Experience', 'Help_Sources']).size().reset_index(name='Number_of_Persons')

    # Create a Bokeh ColumnDataSource
    source = ColumnDataSource(help_counts[help_counts['Coding_Experience'] == help_counts['Coding_Experience'].iloc[0]])

    # Create a Bokeh figure
    p = figure(y_range=help_counts['Help_Sources'].unique(), height=400, width=800,
               title="Most Common Sources of Help for Developers with Varying Levels of Experience",
               toolbar_location=None, tools="")

    # Add horizontal bar glyphs
    p.hbar(y='Help_Sources', right='Number_of_Persons', height=0.5, source=source, 
           fill_color=factor_cmap('Help_Sources', palette=Spectral6, factors=help_counts['Help_Sources'].unique()))

    # Set axis labels and titles
    p.xaxis.axis_label = "Number of Developers"
    p.yaxis.axis_label = "Help Sources"

    # Define a function to update data based on the selected coding experience
    def update_plot(attrname, old, new):
        selected_experience = select.value
        filtered_data = help_counts[help_counts['Coding_Experience'] == selected_experience]
        source.data = ColumnDataSource.from_df(filtered_data)

    # Create a Select widget for coding experience
    experiences = sorted(help_counts['Coding_Experience'].unique())
    select = Select(title="Select Coding Experience:", value=experiences[0], options=experiences)
    select.on_change('value', update_plot)

    # Create layout for the plot and widget
    layout = column(select, p)
    return layout

