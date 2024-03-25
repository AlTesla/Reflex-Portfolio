import reflex as rx
from reflex_simpleicons import simpleicons


def sidebar_header() -> rx.Component:
    return rx.flex(
        rx.box(simpleicons("GitHub",brand_color=True, size=24)),
        rx.heading("AlTeslaDev"),
        spacing="2"
    )



def sidebar() -> rx.Component:
    return rx.vstack(
        sidebar_header(),
        position="fixed",
        height="100%",
        left="0px",
        top="0px",
        z_index="5",
        padding_x="2em",
        padding_y="1em",
        background_color="lightgray",
        align_items="left",
        width="250px",
    )

