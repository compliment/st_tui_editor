import streamlit as st

out = st.components.v2.component(
    "streamlit-component-x.st_tui_editor",
    js="index-*.js",
    css="index-*.css",
    html='<div class="react-root"></div>',
)


def on_content_change():
    """Callback for content changes."""
    pass


def st_tui_editor(
    initial_value="",
    height="600px",
    min_height="300px",
    preview_style="vertical",
    initial_edit_type="markdown",
    language="en-US",
    use_command_shortcut=True,
    usage_statistics=False,
    toolbar_items=None,
    hide_mode_switch=False,
    viewer=False,
    placeholder="",
    autofocus=True,
    extended_autolinks=True,
    link_attributes=None,
    reference_definition=False,
    front_matter=False,
    preview_highlight=True,
    theme=None,
    key=None,
    **options,
):
    """Create a new instance of "st_tui_editor" (Toast UI Editor).



    Parameters

    ----------

    initial_value: str

        The initial markdown content to display in the editor.

    height: str

        Editor height, e.g. '600px', 'auto'.

    min_height: str

        Editor minimum height.

    preview_style: str

        Preview style: 'tab' or 'vertical'.

    initial_edit_type: str

        Initial edit type: 'markdown' or 'wysiwyg'.

    language: str

        Language code (e.g., 'en-US', 'ko-KR').

    use_command_shortcut: bool

        Whether to use keyboard shortcuts.

    usage_statistics: bool

        Whether to send usage statistics to Google Analytics.

    toolbar_items: list or None

        Custom toolbar items.

    hide_mode_switch: bool

        Whether to hide the mode switch tab.

    viewer: bool

        Whether to use viewer mode.

    placeholder: str

        Placeholder text.

    autofocus: bool

        Whether to autofocus on initialization.

    extended_autolinks: bool

        Whether to use extended autolinks.

    link_attributes: dict or None

        Attributes for links.

    reference_definition: bool

        Whether to use reference definition.

    front_matter: bool

        Whether to use front matter.

    preview_highlight: bool

        Whether to highlight the preview.

    theme: str or None

        Theme name (e.g. 'dark').

    key: str or None

        An optional key that uniquely identifies this component.

    **options:

        Any additional options to pass to the TUI Editor.

        Snake_case keys will be converted to camelCase.



    Returns

    -------

    dict

        A dictionary containing the markdown content, e.g. {"content": {"markdown": "..."}}.

    """

    # Collect all parameters into data dict

    data = {
        "initialValue": initial_value,
        "height": height,
        "minHeight": min_height,
        "previewStyle": preview_style,
        "initialEditType": initial_edit_type,
        "language": language,
        "useCommandShortcut": use_command_shortcut,
        "usageStatistics": usage_statistics,
        "toolbarItems": toolbar_items,
        "hideModeSwitch": hide_mode_switch,
        "viewer": viewer,
        "placeholder": placeholder,
        "autofocus": autofocus,
        "extendedAutolinks": extended_autolinks,
        "linkAttributes": link_attributes,
        "referenceDefinition": reference_definition,
        "frontMatter": front_matter,
        "previewHighlight": preview_highlight,
        "theme": theme,
    }

    # Add extra options and convert keys to camelCase

    for k, v in options.items():
        parts = k.split("_")

        camel_key = parts[0] + "".join(x.title() for x in parts[1:])

        data[camel_key] = v

    # Filter out None values

    data = {k: v for k, v in data.items() if v is not None}

    component_value = out(
        key=key,
        default={"content": {"markdown": initial_value}},
        data=data,
        on_content_change=on_content_change,
    )

    return component_value

    component_value = out(
        key=key,
        default={"content": {"markdown": initial_value}},
        data=data,
        on_content_change=on_content_change,
    )

    return component_value
