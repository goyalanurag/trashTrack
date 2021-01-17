import React, { useState } from 'react';
import {Grid,Box,Paper} from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import VerticalBarGraph from '@chartiful/react-vertical-bar-graph'

 

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  paper: {
    margin: theme.spacing(2),
    padding: theme.spacing(2),
    backgroundColor: 'transparent',
    color: 'white'
  },
  
}));

export const Analytics = () => {
    const [data,setData] = useState();
    const classes=useStyles();
    return (<>
        <Grid>
            <Paper className={classes.paper}>
                <Box>
                    <h1>Analysis of Trash</h1>
                </Box>
                <Box>
                   <VerticalBarGraph
                        data={[1, 1, 2, 3, 3, 1, 1]}
                        labels={['Jan2021-01-15', '2021-01-16', '2021-01-17', '2021-01-18', '2021-01-19', '2021-01-20', '2021-01-21']}
                        width={1500}
                        height={600}
                        barRadius={5}
                        barWidthPercentage={0.65}
                        baseConfig={{
                            hasXAxisBackgroundLines: true,
                            xAxisLabelStyle: {
                            position: 'left',
                            // prefix: '$'
                            }
                        }}
                        style={{
                            paddingVertical: 10
                        }}
                        /> 
                </Box>
            </Paper>
        </Grid>
    </>);
}