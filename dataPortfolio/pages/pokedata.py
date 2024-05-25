
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
        
    @rx.var    
    def min_radar(self) -> go.Figure:
        skill_names = self.key_list
        values = []
        weakest_row = self.gen_df.loc[self.gen_df['Total'].idxmin()].to_frame().T
        
        for skill in skill_names :
            skill_value = weakest_row[skill].squeeze()
            values.append(int(skill_value))
            
        df = pd.DataFrame({"Skill": skill_names, "Value": values})
        return px.line_polar(df, 
                            r= "Value", 
                            theta= "Skill",
                            line_close=True,
                            )
        
    @rx.var
    def gen_histogram(self) -> go.Figure:
        df= self.gen_df
        return px.histogram(df, x="Total", color="Type1", hover_name="Name")
    
    @rx.var
    def gen_scatter(self) -> go.Figure:
        df= self.gen_df
        return px.scatter(df, x="Total", color="Type1", hover_name="Name")


    
# region views
def gen_selector() -> rx.Component:
    return rx.card(
        rx.flex(
            simpleicons(tag="pokémon", brand_color=True, size= 256),
            rx.select(
                gens, 
                placeholder=gens[0],
                label="Generation",
                on_change=PokeState.set_selected_gen,
                value=PokeState.selected_gen,
                width="8em"
            ),
            direction='column',
            align_items="center"
        ),
        width="64em",
    )
    

def strongest() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading("Strongest"),
            rx.text(PokeState.max_name),
            rx.image(src=PokeState.max_image, width = "12em", height="auto"),
            rx.plotly(data=PokeState.max_radar, layout={"width":"auto", "height":"8em"}),
            align_items="center"
        ),
        width="31.7em"
    )


def weakest() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading("Weakest"),
            rx.text(PokeState.min_name),
            rx.image(src=PokeState.min_image, width="12em", height="auto"),
            rx.plotly(data=PokeState.min_radar, layout={"width":"auto", "height":"8em"}),
            align_items="center"
        ),
        width="31.7em"
    )
    
    
def histo_gen() -> rx.Component:
    return rx.card(
        rx.plotly(data=PokeState.gen_histogram, layout={"width":960, "height":"auto"}),
        width="64em",
        align_items="center"
    )


def scatter_gen() -> rx.Component:
    return rx.card(
        rx.plotly(data=PokeState.gen_scatter, layout={"width":960, "height":"auto"}),
        width="64em",
        align_items="center"
    )


def pokedata_content() -> rx.Component:
    return rx.vstack(
        rx.vstack( 
            gen_selector(),    
            rx.hstack(
                weakest(),
                strongest(), 
            ),
            histo_gen(),
            scatter_gen(),
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