import reflex as rx
from reflex_simpleicons import simpleicons


def sidebar_header() -> rx.Component:
    return rx.flex(
        rx.box(simpleicons("GitHub",brand_color=True, size=24)),
        rx.heading("AlTeslaDev"),
        spacing="2",
        padding_bottom="1em"
        
    )


def sidebar_item(text: str, ico: str, url: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(ico),
            rx.text(text, weight='bold'),
        ),
        href=url,
        color_scheme='gray'
    )

def sidebar_menu() -> rx.Component:
    return rx.hstack(
        rx.chakra.accordion(
            rx.chakra.accordion_item(
                rx.chakra.accordion_button(
                    rx.hstack(
                        rx.icon("layers", color_scheme="gray"),
                        rx.text("Projects", weight="bold", color_scheme="gray"),
                    ),
                        
                    rx.chakra.accordion_icon(),
                    padding_left="0"
                ),
                rx.chakra.accordion_panel(
                    rx.vstack(
                        rx.link(
                            rx.text("Pokedata"),
                            href="/",
                            color_scheme="gray"

                        )
                    )
                ),
            ),
            rx.chakra.accordion_item(
                rx.chakra.accordion_button(
                    rx.hstack(
                        rx.icon("history", color_scheme="gray"),
                        rx.text("Recent", weight="bold", color_scheme="gray"),   
                    ),
                    rx.chakra.accordion_icon(),
                    padding_left="0"
                ),
                rx.chakra.accordion_panel(
                    rx.chakra.text(
                    "This is an example of an accordion component."
                   )
                ),
            ),
        )
    )


def sidebar_footer() -> rx.Component:
    return rx.vstack(
        rx.link(
            rx.hstack(
                rx.icon("github"),
                rx.text("GitHub", weight='bold'),
            ), 
            href="https://github.com/AlTesla",
            color_scheme='gray',
            is_external=True
        ),
        rx.link(
            rx.hstack(
                rx.icon("linkedin"),
                rx.text("LinkedIn", weight="bold"),
            ),
            href="https://www.linkedin.com/in/alvaro-corona/",
            color_scheme='gray',
            is_external=True
        )
    )



def sidebar() -> rx.Component:
    return rx.vstack(
        sidebar_header(),
        rx.divider(),
        sidebar_item(
            "Welcome", 
            "home",
            "/"
        ),
        sidebar_item(
            "Dashboard", 
            "bar-chart-3",
            "/"
        ),
        sidebar_item(
            "Contact", 
            "mail",
            "/"
        ),
        rx.divider(),
        sidebar_menu(),

        sidebar_footer(),

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

