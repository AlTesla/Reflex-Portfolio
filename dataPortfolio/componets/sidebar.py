import reflex as rx

def sidebar() -> rx.Component:
    return rx.vstack(
        rx.image(src="/favicon.ico", width="3em"),
        rx.heading("AlTeslaDev", margin_bottom="1em"),
        rx.text("first item"),
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

