import { ReactElement } from 'react'
import { Outlet } from 'react-router-dom'
import styles from '../assets/styles/content.module.css'
import Console from './Console';

const Content = ():ReactElement => {
  return (
    <div className={styles["content-wrapper"]}> 
      <div className={styles.content}> 
        <Outlet />
      </div>
      <Console />
    </div>
  )
}

export default Content