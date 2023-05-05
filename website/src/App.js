import { BrowserRouter, Routes, Route } from "react-router-dom";
import UserpageComponent from "./components/userpage-component";
import NavBarComponent from "./components/navbar-component";
import NewuserComponent from "./components/newuser-component";


function App() {
  return (
    <div className="App">
      <NavBarComponent/>
      <BrowserRouter>
        <Routes>
          <Route exact path="/user1" element={<UserpageComponent />} />
          <Route exact path="/newuser" element={<NewuserComponent />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
