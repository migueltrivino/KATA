import { useState } from "react";
import api from "../services/api";
import MDEditor from "@uiw/react-md-editor";
import "../css/NoteItem.css";

export default function NoteItem({ note, fetchNotes }) {
  const [isEditing, setIsEditing] = useState(false);
  const [content, setContent] = useState(note.content);

  const deleteNote = async () => {
    try {
      await api.delete(`/notes/${note._id}`);
      fetchNotes();
    } catch (err) {
      alert("Failed to delete note");
      console.error(err);
    }
  };

  const updateNote = async () => {
    try {
      await api.put(`/notes/${note._id}`, { content });
      setIsEditing(false);
      fetchNotes();
    } catch (err) {
      alert("Failed to update note");
      console.error(err);
    }
  };

  return (
    <div className="note-item" data-color-mode="light">
      {isEditing ? (
        <>
          <MDEditor value={content} onChange={setContent} />
          
          <div className="preview">
            <h3>Vista previa:</h3>
            <MDEditor.Markdown source={content} />
          </div>

          <div className="note-item-buttons">
            <button onClick={updateNote}>Guardar</button>
            <button onClick={() => setIsEditing(false)}>Cancelar</button>
          </div>
        </>
      ) : (
        <>
          <MDEditor.Markdown source={note.content} className="preview" />

          <div className="note-item-buttons">
            <button onClick={() => setIsEditing(true)}>Editar</button>
            <button onClick={deleteNote}>Borrar</button>
          </div>
        </>
      )}
    </div>
  );
}