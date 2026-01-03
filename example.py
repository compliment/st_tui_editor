import streamlit as st
from st_tui_editor import st_tui_editor

st.set_page_config(page_title="Toast UI Editor Demo", layout="wide")
st.title("Toast UI Editor Component")

st.markdown("""
This component wraps the [Toast UI Editor](https://ui.toast.com/tui-editor).
Edit the markdown below and click the **Save** icon (💾) in the toolbar (far right) to update the Streamlit state.
""")

initial_value = """
![image](https://uicdn.toast.com/toastui/img/tui-editor-bi.png)

# Awesome Editor!

It has been _released as opensource in 2018_ and has ~~continually~~ evolved to **receive 10k GitHub ⭐️ Stars**.

## Create Instance

```python
result = st_tui_editor(
    initial_value=initial_markdown,
    key="md-editor",
)
```

> See the table below for default options
> > More API information can be found in the document

| name | type | description |
| --- | --- | --- |
| el | `HTMLElement` | container element |

## Features

* CommonMark + GFM Specifications
   * Live Preview
   * Scroll Sync
   * Auto Indent
   * Syntax Highlight
        1. Markdown
        2. Preview

See original project at: https://ui.toast.com/tui-editor

"""

# The component returns the current state dictionary.
# Initially, it returns the 'default' value defined in __init__.py.
# When saved, it returns the update from the frontend.

st.sidebar.header("Editor Config")
st.sidebar.caption("These changes reruns the component, editor content will be lost.")
height = st.sidebar.text_input("Height", value="600px")
preview_style = st.sidebar.selectbox(
    "Preview Style", options=["vertical", "tab"], index=0
)
initial_edit_type = st.sidebar.selectbox(
    "Initial Edit Type", options=["markdown", "wysiwyg"], index=0
)
theme = st.sidebar.selectbox("Theme", options=["light", "dark"], index=0)
usage_statistics = st.sidebar.checkbox("Enable Usage Statistics", value=True)

value = st_tui_editor(
    initial_value=initial_value,
    key="editor",
    height=height,
    preview_style=preview_style,
    initial_edit_type=initial_edit_type,
    theme=theme if theme != "light" else None,
    usage_statistics=usage_statistics,
)

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Component Return Value")
    st.json(value)

with col2:
    st.subheader("Rendered Output")
    if value:
        # Structure is consistent: {'content': {'markdown': '...'}}
        content = ""
        if "content" in value and "markdown" in value["content"]:
            content = value["content"]["markdown"]

        st.markdown(content)
