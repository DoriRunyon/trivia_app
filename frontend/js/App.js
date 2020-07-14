import React from 'react';
import { hot } from 'react-hot-loader/root';

import Home from './pages/Home';
import SentryBoundary from './utils/SentryBoundary';

const App = () => (
    <Home />
);

export default hot(App);
