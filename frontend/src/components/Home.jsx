import React from 'react';
import {Grid,Box,Paper} from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles((theme) => ({
root: {
    margin: theme.spacing(2)
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
                    <p>"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."</p>
                </Box>
            </Paper>
        </Grid>
    </>);
}