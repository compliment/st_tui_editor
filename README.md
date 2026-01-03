# st-tui-editor

A Streamlit component that integrates the powerful [Toast UI Editor](https://ui.toast.com/tui-editor), a Markdown editor that provides both Markdown and WYSIWYG editing modes.

![TUI Editor in Streamlit](https://uicdn.toast.com/toastui/img/tui-editor-bi.png)

See demo at: https://toastui-markdown-editor.streamlit.app
## Features

- **Dual Modes**: Support for both Markdown and WYSIWYG editing.
- **Live Preview**: Real-time rendering of Markdown content.
- **Theming**: Built-in support for Light and Dark themes.
- **Customization**: Configurable height, preview style (vertical/tab), and more.
- **Streamlit Integration**: 
  - Integrated "Save" toolbar button to sync content back to Streamlit.
  - Returns the edited markdown as a JSON object.

## Installation

Install via pip:

```sh
pip install st-tui-editor
```

## Usage

Here's a simple example of how to use `st-tui-editor` in your Streamlit app:

```python
import streamlit as st
from st_tui_editor import st_tui_editor

st.title("Streamlit TUI Editor")

# Initialize with some default text
initial_text = """
# Hello Streamlit!
This is the **Toast UI Editor** component.
"""

# Render the editor
output = st_tui_editor(
    initial_value=initial_text,
    height="600px",
    initial_edit_type="markdown",
    theme="dark",
    key="my_editor"
)

# Access the value
if output:
    st.write("### Output Preview")
    st.markdown(output.get("markdown"))
    
    st.write("### Raw JSON")
    st.json(output)
```

## API Reference

### `st_tui_editor`

```python
st_tui_editor(
    initial_value="",
    height="500px",
    initial_edit_type="markdown",
    preview_style="vertical",
    theme="light",
    usage_statistics=True,
    key=None
)
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `initial_value` | `str` | `""` | The initial markdown content to display in the editor. |
| `height` | `str` | `"500px"` | The CSS height of the editor (e.g., `"600px"`, `"auto"`). |
| `initial_edit_type` | `str` | `"markdown"` | The initial editing mode. Options: `"markdown"` or `"wysiwyg"`. |
| `preview_style` | `str` | `"vertical"` | The preview style for Markdown mode. Options: `"vertical"` (side-by-side) or `"tab"`. |
| `theme` | `str` | `"light"` | The UI theme. Options: `"light"` or `"dark"`. |
| `usage_statistics` | `bool` | `True` | Whether to send hostname to Google Analytics (TUI Editor default behavior). |
| `key` | `str` | `None` | An optional key that uniquely identifies this component instance. |

### Return Value

The component returns a dictionary (JSON) containing the editor's state.

```json
{
  "markdown": "The content of the editor..."
}
```

The content is updated when the user clicks the **Save** icon in the toolbar.

## Development

If you want to contribute or modify the component locally:

1. **Clone the repository**
2. **Install Python dependencies** (in editable mode):
   ```sh
   pip install -e .
   ```
3. **Build the frontend**:
   ```sh
   cd st_tui_editor/frontend
   npm install
   npm run build
   ```
4. **Run the example**:
   ```sh
   streamlit run example.py
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
