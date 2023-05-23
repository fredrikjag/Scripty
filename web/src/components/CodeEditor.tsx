import Editor from "@monaco-editor/react";


const CodeEditor = () => {
  const code = `function add(a, b) {
    return a + b;
  }
  
  const a = 123;
  function add(a, b) {
    return a + b;
  }
  
  const a = 123;
  function add(a, b) {
    return a + b;
  }
  
  const a = 123;
  function add(a, b) {
    return a + b;
  }
  
  const a = 123;
  function add(a, b) {
    return a + b;
  }
  
  const a = 123;
  function add(a, b) {
    return a + b;
  }
  
  const a = 123;
  function add(a, b) {
    return a + b;
  }
  
  const a = 123;`;

  return (
    <Editor
    height="40vh"
    defaultLanguage="javascript"
    defaultValue={code}
    options={{readOnly: true, domReadOnly: true, minimap: { enabled: false }, contextmenu: false}}
    
  />    
  )
}

export default CodeEditor