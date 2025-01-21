import { useState, useRef } from 'react';
import Webcam from 'react-webcam';
import { Box, Button, TextField, Card, Typography, Container, CircularProgress } from '@mui/material';
import { toast } from 'react-toastify';
import axiosInstance from '../helper/axiosInstance';

const PersonRegistration = () => {
  const [formData, setFormData] = useState({ name: '', usn: '' });
  const [isCameraActive, setIsCameraActive] = useState(true);
  const [capturedImage, setCapturedImage] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const webcamRef = useRef(null);

  const handleInputChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleCapture = () => {
    const imageSrc = webcamRef.current.getScreenshot();
    setCapturedImage(imageSrc);
    setIsCameraActive(false);
  };

  const handleRetake = () => {
    setCapturedImage(null);
    setIsCameraActive(true);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!capturedImage) {
      toast.error('Please capture an image first');
      return;
    }

    setIsLoading(true);
    try {
      const response = await axiosInstance.post('/add_person', {
        name: formData.name,
        usn: formData.usn,
        image: capturedImage
      });

      if (response.data) {
        toast.success('Person registered successfully!');
        setFormData({ name: '', usn: '' });
        setCapturedImage(null);
        setIsCameraActive(true);
      } else {
        toast.error(response.data.error || 'Registration failed');
      }
    } catch (error) {
      console.error('Registration error:', error);
      toast.error(error.response?.data?.error || 'Registration failed');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <Container maxWidth="sm">
      <Card sx={{ p: 4, mt: 4 }}>
        <Typography variant="h4" gutterBottom>
          Person Registration
        </Typography>

        <Box component="form" onSubmit={handleSubmit}>
          <TextField
            fullWidth
            label="Name"
            name="name"
            value={formData.name}
            onChange={handleInputChange}
            margin="normal"
            required
          />

          <TextField
            fullWidth
            label="USN"
            name="usn"
            value={formData.usn}
            onChange={handleInputChange}
            margin="normal"
            required
          />

          <Box sx={{ mt: 2, mb: 2 }}>
            {isCameraActive ? (
              <>
                <Webcam
                  ref={webcamRef}
                  audio={false}
                  screenshotFormat="image/jpeg"
                  style={{ width: '100%', height: 'auto' }}
                />
                <Button
                  onClick={handleCapture}
                  variant="contained"
                  fullWidth
                  sx={{ mt: 1 }}
                >
                  Capture Photo
                </Button>
              </>
            ) : (
              <>
                <img
                  src={capturedImage}
                  alt="captured"
                  style={{ width: '100%', height: 'auto' }}
                />
                <Button
                  onClick={handleRetake}
                  variant="contained"
                  fullWidth
                  sx={{ mt: 1 }}
                >
                  Retake Photo
                </Button>
              </>
            )}
          </Box>

          <Button
            type="submit"
            variant="contained"
            color="primary"
            fullWidth
            disabled={isLoading || !capturedImage}
            sx={{ mt: 2 }}
          >
            {isLoading ? <CircularProgress size={24} /> : 'Register Person'}
          </Button>
        </Box>
      </Card>
    </Container>
  );
};

export default PersonRegistration;