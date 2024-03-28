import reflex as rx
from dataPortfolio.components.sidebar import sidebar


def cover_image() -> rx.Component:
    return rx.box(
        rx.image(
            src="/data_landing.png",
            width="auto"
        ),
        position="sticky"
    )
    

def avatar() -> rx.Component:
    return rx.flex(
        rx.avatar(fallback="Al", size="9"),
        rx.vstack(
            rx.text("Alvaro Corona", weight="bold", size="4"),
            rx.text("@AlTesla", color_scheme="gray")
        )
    )


def landing() -> rx.Component:
    return rx.vstack(
        cover_image(),
        avatar()
    )


@rx.page(route="/index", title="Home")
def index() -> rx.Component:
    return rx.hstack(
        sidebar(),
        landing()
            
        
    )