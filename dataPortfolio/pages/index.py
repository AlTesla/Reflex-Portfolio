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
        rx.avatar(src="/avatar.jpeg", size="9", radius='full'),
        rx.vstack(
            rx.text("Alvaro Corona", weight="bold", size="4"),
            rx.text("I am an Aerospace Engineer and Data Analyst", color_scheme="gray")
        )
    )


def landing() -> rx.Component:
    return rx.box(
        rx.vstack(
            cover_image(),
            rx.hstack(
                avatar(),
                rx.spacer(),
                rx.button("...", color_scheme="gray"),
                rx.button(
                    "LinkedIn",
                    rx.icon("linkedin"),
                    color_scheme="gray"
                ),
                rx.button(
                    "GitHub",
                    rx.icon("github"),
                    color_scheme="gray"
                ),
                width="64em"            
            ),
            rx.heading("About me", as_="h2"),
            rx.text("""
                    As an aerospace engineer, I specialized in technology development, 
                    particularly within the drone (RPA) industry. This innovative field 
                    motivated me to continuously learn and stay ahead of the curve. 
                    Initially, my focus was on product design, but in recent years, 
                    I’ve delved into data engineering and software development, discovering 
                    new passions along the way.
                    """, color_scheme="gray")
        )
    )


def summary() -> rx.Component:
    return rx.box(    
        rx.vstack(
            rx.heading("Experience", as_="h2"),
            rx.text(
                """I'm an Aerospace Engineer and Data Analyst based in Tijuana, Mexico. 
                I enjoy working on technology development and Data visualization projects.
                I ocacionally take on freelance work."""
            ),
            rx.text(
                """ I've worked with some of the latinamerican's most exiting companies 
                including Total Play and LP Bond. I'm passionate about helping startups grow, 
                collaborate in their research and development dipartment, and to substantiate
                through analytical and mathematical knowledge."""
            ),
            rx.text(
                """My work work has been featured on Tijuana Innovadora, 
                Baja Aerospace Expo, and Edx career engagement network."""
            ),
        ),
        width="40%"    
    )


def skills_links() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.vstack(
                rx.heading("Skills", as_="h2"),
                rx.flex(
                    rx.card("Data Viz"),
                    rx.card("Data Integration"),
                    rx.card("3d Modeling"), 
                    rx.card("3d Printing"),
                    spacing='4'
                )
            ),
            rx.vstack(
                rx.fragment(
                    rx.heading("Location", as_="h3", size="4"),
                    rx.text("Tijuana, Baja California")
                ),
                rx.fragment(
                    rx.heading("GitHub", as_="h3", size="4"),
                    rx.text("AlTesla")
                ),
                rx.fragment(
                    rx.heading("Linked In", as_="h3", size="4"),
                    rx.text("alvaro-corona")
                )
            ),
        )

    )


def experience() -> rx.Component:
    return rx.flex(
        rx.card(
            rx.vstack(
                rx.hstack(
                    rx.icon("rocket"),
                    rx.heading("Product Desing Engineer", as_="h3", size="4")
                    ),
                rx.text("LP Bond"),
                spacing='2'
            )
        ),
        rx.spacer(),
        rx.card(
            rx.vstack(
                rx.hstack(
                    rx.icon("satellite-dish"),
                    rx.heading("Quality Inspector", as_="h3", size="4")
                ),
                rx.text("Total Play"),
                spacing='2'
            )
        ),
        rx.spacer(),
        rx.card(
            rx.vstack(
                rx.hstack(
                    rx.icon("cog"),
                    rx.heading("Maintenance Manager", as_="h3", size="4")
                ),
                rx.text("Soriana"),
                spacing='2'
            )
            
        ),
        width="100%",
        padding="2em"
    )


@rx.page(route="/index", title="Landing")
def index() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            sidebar(),
            rx.vstack(
                landing(),
                rx.divider(),
                rx.hstack(
                    summary(),
                    rx.spacer(),
                    skills_links(),
                    padding="2em"
                ),
                experience(),
                max_width="64em"
            ),
            width="80em",
        ),
        align_items="center"
    )