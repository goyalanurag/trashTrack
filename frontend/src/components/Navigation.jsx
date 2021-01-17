import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Button from '@material-ui/core/Button';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  appDiv: {
    backgroundColor: 'black',
    borderBottom: '3px solid',
    boxShadow: '0 10px 20px rgba(0, 0, 0, 0.19), 0 6px 6px rgba(0, 0, 0, 0.23)'
  },
}));

export const Nav = () => {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <AppBar position="static" className={classes.appDiv}>
        <Toolbar>
          <Button color="inherit" className={classes.menuButton}><a href="/signin" style={{textDecoration:'none',color:'white'}}><i class="fas fa-sign-in-alt" style={{paddingRight: '5px'}}></i> Login</a></Button>
          <Button color="inherit" className={classes.menuButton}><a href="/" style={{textDecoration:'none',color:'white'}}><i class="fas fa-home" style={{paddingRight: '5px'}}></i> Home</a></Button>
          <Button color="inherit" className={classes.menuButton}><a href="/maps" style={{textDecoration:'none',color:'white'}}><i class="fas fa-map-marker-alt" style={{paddingRight: '5px'}}></i> Maps</a></Button>
          <Button color="inherit" className={classes.menuButton}><a href="/analytics" style={{textDecoration:'none',color:'white'}}><i class="fas fa-chart-line" style={{paddingRight: '5px'}}></i> Analytics</a></Button>
        </Toolbar>
      </AppBar>
    </div>
  );
}
