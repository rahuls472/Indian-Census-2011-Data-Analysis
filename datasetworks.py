import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
from plotly.subplots import make_subplots


NewDf = pd.read_csv('/home/ghost/Python DS/Indian census data/Modified data.csv')
NewDf['District name'].drop_duplicates(inplace=True)


class datasets:
   def AllStates(self):
      States = NewDf['State name'].unique()

      return {index: state for index, state in enumerate(States)}
   



   def OverallData(self):
      AllDataTogether = (
      NewDf.groupby('State name')[['Population', 'Male', 'Female','Literate']]
      .sum()
      .sort_values(by='Population', ascending=False)
      .reset_index()
      )

      return AllDataTogether.to_dict(orient='records')
   




   def TotalLiteracyRate(self):
        # Grouping data and calculating literacy rate
        df1 = (NewDf.groupby('State name')
            [['Literate', 'Population']]
            .sum()
            .sort_values(by='Literate', ascending=False)  # Sort by literacy rate
            .reset_index()
            )
        
        df1['Literacy Rate'] = ((df1['Literate'] / df1['Population']) * 100).round()
        
        # Plotting horizontal bar chart
        fig = px.bar(df1, 
                    x='Literacy Rate', 
                    y='State name', 
                    text='Literacy Rate',
                    title='State-wise Literacy Rate',
                    hover_name='State name',
                    labels={'State name': 'State', 'Literacy Rate': 'Literacy Rate (%)'},
                    orientation='h',  # Horizontal orientation
                    color='Literacy Rate',  # Color intensity
                    color_continuous_scale='Viridis')  # Color theme
        
        # Updating layout for readability
        fig.update_layout(
            xaxis_title="Literacy Rate (%)",
            yaxis_title="States",
            showlegend=False,
            height=800  # Adjust height for readability if there are many states
        )

        return fig
        
    

   


   def SexwisePopulationVisualization(self):
    # Prepare the data
    MaleSexPop = NewDf.groupby(['State name',])['Male'].sum().sort_values(ascending=False).reset_index()
    FemaleSexPop = NewDf.groupby(['State name',])['Female'].sum().sort_values(ascending=False).reset_index()

    Sexwisedata = MaleSexPop.merge(FemaleSexPop, on='State name')
    Sexwisedata['Sex Ratio'] = (Sexwisedata['Female'] / Sexwisedata['Male']) * 1000

    # Ensure no zero or negative values for log_y
    Sexwisedata['Male'] = Sexwisedata['Male'].replace(0, 1)  # Replace zeros with 1
    Sexwisedata['Female'] = Sexwisedata['Female'].replace(0, 1)  # Replace zeros with 1

    # Create first chart: Sex Ratio by State
    fig1 = px.bar(
        Sexwisedata,
        x='State name',
        y='Sex Ratio',
        text='Sex Ratio',
        color='Sex Ratio',
        color_continuous_scale='Blues',
        title='Sex Ratio by State (Females per 1000 Males)'
    )
    fig1.update_traces(
        marker_line_width=1.5,
        marker_line_color='rgba(0, 0, 0, 0.7)'
    )
    fig1.update_layout(
        title_font_size=16,
        title_x=0.5,
        xaxis_title="State Name",
        yaxis_title="Sex Ratio",
        plot_bgcolor='rgba(240, 240, 240, 1)',
        font=dict(size=12)
    )

    # Create second chart: Population Distribution (Male vs Female)
    fig2 = px.bar(
        Sexwisedata,
        x='State name',
        y=['Male', 'Female'],  # Using column names directly
        barmode='group',
        text_auto=True,
        log_y=True,  # Log scale for y-axis
        hover_name='State name',
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig2.update_layout(
        title="Population Distribution by State (Male vs Female)",
        title_font_size=16,
        title_x=0.5,
        xaxis_title="State Name",
        yaxis_title="Population (Log Scale)",
        font=dict(size=12),
        plot_bgcolor='rgba(245, 245, 245, 1)',
        legend=dict(
            title="Gender",
            orientation="h",
            x=0.5,
            xanchor="center",
            y=1.1
        )
    )

    # Combine the two charts into a subplot
    fig = make_subplots(
        rows=2, cols=1,
        subplot_titles=[
            "Sex Ratio by State (Females per 1000 Males)",
            "Population Distribution by State (Male vs Female)"
        ]
    )

    # Add first chart to subplot
    for trace in fig1.data:
        fig.add_trace(trace, row=1, col=1)

    # Add second chart to subplot
    for trace in fig2.data:
        fig.add_trace(trace, row=2, col=1)

    # Adjust subplot layout
    fig.update_layout(
        height=900,  # Adjust the height to fit two rows
        showlegend=True,
        title_text="Sexwise Population Visualization",
        title_x=0.5,
        title_font_size=20
    )

    return fig





   def overalldataGraph(self):
      stateWise = NewDf.groupby(['State name', 'District name', 'Latitude', 'Longitude'])['Population'].sum().sort_values(ascending=False).reset_index()
      fig = px.scatter_mapbox(
         stateWise,
         lat='Latitude',
         lon='Longitude',
         size='Population',
         color='District name',
         hover_name='State name',
         title='Overall Population Distribution of India District Wise',
         mapbox_style='open-street-map',
         zoom= 4
      )
      fig.update_layout(
        title=dict(
            text='Overall Population Distribution of India District Wise',
            font=dict(size=20, family='Arial', color='blue'),
            x=0.5  # Center the title
        ),
        mapbox=dict(
            center=dict(lat=20.5937, lon=78.9629),  # Center on India
            zoom=4
        ),
        margin=dict(l=0, r=0, t=50, b=0),  # Reduce extra margins
        paper_bgcolor='lightgray',  # Background color outside the map
        plot_bgcolor='lightgray',
        width=1000,  # Map width
        height=800  # Map height
    )
     
      return fig

   


   def statewise(self, state):
    df2 = NewDf[NewDf['State name'] == str(state)]
    fig = px.scatter_mapbox(
        df2,
        lat='Latitude',
        lon='Longitude',
        size='Population',
        color='District name',
        hover_name='State name',
        title='Population Distribution of District',
        mapbox_style='open-street-map',
        zoom= 4
    )
    fig.update_layout(
       title=dict(
            text='Population Distribution of India District Wise',
            font=dict(size=20, family='Arial', color='blue'),
            x=0.5  # Center the title
        ),
        paper_bgcolor='lightgray',  # Background color outside the map
        plot_bgcolor='lightgray',
        width=800,  # Set the desired width in pixels
        height=800,  # Set the desired height in pixels
    )
   #  fig.update_layout(mapbox=dict(accesstoken='your_mapbox_access_token'))  # Add token
      
    return df2.to_dict(orient='records'), fig.to_html(full_html=False,config={'scrollZoom': True},include_plotlyjs='cdn')
   






   def sexdistribution(self,state):
    # Filter data for the selected state
    filter1 = NewDf[NewDf['State name'] == str(state)]

    # Calculate Sex Ratio
    filter1['Sex Ratio'] = (filter1['Female'] / filter1['Male']) * 1000

    # Grouped bar chart for Male and Female population
    fig1 = px.bar(
        filter1,
        x='District name',
        y=['Male', 'Female'],
        barmode='group',
        text_auto=True,
        log_y=True,
        hover_name='District name',
        title=f'Sex Distribution in {state} by District',
        color_discrete_map={"Male": "#1f77b4", "Female": "#e377c2"}
    )

    # Update layout for better visuals in fig1
    fig1.update_layout(
        title=dict(
            text=f"Sex Distribution in {state} by District",
            font=dict(size=20, family="Arial", color="black"),
            x=0.5
        ),
        xaxis=dict(
            title="Districts",
            tickangle=45,
            titlefont=dict(size=14, family="Arial", color="black")
        ),
        yaxis=dict(
            title="Population (Log Scale)",
            titlefont=dict(size=14, family="Arial", color="black"),
            gridcolor="lightgray"
        ),
        legend=dict(
            title="Gender",
            font=dict(size=12),
            orientation="h",
            x=0.5,
            xanchor="center",
            y=-0.2
        ),
        margin=dict(l=50, r=50, t=70, b=100),
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    # Bar chart for Sex Ratio with color scale
    fig2 = px.bar(
        filter1,
        x='District name',
        y='Sex Ratio',
        text_auto=True,
        color='Sex Ratio',  # Add color scale
        color_continuous_scale='Viridis',  # Choose a visually pleasing scale
        title='Sex Ratio by District'
    )

    # Update layout for fig2
    fig2.update_layout(
        xaxis=dict(
            title="Districts",
            tickangle=45,
            titlefont=dict(size=14, family="Arial", color="black")
        ),
        yaxis=dict(
            title="Sex Ratio (per 1000 Males)",
            titlefont=dict(size=14, family="Arial", color="black"),
            gridcolor="lightgray"
        ),
        coloraxis_colorbar=dict(
            title="Sex Ratio",
            titlefont=dict(size=12),
            tickfont=dict(size=10)
        ),
        margin=dict(l=50, r=50, t=50, b=100),
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    # Create subplots for combining the charts
    fig = make_subplots(
        rows=2, cols=1,
        subplot_titles=[
            'Sexwise Population Visualization',
            'Sex Ratio by District'
        ]
    )

    # Add traces from fig1 to the first subplot
    for trace in fig1.data:
        fig.add_trace(trace, row=1, col=1)

    # Add traces from fig2 to the second subplot
    for trace in fig2.data:
        fig.add_trace(trace, row=2, col=1)

    # Adjust the overall layout
    fig.update_layout(
        height=1000,  # Adjust height to fit both plots
        showlegend=True,
        title=dict(
            text=f"Sex Distribution and Ratio in {state}",
            font=dict(size=24, family="Arial", color="black"),
            x=0.5
        ),
        margin=dict(l=50, r=50, t=80, b=50)
    )

    return filter1.to_dict(orient='records'),fig.to_html(full_html=False,include_plotlyjs='cdn',config={'scrollZoom': True})
   



   def DistrictWiseLiteracy(self,state):
        # Filter data for the given state
        Filter1 = NewDf[NewDf['State name'] == str(state)]
        
        # Plot grouped bar chart for male and female literacy
        fig = px.bar(
            Filter1,
            x='District name',
            y=['Male_Literate', 'Female_Literate'],
            barmode='group',  # Grouped bar chart
            text_auto=True,  # Show values on bars
            title=f'District-Wise Male and Female Literates in {state}',  # Dynamic title
            labels={
                'value': 'Number of Literate Individuals',
                'District name': 'Districts',
                'variable': 'Gender'
            },
            template='plotly'  # Predefined Plotly theme
        )
        
        # Update layout for readability
        fig.update_layout(
            xaxis_title="Districts",
            yaxis_title="Number of Literate Individuals",
            legend_title="Gender",
            xaxis_tickangle=-45,  # Tilt district names if needed
            height=600  # Adjust chart size
        )


        return Filter1.to_dict(orient='records'),fig.to_html(full_html=False,include_plotlyjs='cdn',config={'scrollZoom': True})
   




   def maleFemaleLiteracyRate(self,state):
    filter1 = NewDf[NewDf['State name'] == str(state)]

    # Calculate literacy rates
    filter1['Male_Literacy_Rate'] = ((filter1['Male_Literate'] / filter1['Male']) * 100).round()
    filter1['Female_Literacy_Rate'] = ((filter1['Female_Literate'] / filter1['Female']) * 100).round()

    # Create separate bar charts
    fig1 = px.bar(filter1,
                  x='District name',
                  y='Male_Literacy_Rate',
                  hover_name='District name',
                  text_auto=True,
                  title='Male Literacy Rate',
                  color_discrete_sequence=['#1f77b4'])  # Blue for male literacy

    fig2 = px.bar(filter1,
                  x='District name',
                  y='Female_Literacy_Rate',
                  text_auto=True,
                  hover_name='District name',
                  title='Female Literacy Rate',
                  color_discrete_sequence=['#ff7f0e'])  # Orange for female literacy

    # Combine the charts into subplots
    fig = make_subplots(
        rows=2,
        cols=1,
        subplot_titles=[
            'Male Literacy Rate by District',
            'Female Literacy Rate by District'
        ],
        vertical_spacing=0.25  # Adjust spacing between subplots
    )

    # Add traces from individual figures
    for trace in fig1.data:
        fig.add_trace(trace, row=1, col=1)

    for trace in fig2.data:
        fig.add_trace(trace, row=2, col=1)

    # Update layout for the combined figure
    fig.update_layout(
        height=800,
        # width=1000,
        title_text=f'Literacy Rates in {state}',
        showlegend=False,
        xaxis_title='District Name',
        yaxis_title='Literacy Rate (%)',
        font=dict(family='Arial, sans-serif', size=12),
        title_font=dict(size=20),
        margin=dict(t=50, b=50),
        plot_bgcolor='#f9f9f9',
        paper_bgcolor='#f9f9f9',
    )

    # Add hover tooltips for better interactivity
    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>Rate: %{y:.2f}%"
    )

    return fig.to_html(full_html=False,include_plotlyjs='cdn',config={'scrollZoom': True})




   





        
    





    
   
    
  


      


    