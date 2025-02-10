import React, { useEffect, useState } from "react";
import TreeView from "./components/TreeView";

const App = () => {
  const [treeData, setTreeData] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/tree/")  // Django API endpoint
      .then((response) => response.json())
      .then((data) => setTreeData(data))
      .catch((error) => console.error("Error fetching data:", error));
  }, []);

  return (
    <div>
      <h1>Organization Chart</h1>
      <TreeView data={treeData} />
    </div>
  );
};

export default App;
