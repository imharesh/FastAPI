import { Box, Button, TextField, Typography } from '@mui/material';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { useState } from 'react';


const Signup = () => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const navigate = useNavigate();

  const handleSignup = async () => {
    if (password !== confirmPassword) {
      alert('Passwords do not match');
      return;
    }

    try {
      console.log('Attempting to signup with:', { username, email, password });
      const response = await axios.post('http://localhost:8000/signup', {
        username: username,
        email: email,
        password: password,
      });
      console.log('Signup response:', response.data);
      navigate('/');
    } catch (error) {
      console.error('Signup failed', error);
      alert('Signup failed: ' + (error.response?.data?.detail || error.message));
    }
  };

  return (
    <Box display="flex" flexDirection="column" alignItems="center" justifyContent="center" height="100vh">
      <Typography variant="h4" gutterBottom>Signup</Typography>
      <TextField label="Username" variant="outlined" margin="normal" value={username} onChange={(e) => setUsername(e.target.value)} />
      <TextField label="Email" variant="outlined" margin="normal" value={email} onChange={(e) => setEmail(e.target.value)} />
      <TextField label="Password" type="password" variant="outlined" margin="normal" value={password} onChange={(e) => setPassword(e.target.value)} />
      <TextField label="Confirm Password" type="password" variant="outlined" margin="normal" value={confirmPassword} onChange={(e) => setConfirmPassword(e.target.value)} />
      <Button variant="contained" color="primary" onClick={handleSignup}>Signup</Button>
    </Box>
  );
};

export default Signup;