import { useState, useEffect } from 'react';
import {
  Box,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  CircularProgress,
  Button,
  Typography,
  Chip
} from '@mui/material';
import axios from 'axios';
import { toast } from 'react-toastify';

const TrainingStatus = () => {
  const [persons, setPersons] = useState([]);
  const [loading, setLoading] = useState(true);

  const fetchStatus = async () => {
    try {
      const response = await axios.get('http://localhost:8000/training-status');
      setPersons(response.data);
      setLoading(false);
    } catch (error) {
      toast.error('Failed to fetch training status', error);
      setLoading(false);
    }
  };

  const retryTraining = async (usn) => {
    try {
      await axios.post(`http://localhost:8000/retrain/${usn}`);
      toast.success('Training restarted');
      fetchStatus();
    } catch (error) {
      toast.error('Failed to restart training', error);
    }
  };

  useEffect(() => {
    fetchStatus();
    const interval = setInterval(fetchStatus, 5000); // Poll every 5 seconds
    return () => clearInterval(interval);
  }, []);

  if (loading) {
    return (
      <Box sx={{ display: 'flex', justifyContent: 'center', p: 3 }}>
        <CircularProgress />
      </Box>
    );
  }

  return (
    <Box sx={{ p: 3 }}>
      <Typography variant="h4" gutterBottom>
        Training Status
      </Typography>

      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Name</TableCell>
              <TableCell>USN</TableCell>
              <TableCell>Status</TableCell>
              <TableCell>Progress</TableCell>
              <TableCell>Actions</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {persons.map((person) => (
              <TableRow key={person.usn}>
                <TableCell>{person.name}</TableCell>
                <TableCell>{person.usn}</TableCell>
                <TableCell>
                  <Chip
                    label={person.trained ? 'Trained' : 'Training'}
                    color={person.trained ? 'success' : 'warning'}
                  />
                </TableCell>
                <TableCell>
                  {!person.trained && (
                    <CircularProgress
                      size={20}
                      variant="determinate"
                      value={person.progress || 0}
                    />
                  )}
                </TableCell>
                <TableCell>
                  {!person.trained && (
                    <Button
                      variant="outlined"
                      size="small"
                      onClick={() => retryTraining(person.usn)}
                    >
                      Retry
                    </Button>
                  )}
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Box>
  );
};

export default TrainingStatus;