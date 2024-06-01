from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Select
from bokeh.layouts import column
import pandas as pd
from bokeh.palettes import Category20

def create_bokeh_app_visualization():
    
    data = pd.read_csv('survey_result_cleaned.csv')

    # Flatten the array of learning platforms for each respondent
    platforms_data = data[['Continuous_Learning_Frequency', 'Learning_Platforms']].dropna()
    platforms_data['Learning_Platforms'] = platforms_data['Learning_Platforms'].str.strip('[]').str.replace("'", "").str.split(', ')
    platforms_expanded = platforms_data.explode('Learning_Platforms')

    # Count the occurrences of each learning platform among continuous learners
    platform_counts = platforms_expanded['Learning_Platforms'].value_counts().reset_index()
    platform_counts.columns = ['Learning_Platform', 'Number_of_Persons']

    # Assign a color to each learning platform
    platform_color_map = dict(zip(platform_counts['Learning_Platform'], Category20[len(platform_counts)]))
    platform_counts['color'] = platform_counts['Learning_Platform'].map(platform_color_map)

    # Create a Bokeh ColumnDataSource
    source = ColumnDataSource(platform_counts)

    # Create a Bokeh figure
    p = figure(y_range=platform_counts['Learning_Platform'].unique(), height=450, width=450,
               title="Most Popular Learning Platforms Among Continuous Learners",
               toolbar_location=None, tools="")

    # Add hbar glyphs with different colors for each platform
    p.hbar(y='Learning_Platform', right='Number_of_Persons', height=0.8, source=source, color='color')

    # Set axis labels and titles
    p.xaxis.axis_label = "Number of Persons"
    p.yaxis.axis_label = "Learning Platforms"

    # Define a function to update data based on the selected continuous learning frequency
    def update_plot(attrname, old, new):
        selected_frequency = select.value
        filtered_data = platforms_expanded[platforms_expanded['Continuous_Learning_Frequency'] == selected_frequency]
        platform_counts_filtered = filtered_data['Learning_Platforms'].value_counts().reset_index()
        platform_counts_filtered.columns = ['Learning_Platform', 'Number_of_Persons']
        platform_counts_filtered['color'] = platform_counts_filtered['Learning_Platform'].map(platform_color_map)
        source.data = ColumnDataSource.from_df(platform_counts_filtered)

    # Create a Select widget for continuous learning frequency
    frequencies = sorted(platforms_expanded['Continuous_Learning_Frequency'].unique())
    select = Select(title="Select Continuous Learning Frequency:", value=frequencies[0], options=frequencies)
    select.on_change('value', update_plot)

    # Create layout for the plot and widget
    layout = column(select, p)
    return layout
