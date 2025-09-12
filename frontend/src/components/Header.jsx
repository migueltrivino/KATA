import { useNavigate } from "react-router-dom";
import { removeToken } from "../utils/auth";
import "../css/Header.css"

export default function Header() {
  const navigate = useNavigate();

  const handleLogout = () => {
    removeToken();
    navigate("/login");
  };

  return (
    <header className="header">
      <h1>NotasApp</h1>
      <nav>
        <button onClick={handleLogout}>Logout</button>
      </nav>
    </header>
  );
}