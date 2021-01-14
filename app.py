import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

def ellipse_arc(x_center=0, y_center=0, a=1, b =1, start_angle=0, end_angle=2*np.pi, N=100, closed= False):
    t = np.linspace(start_angle, end_angle, N)
    x = x_center + a*np.cos(t)
    y = y_center + b*np.sin(t)
    path = f'M {x[0]}, {y[0]}'
    for k in range(1, len(t)):
        path += f'L{x[k]}, {y[k]}'
    if closed:
        path += ' Z'
    return path  


colors = {'Goal':'Green', 'MissedShots':'Purple', 'BlockedShot':'Red', 'SavedShot':'Blue', 'ShotOnPost':'Yellow'}

pd.options.plotting.backend = "plotly"
df = pd.read_csv('data.csv') # iris is a pandas DataFrame
fig = px.scatter(df,x="XM", y="YM",size="xG",color='result',color_discrete_sequence=["green", "purple", "red", "blue","yellow"],hover_data=['result','shotType'])
# To remove the border on scatter points
# fig.update_traces(marker=dict(
#                               line=dict(width=0,
#                                         color='DarkSlateGrey')),
#                   selector=dict(mode='markers'))

# Set axes range
fig.update_xaxes(
    range=[-1, 105],    
    # showticklabels=False,
    showgrid=False,
    zeroline=False,
    )
fig.update_yaxes(
    range=[-1, 69],
    # showticklabels=False,
    showgrid=False,
    zeroline=False,
    )


#       Pitch start
# #Halfway line, penalty spots, and kickoff spot
fig.add_shape(type="line",
    x0=52, y0=0, x1=52, y1=68,
    line=dict(
        color="#faf0e6",
        width=1,
    )
)

fig.update_layout(
    plot_bgcolor="#3E3E40"
)

# Add a shape whose x and y coordinates refer to the domains of the x and y axes
fig.add_shape(type="rect",
    xref="x domain", yref="y domain",
    x0=0, x1=104, y0=0, y1=68,
    # fillcolor="#555",
    # layer="below",
    line_color="#faf0e6",
    # fillcolor="LightGreen",
        line=dict(
        width=1,
    )
)
# # Center circle
# 52,34
# 9.15
# 4.575 radius
fig.add_shape(type="circle",
    xref="x", yref="y",
    x0=(52-9.15), x1=(52+9.15), y0=(34-14), y1=(34+14),
    line_color="#faf0e6",
)
# # center dot
fig.add_shape(type="circle",
    xref="x", yref="y",
    fillcolor="#faf0e6",
    # layer="below",
    x0=51.5, x1=52.5, y0=33.5, y1=34.5,
    line_color="#faf0e6",
)
# # Left side
# # left big rect
fig.add_shape(type="rect",
    xref="x domain", yref="y domain",
    x0=0, x1=15, y0=13.84, y1=54.16,
    line_color="#faf0e6",
)
# Left Goal 
# ly5 = [30.34,30.34,37.66,37.66]
# lx5 = [0,-0.2,-0.2,0]
fig.add_shape(type="rect",
    x0=0, x1=-0.2, y0=30.34, y1=37.66,
    line=dict(
        color="#faf0e6",
        width=1,
    )
)
# left small rect

# ly7 = [24.84,24.84,43.16,43.16]
# lx7 = [0,4.5,4.5,0]
fig.add_shape(type="rect",
    xref="x domain", yref="y domain",
    x0=0, x1=4.5, y0=24.84, y1=43.16,
    line_color="#faf0e6",
)
# # left dot
# 11,34
fig.add_shape(type="circle",
    xref="x", yref="y",
    fillcolor="#faf0e6",
    x0=10.5, x1=11, y0=33.5, y1=34.5,
    line_color="#faf0e6",
)


# LEft Arc
fig.add_shape(
    type="path",
    path= ellipse_arc(x_center=-32.5,y_center=33.8,a=50, b=20, start_angle=-np.pi/10, end_angle=np.pi/10, N=60),
    line_color="#faf0e6")


# # right side
# # right big rect
# ly2 = [13.84,13.84,54.16,54.16] 
# lx2 = [104,87.5,87.5,104]
fig.add_shape(type="rect",
    xref="x domain", yref="y domain",
    x0=104, x1=87.5, y0=54.16, y1=13.84,
    line_color="#faf0e6",
)
# Right Goal
# ly4 = [30.34,30.34,37.66,37.66]
# lx4 = [104,104.2,104.2,104]
fig.add_shape(type="rect",
    x0=104, x1=104.2, y0=30.34, y1=37.66,
    line=dict(
        color="#faf0e6",
        width=1,
    )
)
# # right small rect
# ly6 = [24.84,24.84,43.16,43.16]
# lx6 = [104,99.5,99.5,104]
fig.add_shape(type="rect",
    xref="x domain", yref="y domain",
    x0=104, x1=99.5,y0=24.84, y1=43.16,
    line_color="#faf0e6",
)
# # right dot
# 93,34
fig.add_shape(type="circle",
    xref="x", yref="y",
    fillcolor="#faf0e6",
    x0=92.5, x1=93, y0=33.5, y1=34.5,
    line_color="#faf0e6",
)
# Right Arc
fig.add_shape(
    type="path",
    path= ellipse_arc(x_center=135,y_center=33.8,a=50, b=20, start_angle=162*np.pi/180, end_angle=198*np.pi/180, N=60),
    line_color="#faf0e6")

#   Pitch Ended
fig.update_shapes(dict(xref='x', yref='y'))



# fig.show()

fig.write_html("index.html")

