import NoteItem from "./NoteItem";
import "../css/NoteList.css"

export default function NoteList({ notes, fetchNotes }) {
  return (
    <div className="note-list">
      {notes.map(note => (
        <NoteItem 
          key={note._id}   
          note={note} 
          fetchNotes={fetchNotes} 
        />
      ))}
    </div>
  );
}