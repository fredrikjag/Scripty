import { ReactElement } from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faLightbulb, faBell } from '@fortawesome/free-regular-svg-icons'
import { faCaretDown, faMagnifyingGlass, faUserCircle, faArrowRightFromBracket, faUserPen} from '@fortawesome/free-solid-svg-icons'
import site_logo from '../assets/Images/Logo_v.1.4.svg'
import styles from '../assets/styles/header.module.css'
import { useNavigate } from 'react-router-dom'

type HeadingProps = {
    firstName: string, 
    userimage?: string,
}

const Header = ({firstName, userimage}: HeadingProps): ReactElement => {

    const navigate = useNavigate();
    const navigateHome = () => {
        navigate('/dashboard');
    };

  return (
    <header className={ styles.header }>
        <div className={ styles.logo } onClick={navigateHome}>
            <img src={ site_logo } alt="Logo" />
            <h2>Scripty</h2>
        </div>
        <div className={ styles.searchbox }>
            <input type="text" placeholder="Search..." />
            <FontAwesomeIcon icon={ faMagnifyingGlass } />
        </div>
        <div className={ styles["common-actions"] }>
            <div className={ styles.darkmode }>
            <FontAwesomeIcon icon={faLightbulb} />
            </div>
            <div className={styles.notifications}>
                <FontAwesomeIcon icon={ faBell } />
            </div>
        </div>
        <div className={styles.user}>
            <div className={ styles["user-details"] }>
                {userimage ? (<img src={ userimage }></img>) : (
                    <FontAwesomeIcon icon={faUserCircle} size="2xl"/> 
                    )}
                <span className={ styles["user-name"] }>{ firstName }</span>
                <FontAwesomeIcon icon={ faCaretDown } size="2xs"/>
                <div className={ styles["user-actions"] }>
                <ul>
                    <li><FontAwesomeIcon icon={faUserPen} style={{color: "#484b94", width: "20px"}} /><a href="#"> Edit Profile </a></li>
                    <li><FontAwesomeIcon icon={faArrowRightFromBracket} style={{color: "#484b94", width: "20px"}} /><a href="#"> Sign Out </a></li>
                </ul>
                </div>
            </div>
        </div>
    </header>
  )
}

export default Header