
import reflex as rx
from reflex_simpleicons import simpleicons
from dataPortfolio.components.sidebar import sidebar
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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
    def min_name(self)-> str:
        weakest_row = self.gen_df.loc[self.gen_df['Total'].idxmin()].to_frame().T
        weakest_name = weakest_row['Name'].squeeze()
        return weakest_name
    
    @rx.var
    def min_image(self)-> str:
        weakest_row = self.gen_df.loc[self.gen_df['Total'].idxmin()].to_frame().T
        weakest_image = weakest_row['ImageUrl'].squeeze()
        return weakest_image
    
    @rx.var
    def max_radar(self) -> go.Figure:
        skill_names = self.key_list
        values = []
        strongest_row = self.gen_df.loc[self.gen_df['Total'].idxmax()].to_frame().T
        
        for skill in skill_names :
            skill_value = strongest_row[skill].squeeze()
            values.append(int(skill_value))
            
        df = pd.DataFrame({"Skill": skill_names, "Value": values})
        return px.line_polar(df, 
                            r= "Value", 
                            theta= "Skill",
                            line_close=True,
                            )
    
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
        rx.vstack(
            rx.heading("Strongest"),
            rx.text(PokeState.max_name),
            rx.image(src=PokeState.max_image, width = "12em", height="auto"),
        )
    )


def weakest() -> rx.Component:
    return rx.card(
        rx.heading("Weakest"),
        rx.text(PokeState.min_name),
        rx.image(src=PokeState.min_image, width="12em", height="auto")
    )


def strongest_radar() -> rx.Component:
    return rx.card(
        rx.plotly(data=PokeState.max_radar, layout={"width":"256", "height":"256"})
    )


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
                rx.hstack(
                    strongest(),
                    strongest_radar(),
                ),
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