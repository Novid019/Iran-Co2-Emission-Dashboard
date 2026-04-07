"""
Iran CO₂ Emissions Dashboard
BS in Analytics and Sustainability Studies (2024-28)
TISS Mumbai — Novid Salhot (M2024BSASS019) — Country: Iran
Data Source: Our World in Data (OWID)
"""

# ──────────────────────────────────────────────────────────────────────────────
# DEPENDENCIES  →  pip install dash dash-bootstrap-components plotly pandas
# ──────────────────────────────────────────────────────────────────────────────

import io, base64
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc

# ══════════════════════════════════════════════════════════════════════════════
# LOAD DATA FROM CSV  (place Final_Clean_Data.csv next to app.py)
# ══════════════════════════════════════════════════════════════════════════════
import os

CSV_PATH = os.path.join(os.path.dirname(__file__), "Final_Clean_Data.csv")

df = pd.read_csv(CSV_PATH)

# Normalise column names (strip BOM / spaces)
df.columns = [c.strip().lstrip('\ufeff') for c in df.columns]

# ══════════════════════════════════════════════════════════════════════════════
# DATA PREP
# ══════════════════════════════════════════════════════════════════════════════
df_no_world = df[df["Country"] != "World"].copy()
iran  = df[df["Country"] == "Iran"].copy()
world = df[df["Country"] == "World"].copy()
india = df[df["Country"] == "India"].copy()

countries_all = sorted(df_no_world["Country"].unique().tolist())

SOURCES = [
    "Coal CO2 (Mt)",
    "Oil CO2 (Mt)",
    "Gas CO2 (Mt)",
    "Cement CO2 (Mt)",
    "Flaring CO2 (Mt)",
]
SOURCE_LABELS = ["Coal", "Oil", "Gas", "Cement", "Flaring"]

# ══════════════════════════════════════════════════════════════════════════════
# COLOUR PALETTE  — warm off-white / beige light theme
# ══════════════════════════════════════════════════════════════════════════════
C_BG        = "#fdf6ec"          # warm cream page background
C_CARD      = "#ffffff"          # pure white cards
C_SIDEBAR   = "#1b3a2d"          # deep forest green sidebar
C_GREEN     = "#1e7e45"          # Iran flag green (medium)
C_GREEN_LT  = "#27ae60"          # lighter green accent
C_RED       = "#c0392b"          # Iran flag red
C_AMBER     = "#d4a017"          # warm amber accent
C_GREY      = "#6b7280"
C_DARK_TEXT = "#1a1a2e"
C_BORDER    = "#e5d9c8"          # warm border
C_MUTED     = "#a0856c"

SOURCE_COLORS = [C_GREEN, "#e8a020", C_RED, C_AMBER, "#7c5cbf"]

PLOT_BG  = "rgba(0,0,0,0)"
PAPER_BG = "rgba(0,0,0,0)"

BASE_LAYOUT = dict(
    paper_bgcolor=PAPER_BG,
    plot_bgcolor=PLOT_BG,
    font=dict(family="Inter, Segoe UI, Arial, sans-serif", color=C_DARK_TEXT, size=11),
    margin=dict(l=12, r=12, t=36, b=40),
    legend=dict(
        bgcolor="rgba(255,255,255,0.85)",
        bordercolor=C_BORDER,
        borderwidth=1,
        font=dict(size=10, color=C_DARK_TEXT),
    ),
    xaxis=dict(gridcolor="#ecdfc8", showgrid=True, zeroline=False,
               linecolor=C_BORDER, tickfont=dict(color=C_DARK_TEXT)),
    yaxis=dict(gridcolor="#ecdfc8", showgrid=True, zeroline=False,
               linecolor=C_BORDER, tickfont=dict(color=C_DARK_TEXT)),
)

# ══════════════════════════════════════════════════════════════════════════════
# LAYOUT HELPERS
# ══════════════════════════════════════════════════════════════════════════════
def card(children, extra_style=None):
    base = {
        "background": C_CARD,
        "border": f"1px solid {C_BORDER}",
        "borderRadius": "12px",
        "padding": "18px",
        "marginBottom": "16px",
        "boxShadow": "0 2px 12px rgba(160,133,108,0.15)",
    }
    if extra_style:
        base.update(extra_style)
    return html.Div(children, style=base)


def kpi_block(label, value, color):
    return html.Div([
        html.Div(label, style={"fontSize": "10px", "color": "rgba(255,255,255,0.65)",
                               "textTransform": "uppercase", "letterSpacing": "0.8px",
                               "marginBottom": "4px"}),
        html.Div(value, style={"fontSize": "19px", "fontWeight": "700", "color": color}),
    ], style={
        "background": "rgba(255,255,255,0.06)",
        "borderLeft": f"3px solid {color}",
        "borderRadius": "6px",
        "padding": "10px 12px",
        "marginBottom": "8px",
    })


CITATION = html.Div(
    "📊 Source: Our World in Data (OWID) — Global Carbon Project & World Bank",
    style={"fontSize": "10px", "color": C_MUTED, "marginTop": "6px",
           "fontStyle": "italic", "textAlign": "right"}
)

# ══════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════════════════════════════════════
sidebar = html.Div([
    # Flag gradient stripe
    html.Div(style={
        "height": "5px",
        "background": f"linear-gradient(to right, {C_GREEN_LT} 33%, #f8f8f8 33%, #f8f8f8 66%, {C_RED} 66%)"
    }),

    html.Div([
        html.Div("🇮🇷", style={"fontSize": "34px", "textAlign": "center", "marginBottom": "4px"}),
        html.H4("Iran CO₂ Dashboard",
                style={"color": "#ffffff", "textAlign": "center",
                       "fontWeight": "700", "fontSize": "15px", "marginBottom": "2px"}),
        html.P("TISS Mumbai · M2024BSASS019 · Novid Salhot",
               style={"fontSize": "10px", "color": "rgba(255,255,255,0.55)",
                      "textAlign": "center", "marginBottom": "18px"}),

        html.Hr(style={"borderColor": "rgba(255,255,255,0.15)", "margin": "0 0 14px 0"}),

        kpi_block("Latest Emissions (2024)", "792.6 Mt CO₂", "#ef8c8c"),
        kpi_block("Per Capita (2024)",        "8.66 t/person", C_AMBER),
        kpi_block("Global Share (2024)",       "2.05%",         "#81d99a"),

        html.Hr(style={"borderColor": "rgba(255,255,255,0.15)", "margin": "14px 0"}),

        html.Label("📅 Year Range",
                   style={"fontSize": "11px", "color": "#81d99a",
                          "fontWeight": "600", "marginBottom": "6px", "display": "block"}),
        dcc.RangeSlider(
            id="year-slider",
            min=2006, max=2024, step=1,
            value=[2006, 2024],
            marks={2006: {"label": "2006", "style": {"color": "rgba(255,255,255,0.6)", "fontSize": "10px"}},
                   2015: {"label": "2015", "style": {"color": "rgba(255,255,255,0.6)", "fontSize": "10px"}},
                   2024: {"label": "2024", "style": {"color": "rgba(255,255,255,0.6)", "fontSize": "10px"}}},
            tooltip={"placement": "bottom", "always_visible": False},
        ),
        html.Div(style={"marginBottom": "14px"}),

        html.Label("🌐 Compare Countries",
                   style={"fontSize": "11px", "color": "#81d99a",
                          "fontWeight": "600", "marginBottom": "6px", "display": "block"}),
        dcc.Dropdown(
            id="compare-countries",
            options=[{"label": c, "value": c} for c in countries_all if c not in ["Iran", "World"]],
            value=["India", "Saudi Arabia", "Iraq"],
            multi=True,
            placeholder="Select countries…",
            style={"fontSize": "12px"},
        ),
        html.Div(style={"marginBottom": "14px"}),

        html.Label("⚡ Emission Source (Chart 5)",
                   style={"fontSize": "11px", "color": "#81d99a",
                          "fontWeight": "600", "marginBottom": "6px", "display": "block"}),
        dcc.Dropdown(
            id="source-filter",
            options=[{"label": l, "value": s} for l, s in zip(SOURCE_LABELS, SOURCES)],
            value=SOURCES,
            multi=True,
            placeholder="All sources",
            style={"fontSize": "12px"},
        ),
        html.Div(style={"marginBottom": "18px"}),

        html.Hr(style={"borderColor": "rgba(255,255,255,0.15)", "margin": "0 0 12px 0"}),
        html.Label("📥 Download Charts (PNG)",
                   style={"fontSize": "11px", "color": "#81d99a",
                          "fontWeight": "600", "marginBottom": "8px", "display": "block"}),
        *[
            html.Button(
                f"⬇ Chart {i+1}",
                id=f"btn-dl-{i+1}",
                n_clicks=0,
                style={
                    "width": "100%", "marginBottom": "5px",
                    "background": "rgba(255,255,255,0.07)",
                    "color": "#81d99a",
                    "border": "1px solid rgba(129,217,154,0.4)",
                    "borderRadius": "6px", "padding": "7px",
                    "cursor": "pointer", "fontSize": "12px",
                    "transition": "background 0.2s",
                }
            )
            for i in range(6)
        ],
        *[dcc.Download(id=f"download-{i+1}") for i in range(6)],

    ], style={"padding": "16px"}),

    html.Div(style={
        "height": "5px",
        "background": f"linear-gradient(to right, {C_GREEN_LT} 33%, #f8f8f8 33%, #f8f8f8 66%, {C_RED} 66%)"
    }),

], style={
    "width": "265px",
    "minWidth": "265px",
    "background": C_SIDEBAR,
    "height": "100vh",
    "overflowY": "auto",
    "position": "sticky",
    "top": "0",
    "borderRight": "none",
    "boxShadow": "3px 0 20px rgba(0,0,0,0.12)",
})

# ══════════════════════════════════════════════════════════════════════════════
# MAIN CONTENT
# ══════════════════════════════════════════════════════════════════════════════
main = html.Div([

    # ── Header ─────────────────────────────────────────────────────────────
    html.Div([
        html.Div([
            html.H2("Iran — CO₂ Emissions & Climate Analysis",
                    style={"color": C_GREEN, "margin": "0", "fontWeight": "800", "fontSize": "22px"}),
            html.P("BS Analytics & Sustainability Studies 2024–28 | TISS Mumbai | Assignment I",
                   style={"color": C_MUTED, "fontSize": "12px", "margin": "2px 0 0 0"}),
        ]),
        html.Div([
            html.Span("Data: OWID", style={
                "background": f"{C_GREEN}22", "color": C_GREEN,
                "border": f"1px solid {C_GREEN}44",
                "borderRadius": "20px", "padding": "4px 12px",
                "fontSize": "11px", "fontWeight": "600"
            }),
        ]),
    ], style={
        "display": "flex", "justifyContent": "space-between", "alignItems": "center",
        "borderBottom": f"3px solid {C_GREEN}", "paddingBottom": "12px", "marginBottom": "20px"
    }),

    # ── Row 1: Chart 1 + Chart 2 ───────────────────────────────────────────
    html.Div([
        card([
            html.H6("📊 Chart 1 — Total CO₂ Emissions (Mt)",
                    style={"color": C_GREEN, "marginBottom": "8px", "fontWeight": "700"}),
            dcc.Graph(id="chart-1", config={"displayModeBar": True, "toImageButtonOptions": {"format": "png", "scale": 2}}),
            CITATION,
        ], {"flex": "1"}),
        card([
            html.H6("📊 Chart 2 — Per Capita CO₂ vs World Average",
                    style={"color": C_GREEN, "marginBottom": "8px", "fontWeight": "700"}),
            dcc.Graph(id="chart-2", config={"displayModeBar": True, "toImageButtonOptions": {"format": "png", "scale": 2}}),
            CITATION,
        ], {"flex": "1"}),
    ], style={"display": "flex", "gap": "16px"}),

    # ── Row 2: Chart 3 ─────────────────────────────────────────────────────
    card([
        html.H6("📊 Chart 3 — Per Capita CO₂ Comparison (Latest Year)",
                style={"color": C_GREEN, "marginBottom": "8px", "fontWeight": "700"}),
        dcc.Graph(id="chart-3", config={"displayModeBar": True, "toImageButtonOptions": {"format": "png", "scale": 2}}),
        CITATION,
    ]),

    # ── Row 3: Chart 4 + Chart 6 ───────────────────────────────────────────
    html.Div([
        card([
            html.H6("📊 Chart 4 — GDP per Capita vs CO₂ Emissions (Scatter)",
                    style={"color": C_GREEN, "marginBottom": "8px", "fontWeight": "700"}),
            dcc.Graph(id="chart-4", config={"displayModeBar": True, "toImageButtonOptions": {"format": "png", "scale": 2}}),
            CITATION,
        ], {"flex": "1"}),
        card([
            html.H6("📊 Chart 6 — Global CO₂ Share (Pie)",
                    style={"color": C_GREEN, "marginBottom": "8px", "fontWeight": "700"}),
            dcc.Graph(id="chart-6", config={"displayModeBar": True, "toImageButtonOptions": {"format": "png", "scale": 2}}),
            CITATION,
        ], {"flex": "1"}),
    ], style={"display": "flex", "gap": "16px"}),

    # ── Row 4: Chart 5 ─────────────────────────────────────────────────────
    card([
        html.H6("📊 Chart 5 — Iran CO₂ Emissions by Source (Stacked Bar)",
                style={"color": C_GREEN, "marginBottom": "8px", "fontWeight": "700"}),
        dcc.Graph(id="chart-5", config={"displayModeBar": True, "toImageButtonOptions": {"format": "png", "scale": 2}}),
        CITATION,
    ]),

], style={
    "flex": "1",
    "padding": "24px 28px",
    "overflowY": "auto",
    "height": "100vh",
    "background": C_BG,
})

# ══════════════════════════════════════════════════════════════════════════════
# ROOT LAYOUT
# ══════════════════════════════════════════════════════════════════════════════
app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.FLATLY,
        "https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap",
    ],
    suppress_callback_exceptions=True,
    title="Iran CO₂ Dashboard | TISS",
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)
server = app.server  # expose for Gunicorn on Render

app.layout = html.Div(
    [html.Div([sidebar, main],
              style={"display": "flex", "flexDirection": "row",
                     "height": "100vh", "overflow": "hidden"})],
    style={"background": C_BG, "fontFamily": "Inter, Segoe UI, Arial, sans-serif"}
)


# ══════════════════════════════════════════════════════════════════════════════
# HELPERS
# ══════════════════════════════════════════════════════════════════════════════
def fi(yr):          # filtered iran
    return iran[(iran["Year"] >= yr[0]) & (iran["Year"] <= yr[1])].copy()

def fw(yr):          # filtered world
    return world[(world["Year"] >= yr[0]) & (world["Year"] <= yr[1])].copy()


# ══════════════════════════════════════════════════════════════════════════════
# CHART 1 — Total CO₂ trendline
# ══════════════════════════════════════════════════════════════════════════════
@app.callback(Output("chart-1", "figure"), Input("year-slider", "value"))
def chart1(yr):
    d = fi(yr).dropna(subset=["Total CO2 Emissions (Mt)"])
    if d.empty:
        return go.Figure()

    years  = d["Year"].values
    vals   = d["Total CO2 Emissions (Mt)"].values

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=years, y=vals,
        mode="lines+markers",
        name="Iran Total CO₂",
        line=dict(color=C_RED, width=3),
        marker=dict(size=6, color=C_RED),
        fill="tozeroy",
        fillcolor=f"{C_RED}22",
        hovertemplate="Year: %{x}<br>CO₂: %{y:.1f} Mt<extra></extra>",
    ))

    # Trendline
    z = np.polyfit(years, vals, 1)
    fig.add_trace(go.Scatter(
        x=years, y=np.poly1d(z)(years),
        mode="lines", name="Trend",
        line=dict(color=C_AMBER, width=2, dash="dot"),
        hoverinfo="skip",
    ))

    layout = dict(**BASE_LAYOUT)
    layout["yaxis"] = dict(BASE_LAYOUT["yaxis"], title="Total CO₂ (Mt)")
    layout["xaxis"] = dict(BASE_LAYOUT["xaxis"], title="Year")
    layout["height"] = 320
    layout["title"]  = dict(text="", font=dict(size=12))
    fig.update_layout(**layout)
    return fig


# ══════════════════════════════════════════════════════════════════════════════
# CHART 2 — Per Capita vs World Avg
# ══════════════════════════════════════════════════════════════════════════════
@app.callback(Output("chart-2", "figure"), Input("year-slider", "value"))
def chart2(yr):
    d  = fi(yr).dropna(subset=["Per Capita CO2 (Mt)"])
    wd = fw(yr).dropna(subset=["Per Capita CO2 (Mt)"])

    if d.empty:
        return go.Figure()

    years = d["Year"].values
    vals  = d["Per Capita CO2 (Mt)"].values

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=years, y=vals,
        mode="lines+markers",
        name="Iran Per Capita",
        line=dict(color=C_GREEN, width=3),
        marker=dict(size=6, color=C_GREEN),
        fill="tozeroy",
        fillcolor=f"{C_GREEN}22",
        hovertemplate="Year: %{x}<br>Per Capita: %{y:.2f} t<extra></extra>",
    ))

    if not wd.empty:
        fig.add_trace(go.Scatter(
            x=wd["Year"].values, y=wd["Per Capita CO2 (Mt)"].values,
            mode="lines", name="World Avg",
            line=dict(color=C_GREY, width=2, dash="dash"),
            hovertemplate="Year: %{x}<br>World: %{y:.2f} t<extra></extra>",
        ))

    # Trendline
    z = np.polyfit(years, vals, 1)
    fig.add_trace(go.Scatter(
        x=years, y=np.poly1d(z)(years),
        mode="lines", name="Trend",
        line=dict(color=C_AMBER, width=2, dash="dot"),
        hoverinfo="skip",
    ))

    layout = dict(**BASE_LAYOUT)
    layout["yaxis"] = dict(BASE_LAYOUT["yaxis"], title="Per Capita CO₂ (t/person)")
    layout["xaxis"] = dict(BASE_LAYOUT["xaxis"], title="Year")
    layout["height"] = 320
    fig.update_layout(**layout)
    return fig


# ══════════════════════════════════════════════════════════════════════════════
# CHART 3 — Horizontal bar: per capita comparison
# ══════════════════════════════════════════════════════════════════════════════
@app.callback(
    Output("chart-3", "figure"),
    Input("compare-countries", "value"),
    Input("year-slider", "value"),
)
def chart3(compare, yr):
    all_c = list(set((compare or []) + ["Iran", "India"]))
    latest_yr = yr[1]
    rows = []
    for c in all_c:
        sub = df_no_world[(df_no_world["Country"] == c) & (df_no_world["Year"] == latest_yr)]
        if sub.empty:
            sub = df_no_world[df_no_world["Country"] == c].sort_values("Year").tail(1)
        if not sub.empty:
            v = sub["Per Capita CO2 (Mt)"].values[0]
            if pd.notna(v):
                rows.append({"Country": c, "PerCap": float(v)})

    if not rows:
        return go.Figure()

    d = pd.DataFrame(rows).sort_values("PerCap")
    colors = []
    for c in d["Country"]:
        if c == "Iran":   colors.append(C_RED)
        elif c == "India": colors.append(C_GREEN)
        else:              colors.append("#b0c4b8")

    fig = go.Figure(go.Bar(
        x=d["PerCap"], y=d["Country"],
        orientation="h",
        marker_color=colors,
        marker_line=dict(color="white", width=0.5),
        hovertemplate="%{y}: %{x:.2f} t CO₂/person<extra></extra>",
        text=[f"{v:.2f}" for v in d["PerCap"]],
        textposition="outside",
        textfont=dict(color=C_DARK_TEXT, size=10),
    ))

    layout = dict(**BASE_LAYOUT)
    layout["xaxis"] = dict(BASE_LAYOUT["xaxis"], title="Per Capita CO₂ (t/person)")
    layout["yaxis"] = dict(BASE_LAYOUT["yaxis"], title="")
    layout["height"] = max(320, len(d) * 44 + 80)
    fig.update_layout(**layout)
    return fig


# ══════════════════════════════════════════════════════════════════════════════
# CHART 4 — GDP per Capita vs Total CO₂ (Scatter)
# ══════════════════════════════════════════════════════════════════════════════
@app.callback(
    Output("chart-4", "figure"),
    Input("compare-countries", "value"),
    Input("year-slider", "value"),
)
def chart4(compare, yr):
    all_c = list(set((compare or []) + ["Iran", "India"]))
    sub = df_no_world[
        (df_no_world["Country"].isin(all_c)) &
        (df_no_world["Year"] >= yr[0]) &
        (df_no_world["Year"] <= yr[1]) &
        (df_no_world["GDP per Capita (Constant US$)"].notna())
    ]

    fig = go.Figure()
    palette = [C_RED, C_GREEN, "#e8a020", "#7c5cbf", "#17a2b8",
               "#fd7e14", "#6610f2", "#20c997", "#e83e8c", "#343a40"]

    for idx, c in enumerate(all_c):
        d = sub[sub["Country"] == c]
        if d.empty:
            continue
        clr = C_RED if c == "Iran" else (C_GREEN if c == "India" else palette[idx % len(palette)])
        fig.add_trace(go.Scatter(
            x=d["GDP per Capita (Constant US$)"].values,
            y=d["Total CO2 Emissions (Mt)"].values,
            mode="markers+lines", name=c,
            marker=dict(color=clr, size=8 if c == "Iran" else 6, symbol="circle"),
            line=dict(color=clr, width=1.5),
            hovertemplate=f"<b>{c}</b><br>GDP/cap: $%{{x:,.0f}}<br>CO₂: %{{y:.1f}} Mt<extra></extra>",
        ))

    layout = dict(**BASE_LAYOUT)
    layout["xaxis"] = dict(BASE_LAYOUT["xaxis"], title="GDP per Capita (Constant US$)")
    layout["yaxis"] = dict(BASE_LAYOUT["yaxis"], title="Total CO₂ Emissions (Mt)")
    layout["height"] = 360
    fig.update_layout(**layout)
    return fig


# ══════════════════════════════════════════════════════════════════════════════
# CHART 5 — Stacked bar by source
# ══════════════════════════════════════════════════════════════════════════════
@app.callback(
    Output("chart-5", "figure"),
    Input("source-filter", "value"),
    Input("year-slider", "value"),
)
def chart5(sources, yr):
    d    = fi(yr)
    srcs = sources if sources else SOURCES

    fig = go.Figure()
    for src, clr, lbl in zip(SOURCES, SOURCE_COLORS, SOURCE_LABELS):
        if src not in srcs:
            continue
        col_vals = pd.to_numeric(d[src], errors="coerce").fillna(0)
        fig.add_trace(go.Bar(
            x=d["Year"].values, y=col_vals.values,
            name=lbl, marker_color=clr,
            hovertemplate=f"{lbl}: %{{y:.1f}} Mt<extra></extra>",
        ))

    layout = dict(**BASE_LAYOUT)
    layout["barmode"] = "stack"
    layout["xaxis"]   = dict(BASE_LAYOUT["xaxis"], title="Year")
    layout["yaxis"]   = dict(BASE_LAYOUT["yaxis"], title="CO₂ Emissions (Mt)")
    layout["height"]  = 360
    fig.update_layout(**layout)
    return fig


# ══════════════════════════════════════════════════════════════════════════════
# CHART 6 — Pie: global share
# ══════════════════════════════════════════════════════════════════════════════
@app.callback(
    Output("chart-6", "figure"),
    Input("compare-countries", "value"),
    Input("year-slider", "value"),
)
def chart6(compare, yr):
    latest_yr = yr[1]
    all_c     = list(set((compare or []) + ["Iran", "India"]))

    total_world_row = world[world["Year"] == latest_yr]["Total CO2 Emissions (Mt)"]
    wv = float(total_world_row.values[0]) if not total_world_row.empty else 38598.0

    rows        = []
    shown_total = 0.0
    palette     = [C_RED, C_GREEN, "#e8a020", "#7c5cbf", "#17a2b8",
                   "#fd7e14", "#6610f2", "#20c997", "#e83e8c"]

    for c in all_c:
        sub = df_no_world[(df_no_world["Country"] == c) & (df_no_world["Year"] == latest_yr)]
        if sub.empty:
            sub = df_no_world[df_no_world["Country"] == c].sort_values("Year").tail(1)
        if not sub.empty:
            v = sub["Total CO2 Emissions (Mt)"].values[0]
            if pd.notna(v):
                rows.append({"Country": c, "CO2": float(v)})
                shown_total += float(v)

    rows.append({"Country": "Rest of World", "CO2": max(wv - shown_total, 0)})
    d = pd.DataFrame(rows)

    colors = []
    for idx, c in enumerate(d["Country"]):
        if c == "Iran":           colors.append(C_RED)
        elif c == "India":        colors.append(C_GREEN)
        elif c == "Rest of World": colors.append("#d0c8b8")
        else:                      colors.append(palette[idx % len(palette)])

    fig = go.Figure(go.Pie(
        labels=d["Country"].values, values=d["CO2"].values,
        marker=dict(colors=colors, line=dict(color="white", width=1.5)),
        hole=0.42,
        hovertemplate="%{label}: %{value:.1f} Mt (%{percent})<extra></extra>",
        textinfo="percent+label",
        textfont=dict(size=10, color=C_DARK_TEXT),
    ))

    layout = dict(**BASE_LAYOUT)
    layout["showlegend"] = False
    layout["annotations"] = [dict(
        text=str(latest_yr), x=0.5, y=0.5,
        font=dict(size=16, color=C_GREEN, family="Inter, Arial"),
        showarrow=False,
    )]
    layout["height"] = 360
    fig.update_layout(**layout)
    return fig


# ══════════════════════════════════════════════════════════════════════════════
# PNG DOWNLOAD CALLBACKS  (server-side via kaleido; graceful fallback)
# ══════════════════════════════════════════════════════════════════════════════
def make_dl_callback(chart_id, dl_id, btn_id):
    @app.callback(
        Output(dl_id, "data"),
        Input(btn_id, "n_clicks"),
        State(chart_id, "figure"),
        prevent_initial_call=True,
    )
    def _dl(n_clicks, fig_data):
        if not fig_data or not n_clicks:
            return dash.no_update
        try:
            import plotly.io as pio
            fig = go.Figure(fig_data)
            img_bytes = pio.to_image(fig, format="png", width=1200, height=500, scale=2)
            return dcc.send_bytes(img_bytes, filename=f"{chart_id}.png")
        except Exception:
            # kaleido not available — send SVG instead
            try:
                import plotly.io as pio
                fig = go.Figure(fig_data)
                svg_str = pio.to_image(fig, format="svg").decode("utf-8")
                encoded = base64.b64encode(svg_str.encode()).decode()
                return dict(
                    content=encoded, filename=f"{chart_id}.svg",
                    type="image/svg+xml", base64=True
                )
            except Exception:
                return dash.no_update

for i in range(1, 7):
    make_dl_callback(f"chart-{i}", f"download-{i}", f"btn-dl-{i}")


# ══════════════════════════════════════════════════════════════════════════════
# RUN
# ══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("\n" + "="*60)
    print("  IRAN CO₂ DASHBOARD — TISS Mumbai")
    print("  Student: Novid Salhot | M2024BSASS019")
    print("  Data: Our World in Data (OWID)")
    print("="*60)
    print("\n  ▶  Open your browser at: http://127.0.0.1:8050")
    print("  ▶  Press Ctrl+C to stop\n")
    app.run(debug=False, host="0.0.0.0", port=10000)
