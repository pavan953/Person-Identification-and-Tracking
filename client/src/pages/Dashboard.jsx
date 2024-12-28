import { Grid, Card, CardContent, Typography } from '@mui/material';
import { useEffect, useState } from 'react';
import { toast } from 'react-toastify';
import axiosInstance from '../helper/axiosInstance';

const Dashboard = () => {
  const [persons, setPersons] = useState(0);
  useEffect(() => {
    fetchPersons();
  }, []);

  const fetchPersons = async () => {
    try {
      const response = await axiosInstance.get('/persons');
      setPersons(response.data.length);

    } catch (error) {
      toast.error('Failed to fetch persons', error);
    }
  };
  return (
    <Grid container spacing={3} sx={{ p: 3 }}>
      <Grid item xs={12} md={6} lg={3}>
        <Card>
          <CardContent>
            <Typography variant="h6">Total Persons</Typography>
            <Typography variant="h4">{persons}</Typography>
          </CardContent>
        </Card>
      </Grid>
      {/* Add more stats cards */}
    </Grid>
  );
};

export default Dashboard;