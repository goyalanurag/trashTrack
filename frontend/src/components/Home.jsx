import React, { useLayoutEffect } from 'react';
import {Grid,Box,Paper} from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import { useLoadScript } from '@react-google-maps/api';

const useStyles = makeStyles((theme) => ({
root: {
    margin: theme.spacing(2),
    marginTop: theme.spacing(8)
},
  paper: {
      padding: theme.spacing(2),
      backgroundColor: 'rgb(3, 32, 70)',
      color: 'white'
  },
}));

export const Home = () => {
    const classes=useStyles();
    return (<>
        <Grid className={classes.root}>
            <Paper className={classes.paper}>
                <Box>
                    <h1>Introduction</h1>
                    <hr/>
                    <h2>Trash-Track</h2>
                    <p style={{fontSize: '20px'}}>Geo Tracking of littered garbage, triggering alerts and mapping areas with high waste index.</p>
                </Box>
            </Paper>
            <Paper className={classes.paper}>
                <Box>
                    <h2>Working of the Model</h2>
                    <hr/>
                    <h3>Web application</h3>
                    <ul style={{fontSize: '20px'}}>
                        <li>Fetches district-specific data from database and projects the locations on a map.</li>
                        <li>Graphical analysis of time-based trend of garbage amount at specific locations.</li>
                    </ul>
                    <h3>Backend</h3>
                    <ul style={{fontSize: '20px'}}>
                        <li>Images are collected by cameras installed on public vehicles.</li>
                        <li>Machine learning model analyzes for the amount of garbage (low/medium/high).</li>
                        <li>Geolocation coordinates are maaped to a location cluster.</li>
                    </ul>
                </Box>
            </Paper>
        </Grid>
    </>);
}