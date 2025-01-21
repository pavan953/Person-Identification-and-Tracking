// import { Button } from '@mui/material'
// import axiosInstance from '../helper/axiosInstance';
// import { toast } from 'react-toastify';

// const Recognize = () => {

//   const handleStartRecognition = async () => {
//     const res = await axiosInstance.post('/start_recognition')
//     console.log(res);
//     if (res.data) {
//       toast.success('Recognition started successfully')
//     }
//     else {
//       toast.error('Recognition failed')
//     }
//   }
//   const handleStopRecognition = async () => {
//     const res = await axiosInstance.post('/stop_recognition')
//     console.log(res);
//     if (res.data) {
//       toast.success('Recognition stopped successfully')
//     }
//     else {
//       toast.error('Recognition failed')
//     }
//   }
//   return (
//     <div><Button variant="contained" onClick={handleStartRecognition}>Start Recognition</Button>
//       <Button variant='contained' onClick={handleStopRecognition}>Stop Recognition</Button></div>
//   )
// }

// export default Recognize

import { Button } from '@mui/material'
import Webcam from 'react-webcam'
import axiosInstance from '../helper/axiosInstance';
import { toast } from 'react-toastify';
import React, { useState } from 'react';

const Recognize = () => {
  const webcamRef = React.useRef(null);
  const [showCamera, setShowCamera] = useState(false);

  const videoConstraints = {
    width: 720,
    height: 480,
    facingMode: "user"
  };

  const handleStartRecognition = async () => {
    const res = await axiosInstance.post('/start_recognition')
    console.log(res);
    if (res.data) {
      setShowCamera(true);
      toast.success('Recognition started successfully')
    } else {
      toast.error('Recognition failed')
    }
  }

  const handleStopRecognition = async () => {
    const res = await axiosInstance.post('/stop_recognition')
    console.log(res);
    if (res.data) {
      setShowCamera(false);
      toast.success('Recognition stopped successfully')
    } else {
      toast.error('Recognition failed')
    }
  }

  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '20px', padding: '20px' }}>
      {showCamera && (
        <div style={{ border: '2px solid #ccc', borderRadius: '10px', overflow: 'hidden' }}>
          <Webcam
            ref={webcamRef}
            audio={false}
            screenshotFormat="image/jpeg"
            videoConstraints={videoConstraints}
          />
        </div>
      )}
      <div style={{ display: 'flex', gap: '10px' }}>
        <Button variant="contained" color="primary" onClick={handleStartRecognition}>
          Start Recognition
        </Button>
        <Button variant="contained" color="error" onClick={handleStopRecognition}>
          Stop Recognition
        </Button>
      </div>
    </div>
  )
}

export default Recognize