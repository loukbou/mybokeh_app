from collections import Counter
from math import pi

import pandas as pd
from bokeh.models import ColumnDataSource, Legend, LegendItem
from bokeh.plotting import figure
from bokeh.layouts import column
from bokeh.palettes import Category20

def create_teaching_pb_visualization():
    data = pd.read_csv('survey_result_cleaned.csv')

    # Explode Teaching_Problems_POV and get the unique values
    all_problems = data['Teaching_Problems_POV'].str.split(',').explode().str.strip()
    unique_values = all_problems.dropna().unique().tolist()

    # Count occurrences of each unique value
    counts = Counter(all_problems)

    # Colors for the wedges, using a color palette to ensure enough colors
    colors = Category20[max(len(unique_values), 20)]

    # Initial pie chart data source
    source = ColumnDataSource(data=dict(teaching_problems=[], counts=[], start_angle=[], end_angle=[], color=[], alpha=[]))

    # Create the pie chart
    p = figure(title="Teaching Problems Distribution", toolbar_location=None,
               tools="hover", tooltips="@teaching_problems: @counts", x_range=(-1, 1), y_range=(-1, 1), width=600, height=600)

    # Create a donut hole
    wedges = p.annular_wedge(x=0, y=0, inner_radius=0.3, outer_radius=0.8,
                             start_angle="start_angle", end_angle="end_angle",
                             line_color="white", fill_color="color", fill_alpha="alpha", source=source)

    p.axis.visible = False
    p.grid.visible = False

    # Function to update the pie chart
    def update_chart():
        total = sum(counts.values())
        if total > 0:
            angles = [count / total * 2 * pi for count in counts.values()]
            start_angle = [sum(angles[:i]) for i in range(len(angles))]
            end_angle = [start + angle for start, angle in zip(start_angle, angles)]
            alpha = [1] * len(counts)
        else:
            angles = []
            start_angle = []
            end_angle = []
            alpha = []

        data = {
            'teaching_problems': list(counts.keys()),
            'counts': list(counts.values()),
            'start_angle': start_angle,
            'end_angle': end_angle,
            'color': colors[:len(counts)],
            'alpha': alpha
        }

        source.data = data

    # Update the chart and counts initially
    update_chart()

    # Create legend items
    legend_items = []
    for i, teaching_problem in enumerate(counts.keys()):
        color = colors[i % len(colors)]
        legend_items.append(LegendItem(label=teaching_problem, renderers=[wedges], index=i))
        
    legend = Legend(items=legend_items, location='center')
    p.add_layout(legend, 'right')

    # Create layout
    layout = column(p)

    return layout

