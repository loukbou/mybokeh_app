import pandas as pd
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Select
from bokeh.layouts import column
from bokeh.transform import factor_cmap
from bokeh.palettes import Spectral6

def create_immigration_visualisation():

    df = pd.read_csv('survey_result_cleaned.csv')
    
    # Prepare data for Immigration graph
    def get_immigration_data(job_title):
        filtered_data = df[df['Job_Title'] == job_title]
        immigration_data = filtered_data['Immigration_Plans'].value_counts().reset_index()
        immigration_data.columns = ['Immigration_Plans', 'count']
        return immigration_data

    # Initial data for the plot
    initial_job_title = df['Job_Title'].unique()[0]
    immigration_data = get_immigration_data(initial_job_title)
    immigration_source = ColumnDataSource(immigration_data)

    # Create the Immigration graph
    immigration_p = figure(x_range=immigration_data['Immigration_Plans'], height=400, width=400, title="Immigration Plans",
                           toolbar_location=None, tools="")

    immigration_p.vbar(x='Immigration_Plans', top='count', width=0.5, source=immigration_source, legend_field='Immigration_Plans',
                       line_color='white', fill_color=factor_cmap('Immigration_Plans', palette=Spectral6, factors=immigration_data['Immigration_Plans']))

    immigration_p.xgrid.grid_line_color = None
    immigration_p.y_range.start = 0
    immigration_p.xaxis.axis_label = "Immigration Plans"
    immigration_p.yaxis.axis_label = "Number of persons"
    immigration_p.legend.title = "Immigration Plans"
    immigration_p.xaxis.major_label_orientation = 1

    # Create a dropdown menu for selecting Job Title
    job_titles = df['Job_Title'].unique().tolist()
    dropdown = Select(title="Job Title", value=initial_job_title, options=job_titles)

    # Update function
    def update(attr, old, new):
        selected_job_title = dropdown.value
        new_data = get_immigration_data(selected_job_title)
        immigration_source.data = new_data.to_dict(orient='list')

    dropdown.on_change('value', update)

    layout = column(dropdown, immigration_p)
    return layout
