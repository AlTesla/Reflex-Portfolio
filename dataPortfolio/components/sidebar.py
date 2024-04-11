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
                            href="/pokedata",
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
    return rx.box(
        rx.vstack(
            sidebar_header(),
            rx.divider(),
            rx.vstack(
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
                sidebar_menu(),
            ),
            rx.divider(),
            rx.spacer(),
            sidebar_footer(),
            height="100dvh"

        ),
        align_items="left",
        min_width="15em",
        height="100%",
        position="sticky",
        top="",
        border_right="1px solid #F4F3F6",
    )

