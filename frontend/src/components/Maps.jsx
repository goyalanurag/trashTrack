import React from 'react';
import {Grid,Box,Paper} from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import { GoogleMap, useJsApiLoader } from '@react-google-maps/api';


const containerStyle = {
  width: '100%',
  height: '400px'
};

const center = {
  lat: 27.2046,
  lng: 77.4977
};

export const Maps = () => {
  const { isLoaded } = useJsApiLoader({
    id: 'google-map-script',
    googleMapsApiKey: "AIzaSyAJG6ongGT9nxtHUSpg-CXrcV8UoRb4oD8"
  })

  const [map, setMap] = React.useState(null)

  const onLoad = React.useCallback(function callback(map) {
    const bounds = new window.google.maps.LatLngBounds();
    map.fitBounds(bounds);
    setMap(map)
  }, [])

  const onUnmount = React.useCallback(function callback(map) {
    setMap(null)
  }, [])

  return isLoaded ? (
      <GoogleMap
        mapContainerStyle={containerStyle}
        center={center}
        zoom={10}
        onLoad={onLoad}
        onUnmount={onUnmount}
      >
        { /* Child components, such as markers, info windows, etc. */ }
        <></>
      </GoogleMap>
  ) : <></>
}

// export default React.memo(Maps)