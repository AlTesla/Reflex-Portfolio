
import reflex as rx
from reflex_simpleicons import simpleicons
from dataPortfolio.components.sidebar import sidebar
import pandas as pd

#region State
path = "https://mydatabucket-altesla.s3.us-west-1.amazonaws.com/Pokemon_data.csv"
poke_frame = pd.read_csv(path)
poke_frame = poke_frame.drop("Unnamed: 0", axis=1)
gens = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th']

class PokeState(rx.State):
    gen = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th']
    selected_gen: str ='4th'

    @rx.var
    def gen_df(self) -> pd.DataFrame:
        pk_df = poke_frame[poke_frame["Generation"] == self.selected_gen].copy()
        return pk_df

    """
    @rx.var
    def max_row(self) -> pd.DataFrame:
        strongest_row = self.gen_df.loc[self.gen_df['Total'].idxmax()].to_frame().T
        #strongest_row = self.gen_df[self.gen_df['Total'] == self.gen_df['Total'].max()]
        return strongest_row
    """    
    @rx.var
    def max_name(self) -> str:
        strongest_row = self.gen_df.loc[self.gen_df['Total'].idxmax()].to_frame().T
        strongest_name = strongest_row['Name'].squeeze()
        return strongest_name
    
    @rx.var
    def max_image(self) -> str:
        strongest_row = self.gen_df.loc[self.gen_df['Total'].idxmax()].to_frame().T
        strongest_image = strongest_row["ImageUrl"].squeeze()
        return strongest_image

# region views

def gen_selector() -> rx.Component:
    return rx.card(
        rx.flex(
            simpleicons(tag="pokémon", brand_color=True, size= 128),
            rx.select(
                gens, 
                placeholder=gens[0],
                label="Generation",
                on_change=PokeState.set_selected_gen,
                value=PokeState.selected_gen,
                width="8em"
                ),
            direction='column',
            align='center'
        )
    )
    

def strongest() -> rx.Component:
    return rx.card(
        rx.heading("Strongest"),
        rx.text(PokeState.max_name),
        rx.image(src=PokeState.max_image, width = "12em", height="auto")    
    )


@rx.page(route="/pokedata", title="Pokedata")
def pokedata() -> rx.Component:
    return rx.box(
        rx.hstack(
            sidebar(),
            rx.vstack(
                rx.section(
                    rx.heading("Pokedata Visulization", as_="h1", size="9", align="center"),
                ),
                rx.hstack(
                    rx.spacer(), 
                    rx.box(
                        gen_selector(),
                        width="15em",
                        height="auto"

                    ),
                    strongest(),
                ),
                width=""

            )
        ), 
        width="80em"
    )