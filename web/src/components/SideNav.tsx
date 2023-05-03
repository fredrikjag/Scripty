import { ReactElement } from 'react'
import styles from '../assets/styles/sidenav.module.css'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faRepeat, faChartLine, faClockRotateLeft } from '@fortawesome/free-solid-svg-icons'
import { faFolderOpen, faUser } from '@fortawesome/free-regular-svg-icons'
import { Link } from 'react-router-dom'


const SideNav = ():ReactElement => {
  return (
    <nav className={styles["side-nav"]}>
        <ul>
            <li>
                <FontAwesomeIcon icon={faChartLine} style={{color: '#484b94'}}/>
                <Link className={styles.text} to="/dashboard">Dashboard</Link>
            </li>
            <li>
                <FontAwesomeIcon icon={faFolderOpen} style={{color: '#484b94'}}/>
                <Link className={styles.text} to="/scripts">Scripts</Link>
            </li>
            <li>
                <FontAwesomeIcon icon={faRepeat} style={{color: '#484b94'}}/>
                <Link className={styles.text} to="/pipelines">Pipelines</Link>
            </li>
            <li>
                <FontAwesomeIcon icon={faClockRotateLeft} style={{color: '#484b94'}}/>
                <Link className={styles.text} to="/history">History</Link>
            </li>
            <li>
                <FontAwesomeIcon icon={faUser} style={{color: '#484b94'}}/>
                <Link className={styles.text} to="/users">Users</Link>
            </li>
        </ul>  
    </nav>
  )
}

export default SideNav