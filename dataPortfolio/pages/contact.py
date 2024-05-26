import reflex as rx
# region State
class EditorState(rx.State):
    content:str = "<p>Editor content</p>"
    
    def handle_change(self, content: str):
        self.content = content

# region views

# region Page 
@rx.page(route="/contact", title="Contact")
def contact() -> rx.Component:    
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