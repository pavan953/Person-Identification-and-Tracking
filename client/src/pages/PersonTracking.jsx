import { useState } from 'react';
import { Box, TextField, Button, Typography } from '@mui/material';
import { toast } from 'react-toastify';
import axiosInstance from '../helper/axiosInstance';

const PersonTracking = () => {
  const [usn, setUsn] = useState('');

  const handleTrack = async () => {
    try {
      const response = await axiosInstance.post('/track_person', { usn: usn });
      console.log(response);

      toast.success('Tracking started');
    } catch (error) {
      toast.error(error.response?.data?.error || 'Tracking failed');
    }
  };

  const handleStopTracking = async () => {
    try {
      const res = await axiosInstance.post('/stop_recognition')
      toast.success("Tracking Stopped")
    } catch (error) {
      toast.error(error.response?.data.error || "Failed to stop tracking")
    }
  }

  return (
    <div className="h-screen flex items-center justify-center">
      <Box sx={{ p: 3 }}>
        <Typography variant="h4" gutterBottom>
          Track Person
        </Typography>
        <TextField
          fullWidth
          label="USN"
          value={usn}
          onChange={(e) => setUsn(e.target.value)}
          sx={{ mb: 2 }}
        />
        <div className="flex gap-y-4">
          <Button variant="contained" onClick={handleTrack}>
            Start Tracking
          </Button>
          <Button variant='contained' onClick={handleStopTracking}>
            Stop Tracking
          </Button>
        </div>
      </Box>
    </div>
  );
};

export default PersonTracking;