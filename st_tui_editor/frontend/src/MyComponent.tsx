import { ComponentArgs } from "@streamlit/component-v2-lib";
import {
  FC,
  ReactElement,
  useEffect,
  useRef,
  useMemo,
  useCallback,
} from "react";
import "@toast-ui/editor/dist/toastui-editor.css";
import "@toast-ui/editor/dist/theme/toastui-editor-dark.css";
import { Editor, Viewer } from "@toast-ui/react-editor";

export type MyComponentStateShape = {
  content: { markdown: string };
};

export type MyComponentDataShape = {
  initialValue?: string;
  height?: string;
  minHeight?: string;
  previewStyle?: "tab" | "vertical";
  initialEditType?: "markdown" | "wysiwyg";
  language?: string;
  useCommandShortcut?: boolean;
  usageStatistics?: boolean;
  toolbarItems?: any[];
  hideModeSwitch?: boolean;
  viewer?: boolean;
  placeholder?: string;
  autofocus?: boolean;
  extendedAutolinks?: boolean;
  linkAttributes?: Record<string, string>;
  referenceDefinition?: boolean;
  frontMatter?: boolean;
  previewHighlight?: boolean;
  theme?: string;
  // Catch all for any other props
  [key: string]: any;
};

export type MyComponentProps = Pick<
  ComponentArgs<MyComponentStateShape, MyComponentDataShape>,
  "setStateValue"
> &
  MyComponentDataShape;

const MyComponent: FC<MyComponentProps> = ({
  initialValue,
  setStateValue,
  viewer,
  ...editorProps
}): ReactElement => {
  const editorRef = useRef<Editor>(null);
  const latestSetStateValue = useRef(setStateValue);

  // Update ref when setStateValue changes
  useEffect(() => {
    latestSetStateValue.current = setStateValue;
  }, [setStateValue]);

  // Force re-mount when these props change
  const componentKey = useMemo(() => {
    return `${editorProps.theme || "light"}-${editorProps.initialEditType || "markdown"}`;
  }, [editorProps.theme, editorProps.initialEditType]);

  useEffect(() => {
    if (!viewer && editorRef.current) {
      const instance = editorRef.current.getInstance();

      const createSaveButton = (currentTheme: "light" | "dark") => {
        const button = document.createElement("button");
        button.className = "toastui-editor-toolbar-icons save";
        button.style.backgroundImage = "none";
        button.style.margin = "0";
        button.style.display = "flex";
        button.style.alignItems = "center";
        button.style.justifyContent = "center";

        // Set color based on theme
        button.style.color = currentTheme === "dark" ? "#d5d5d5" : "#333";

        button.innerHTML = `
          <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 16 16" width="20" height="20">
            <path d="M14 3a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1zM2 2a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2z"/>
            <path fill-rule="evenodd" d="M9.146 8.146a.5.5 0 0 1 .708 0L11.5 9.793l1.646-1.647a.5.5 0 0 1 .708.708l-2 2a.5.5 0 0 1-.708 0l-2-2a.5.5 0 0 1 0-.708"/>
            <path fill-rule="evenodd" d="M11.5 5a.5.5 0 0 1 .5.5v4a.5.5 0 0 1-1 0v-4a.5.5 0 0 1 .5-.5"/>
            <path d="M3.56 11V7.01h.056l1.428 3.239h.774l1.42-3.24h.056V11h1.073V5.001h-1.2l-1.71 3.894h-.039l-1.71-3.894H2.5V11z"/>
          </svg>
        `;

        return button;
      };

      const saveButtonEl = createSaveButton(
        (editorProps.theme as "light" | "dark") || "light",
      );

      // Define the save function
      saveButtonEl.onclick = () => {
        const markdown = instance.getMarkdown();
        latestSetStateValue.current("content", { markdown });
      };
      // Add the button to the toolbar.
      instance.insertToolbarItem(
        { groupIndex: 5, itemIndex: 0 },
        {
          name: "save",
          el: saveButtonEl,
          tooltip: "Save Markdown",
        },
      );
    }
  }, [componentKey, viewer]);

  if (viewer) {
    return (
      <Viewer
        key={`viewer-${componentKey}`}
        initialValue={initialValue || " "}
        {...editorProps}
      />
    );
  }

  return (
    <Editor
      key={`editor-${componentKey}`}
      initialValue={initialValue || " "}
      ref={editorRef}
      {...editorProps}
    />
  );
};

export default MyComponent;
