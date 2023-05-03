import React from 'react'

const LoginForm = () => {
  return (
    <>
      <div className="content">
        <form method="post" action="/">
        <div className="login-box">
            <h1>Telia Cygate Bonusgenerator</h1>
            <div className="input-container">
                <input type="text" placeholder="Username" name="username" autoComplete='off' required />
            </div>
            <div className="input-container">
                <input type="password" placeholder="Password" name="password" required />
            </div>
            <div className="button-container">
                <div className="button-content">
                    <input type="submit" value="Sign in"/>
                </div>
            </div>
        </div>
        </form>
    </div>
    </>
  )
}

export default LoginForm