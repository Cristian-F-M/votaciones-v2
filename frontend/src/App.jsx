// import { BrowserRouter } from "react-router-dom";
import { Route, BrowserRouter, NavLink, Link, Routes } from "react-router-dom";
import { Home } from "@/pages/Home";
import { Login } from "@/pages/Login";
import { Register } from "@/pages/Register";
import { NotFound } from "@/pages/404";
import { Dashboard } from "@/pages/Dashboard";
import { Header } from "@/components/Header";

function App() {
    return (
        <>
            <BrowserRouter>
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/Login" element={<Login />} />
                    <Route path="/Register" element={<Register />} />
                    <Route path="/Dashboard" element={<Dashboard />} />
                    <Route path="*" element={<NotFound />} />
                </Routes>
            </BrowserRouter>
        </>
    );
}

export default App;
