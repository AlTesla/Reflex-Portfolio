import reflex as rx
from reflex_simpleicons import simpleicons
from dataPortfolio.components.sidebar import sidebar
import pandas as pd


path = "https://mydatabucket-altesla.s3.us-west-1.amazonaws.com/Pokemon_data.csv"


def dataframe():
    poke_frame = pd.read_csv(path)
    return poke_frame


def gen_selector() -> rx.Component:
    poke_gen = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th']
    return rx.card(
        rx.flex(
            simpleicons(tag="pokémon", brand_color=True, size= 128),
            rx.select(poke_gen, 
                placeholder="Selection of Generation",
                label="Generation",
                ),
            direction='column'
        )
    )
    


@rx.page(route="/pokedata", title="Pokedata")
def pokedata() -> rx.Component:
    return rx.hstack(
        sidebar(),
        rx.vstack(
            rx.heading("Pokedata Visulization", as_="h1", size="9", align="center", width="1600px"),
            rx.spacer(), 
            rx.box(
                gen_selector(),
                width="15em",
                height="15em"

            )
        )
    )
