import React, { useState, useEffect } from 'react'
/* React Hooks
    only usable within function components, cannot use within class components (now somewhat obsolete)
    have to be called in the same order every time - aka NO conditionals, functions, or loops
      can only be at top level of functional component

*/

// useState - allows for the maintaining of state, and a corresponding update function
// useEffect - similar to an "onAction" function, allows for additional effects after something is changed


function App() {
  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch("/members").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])

  return (
    <div>
      App

      {(typeof data.members === 'undefined') ? (
        <p>Loading... </p>
      ) : (
        data.members.map((member, i) => (
          <p key={i}>
            {member}
          </p> 
        ))
      )}

    </div>
  )
}

export default App
