import reflex as rx
from reflex_simpleicons import simpleicons
from dataPortfolio.components.sidebar import sidebar
import pandas as pd


path = "https://mydatabucket-altesla.s3.us-west-1.amazonaws.com/Pokemon_data.csv"
poke_frame = pd.read_csv(path)


class PokeState(rx.State):
    gens: list[str] = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th']
    selected_gen: str = '1st'



def gen_selector() -> rx.Component:
    return rx.card(
        rx.flex(
            simpleicons(tag="pokémon", brand_color=True, size= 128),
            rx.select(PokeState.gens, 
                placeholder=PokeState.gens[0],
                label="Generation",
                on_change=PokeState.set_selected_gen,
                value=PokeState.selected_gen,
                ),
            direction='column'
        )
    )
    

def strongest() -> rx.Component:
    chosen_gen= [f"{PokeState.selected_gen}"]
    gen_df = poke_frame[poke_frame['Generation'] == chosen_gen[0]]
    #gen_df = poke_frame[poke_frame['Generation'].isin(chosen_gen)]
    #strongest_row = gen_df.loc[gen_df['Total'].idxmax()]
    #strongest_name = strongest_row['Name']
    return rx.box(
        rx.text(chosen_gen[0]),
        rx.data_table(data=gen_df[["Name", "Total", "Generation"]])
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

            ),
            rx.text(PokeState.selected_gen.to_string()),
            strongest()
        )
    )
