import reflex as rx
from dataPortfolio.components.sidebar import sidebar
import pandas as pd



path = "https://mydatabucket-altesla.s3.us-west-1.amazonaws.com/Pokemon_data.csv"


def dataframe():
    poke_frame = pd.read_csv(path)
    return poke_frame


@rx.page(route="/pokedata", title="Pokedata")
def pokedata() -> rx.Component:
    return rx.hstack(
        sidebar(),
        rx.vstack(
            rx.heading("Pokedata Visulization", as_="h1", size="9", align="center", width="1600px"),
            rx.spacer(), 
            rx.box(
                rx.data_table(
                    data = dataframe()[["Name"]],
                    search = True,
                    )
                ),
                width="15em",
                height="5em"

            )
    )
