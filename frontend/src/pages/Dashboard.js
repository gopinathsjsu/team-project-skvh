import React,{ useEffect, useState } from 'react'
import axios from 'axios'
import { useNavigate } from "react-router-dom"
import Layout from "../components/Layout"
import AboutUs from "../components/AboutUs"
import Plans from "../components/Plans"
import Classes from "../components/Classes"
import CheckInOut from "../components/CheckInOut"
import EnrollNewMember from "../components/EnrollNewMember"
import Analytics from "../components/Analytics"
import UpcomingClasses from "../components/UpcomingClasses"
import PastActivity from "../components/PastActivity"
import LogActivity from "../components/LogActivity"
import {Image,Heading} from "@chakra-ui/react";
import BottomNavBar from "../components/BottomNavigationBar";


function Dashboard() {
    const navigate = useNavigate();
    const [user, setUser] = useState({})
    const [locations, setLocations] = useState([])
    const [selectedLocation, setSelectedLocation] = useState(localStorage.getItem('selectedLocation') || "")
    const [plans, setPlans] = useState([])
    const [classes, setClasses] = useState([]);
    const [enrolledClasses, setEnrolledClasses] = useState([]);
    const [componentToDisplay, setComponentToDisplay] = useState('homepage');
    const [pastActivity, setPastActivity] = useState([]);


    useEffect(()=>{
        if(localStorage.getItem('token') !== ""){
            getUser();
        }   
            getLocations();
            getPlans();
            getClasses(selectedLocation);
            getEnrolledClasses();
            getPastActivity();
    },[]) // eslint-disable-line react-hooks/exhaustive-deps
 
    const getPastActivity = () => {
        axios.get('users/past_activity', { headers:{Authorization: 'Token ' + localStorage.getItem('token')}})
        .then((res) => {
            const data = res.data;
            if(res.data.success) {
                setPastActivity(data.data);
            }
        })
    };

    const getUser = () => {
        axios.get('users/details', { headers:{Authorization: 'Token ' + localStorage.getItem('token')}})
        .then((r) => {
            if (r.data.success) {
                setUser(r.data.data)
            }
        })
        .catch((e) => {
            console.log(e)
        });
    }
 
    const logoutAction = () => {
        console.log('localStorage');
        axios.post('users/logout',{}, { headers:{Authorization: 'Token ' + localStorage.getItem('token')}})
        .then((r) => {
            localStorage.removeItem('token');
            setUser({});
        })
        .catch((e) => {
            console.log(e)
        });
    }
     
    const getLocations = () => {
        axios.get('/locations/')
        .then((r) => {
            if (r.data.success) {
                setLocations(r.data.data)
            }
        })
        .catch((e) => {
            console.log(e)
        });
    }

    const enrolledClassesCallback = (revisedClasses) => {
        const updatedClasses = classes.map((cls) => {
          const matchingEnrolledClass = revisedClasses.find((enrolledCls) => enrolledCls.id === cls.id);
          if (matchingEnrolledClass) {
            return matchingEnrolledClass;
          } else {
            return cls;
          }
        });
        setClasses(updatedClasses);
        setEnrolledClasses(revisedClasses);
      };
      

    const getPlans = () => {
        axios.get('/plans/')
        .then((r) => {
            if (r.data.success) {
                setPlans(r.data.data)
            }
        })
        .catch((e) => {
            console.log(e)
        });
    }

    const getClasses = (locationId) => {
        if(locationId !== ""){
            axios.get(`/location/${locationId}/classes/`)
            .then((r) => {
                if (r.data.success) {
                    setClasses(r.data.data)
                }
            })
            .catch((e) => {
                console.log(e)
            }            
            );}
    }

    const getEnrolledClasses = () => {
        axios.get('/users/classes', { headers:{Authorization: 'Token ' + localStorage.getItem('token')}})
        .then((r) => {
            if (r.data.success) {
                setEnrolledClasses(r.data.data)
            }
        })
        .catch((e) => {
            console.log(e)
        });
    }

    const handleLocationChange = (e) => {
        const locationId = e.target.value;
        setSelectedLocation(locationId);
        localStorage.setItem('selectedLocation', locationId);
    }

    const handleSelectChange = (event) => {
        setComponentToDisplay(event.target.value);
    };

}