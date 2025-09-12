import { useState } from "react";
import api from "../services/api";
import "../css/Login.css"
import { saveToken } from "../utils/auth";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleLogin = async () => {
    try {
      const res = await api.post("/auth/login", { username, password });
      saveToken(res.data.access_token);
      navigate("/dashboard");
    } catch (err) {
      alert("Login failed");
    }
  };

  return (
    <div className="login-container">
      <h2>Login</h2>
      <input 
        placeholder="Username" 
        value={username} 
        onChange={(e) => setUsername(e.target.value)} 
      />
      <input 
        type="password" 
        placeholder="Password" 
        value={password} 
        onChange={(e) => setPassword(e.target.value)} 
      />
      <button onClick={() => handleLogin(username, password)}>Login</button>
      <p className="signup-text">
        ¿No tienes cuenta?{" "}
        <span className="signup-link" onClick={() => navigate("/signup")}>
          Regístrate
        </span>
      </p>
    </div>
  );
}