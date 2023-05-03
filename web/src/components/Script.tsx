import { ReactElement } from 'react'
import styles from '../assets/styles/script.module.css'
import buttonStyles from '../assets/styles/buttons.module.css'

type ScriptProps = {
  id: string,
  name: string, 
  description: string,
  scheduled: string,
  created: string ,
  modified: string | undefined,
  last_used: string | undefined,
  version: string
}


const Script = ({id, name, description, scheduled, created, modified, last_used, version}:ScriptProps):ReactElement => {
  return (
    <>
      <div className={styles["script-object"]}>
        <p>{name}</p>
        <p>{description}</p>
        <p>{scheduled || 'n/a'}</p>
        <p>{created}</p>
        <p>{modified || 'n/a'}</p>
        <p>{last_used || 'n/a'}</p>
        <p>{version}</p>
        <div className={styles["script-object-button-holder"]}>
          <div className={buttonStyles["action-button"]}><span>Execute</span></div>
          <div className={styles.edit}><p>Edit</p></div>
        </div>
      </div>
    </>
  )
}

export default Script