import React from "react";
import Reactdom from "react-dom";
import Home from "./home.jsx";

const mont = Reactdom.createRoot(document.getElementById("main"));
mont.render(<Home></Home>);
