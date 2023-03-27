import React from "react";
import Reactdom from "react-dom/client";
import Home from "./home.jsx";
import { createBrowserRouter, Link, RouterProvider } from "react-router-dom";

import "../src/css/main.css";

const BASEPATH = "/test";

const router = createBrowserRouter([
  { path: `${BASEPATH}/`, element: <Home></Home> },
  { path: `${BASEPATH}/item`, element: <p>qwe</p> },
]);

const UserInfo = function ({ info }) {
  return (
    <div>
      <img src={info.photo}></img>
      <div>
        <span>{info.name}</span>
        <div>
          <button></button>
        </div>
      </div>
    </div>
  );
};

const LoginForm = function ({ callback }) {
  const [id, setid] = React.useState("");
  const [pwd, setPwd] = React.useState("");

  const handle_login = () => {
    fetch("/Loginadmin", {
      method: "POST",
      headers: {
        "content-type": "application/json",
      },
      body: JSON.stringify({
        student_id: id,
        password: pwd,
      }),
    })
      .then((Response) => {
        if (Response.ok) {
          console.log("login success!");
          return Response.json();
        }
        return Promise.reject(Response.json());
      })
      .catch((e) => {
        console.log(e);
      })
      .then((json) => {
        if (json.status === 0) callback(json);
      });
  };

  return (
    <div className={`page_cover`}>
      <div className={`login_form`}>
        <span className={`login_col_text`}>學號</span>
        <input
          type={`text`}
          onInput={(event) => {
            setid(event.target.value);
          }}
        />
        <span className={`login_col_text`}>密碼</span>
        <input
          type={`password`}
          onInput={(e) => {
            setPwd(e.target.value);
          }}
        />
        <div className={`login_btn_container`}>
          <button className={`login_btn`} onClick={handle_login}>
            登入
          </button>
        </div>
      </div>
    </div>
  );
};

const NavBar = function ({ userInfo, items }) {
  return (
    <div className={`side_bar`}>
      <UserInfo info={userInfo}></UserInfo>
      <div className={`nav_options`}>
        <Link></Link>
        {/*<Link to={"test/item"}>配件</Link>*/}
      </div>
    </div>
  );
};

const Main = function () {
  const [user_info, setInfo] = React.useState({});
  const [isLogin, setLogin] = React.useState(false);

  React.useEffect(() => {
    fetch("/getUserInfo", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({}),
    })
      .then((Response) => {
        if (Response.ok) {
          setLogin(true);
          return Response.json();
        }
        return Promise.reject(Response.json());
      })
      .catch((error) => {
        console.log(error);
        return { name: "unknow", photo: "" };
      })
      .then((json) => {
        console.log(json);
        setInfo(json);
      });
  }, [isLogin]);

  let main_content = (
    <div className={`main`}>
      <NavBar userInfo={user_info}></NavBar>
      <div>
        <RouterProvider router={router}></RouterProvider>
      </div>
    </div>
  );

  return isLogin ? (
    main_content
  ) : (
    <LoginForm
      callback={(json) => {
        if (json !== undefined) {
          setLogin(true);
        }
      }}
    ></LoginForm>
  );
};

const mont = Reactdom.createRoot(document.getElementById("main"));
mont.render(<Main></Main>);
