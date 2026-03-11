from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

# Carrega os dados
df = pd.read_csv("ecommerce_estatistica.csv", index_col=0)

# Criar gráficos
def cria_graficos():

    # Histograma
    fig1 = px.histogram(
        df,
        x="Preço",
        nbins=20,
        title="Distribuição de Preços"
    )

    # Dispersão
    fig2 = px.scatter(
        df,
        x="Preço",
        y="Nota",
        color="Temporada",
        title="Relação entre Preço e Nota"
    )

    # Heatmap
    corr = df[["Preço", "Nota", "Qtd_Vendidos_Cod", "N_Avaliações"]].corr()

    fig3 = px.imshow(
        corr,
        text_auto=True,
        aspect="auto",
        title="Correlação entre Variáveis"
    )

    # Barras
    top_marcas = df["Marca"].value_counts().head(10).reset_index()
    top_marcas.columns = ["Marca", "Quantidade"]

    fig4 = px.bar(
        top_marcas,
        x="Quantidade",
        y="Marca",
        orientation="h",
        title="Top 10 Marcas"
    )

    # Pizza
    temp = df["Temporada"].value_counts()

    fig5 = px.pie(
        names=temp.index,
        values=temp.values,
        title="Distribuição por Temporada"
    )

    # Densidade
    fig6 = px.density_contour(
        df,
        x="Preço",
        y="Nota",
        title="Densidade entre Preço e Nota"
    )

    # Regressão
    fig7 = px.scatter(
        df,
        x="Qtd_Vendidos_Cod",
        y="Nota",
        trendline="ols",
        title="Relação entre Vendas e Avaliações"
    )

    return fig1, fig2, fig3, fig4, fig5, fig6, fig7



# Criar App
def cria_app():

    app = Dash(__name__)

    fig1, fig2, fig3, fig4, fig5, fig6, fig7 = cria_graficos()

    app.layout = html.Div([

        html.H1(
            "Dashboard Interativo - Ecommerce",
            style={
                "textAlign": "center",
                "marginBottom": "20px"
            }
        ),

        html.P(
            "Análise exploratória dos dados de ecommerce.",
            style={"textAlign": "center"}
        ),

        # Linha 1
        html.Div([
            dcc.Graph(figure=fig1),
            dcc.Graph(figure=fig2)
        ], style={"display": "flex"}),

        # Linha 2
        html.Div([
            dcc.Graph(figure=fig3),
            dcc.Graph(figure=fig4)
        ], style={"display": "flex"}),

        # Linha 3
        html.Div([
            dcc.Graph(figure=fig5),
            dcc.Graph(figure=fig6)
        ], style={"display": "flex"}),

        # Linha 4
        html.Div([
            dcc.Graph(figure=fig7)
        ])

    ],
    style={
        "maxWidth": "1200px",
        "margin": "auto"
    })

    return app



# Executar
if __name__ == "__main__":
    app = cria_app()
    app.run(debug=True, port=8050)