
import './App.css'
import get from './api/get'
function App() {
  

  const testGet = async ()=>{
    const resp = await get("/api/user-profile/1")
    console.log(resp)
  }

  return (
    <>
     <button onClick={()=>testGet()}>Get User Profile</button>
   
    </>
  )
}

export default App
