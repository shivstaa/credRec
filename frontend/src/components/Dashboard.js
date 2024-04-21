import * as React from 'react';
import { styled, createTheme, ThemeProvider } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import Fab from '@mui/material/Fab';
import theme from './Theme.js';


const FabUnit = styled('div')({
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    position: 'absolute',
    zIndex: 1,
    bottom: -28,
    left: 0,
    right: 0,
    margin: '0 auto',
  });

const StyledFab = styled(Fab)({

  });  


export default function Dashboard() {
  return (
    <ThemeProvider theme={theme}>
      <Box sx={{ display: 'flex' }}>
        <CssBaseline />
        <AppBar position="absolute">
          <Toolbar>
            <Typography variant="h7" noWrap>
              Logo or Name Placeholder
            </Typography>            
            <Box sx={{ flexGrow: 1 }} />
            <Typography variant="h7" noWrap>
              Settings
            </Typography>
            <Box sx={{ flexGrow: 0.04 }} />
            <Typography variant="h7" noWrap>
              Logout
            </Typography>
          </Toolbar>
        </AppBar>
        <Paper
          elevation={3}
          sx={{
            width: 240,
            height: 'calc(100vh - 64px)',
            overflowY: 'auto',
            flexShrink: 0,
            position: 'fixed',
            left: 0,
            top: '64px',
          }}
        ></Paper>
        <Box
          component="main"
          sx={{
            backgroundColor: (theme) =>
              theme.palette.mode === "light"
                ? theme.palette.grey[100]
                : theme.palette.grey[900],
            flexGrow: 1,
            height: "100vh",
            overflow: "auto",
          }}
        >
          <Toolbar />
          <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
          <Grid container spacing={3}>
              <Grid item xs={12} md={12} lg={15}>
                <Paper
                  sx={{
                    p: 2,
                    display: "flex",
                    flexDirection: "column",
                    height: 240,
                  }}
                >
                    Chatlisthere
                </Paper>
              </Grid>
              <Grid item xs={12}>
                <input sx={{ p: 2, display: 'flex', flexDirection: 'column' }}
                    className="flex h-9 w-full rounded-lg border border-input px-3 py-1 text-sm shadow-sm transition-colors file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none"
                />
              </Grid>
                <Box
                    elevation={3}
                    sx={{
                    width: 240,
                    height: 'calc(100vh - 64px)',
                    overflowY: 'auto',
                    flexShrink: 0,
                    position: 'fixed',
                    right: 0,
                    top: '64px',
                }}
                ></Box>
            </Grid>
          </Container>
        </Box>
      </Box>
    </ThemeProvider>
  );
}
