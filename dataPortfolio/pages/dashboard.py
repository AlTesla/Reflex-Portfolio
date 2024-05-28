import reflex as rx
from dataPortfolio.components.sidebar import sidebar
from reflex_simpleicons import simpleicons 

def dashboard_item(heading:str ,text: str, ico: str, url: str, lang: str) -> rx.Component:
    return rx.link(
        rx.card(
            rx.vstack(
                rx.hstack(
                    rx.icon(ico),
                    rx.heading(heading)
                ),
                rx.text(text),
                rx.hstack(
                    simpleicons(lang, size=16),
                    rx.text(lang)
                )
            )
            
        ),
        href=url,
        color_scheme="gray",
        is_external=True    
    )


def dashboard_content() -> rx.Component:
    return rx.vstack(
        rx.card(
            rx.heading(
                "Dashboard",
                size="9",
                align="center"
            ),
            width="100%"
        ),
        dashboard_item(
            "belly-button-challenge",
            "Challenge assigment for Data Analytics Bootcamp",
            "github",
            "https://github.com/AlTesla/belly-button-challenge",
            "JavaScript"    
        ),
        dashboard_item(
            "Crowndfunding _ETL",
            "Challenge assigment for Data Analytics Bootcamp",
            "github",
            "https://github.com/estefaniamm99/Crowdfunding_ETL",
            "Python"
        ),
        width="64em"
    )

@rx.page(route="/dashboard", title="Dashboard")
def dashboard() -> rx.Component:    
    return rx.vstack(
        rx.hstack(
            sidebar(),
            dashboard_content(),
        ),
        align_items="center"
    )