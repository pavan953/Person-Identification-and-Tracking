import { useEffect, useState } from 'react';
import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  Button,
  Box
} from '@mui/material';
import { toast } from 'react-toastify';
import { useNavigate } from 'react-router-dom';
import axiosInstance from '../helper/axiosInstance';

const PersonList = () => {
  const [persons, setPersons] = useState([]);
  const navigate = useNavigate();
  useEffect(() => {
    fetchPersons();
  }, []);

  const fetchPersons = async () => {
    try {
      const response = await axiosInstance.get('/persons');
      console.log(response);

      setPersons(response.data);
    } catch (error) {
      toast.error('Failed to fetch persons', error);
    }
  };

  return (
    <TableContainer component={Paper} sx={{ m: 3 }}>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>Image</TableCell>
            <TableCell>Name</TableCell>
            <TableCell>USN</TableCell>
            <TableCell>Status</TableCell>
            <TableCell>Actions</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {persons.map((person) => (
            <TableRow key={person.id}>
              <TableCell>
                <Box sx={{ width: 100, height: 100 }}>
                  <img
                    src={`../../../${person.image}`}
                    alt={person.name}
                    style={{ width: '100%', height: '100%', objectFit: 'cover' }}
                  />
                </Box>
              </TableCell>
              <TableCell>{person.name}</TableCell>
              <TableCell>{person.usn}</TableCell>
              <TableCell>
                {person.trained ? 'Trained' : 'Training...'}
              </TableCell>
              <TableCell>
                <Button
                  variant="contained"
                  onClick={() => navigate(`/track?usn=${person.usn}`)}
                >
                  Track
                </Button>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default PersonList;