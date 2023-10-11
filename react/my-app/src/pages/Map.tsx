import React, { useEffect, useRef, useState } from 'react';
import mapboxgl from 'mapbox-gl';

// const API_KEY = 'd41d8cd98f00b204e9800998ecf8427e';
const MAPBOX_API_Token = 'pk.eyJ1IjoibW9yaXNha2ktbWFwIiwiYSI6ImNsbThqMnduazBhM20zaXM1ZmJzY2toeWQifQ.ZJ3jdmwfPm09pwXiVdmxJw';


export const Map: React.FC = () => {
    const mapContainerRef = useRef<HTMLDivElement | null>(null);
    const [map, setMap] = useState<mapboxgl.Map | null>(null);
  
    useEffect(() => {
      mapboxgl.accessToken = MAPBOX_API_Token;
  
      const initializeMap = () => {
        if (mapContainerRef.current) {
          const newMap = new mapboxgl.Map({
            container: mapContainerRef.current,
            style: 'mapbox://styles/mapbox/streets-v11',
            center: [139.6917,35.6895],
            zoom: 10,
          });
  
          newMap.on('load', () => {
          });

          setMap(newMap); 
        }
      };
  
      initializeMap();
  
      return () => {
        if (map) {
          map.remove();
        }
      };
    }, []);
  
    return (
      <div ref={mapContainerRef} style={{ width: '100%', height: '600px' }} />
    );
  };
