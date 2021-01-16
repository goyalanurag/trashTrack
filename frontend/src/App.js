
import './App.css';
import {BrowserRouter,Switch, Route} from 'react-router-dom';
import {Nav} from './components/Navigation';
import {Sign} from './components/SignIn';
import {Home} from './components/Home';
import {Maps} from './components/Maps';

function App() {
  return (<>
    <Nav/>
    <BrowserRouter>
      <Switch>
        <Route exact path="/signin" component={Sign}/>
        <Route exact path="/" component={Home}/>
        <Route exact path="/maps" component={Maps}/>
      </Switch>
    </BrowserRouter>
  </>  );
}

export default App;
