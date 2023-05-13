import { ReactElement } from 'react'
import { Routes, Route } from 'react-router-dom'
import styles from '../assets/styles/content.module.css'
import Console from './Console';
import Dashboard from '../pages/Dashboard'
import Scripts from '../pages/Scripts'
import History from '../pages/History'
import Users from '../pages/Users'
import Pipelines from '../pages/Pipelines';
import CreateScript from '../pages/CreateScript';


const Content = ():ReactElement => {
  return (
    <div className={styles["content-wrapper"]}> 
      <div className={styles.content}> 
        <Routes>
          <Route path='/dashboard' element={<Dashboard />} />
          <Route path='/scripts' element={<Scripts />} />
          <Route path='/pipelines' element={<Pipelines />} />
          <Route path='/history' element={<History />} />
          <Route path='/users' element={<Users />} />
          <Route path='/scripts/create' element={<CreateScript />} />
        </Routes> 
      </div>
      <Console />
    </div>
  )
}

export default Content