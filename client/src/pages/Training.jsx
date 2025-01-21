import { useState, useEffect } from 'react';
import {
  Box,
  Card,
  CardContent,
  Typography,
  Button,
  LinearProgress,
  Grid,
  List,
  ListItem,
  ListItemText
} from '@mui/material';
import axios from 'axios';
import { toast } from 'react-toastify';

const Training = () => {
  const [trainingStatus, setTrainingStatus] = useState({
    isTraining: false,
    progress: 0,
    epoch: 0,
    totalEpochs: 100,
    metrics: null,
    error: null
  });

  const startTraining = async () => {
    try {
      await axios.post('http://localhost:8000/train_model');
      toast.success('Training started');
      fetchStatus();
    } catch (error) {
      toast.error('Failed to start training', error);
    }
  };

  const fetchStatus = async () => {
    try {
      const response = await axios.get('http://localhost:8000/training_status');
      setTrainingStatus(prev => ({
        ...prev,
        ...response.data
      }));

      if (response.data.error) {
        toast.error(`Training error: ${response.data.error}`);
      }
    } catch (error) {
      console.error('Failed to fetch status:', error);
    }
  };

  useEffect(() => {
    fetchStatus();
    const interval = setInterval(fetchStatus, 5000);
    return () => clearInterval(interval);
  }, []);

  return (
    <Box sx={{ p: 3 }}>
      <Typography variant="h4" gutterBottom>Model Training</Typography>

      <Grid container spacing={3}>
        {trainingStatus.error && (
          <Grid item xs={12}>
            <Card sx={{ bgcolor: 'error.light' }}>
              <CardContent>
                <Typography color="error">
                  Error: {trainingStatus.error}
                </Typography>
              </CardContent>
            </Card>
          </Grid>
        )}

        <Grid item xs={12} md={6}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>Training Progress</Typography>
              <LinearProgress
                variant="determinate"
                value={trainingStatus.progress}
                sx={{ my: 2 }}
              />
              <Typography>
                Epoch: {trainingStatus.epoch}/{trainingStatus.totalEpochs}
              </Typography>

              <Button
                variant="contained"
                onClick={startTraining}
                disabled={trainingStatus.isTraining}
                sx={{ mt: 2 }}
              >
                {trainingStatus.isTraining ? 'Training...' : 'Start Training'}
              </Button>
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12} md={6}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>Training Metrics</Typography>
              {trainingStatus.metrics && (
                <List>
                  <ListItem>
                    <ListItemText
                      primary="Loss"
                      secondary={trainingStatus.metrics.loss}
                    />
                  </ListItem>
                  <ListItem>
                    <ListItemText
                      primary="Accuracy"
                      secondary={trainingStatus.metrics.accuracy}
                    />
                  </ListItem>
                </List>
              )}
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </Box>
  );
};

export default Training;