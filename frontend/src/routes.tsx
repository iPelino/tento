import React from 'react';
import { RouteObject } from 'react-router-dom';

// Define types for route objects
interface AppRouteObject extends RouteObject {
  title?: string;
  requiresAuth?: boolean;
  roles?: string[];
}

// Define routes
const routes: AppRouteObject[] = [
  {
    path: '/',
    title: 'Home',
    element: <div>Home Page</div>,
  },
  {
    path: '/dashboard',
    title: 'Dashboard',
    element: <div>Dashboard</div>,
    requiresAuth: true,
  },
  {
    path: '/properties',
    title: 'Properties',
    element: <div>Properties</div>,
  },
  {
    path: '/leases',
    title: 'Leases',
    element: <div>Leases</div>,
    requiresAuth: true,
  },
  {
    path: '/payments',
    title: 'Payments',
    element: <div>Payments</div>,
    requiresAuth: true,
  },
  {
    path: '/maintenance',
    title: 'Maintenance',
    element: <div>Maintenance</div>,
    requiresAuth: true,
  },
  {
    path: '/profile',
    title: 'Profile',
    element: <div>Profile</div>,
    requiresAuth: true,
  },
  {
    path: '/admin',
    title: 'Admin',
    element: <div>Admin</div>,
    requiresAuth: true,
    roles: ['admin'],
  },
  {
    path: '*',
    title: 'Not Found',
    element: <div>Page Not Found</div>,
  },
];

export default routes;
