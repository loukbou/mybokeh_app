from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Select
from bokeh.layouts import column
import pandas as pd
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Select
from bokeh.layouts import column
from bokeh.transform import factor_cmap
from bokeh.palettes import Spectral6


def create_frequence_visualization():
    
    data = pd.read_csv('survey_result_cleaned.csv')

    # Prepare the data
    experience_job_data = data[['Coding_Experience', 'Job_Title']].dropna()

   # Count the number of occurrences of each Job Title per Coding Experience
    counts = experience_job_data.groupby(['Coding_Experience', 'Job_Title']).size().reset_index(name='count')

    # Sort counts in descending order by count
    counts = counts.sort_values(by='count', ascending=False)

    # Convert to a format suitable for Bokeh
    source = ColumnDataSource(counts)


    # Get unique values for dropdown
    years_of_experience = sorted(counts['Coding_Experience'].unique().tolist())

    # Create a color map
    job_titles = counts['Job_Title'].unique().tolist()
    color_map = factor_cmap('Job_Title', palette=Spectral6, factors=job_titles)

    # Create the figure
    p = figure(x_range=job_titles, height=600, width=800, title="Job Titles by Coding Experience",
               toolbar_location=None, tools="")

    # Add bars
    p.vbar(x='Job_Title', top='count', width=0.9, source=source, legend_field='Job_Title', line_color='white', fill_color=color_map)

    # Customize plot
    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.xaxis.axis_label = "Job Title"
    p.yaxis.axis_label = "Number of Persons"
    p.legend.title = "Job Title"
    p.xaxis.major_label_orientation = 1

    # Hide x-axis labels
    p.xaxis.major_label_text_font_size = '0pt'

    # Create a dropdown menu for selecting years of coding experience
    dropdown = Select(title="Years of Coding Experience", value=str(years_of_experience[0]), options=[str(x) for x in years_of_experience])

    # Update function
    def update(attr, old, new):
        selected_experience = dropdown.value
        new_data = counts[counts['Coding_Experience'] == selected_experience]
        source.data = new_data

    dropdown.on_change('value', update)

    # Layout
    layout = column(dropdown, p)
    return layout
