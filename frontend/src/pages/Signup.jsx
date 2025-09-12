import { useState } from "react";
import api from "../services/api";
import { useNavigate } from "react-router-dom";
import "../css/Signup.css"

export default function Signup() {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleSignup = async () => {
  try {
    await api.post("/auth/signup", { username, email, password });
    alert("Usuario creado");
    navigate("/login");
  } catch (err) {
    if (err.response && err.response.data.detail) {
      alert(err.response.data.detail); 
    } else {
      alert("Signup failed");
    }
}
  };

  return (
    <div className="signup-container">
      <h2>Signup</h2>
      <input 
        placeholder="Username" 
        value={username} 
        onChange={(e) => setUsername(e.target.value)} 
      />
      <input 
        placeholder="Email" 
        value={email} 
        onChange={(e) => setEmail(e.target.value)} 
      />
      <input 
        type="password" 
        placeholder="Password" 
        value={password} 
        onChange={(e) => setPassword(e.target.value)} 
      />
      <button onClick={() => handleSignup(username, email, password)}>Signup</button>

      <p className="login-text">
        ¿Ya tienes cuenta?{" "}
        <span className="login-link" onClick={() => navigate("/login")}>
          Inicia sesión
        </span>
      </p>
    </div>
  );
}