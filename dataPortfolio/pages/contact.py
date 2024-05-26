import reflex as rx

class EditorState(rx.State):
    content:str = "<p>Editor content</p>"




@rx.page(route="/contact", title="Contact")
def contact() -> rx.Component:
    return