import pandas as pd
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Select
from bokeh.layouts import column
from bokeh.transform import factor_cmap
from bokeh.palettes import Spectral6


def create_education_visualisation():
     # Load the dataset
    df = pd.read_csv('survey_result_cleaned.csv')
    # Prepare data for Education graph
    education_data = df['Education'].value_counts().reset_index()
    education_data.columns = ['Education', 'count']
    education_source = ColumnDataSource(education_data)

    # Create the Education graph
    education_p = figure(x_range=education_data['Education'], height=400, width=700, title="Education Levels",
                         toolbar_location=None, tools="")

    education_p.vbar(x='Education', top='count', width=0.5, source=education_source, legend_field='Education',
                     line_color='white', fill_color=factor_cmap('Education', palette=Spectral6, factors=education_data['Education']))

    education_p.xgrid.grid_line_color = None
    education_p.y_range.start = 0
    education_p.xaxis.axis_label = "Education Level"
    education_p.yaxis.axis_label = "Number of persons"
    education_p.legend.title = "Education Level"
    education_p.xaxis.major_label_orientation = 1

     # Layout
    layout = column(education_p)
    return layout


