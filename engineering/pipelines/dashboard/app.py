"""
SpaceX Launch Records Dashboard (Dash)

Location:
- engineering/pipelines/dashboard/app.py

Data:
- notebooks/spacex_launch_dash.csv (preferred, Coursera-compatible)
Fallback:
- data/processed/spacex_launch_dash.csv (if you choose to store it there)

Run:
  python engineering/pipelines/dashboard/app.py
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px


def resolve_data_path() -> Path:
    project_root = Path(__file__).resolve().parents[3]  # .../engineering/pipelines/dashboard -> project root

    candidates = [
        project_root / "notebooks" / "spacex_launch_dash.csv",
        project_root / "data" / "processed" / "spacex_launch_dash.csv",
    ]
    for p in candidates:
        if p.exists():
            return p

    raise FileNotFoundError(
        "spacex_launch_dash.csv not found. Expected one of:\n"
        + "\n".join(str(p) for p in candidates)
    )


# Read the data
data_path = resolve_data_path()
spacex_df = pd.read_csv(data_path)

max_payload = spacex_df["Payload Mass (kg)"].max()
min_payload = spacex_df["Payload Mass (kg)"].min()

# Create the Dash app
app = dash.Dash(__name__)
app.title = "SpaceX Launch Records Dashboard"

# Layout
app.layout = html.Div(
    children=[
        html.H1(
            "SpaceX Launch Records Dashboard",
            style={"textAlign": "center"},
        ),

        dcc.Dropdown(
            id="site-dropdown",
            options=[
                {"label": "All Sites", "value": "ALL"},
                {"label": "CCAFS LC-40", "value": "CCAFS LC-40"},
                {"label": "CCAFS SLC-40", "value": "CCAFS SLC-40"},
                {"label": "KSC LC-39A", "value": "KSC LC-39A"},
                {"label": "VAFB SLC-4E", "value": "VAFB SLC-4E"},
            ],
            value="ALL",
            placeholder="Select a Launch Site",
            searchable=True,
            clearable=False,
            style={"width": "70%", "margin": "0 auto"},
        ),

        html.Br(),

        html.Div(
            dcc.Graph(id="success-pie-chart"),
            style={"width": "80%", "margin": "0 auto"},
        ),

        html.Br(),

        html.P("Payload range (kg):", style={"textAlign": "center"}),

        dcc.RangeSlider(
            id="payload-slider",
            min=min_payload,
            max=max_payload,
            step=1000,
            marks={
                int(min_payload): str(int(min_payload)),
                int(max_payload): str(int(max_payload)),
            },
            value=[min_payload, max_payload],
            tooltip={"placement": "bottom", "always_visible": False},
        ),

        html.Br(),

        html.Div(
            dcc.Graph(id="success-payload-scatter-chart"),
            style={"width": "90%", "margin": "0 auto"},
        ),
    ],
    style={"maxWidth": "1200px", "margin": "0 auto", "padding": "16px"},
)


@app.callback(
    Output("success-pie-chart", "figure"),
    Input("site-dropdown", "value"),
)
def update_pie_chart(selected_site: str):
    if selected_site == "ALL":
        fig = px.pie(
            spacex_df,
            names="Launch Site",
            values="class",
            title="Total Successful Landings by Site",
        )
        return fig

    filtered = spacex_df[spacex_df["Launch Site"] == selected_site]
    success_counts = (
        filtered["class"]
        .value_counts()
        .rename_axis("class")
        .reset_index(name="count")
    )
    success_counts["Outcome"] = success_counts["class"].map({1: "Success", 0: "Failure"})

    fig = px.pie(
        success_counts,
        names="Outcome",
        values="count",
        title=f"Launch Outcomes for {selected_site}",
    )
    return fig


@app.callback(
    Output("success-payload-scatter-chart", "figure"),
    [Input("site-dropdown", "value"), Input("payload-slider", "value")],
)
def update_scatter_chart(selected_site: str, payload_range):
    low, high = payload_range

    df = spacex_df[
        (spacex_df["Payload Mass (kg)"] >= low) & (spacex_df["Payload Mass (kg)"] <= high)
    ]

    if selected_site != "ALL":
        df = df[df["Launch Site"] == selected_site]

    title = "Payload vs. Launch Outcome"
    if selected_site != "ALL":
        title += f" ({selected_site})"

    fig = px.scatter(
        df,
        x="Payload Mass (kg)",
        y="class",
        color="Booster Version Category",
        title=title,
        hover_data=["Flight Number"],
    )
    return fig


if __name__ == "__main__":
    app.run(debug=True)
