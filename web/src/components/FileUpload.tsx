import{ ChangeEvent } from 'react';
import axios from 'axios';
import buttonStyles from '../assets/styles/buttons.module.css';

const FileUpload = () => {
  const handleFileChange = (event: ChangeEvent<HTMLInputElement>) => {

    const file = event.target.files && event.target.files[0];
    if (file) {
      uploadFile(file);
    }
  };

  const uploadFile = async (file: File) => {
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post(
        'http://127.0.0.1:5000/api/v1/d/script/upload',
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        }
      );

      console.log('File uploaded successfully');
      console.log('Response:', response.data);
    } catch (error) {
      console.error('File upload error:', error);
      // Handle error
    }
  };

  return (
    <div className={buttonStyles["upload-file-wrapper"]}>
      <p>Drag and drop</p>
      <p>or</p>
      <label htmlFor="file-upload" className={buttonStyles["primary-upload"]}>
        Choose File
        <input type="file" id="file-upload" onChange={handleFileChange} />
      </label>
    </div>
  );
};

export default FileUpload;
