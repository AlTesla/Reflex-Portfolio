import reflex as rx
from reflex_simpleicons import simpleicons
from dataPortfolio.components.sidebar import sidebar
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import styles.styles as style


# region Data Frame
path = "https://mydatabucket-altesla.s3.us-west-1.amazonaws.com/steam.csv"
steam_frame = pd.read_csv(path)
steam_frame = steam_frame.drop("Unnamed: 0", axis=1)

# region State
class steamState(rx.State):
    
    @rx.var
    def st_df(self) -> pd.DataFrame:
        st_df = steam_frame
        return st_df

def steam_text() -> rx.Component:
    return rx.text(
        "this an exploratory data analysis of Steam games"
    )


def steam_content() -> rx.Component:
    return rx.vstack(
        rx.heading("Steam EDA"),
        rx.text("This an exploratory data analysis of Steam games"),
        width= "64em"
    )

@rx.page(route="/steam", title="Steam")
def steam() -> rx.Component:
    return rx.hstack(
        sidebar(),
        steam_content(),
    )