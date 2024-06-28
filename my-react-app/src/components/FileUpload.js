import React, { useState } from 'react';

const FileUpload = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [summary, setSummary] = useState("");
  const [error, setError] = useState("");

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleFileUpload = async () => {
    if (!selectedFile) {
      setError("No file selected");
      return;
    }

    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
      const res = await fetch('http://127.0.0.1:5000/upload', {
        method: 'POST',
        body: formData
      });
      if (res.ok) {
        const data = await res.json();
        setSummary(data.message);  // Assuming the backend returns the summary in `message`
        setError("");
      } else {
        throw new Error('Error uploading file');
      }
    } catch (error) {
      console.error('Error uploading file:', error);
      setError("Error uploading file");
    }
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', marginTop: '50px' }}>
      <h2>Sube una imagen de un manuscrito para generar un resumen</h2>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleFileUpload} style={{ marginTop: '20px' }}>Subir y resumir</button>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <div style={{ width: '50%', marginTop: '20px' }}>
        <h3>Resumen:</h3>
        <textarea 
          value={summary} 
          readOnly 
          rows="10" 
          style={{ width: '100%', padding: '10px', fontSize: '16px' }}
        />
      </div>
    </div>
  );
};

export default FileUpload;
