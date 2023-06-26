import React, {useEffect, useState} from 'react';
import {
    Avatar,
    Box,
    Button,
    Container,
    OutlinedInput , FormHelperText,
    InputLabel, FormControl,
    Grid,
    Link, MenuItem,
    TextField,
    Typography
} from "@mui/material";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import Select from '@mui/material/Select';
import axios from "axios";
import {useNavigate} from 'react-router-dom';

import {getRoles} from './actions';

function Copyright(props) {
    return (
        <Typography variant="body2" color="text.secondary" align="center" {...props}>
            {'Copyright © '}
            <Link color="inherit" href="#">
                Isotopes Music
            </Link>{' '}
            {new Date().getFullYear()}
            {'.'}
        </Typography>
    );
}


const Register = (props) => {
    const [first_name, setFirstName] =useState('')
    const [last_name, setLastName] = useState('')
    const [email, setEmail] = useState('');
    const [roles, setRoles] = useState([]);
    const [role_id, setRoleID] = useState(props.id);
    const [password, setPassword] = useState('');
    const [confirm_password, setConfirmPassword] = useState('');
    const [redirect, setRedirect] = useState(false);
    const [loading,setLoading] = useState(false);

    let navigator = useNavigate();

    useEffect(() =>{
        // fetch post
        const fetchData = async () =>{
            setLoading(true);
            let response = await getRoles();
            if(response) {
                setRoles(response.data);
                setLoading(false)
            }
        }
        fetchData()},[])

    const handleSubmit = async (e) => {
        e.preventDefault();

        await axios.post('register', {
            first_name,
            last_name,
            role_id,
            email,
            password,
            confirm_password
        });
        // setIsLoading(true);
        setRedirect(true);
        // setIsLoading(false)
    };

    const handleChange = (event) => {
        setRoleID(event.target.value);
    };

    if (redirect) {
        navigator('/login');
    }

    return (
        <Container component="main" maxWidth="xs">
            <Box
                sx={{
                    marginTop: 8,
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                }}
            >
                <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
                    <LockOutlinedIcon />
                </Avatar>
                <Typography component="h1" variant="h5">
                    Sign up
                </Typography>
                <Box component="form" noValidate onSubmit={handleSubmit} sx={{ mt: 3 }}>
                    <Grid container spacing={2}>
                        <Grid item xs={12} sm={6}>
                            <TextField
                                autoComplete="given-name"
                                name="firstName"
                                required
                                fullWidth
                                id="first_mame"
                                label="First Name"
                                autoFocus
                                onChange={e => setFirstName(e.target.value)}
                            />
                        </Grid>
                        <Grid item xs={12} sm={6}>
                            <TextField
                                required
                                fullWidth
                                id="lastName"
                                label="Last Name"
                                name="last_name"
                                autoComplete="family-name"
                                onChange={e => setLastName(e.target.value)}
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <TextField
                                required
                                fullWidth
                                id="email"
                                label="Email Address"
                                name="email"
                                autoComplete="email"
                                onChange={e => setEmail(e.target.value)}
                            />
                        </Grid>
                        <Grid item xs={12} >
                            <FormControl fullWidth>
                                <InputLabel id="demo-multiple-name-label">Isotope Type</InputLabel>
                                    <Select
                                        onChange={handleChange}
                                    >
                                        <MenuItem disabled value="">
                                            <em>Isotope type</em>
                                        </MenuItem>
                                        {(roles).map((role) => (
                                            <MenuItem
                                                key={role.id}
                                                value={role.id}
                                            >
                                                {role.name}
                                            </MenuItem>
                                        ))}
                                    </Select>
                                    <FormHelperText>Select Isotope Type</FormHelperText>
                            </FormControl>
                        </Grid>
                        <Grid item xs={12}>
                            <TextField
                                required
                                fullWidth
                                name="password"
                                label="Password"
                                type="password"
                                id="password"
                                autoComplete="new-password"
                                onChange={e => setPassword(e.target.value)}
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <TextField
                                required
                                fullWidth
                                name="password"
                                label="Confirm Password"
                                type="password"
                                id="confirm_password"
                                autoComplete="new-password"
                                onChange={e => setConfirmPassword(e.target.value)}
                            />
                        </Grid>
                    </Grid>
                    <Button
                        type="submit"
                        fullWidth
                        variant="contained"
                        sx={{ mt: 3, mb: 2 }}
                    >
                        Sign Up
                    </Button>
                    <Grid container justifyContent="flex-end">
                        <Grid item>
                            <Link href="/login" variant="body2">
                                Already have an account? Sign in
                            </Link>
                        </Grid>
                    </Grid>
                </Box>
            </Box>
            <Copyright sx={{ mt: 5 }} />
        </Container>
    );
};

export default Register;