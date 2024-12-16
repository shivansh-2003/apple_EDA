import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Title and Description
st.title("Apple Financial Dashboard (2009-2024)")
st.markdown("""
Explore Apple's financial performance during its transformative years. This dashboard provides:
- Key metrics like revenue, profit, and EPS.
- Trends over time with interactive graphs.
- Insights into Apple's financial strategy and growth trajectory.
""")

# Load Dataset (Directly from the file)
# Define the Apple Financial Data
data = {
    "year": [2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009],
    "EBITDA (millions)": [134661, 125820, 130541, 120233, 77344, 76477, 81801, 71501, 70529, 82487, 60449, 55756, 58518, 35604, 19412, 12474],
    "Revenue (millions)": [391035, 383285, 394328, 365817, 274515, 260174, 265595, 229234, 215639, 233715, 182795, 170910, 156508, 108249, 65225, 42905],
    "Gross Profit (millions)": [180683, 169148, 170782, 152836, 104956, 98392, 101839, 88186, 84263, 93626, 70537, 64304, 68662, 43818, 25684, 17222],
    "Op Income (millions)": [123216, 114301, 119437, 108949, 66288, 63930, 70898, 61344, 60024, 71230, 52503, 48999, 55241, 33790, 18385, 11740],
    "Net Income (millions)": [93736, 96995, 99803, 94680, 57411, 55256, 59531, 48351, 45687, 53394, 39510, 37037, 41733, 25922, 14013, 8235],
    "EPS": [6.08, 6.13, 6.11, 5.61, 3.28, 2.97, 2.98, 2.30, 2.08, 2.31, 1.61, 1.42, 1.58, 0.99, 0.54, 0.32],
    "Shares Outstanding": [15408, 15813, 16326, 16865, 17528, 18596, 20000, 21007, 22001, 23172, 24491, 26087, 26470, 26226, 25892, 25396],
    "Year Close Price": [243.04, 191.5919, 128.5816, 174.7132, 129.7556, 71.1734, 37.6645, 39.8109, 26.8131, 23.8379, 24.5797, 17.4799, 16.176, 12.2002, 9.7168, 6.3481],
    "Total Assets (millions)": [364980, 352583, 352755, 351002, 323888, 338516, 365725, 375319, 321686, 290345, 231839, 207000, 176064, 116371, 75183, 47501],
    "Cash on Hand (millions)": [65171, 61555, 48304, 62639, 90943, 100557, 66301, 74181, 67155, 41601, 25077, 40546, 29129, 25952, 25620, 23464],
    "Long Term Debt (millions)": [85750, 95281, 98959, 109106, 98667, 91807, 93735, 97207, 75427, 53329, 28987, 16960, 0, 0, 0, 0],
    "Total Liabilities (millions)": [308030, 290437, 302083, 287912, 258549, 248028, 258578, 241272, 193437, 170990, 120292, 83451, 57854, 39756, 27392, 15861],
    "Gross Margin": [46.21, 45.03, 43.06, 43.02, 38.78, 37.95, 38.21, 38.43, 38.52, 40.13, 39.26, 37.41, 41.91, 42.41, 38.76, 40.95],
    "PE ratio": [39.97, 29.84, 21.83, 28.93, 35.14, 22.49, 12.39, 16.37, 12.84, 10.12, 13.25, 12.14, 10.27, 9.73, 15.19, 20.52],
    "Employees": [164000, 161000, 164000, 154000, 147000, 137000, 132000, 123000, 116000, 110000, 97000, 84400, 76100, 63300, 49400, 36800]
}

# Convert to DataFrame
apple_data = pd.DataFrame(data)

# Sidebar Navigation
st.sidebar.title("Navigation")
option = st.sidebar.radio("Select a Page", ['Overview', 'Visualizations', 'Key Takeaways'])

# Overview Page
if option == 'Overview':
    st.header("Dataset Overview")
    st.write(apple_data.head())
    st.markdown("""
    #### Features:
    - **Year**: Fiscal year.
    - **Revenue, Gross Profit, Net Income**: Key financial metrics (in millions).
    - **EPS**: Earnings per share (in USD).
    - **Assets, Liabilities, Debt**: Balance sheet items (in millions).
    """)
    st.write("### Summary Statistics")
    st.write(apple_data.describe())

# Visualizations Page
elif option == 'Visualizations':
    st.header("Interactive Financial Graphs")

    # Revenue and Net Income Over Time
    st.subheader("Revenue and Net Income Growth (2009-2024)")
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=apple_data['year'], y=apple_data['Revenue (millions)'], 
                              mode='lines+markers', name='Revenue', line=dict(color='blue')))
    fig1.add_trace(go.Scatter(x=apple_data['year'], y=apple_data['Net Income (millions)'], 
                              mode='lines+markers', name='Net Income', line=dict(color='green')))
    fig1.update_layout(title="Revenue vs Net Income",
                       xaxis_title="Year", yaxis_title="Amount (in Millions)", template="plotly_white")
    st.plotly_chart(fig1)

    # EPS Growth
    st.subheader("Earnings Per Share (EPS) Growth")
    fig2 = px.line(apple_data, x='year', y='EPS', markers=True, 
                   title="Earnings Per Share Growth (2009-2024)", 
                   labels={'year': 'Year', 'EPS': 'Earnings Per Share (USD)'})
    st.plotly_chart(fig2)

    # Assets and Liabilities
    st.subheader("Assets vs Liabilities")
    fig3 = go.Figure()
    fig3.add_trace(go.Bar(x=apple_data['year'], y=apple_data['Total Assets (millions)'], 
                          name='Total Assets', marker=dict(color='blue')))
    fig3.add_trace(go.Bar(x=apple_data['year'], y=apple_data['Total Liabilities (millions)'], 
                          name='Total Liabilities', marker=dict(color='orange')))
    fig3.update_layout(title="Assets vs Liabilities",
                       xaxis_title="Year", yaxis_title="Amount (in Millions)", barmode='group', template="plotly_white")
    st.plotly_chart(fig3)

    # Cash on Hand
    st.subheader("Cash on Hand (Liquidity)")
    fig4 = px.line(apple_data, x='year', y='Cash on Hand (millions)', markers=True, 
                   title="Cash on Hand (2009-2024)", labels={'year': 'Year', 'Cash on Hand (millions)': 'Cash (in Millions)'})
    st.plotly_chart(fig4)
    # Revenue vs Gross Margin
    st.subheader("Revenue vs Gross Margin")

# Create a figure with two y-axes: one for Revenue and one for Gross Margin
    fig5 = go.Figure()

# Add Revenue (Bar Chart) to the primary y-axis
# 
    fig5.add_trace(go.Bar(x=apple_data['year'], 
                     y=apple_data['Revenue (millions)'], 
                     name='Revenue (millions)', 
                     marker=dict(color='orange')))

# Add Gross Margin (Line Chart) to the secondary y-axis (right side)
    fig5.add_trace(go.Scatter(x=apple_data['year'], 
                         y=apple_data['Gross Margin'] * 100,  # Scale Gross Margin to percentage
                         mode='lines+markers', 
                         name='Gross Margin (%)', 
                         line=dict(color='red'),
                         yaxis='y2'))  # Link this trace to the secondary y-axis

# Update Layout
    fig5.update_layout(
    title="Revenue vs Gross Margin (2009-2024)",
    xaxis_title="Year", 
    yaxis_title="Revenue (in millions)",  # Primary y-axis title (left side)
    yaxis2=dict(
        title="Gross Margin (%)",  # Secondary y-axis title (right side)
        overlaying='y',  # Overlay the secondary axis on the primary axis
        side='right',  # Position the secondary axis on the right side
        range=[0, 100]  # Set the range for gross margin to 0-100%
    ),
    template="plotly_white",  # Set the template for a clean look
    barmode="group",  # Group the bars with the line
    showlegend=True  # Show the legend to differentiate between Revenue and Gross Margin
)

# Display the chart
    st.plotly_chart(fig5)
      # PE Ratio Over Time
    st.subheader("PE Ratio (Valuation)")
    fig6 = px.line(apple_data, x='year', y='PE ratio', markers=True, 
                   title="PE Ratio Over Time", labels={'year': 'Year', 'PE ratio': 'Price-to-Earnings Ratio'})
    fig6.update_traces(line=dict(color='purple'))
    st.plotly_chart(fig6)

    st.subheader("Employee Growth")

# Creating a bar chart to visualize Employee Growth
    fig7 = px.bar(apple_data, 
              x='year', 
              y='Employees', 
              title="Employees at Apple (2009-2024)",
              labels={'year': 'Fiscal Year', 'Employees': 'Number of Employees'},
              color='Employees',  # Color by the number of employees for better visual impact
              color_continuous_scale='Viridis',  # Use a continuous color scale for better representation
              text='Employees',  # Display the number of employees on the bars for easy reference
              template='plotly_dark')  # Use a dark template for better contrast

# Update traces for styling
    fig7.update_traces(
    marker=dict(line=dict(color='black', width=1)),  # Add black borders to bars for clarity
    texttemplate='%{text}',  # Display employee numbers on bars
    textposition='outside',  # Position the text outside the bars
    hovertemplate='Year: %{x}<br>Employees: %{y}',  # Add hover info with year and employee count
)

# Add title and adjust layout for clarity
    fig7.update_layout(
    title={
        'text': "Apple's Employee Growth (2009-2024)",
        'x': 0.5,  # Center the title
        'xanchor': 'center',
        'yanchor': 'top'
    },
    xaxis_title='Fiscal Year',
    yaxis_title='Number of Employees',
    xaxis=dict(
        tickmode='array',  # Custom tick values for better control
        tickvals=apple_data['year'],  # Use the actual years in the dataset
        ticktext=apple_data['year'].astype(str),  # Ensure the years are labeled correctly
        tickangle=45,  # Rotate the tick labels slightly to avoid overlap
    ),
    yaxis=dict(tickformat=',.0f'),  # Format y-axis with commas for easier reading
    showlegend=False,  # Hide legend since it's not needed
    plot_bgcolor='rgba(0,0,0,0)',  # Set a transparent background for a clean look
    margin={'t': 50, 'b': 100, 'l': 60, 'r': 60},  # Add margin to avoid label clipping
)

# Display the plot
    st.plotly_chart(fig7)

elif option == 'Key Takeaways':
    st.header("Key Insights and Takeaways")
    st.markdown("""
    ### Financial Performance Highlights

    - **Revenue Growth**: 
        - Apple's revenue has shown a consistent upward trend from 2009 to 2024, reflecting its strong market presence and ability to innovate. 
        - Key factors driving this growth include new product launches, increased services revenue, and global expansion into emerging markets.
        - The sharp increase in revenue post-2015 highlights the impact of flagship products like the iPhone, iPad, and growth in the services sector.

    - **Profitability**: 
        - High gross margins across the years illustrate Apple's strong pricing power and operational efficiency. 
        - The company has maintained gross margins above industry benchmarks, indicating effective cost management and superior product value propositions.
        - Strong profitability is further emphasized by robust net income, which underscores the company’s ability to convert revenue into substantial shareholder returns.

    - **Earnings Per Share (EPS) Growth**:
        - EPS growth showcases Apple's commitment to enhancing shareholder value.
        - Sustained increases in EPS over the years reflect higher net income and share buybacks, which reduce outstanding shares and boost per-share earnings.
        - The trend demonstrates Apple’s ability to navigate changing economic landscapes while delivering consistent returns to investors.

    ### Balance Sheet and Financial Strategy

    - **Balance Sheet Strength**:
        - Apple's substantial asset base, consistently exceeding liabilities, highlights its financial stability.
        - High levels of liquidity, reflected in strong cash reserves, empower the company to invest in R&D, make acquisitions, and return capital to shareholders.
        - This financial cushion provides Apple with flexibility to adapt to market changes and seize new opportunities.

    - **Debt Management**: 
        - While Apple has taken on long-term debt over the years, it remains highly manageable relative to its revenue and cash flow.
        - Strategic use of debt has allowed the company to finance share buybacks, dividends, and infrastructure projects without compromising financial health.
        - Low interest rates and the company's strong credit rating make debt a cost-effective tool for strategic investments.

    ### Workforce and Operational Insights

    - **Employee Growth**:
        - The steady increase in the number of employees reflects Apple’s global expansion and the need for a larger workforce to support product innovation, retail operations, and services.
        - Investment in talent indicates Apple’s focus on maintaining its leadership in technology and services.
        - Workforce growth also aligns with the company’s increasing emphasis on emerging areas like AI, AR/VR, and sustainable technologies.

    ### Market Valuation and Investor Sentiment

    - **PE Ratio (Valuation)**:
        - The Price-to-Earnings (PE) ratio reveals how the market perceives Apple’s growth potential.
        - Fluctuations in the PE ratio provide insights into investor sentiment, with higher values during periods of optimism about Apple's future growth prospects.
        - Stable PE ratios in recent years highlight balanced expectations regarding the company's long-term value.

    ### Key Observations
    - Apple's consistent financial performance underscores its ability to innovate and adapt.
    - The company’s focus on profitability, shareholder value, and operational excellence has positioned it as a leader in the tech industry.
    - With a strong balance sheet and a growing workforce, Apple remains well-prepared to tackle future challenges and capitalize on emerging opportunities.
    """)
    st.write("Explore detailed visualizations in the **Visualizations** tab to gain deeper insights into Apple's financial journey!")