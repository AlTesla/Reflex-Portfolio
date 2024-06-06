import reflex as rx
from reflex_simpleicons import simpleicons
from dataPortfolio.components.sidebar import sidebar
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

@rx.page(route="/steam", title="Steam")
def steam() -> rx.Component:
    return rx.hstack(
        sidebar(),
    )