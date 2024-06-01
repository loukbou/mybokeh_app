from bokeh.layouts import gridplot, Spacer
from bokeh.io import curdoc
from help_source import create_help_source_visualization
from frequence import create_frequence_visualization
from bokeh_app import create_bokeh_app_visualization
from teaching_pb import create_teaching_pb_visualization
from immigration import create_immigration_visualisation
from education import create_education_visualisation

# Create each visualization
vis1 = create_help_source_visualization()
vis2 = create_frequence_visualization()
vis3 = create_bokeh_app_visualization()
vis4 = create_teaching_pb_visualization()
vis5 = create_immigration_visualisation()
vis6 = create_education_visualisation()

# Create spacers
spacer = Spacer(width=30, height=50)

# Organize visualizations in a grid layout with spacers
grid = gridplot([[vis1, vis3], [spacer], [vis2, vis4],[spacer], [vis5, vis6]])

# Add the grid layout to the current document
curdoc().add_root(grid)
