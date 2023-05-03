import { ReactElement } from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faChevronUp } from '@fortawesome/free-solid-svg-icons'
import styles from '../assets/styles/console.module.css'


const Console = ():ReactElement => {
  return (
    <div className={styles.console}>
        <p>Completed </p>
        <FontAwesomeIcon icon={faChevronUp} />
    </div>
  )
}

export default Console