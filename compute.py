import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import json
import pandas

SOURCE_FILE="./dati-json/dpc-covid19-ita-regioni.json"

raw_data = pandas.io.json.read_json(SOURCE_FILE)

dates_list = set(raw_data['data'].tolist())

print(dates_list)

grouped_by_date = raw_data.groupby("data", axis=1)

## TOTAL LISTS
list_total_hospitalized_with_symptoms = list()
list_total_intensive_care = list()
list_total_hospitalized = list()
list_total_home_isolation = list()
list_total_currently_positive = list()
list_total_new_currently_positive = list()
list_total_discharged_healed = list()
list_total_deads = list()
list_total_tampons = list()
list_total_cases = list()

## PERCENTAGE LISTS
list_percentage_intensive_care_over = list()
list_percentage_total_case = list()
list_percentage_total_deads = list()
list_percentage_currently_positive = list()
list_percentage_total_tampons = list()
list_percentage_total_discharged_healed = list()
list_percentage_total_home_isolation = list()

first_run = True
for date in sorted(dates_list):
    is_in_date = raw_data['data']==date
    data_current_date = raw_data[is_in_date]
    #print(data_current_date)
    total_hospitalized_with_symptoms = data_current_date["ricoverati_con_sintomi"].sum()
    total_intensive_care = data_current_date["terapia_intensiva"].sum()
    total_hospitalized = data_current_date["totale_ospedalizzati"].sum()
    total_home_isolation = data_current_date["isolamento_domiciliare"].sum()
    total_currently_positive = data_current_date["totale_attualmente_positivi"].sum()
    total_new_currently_positive = data_current_date["nuovi_attualmente_positivi"].sum()
    total_discharged_healed = data_current_date["dimessi_guariti"].sum()
    total_deads = data_current_date["deceduti"].sum()
    total_tampons = data_current_date["tamponi"].sum()
    total_cases = data_current_date["totale_casi"].sum()
    print("Current date: " + date)
    print("Total hospitalized with symptoms: " + str(total_hospitalized_with_symptoms))
    print("Total intensice care: " + str(total_intensive_care))
    print("Total hospitalized: " + str(total_hospitalized))
    print("Total home isolation: " + str(total_home_isolation))
    print("Total currently positive: " + str(total_currently_positive))
    print("Total new currently positive: " + str(total_new_currently_positive))
    print("Total discharged healed: " + str(total_discharged_healed))
    print("Total deads: " + str(total_deads))
    print("Total tampons: " + str(total_tampons))
    print("Total cases: " + str(total_cases))
    print("======================================================================")
    list_total_hospitalized_with_symptoms.append(total_hospitalized_with_symptoms)
    list_total_intensive_care.append(total_intensive_care)
    list_total_hospitalized.append(total_hospitalized)
    list_total_home_isolation.append(total_home_isolation)
    list_total_currently_positive.append(total_currently_positive)
    list_total_new_currently_positive.append(total_new_currently_positive)
    list_total_discharged_healed.append(total_discharged_healed)
    list_total_deads.append(total_deads)
    list_total_tampons.append(total_tampons)
    list_total_cases.append(total_cases)
    if first_run: 
        list_percentage_total_case.append(1.0)
        list_percentage_intensive_care_over.append(1.0)
        list_percentage_total_deads.append(1.0)
        list_percentage_currently_positive.append(1.0)
        list_percentage_total_tampons.append(1.0)
        list_percentage_total_discharged_healed.append(1.0)
        list_percentage_total_home_isolation.append(1.0)
        first_run = False
    else:
        list_percentage_total_case.append(float(total_cases - list_total_cases[-2]) * 100.0 / float (total_cases))
        list_percentage_intensive_care_over.append(float(total_intensive_care - list_total_intensive_care[-2]) * 100.0 / float(total_intensive_care))
        list_percentage_total_deads.append(float(total_deads - list_total_deads[-2]) * 100.0 / float (total_deads))
        list_percentage_currently_positive.append(float(total_currently_positive - list_total_currently_positive[-2]) * 100.0 / float (total_currently_positive))
        list_percentage_total_tampons.append(float(total_tampons - list_total_tampons[-2]) * 100.0 / float (total_tampons))
        list_percentage_total_discharged_healed.append(float(total_discharged_healed - list_total_discharged_healed[-2]) * 100.0 / float (total_discharged_healed))
        list_percentage_total_home_isolation.append(abs(float(total_home_isolation - list_total_home_isolation[-2])) * 100.0 / float (total_home_isolation))

fig = go.Figure()
# Create and style traces
fig.add_trace(go.Scatter(x=sorted(dates_list), y=list_total_deads, name='Total deads',
                         line=dict(color='firebrick', width=4)))

fig.add_trace(go.Scatter(x=sorted(dates_list), y=list_total_cases, name='Total cases',
                         line=dict(color='blue', width=4)))

fig.add_trace(go.Scatter(x=sorted(dates_list), y=list_total_discharged_healed, name='Total discharged',
                         line=dict(color='green', width=4)))

# Edit the layout
fig.update_layout(title='COVID 19 Trends',
                   xaxis_title='Day',
                   yaxis_title='Number of cases')


fig.show()


fig_percentages = go.Figure()
# Create and style traces


fig_percentages.add_trace(go.Scatter(x=sorted(dates_list), y=list_percentage_total_case, name='Total case',
                         line=dict(color='green', width=4)))
fig_percentages.add_trace(go.Scatter(x=sorted(dates_list), y=list_percentage_intensive_care_over, name='Intensive care',
                         line=dict(color='blue', width=4)))
fig_percentages.add_trace(go.Scatter(x=sorted(dates_list), y=list_percentage_total_deads, name='Total deads',
                         line=dict(color='red', width=4)))
fig_percentages.add_trace(go.Scatter(x=sorted(dates_list), y=list_percentage_currently_positive, name='Total currently positive',
                         line=dict(color='yellow', width=4)))
fig_percentages.add_trace(go.Scatter(x=sorted(dates_list), y=list_percentage_total_tampons, name='Total tampons',
                         line=dict(color='skyblue', width=4)))
fig_percentages.add_trace(go.Scatter(x=sorted(dates_list), y=list_percentage_total_discharged_healed, name='Total discharged healed',
                         line=dict(color='brown', width=4)))                        
fig_percentages.add_trace(go.Scatter(x=sorted(dates_list), y=list_percentage_total_home_isolation, name='Total home isolation',
                         line=dict(color='lime', width=4)))       

                         
# Edit the layout
fig_percentages.update_layout(title='COVID 19 Percentage Trends',
                   xaxis_title='Day',
                   yaxis_title='Total deads',
                   yaxis_type='log')


fig_percentages.show()