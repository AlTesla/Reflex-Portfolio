
import reflex as rx
from reflex_simpleicons import simpleicons
from dataPortfolio.components.sidebar import sidebar
import pandas as pd
import plotly.express as px
import numpy as np


#region State
path = "https://mydatabucket-altesla.s3.us-west-1.amazonaws.com/Pokemon_data.csv"
poke_frame = pd.read_csv(path)
poke_frame = poke_frame.drop("Unnamed: 0", axis=1)
gens = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th']

class PokeState(rx.State):
    gen = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th']
    selected_gen: str ='1st'
    key_list = ["HP","Attack","Defense", "SpAtk", "SpDef", "Speed"]
    data_columns = ['ID', 'Name', 'Total', 'HP', 'Attack', 'Defense', 'SpAtk', 'SpDef',
                    'Speed', 'Type1', 'Type2', 'Height', 'Weight', 'ImageUrl','Generation']
    
    
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

    @rx.var
    def min_name(self)->str:
        weakest_row = self.gen_df.loc[self.gen_df['Total'].idxmin()].to_frame().T
        weakest_name = weakest_row['Name'].squeeze()
        return weakest_name
    
    @rx.var
    def min_image(self)->str:
        weakest_row = self.gen_df.loc[self.gen_df['Total'].idxmin()].to_frame().T
        weakest_image = weakest_row['ImageUrl'].squeeze()
        return weakest_image
    """     
    @rx.var
    def poke_keys(self) -> list:
        key_list = ["HP","Attack","Defense", "SpAtk", "SpDef", "Speed"]
        return key_list
    """
    @rx.var
    def max_values(self) -> list:
        strongest_row = self.gen_df.loc[self.gen_df['Total'].idxmax()].to_frame().T
        strongest_row = strongest_row[["HP","Attack","Defense", "SpAtk", "SpDef", "Speed"]]
        max_values_list = [2,3,2,4,5,1]
        return max_values_list        
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
        rx.hstack(
            rx.vstack(
                rx.heading("Strongest"),
                rx.text(PokeState.max_name),
                rx.image(src=PokeState.max_image, width = "12em", height="auto"),
            ),
             max_radar()
        ),
        width = "60em"
    )


def weakest() -> rx.Component:
    return rx.card(
        rx.heading("Weakest"),
        rx.text(PokeState.min_name),
        rx.image(src=PokeState.min_image, width="12em", height="auto")
    )


def max_radar() -> rx.Component:
    fig = px.line_polar(r=[106, 90, 130, 90, 154, 110],
                        theta=["HP","Attack","Defense", "SpAtk", "SpDef", "Speed"],
                        line_close=True)
    return rx.plotly(data=fig, height="10em", width="10em")


def pokedata_content() -> rx.Component:
    return rx.vstack(
        rx.section(
            rx.heading("Pokedata Visulization",
                       as_="h1", 
                       size="9", 
                       align="center"),
            width="100%"
        ),
        rx.hstack(
            rx.spacer(), 
            rx.box(
                gen_selector(),
                width="15em",
                height="auto"
            ),
            rx.vstack(
                strongest(),
                weakest(),
            )
        ),
        width="64em"
    )
    
    

@rx.page(route="/pokedata", title="Pokedata")
def pokedata() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            sidebar(),
            pokedata_content(),
        ),
        align_items="center"
    )