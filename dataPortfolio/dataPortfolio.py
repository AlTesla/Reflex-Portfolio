import reflex as rx 

class State(rx.State):
    pass 

def index() -> rx.Component:
    return rx.text("hola Reflex!")

def sidebar():
    return rx.vstack(
        rx.heading("Home", margin_bottom="1em")
    )

app = rx.App()
app.add_page(index)
app.add_page(sidebar)
app.compile()