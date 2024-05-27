import reflex as rx
from dataPortfolio.components.sidebar import sidebar
# region State
class FormState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
    
    
class EditorState(rx.State):
    content:str = "<p>Editor content</p>"
    
    def handle_change(self, content: str):
        self.content = content

# region views
def form_example():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="First Name",
                    name="first_name",
                ),
                rx.input(
                    placeholder="Last Name",
                    name="last_name",
                ),
                rx.hstack(
                    rx.checkbox("Checked", name="check"),
                    rx.switch("Switched", name="switch"),
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=FormState.handle_submit,
            reset_on_submit=True,
        ),
        #rx.divider(),
        #rx.heading("Results"),
        #rx.text(FormState.form_data.to_string()),
    )

def editor_view() -> rx.Component:
    return rx.vstack(
        rx.editor(
            set_contents=EditorState.content,
            on_change=EditorState.handle_change,
        ),
        rx.box(
            rx.html(EditorState.content),
            border="1px dashed #ccc",
            border_radius="0.25em",
            width="100%",
        ),
    )
def why_contact() -> rx.Component:
    return rx.text(
        """
        Please feel free to leave a message, I promise to read it promptly 
        and provide feedback. Whether you’re curious about my data
         or engineering projects or just want to chat, I’m all ears!
         Let’s collaborate and make something awesome together.
        """
    )
def contanct_content() -> rx.Component:
    return rx.vstack(
        rx.card(
            rx.heading(
                "Contact me",
                size="9",
                align="center"
            ),
            why_contact(),
            width="64em",
            align_items="center"
        ),
        rx.card(
            form_example(),
            width="64em"    
        ),
        rx.card(
            editor_view(),
            width="64em"
        )
    )
    
# region Page 
@rx.page(route="/contact", title="Contact")
def contact() -> rx.Component:    
    return rx.vstack(
        rx.hstack(
            sidebar(),
            contanct_content(),
        ),
        align_items="center"
    )