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
            ),
            width="31.7em",
            height="10em",
        ),
        href=url,
        color_scheme="indigo",
        is_external=True    
    )
    
    
def items_view() -> rx.Component:
    return rx.flex(
        dashboard_item(
            "Belly Button Biodiversity ",
            "The Belly Button Biodiversity project focuses on \
             exploring the fascinating world of bacterial \
             species residing in human navels",
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
        dashboard_item(
            "VBA Stock Market",
            "Stock market data analysis using visual basic \
             scripts on microsoft excel",
            "github",
            "https://github.com/AlTesla/VBA-challenge",
            "dotnet"    
        ),
        dashboard_item(
            "EmployeeSQL",
            "This repository contains a comprehensive employee database", 
            "github",
            "https://github.com/AlTesla/sql-challenge",
            "postgresql"
        ),
        dashboard_item(
            "Pymaceutical",
            "Analysis of different cancer treatment on mice", 
            "github",
            "https://github.com/AlTesla/Matplotlib-challenge",
            "jupyter"
        ),
        width="100%", 
        flex_wrap="wrap",
        spacing="2", 
        justify="between"
    ),

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
        items_view(),
        
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