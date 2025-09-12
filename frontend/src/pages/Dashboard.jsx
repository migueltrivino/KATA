import { useEffect, useState } from "react";
import api from "../services/api";
import Header from "../components/Header"
import NoteEditor from "../components/NoteEditor";
import NoteList from "../components/NoteList";
import { removeToken } from "../utils/auth";
import { useNavigate } from "react-router-dom";

export default function Dashboard() {
  const [notes, setNotes] = useState([]);
  const navigate = useNavigate();

  const fetchNotes = async () => {
    try {
      const res = await api.get("/notes/");
      setNotes(res.data);
    } catch (err) {
      console.log(err);
      removeToken();
      navigate("/login");
    }
  };

  useEffect(() => {
    fetchNotes();
  }, []);

  return (
    <div>
      <Header/>
      <h1>Dashboard</h1>
      <NoteEditor fetchNotes={fetchNotes} />
      <NoteList notes={notes} fetchNotes={fetchNotes} />
    </div>
  );
}