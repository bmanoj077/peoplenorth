import React, { useEffect, useState } from "react";
import axios from "axios";

const TreeView = () => {
  const [employees, setEmployees] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/employees/")
      .then((response) => {
        console.log("API Response:", response.data); // Log the response to check the data structure
        setEmployees(response.data);
      })
      .catch((error) => console.error("Error fetching employees:", error));
  }, []);
  

  const renderTree = (node) => {
    if (!node) return null;
    return (
      <div style={{ marginLeft: 20 }} key={node.id}>
        <strong>{node.name}</strong>
        {node.children && node.children.length > 0 && (
          <ul>
            {node.children.map((child) => (
              <li key={child.id}>{renderTree(child)}</li>
            ))}
          </ul>
        )}
      </div>
    );
  };

  return (
    <div>
      <h2>Organization Chart</h2>
      {employees.length === 0 ? <p>Loading...</p> : employees.map(renderTree)}
    </div>
  );
};

export default TreeView;
