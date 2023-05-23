import Content from "./components/Content"
import { Routes, Route } from "react-router-dom"
import Dashboard from "./pages/Dashboard"
import Scripts from "./pages/Scripts"
import Pipelines from "./pages/Pipelines"
import History from "./pages/History"
import Users from "./pages/Users"
import CreateScript from "./pages/CreateScript"
import LoginPage from "./pages/LoginPage"
import ProtectedPages from "./pages/ProtectedPages"


function App() {
  return (
    
  //   <div className='App'>
  //     <Heading firstName="Fredrik" />
  //     <main className={ styles.main }>
  //       <SideNav />
  //       <Content />
  //     </main>
  //  </div>

    <Routes>
      <Route index element={<LoginPage />} />
      <Route path="/" element={<ProtectedPages />}>
        <Route path='/dashboard' element={<Dashboard />} />
        <Route path='/scripts' element={<Scripts />} />
        <Route path='/pipelines' element={<Pipelines />} />
        <Route path='/history' element={<History />} />
        <Route path='/users' element={<Users />} />
        <Route path='/scripts/create' element={<CreateScript />} />
      </Route>
    </Routes>
  )
}

export default App
