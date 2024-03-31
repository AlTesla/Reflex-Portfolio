import reflex as rx
from dataPortfolio.components.sidebar import sidebar



path = "https://github.com/ACRivera95/project-3.1/blob/main/Output/Pokemon_data.json"



@rx.page(route="/pokedata", title="Pokedata")
def pokedata() -> rx.Component:
    return rx.hstack(
        sidebar(),
        rx.vstack(
            rx.heading("Pokedata Visulization", as_="h1", size="9", align="center", width="1600px")
        )
    )
