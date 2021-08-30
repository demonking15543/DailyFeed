import 'antd/dist/antd.css'; 

import CustomLayout from './components/Container';
import BaseRouter from './components/Routers';
import { BrowserRouter as Router } from 'react-router-dom';


function App() {
  return (
    <div>
      <Router>
      <CustomLayout>
        <BaseRouter />
      </CustomLayout>
      </Router>
      
   </div>
  );
}

export default App;
