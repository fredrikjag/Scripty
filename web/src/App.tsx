import Heading from "./components/Heading"
import SideNav from "./components/SideNav"
import styles from "./assets/styles/app.module.css"
import Content from "./components/Content"



function App() {
  return (
    <div className='App'>
      <Heading firstName="Fredrik" />
      <main className={ styles.main }>

        <SideNav />
        <Content />
      </main>


   </div>
    

  )
}

export default App
