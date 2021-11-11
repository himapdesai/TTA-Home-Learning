#from Car Evaluation Data Set import data
import altair as alt
from altair.vegalite.v4.api import condition, value
from altair.vegalite.v4.schema.channels import Color
#from sklearn.cluster import KMeans
#from sklearn import datasets
import pandas as pd


cars = pd.read_csv('car_data.csv')
print(cars)

# data = pd.DataFrame({'col-1': list['buying', 'maint', 'doors', 'persons', 'lung_boot', 'safety'],
#                       'col-2': ['vhigh','vhigh',2,2,'small','low']
#                     })

# df = pd.DataFrame(data['data'], columns=data['feature_name'])

# df.head()

#sklearn.datasets.load_iris

# cars.head()


# df = pd.DataFrame(cars, index=None)
#  rows = len(df.axes[x])
#  cols = len(df.axes[y])


# data = pd.DataFrame({'col-1': list['buying', 'maint', 'doors', 'persons', 'lung_boot', 'safety'],
#                      'col-2': ['vhigh','vhigh',2,2,'small','low']
#                     })
# chart = alt.Chart(data)
# alt.renderers.enable('mimetype')
# chart1 = alt.Chart(data).mark_point().encode(
#     x='col-1',
#     y='col-2'
# ).interactive()

# chart1.show()

# brish = alt.selection_interval()

# points = alt.Chart(cars).mark_point().encode(
#     x='Values:Q',
#     y='Attribute:Q',
#     Color=alt.condition(brush, 'Origin:N', alt.value('Lightgray'))
# ).add_selection(
#     brush
# )

# points.show()
