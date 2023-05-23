import buttonStyles from '../assets/styles/buttons.module.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faCirclePlus } from '@fortawesome/free-solid-svg-icons'
import styles from '../assets/styles/create_script.module.css'
import { useNavigate  } from 'react-router-dom'
import { useRef, useState } from 'react';
import FileUpload from '../components/FileUpload';
import axios from 'axios';
import CodeEditor from '../components/CodeEditor';

const CreateScript = () => {

    const navigate = useNavigate()

    const [name, setName] = useState('');
    const [description, setDescription] = useState('');
    const [version, setVersion] = useState('');
    const [schedule, setSchedule] = useState('');
    const [repeat, setRepeat] = useState('');
    const [repeatTimebased, setRepeatTimebased] = useState('');
    
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
        <div className={styles["details-title"]}>
                <h4>Details</h4>
            </div>
        <div className={styles.details}>
            <form className={styles['details-form']}>
                <input type="text" value={name} placeholder="Name"  style={{ color: name ? 'black' : '#b0b0b0' }} onChange={(e) => setName(e.target.value)}/>
                <input type="text" value={description} placeholder="Description"  style={{ color: description ? 'black' : '#b0b0b0' }} onChange={(e) => setDescription(e.target.value)}/>
                <input type="datetime-local" value={schedule} placeholder="Schedule" style={{ color: schedule ? 'black' : '#b0b0b0' }} onChange={(e) => setSchedule(e.target.value)}/>
                or <input type="text" value={repeatTimebased} placeholder="Repeat timebased (e.g 60 minutes)"  style={{ color: repeatTimebased ? 'black' : '#b0b0b0' }} onChange={(e) => setRepeatTimebased(e.target.value)}/>
                <input type="text" value={repeat} placeholder="Repeat (Times)"  style={{ color: repeat ? 'black' : '#b0b0b0' }} onChange={(e) => setRepeat(e.target.value)}/>
            </form>
        </div>

        <div className={styles["arguments-title"]}>
            <h4>Arguments</h4>
            <FontAwesomeIcon icon={faCirclePlus} size="xl" onClick={() => console.log("test")}/>
        </div>
        <div className={styles.arguments}>
        
        </div>

        <div className={styles["script-view"]}>
            <FileUpload />

            <CodeEditor />
        </div>

    </>
)   
}

export default CreateScript