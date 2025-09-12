import { useState } from "react";
import api from "../services/api";
import MDEditor from "@uiw/react-md-editor";
import "../css/NoteEditor.css"

export default function NoteEditor({ fetchNotes }) {
  const [content, setContent] = useState("");

  const createNote = async () => {
    try {
      await api.post("/notes/", { content });
      setContent("");
      fetchNotes();
    } catch (err) {
      alert("Failed to create note");
      console.error(err);
    }
  };

  return (
    <div className="note-editor">
      <h3>New Note</h3>

      <MDEditor value={content} onChange={setContent} />

      <div className="preview">
        <h4>Preview:</h4>
        <MDEditor.Markdown source={content} />
      </div>

      <button onClick={createNote}>Add Note</button>
    </div>
  );
}