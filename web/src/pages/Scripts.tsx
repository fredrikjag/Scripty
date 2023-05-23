import { ReactElement, useEffect, useState } from 'react';
import Script from '../components/Script';
import styles from '../assets/styles/scripts.module.css';
import buttonStyles from '../assets/styles/buttons.module.css';
import { useNavigate  } from 'react-router-dom'
import axios from 'axios';

type ScriptProps = {
  script_id: string,
  name: string, 
  description: string,
  scheduled: string,
  created: string ,
  modified: string | undefined,
  last_used: string | undefined,
  version: string
}

const Scripts = (): ReactElement => {

  const [ScriptList, setScriptList] = useState<ScriptProps[]>([]);
  const navigate = useNavigate()

  const API_URL = 'http://127.0.0.1:5000/api/v1/d/script';
  const accessToken = localStorage.getItem('accessToken');
  axios.defaults.headers.common['Authorization'] = `Bearer ${accessToken}`;

  useEffect(() => {
    const getScripts = async () => {
      try {
        const response = await axios.get(API_URL);
        if (response.status !== 200) {
          navigate('/')
        }
        const listItems = response.data.scripts;
          if (Array.isArray(listItems)) {
            setScriptList(listItems);
          } else {
            console.error('Invalid response data:', response.data);
            setScriptList([]);
          }
      } catch (error) {
        //console.error('Error:', error);
      }
    };

    getScripts();
  }, []);

  return (
    <>
      <div className={styles.head}>
        <h2>Scripts</h2>
      </div>
      <div className={styles['table-header']}>
        <div className={styles['table-header-object']}>
          <p>Name</p>
        </div>
        <div className={styles['table-header-object']}>
          <p>Description</p>
        </div>
        <div className={styles['table-header-object']}>
          <p>Scheduled</p>
        </div>
        <div className={styles['table-header-object']}>
          <p>Created</p>
        </div>
        <div className={styles['table-header-object']}>
          <p>Modified</p>
        </div>
        <div className={styles['table-header-object']}>
          <p>Last used</p>
        </div>
        <div className={styles['table-header-object']}>
          <p>Version</p>
        </div>
        <div className={styles['table-header-object']}>
          <div className={buttonStyles['action-subtile-button']} onClick={() => navigate("/scripts/create")}>
            <span>Add</span>
          </div>
        </div>
      </div>
      {ScriptList && ScriptList.map((script) => {
          return (
            <li key={script.script_id}>
              <Script
                id={script.script_id}
                name={script.name}
                description={script.description}
                scheduled={script.scheduled}
                created={script.created}
                modified={script.modified}
                last_used={script.last_used}
                version={script.version}
              />
            </li>
          );
        })}
    </>
  );
};

export default Scripts;
