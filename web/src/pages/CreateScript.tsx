import buttonStyles from '../assets/styles/buttons.module.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faCirclePlus } from '@fortawesome/free-solid-svg-icons'
import styles from '../assets/styles/create_script.module.css'
import { useNavigate  } from 'react-router-dom'
import React, { useState } from 'react';

const CreateScript = () => {

    const navigate = useNavigate()

    const [name, setName] = useState('');
    const [description, setDescription] = useState('');
    const [version, setVersion] = useState('');
    const [schedule, setSchedule] = useState('');
    const [repeat, setRepeat] = useState('');

    return (
    <>
        <div className={styles.title}>
            <h2>Create Script</h2>
            <div className={styles["details-buttons"]}>
                <div className={buttonStyles['action-subtile-button']}  onClick={() => navigate("/scripts")}>
                    <span>Cancel</span>
                </div>
                <div className={buttonStyles['action-button']}>
                    <span>Save</span>
                </div>
            </div>
        </div>
        <div className={styles.details}>
            <div className={styles["details-title"]}>
                <h4>Details</h4>
            </div>
            <form className={styles['details-form']}>
                <input type="text" value={name} placeholder="Name"  style={{ color: name ? 'black' : '#b0b0b0' }} onChange={(e) => setName(e.target.value)}/>
                <input type="text" value={description} placeholder="Description"  style={{ color: description ? 'black' : '#b0b0b0' }} onChange={(e) => setDescription(e.target.value)}/>
                <input type="text" value={version} placeholder="Version"  style={{ color: version ? 'black' : '#b0b0b0' }} onChange={(e) => setVersion(e.target.value)}/>
                <input type="text" value={schedule} placeholder="Schedule"  style={{ color: schedule ? 'black' : '#b0b0b0' }} onChange={(e) => setSchedule(e.target.value)}/>
                <input type="text" value={repeat} placeholder="Repeat (Times)"  style={{ color: repeat ? 'black' : '#b0b0b0' }} onChange={(e) => setRepeat(e.target.value)}/>
            </form>
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