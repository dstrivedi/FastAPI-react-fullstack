import "./App.css";
import React, { useEffect, useState } from "react";

function App() {
  const [users, setUsers] = useState([]);
  const [form, setForm] = useState({ name: "", email: "", age: "" });

  useEffect(() => {
    getAllUsers()
  }, [])

  const getAllUsers = async() => {
    try {
      const response = await fetch("http://127.0.0.1:8000/users/");
      if (!response.ok) {
        throw Error("Network response was not OK.")
      } else {
        const data = await response.json();
        setUsers(data);
      }
    } catch (error) {
      console.error("Something went wrong", error)
    }
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch("http://127.0.0.1:8000/users/", {
      method: "POST",
      headers: { "Content-type": "application/json" },
      body: JSON.stringify(form),
    });
    if (response.ok) {
      setForm({ name: "", email: "", age: "" });
    } else {
      const errorData = await response.json();
      console.error("Error creating user:", errorData);
      alert("Failed to create User. See console for details")
    }
    getAllUsers();
  };

  const handleDelete = async (id) => {
    const response = await fetch(`http://127.0.0.1:8000/users/${id}`, {
      method: 'DELETE'
    });
    if (response.ok) {
      getAllUsers();
    } else {
      const errorData = await response.json();
      console.error("Error deleting user", errorData)
    }
  }

  return (
    <div className="App">
      <main className="App-header">
        <h1>Add User</h1>
        <form onSubmit={handleSubmit}>
          <div>
            <label htmlFor="name">Name: </label>
            <input
              placeholder="Enter Name"
              type="text"
              name="name"
              value={form.name}
              onChange={(e) => setForm({ ...form, name: e.target.value })}
            />
          </div>
          <div>
            <label htmlFor="email">Email: </label>
            <input
              type="email"
              placeholder="Enter Email"
              name="email"
              value={form.email}
              onChange={(e) => setForm({ ...form, email: e.target.value })}
            />
          </div>
          <div>
            <label htmlFor="age">Age: </label>
            <input
              type="number"
              name="age"
              placeholder="Enter Age"
              value={form.age}
              onChange={(e) => setForm({ ...form, age: e.target.value })}
            />
          </div>
          <button type="submit">Add</button>
        </form>
        <div className="user-list">
          <h2>All Users</h2>
          <ul>
            {users.map((user) => (
              <li key={user.id}>
                <div>
                  <strong>{user.name}</strong>
                  <div className="user-email">{user.email}</div>
                </div>
                <span>{user.age} yrs</span>
                <button className="delete-btn" onClick={() => handleDelete(user.id)}>❌</button>
              </li>
            ))}
          </ul>
        </div>
      </main>
    </div>
  );
}

export default App;
