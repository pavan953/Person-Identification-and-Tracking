import { useEffect, useState } from 'react';
import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
} from '@mui/material';
import { toast } from 'react-toastify';
import axiosInstance from '../helper/axiosInstance';

const PersonList = () => {
  const [persons, setPersons] = useState([]);
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
            <TableCell>Name</TableCell>
            <TableCell>USN</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {persons.map((person) => (
            <TableRow key={person.id}>
              <TableCell>{person.name}</TableCell>
              <TableCell>{person.usn}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default PersonList;