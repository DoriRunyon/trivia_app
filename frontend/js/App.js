import React from 'react';
import { hot } from 'react-hot-loader/root';

import Home from './pages/Home';
import SentryBoundary from './utils/SentryBoundary';
import { CookiesProvider } from 'react-cookie';

const App = () => (
  <CookiesProvider>
    <Home />
  </CookiesProvider>
);

export default hot(App);
