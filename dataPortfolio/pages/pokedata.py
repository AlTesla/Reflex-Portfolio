import reflex as rx
from reflex_simpleicons import simpleicons
from dataPortfolio.components.sidebar import sidebar
import pandas as pd


path = "https://mydatabucket-altesla.s3.us-west-1.amazonaws.com/Pokemon_data.csv"
poke_frame = pd.read_csv(path)
gens = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th']

class PokeState(rx.State):
    selected_gen: str = '1st'

    @rx.var
    def gen_df(self) -> pd.DataFrame:
        pk_df = poke_frame[poke_frame["Generation"] == self.selected_gen]
        return pk_df


    @rx.var
    def max_row(self) -> str:
        strongest_row = self.gen_df.loc[self.gen_df['Total'].idxmax()]
        return strongest_row
    
    @rx.var
    def max_name(self) -> str:
        strongest_name =self.max_row['Name']
        return strongest_name
    
    @rx.var
    def max_image(self) -> str:
        strongest_image = self.max_row["ImageUrl"]
        return strongest_image



def gen_selector() -> rx.Component:
    return rx.card(
        rx.flex(
            simpleicons(tag="pokémon", brand_color=True, size= 128),
            rx.select(gens, 
                placeholder=gens[0],
                label="Generation",
                on_change=PokeState.set_selected_gen,
                value=PokeState.selected_gen,
                ),
            direction='column'
        )
    )
    

def strongest() -> rx.Component:
    return rx.box(
        rx.text(PokeState.max_name),
        
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
