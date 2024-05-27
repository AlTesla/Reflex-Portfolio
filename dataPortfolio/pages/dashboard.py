import reflex as rx
from dataPortfolio.components.sidebar import sidebar 

def dashboard_content() -> rx.Component:
    return rx.vstack(
        rx.card(
            rx.heading(
                "Dashboard",
                size="9"
                align="center"
            )
        )
    )

@rx.page(route="/dashboard", title="Dashboard")
def dashboard() -> rx.Component:
    return rx.hstack(
        sidebar(),

    )