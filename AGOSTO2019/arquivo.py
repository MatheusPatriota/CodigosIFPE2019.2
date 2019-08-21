import plotly.graph_objects as go

fig = go.Figure(data=go.Heatmap(
    y=['50kg','55kg','60kg', '65kg', '70kg', '75kg' ,'80kg','85kg' ,'90kg', '95kg', '100kg'],

    x=['1.50m', '1.55m', '1.60m', '1.65m', '1.70m',  '1.75m', '1.80m',  '1.85', '1.90m',  '1.95m', '2.0m'],

    z=[[ 22.2 ,20.8, 19.5 ,18.4 ,17.3 ,16.3 ,15.4, 14.6, 13.9 ,13.1 ,12.5],
       [24.4 ,22.9 ,21.5 ,20.2 ,19. , 18. , 17. , 16.1 ,15.2 ,14.5 ,13.8],
       [26.7 ,25. , 23.4 ,22. , 20.8 ,19.6 ,18.5 ,17.5, 16.6, 15.8 ,15. ],
       [28.9 ,27.1 ,25.4 ,23.9, 22.5, 21.2, 20.1, 19. , 18. , 17.1 ,16.2],
       [31.1, 29.1, 27.3 ,25.7 ,24.2 ,22.9, 21.6 ,20.5 ,19.4 ,18.4 ,17.5],
       [33.3 ,31.2, 29.3, 27.5 ,26.  ,24.5, 23.1, 21.9, 20.8 ,19.7, 18.8],
       [35.6 ,33.3 ,31.2 ,29.4 ,27.7 ,26.1 ,24.7 ,23.4 ,22.2 ,21. , 20. ],
       [37.8 ,35.4, 33.2 ,31.2, 29.4, 27.8 ,26.2, 24.8 ,23.5, 22.4, 21.2],
       [40. , 37.5 ,35.2, 33.1, 31.1, 29.4, 27.8, 26.3, 24.9, 23.7, 22.5],
       [42.2 ,39.5, 37.1, 34.9, 32.9, 31.,  29.3, 27.8, 26.3, 25.,  23.8],
       [44.4, 41.6, 39.1, 36.7, 34.6, 32.7, 30.9, 29.2, 27.7, 26.3, 25. ]]))

fig.update_layout(
    title='Tabela IMC Interativa',
    xaxis_nticks=36)


fig.show()