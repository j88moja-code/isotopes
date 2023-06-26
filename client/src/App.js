import './App.css';
import {BrowserRouter, Route, Routes} from 'react-router-dom';
import Home from "./pages/Home";
import Login from "./pages/public/Login";
import Register from "./pages/public/Register";

function App() {
  return (
    <BrowserRouter forceRefresh>
        <Routes>
            {/* PROTECTED ROUTES  */}
            <Route path="/" element={<Home />} />

            {/* END PROTECTED ROUTES  */}
            <Route path="login" element={<Login />} />
            <Route path="register" element={<Register />} />
        </Routes>
    </BrowserRouter>
  );
}

export default App;
