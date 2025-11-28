import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/data")
      .then(res => setData(res.data.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h1>React + FastAPI Full-Stack</h1>
      <p>Data from backend: {data ? data.join(", ") : "Loading..."}</p>
    </div>
  );
}

export default App;
