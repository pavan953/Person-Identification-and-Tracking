import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { ToastContainer } from 'react-toastify';
import Navbar from './components/Navbar';
import Dashboard from './pages/Dashboard';
import PersonRegistration from './pages/PersonRegistraction';
import PersonTracking from './pages/PersonTracking';
import PersonList from './pages/PersonList';
import TrainingStatus from './pages/TrainingStatus';
import Training from './pages/Training';
import 'react-toastify/dist/ReactToastify.css';

function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/register" element={<PersonRegistration />} />
        <Route path="/track" element={<PersonTracking />} />
        <Route path="/persons" element={<PersonList />} />
        {/* <Route path="/training-status" element={<TrainingStatus />} />
        <Route path="/training" element={<Training />} /> */}
        <Route path='/recognize' element={<Recognize />} />
      </Routes>
      <ToastContainer position="bottom-right" />
    </BrowserRouter>
  );
}

export default App;