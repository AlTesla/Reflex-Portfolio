import reflex as rx 
from dataPortfolio.components.sidebar import sidebar

class State(rx.State):
    pass 


def index() -> rx.Component:
    return rx.box(
        sidebar(),
    )

app = rx.App()
app.add_page(index)