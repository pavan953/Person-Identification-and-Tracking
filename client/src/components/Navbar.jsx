import { AppBar, Toolbar, Button, Box } from '@mui/material';
import { useNavigate } from 'react-router-dom';

const Navbar = () => {
  const navigate = useNavigate();

  return (
    <AppBar position="static">
      <Toolbar>
        <Box sx={{ flexGrow: 1, display: 'flex', gap: 2 }}>
          <Button color="inherit" onClick={() => navigate('/')}>
            Dashboard
          </Button>
          <Button color="inherit" onClick={() => navigate('/register')}>
            Register
          </Button>
          <Button color="inherit" onClick={() => navigate('/track')}>
            Track
          </Button>
          <Button color="inherit" onClick={() => navigate('/persons')}>
            Persons
          </Button>
          {/* <Button color="inherit" onClick={() => navigate('/training-status')}>
            Training
          </Button>
          <Button color="inherit" onClick={() => navigate('/train-model')}>
            Train
          </Button> */}
          <Button color="inherit" onClick={() => navigate('/recognize')}>
            Recognize
          </Button>
        </Box>
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;