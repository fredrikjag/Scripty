import buttonStyles from '../assets/styles/buttons.module.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faCirclePlus } from '@fortawesome/free-solid-svg-icons'
import styles from '../assets/styles/create_script.module.css'


const CreateScript = () => {
  return (
    <>
        <div className={styles.title}>
            <h2>Create Script</h2>
        </div>
        <div className={styles.details}>
            <div className={styles["details-title"]}>
                <h4>Details</h4>
                <div className={styles["details-buttons"]}>
                    <div className={buttonStyles['action-subtile-button']}>
                        <span>Cancel</span>
                    </div>
                    <div className={buttonStyles['action-button']}>
                        <span>Save</span>
                    </div>
                </div>
            </div>
        </div>

        <div className={styles.arguments}>
            <div className={styles["arguments-title"]}>
                <h4>Arguments</h4>
                <FontAwesomeIcon icon={faCirclePlus} size="xl" style={{color: "#9FA1D9",}} onClick={() => console.log("test")}/>
            </div>
        </div>

        <div className={styles["script-view"]}>
        </div>
    </>
  )
}

export default CreateScript