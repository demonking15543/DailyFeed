
import React, { Component } from 'react';
import axios from 'axios';
import Articles from './Article';


export default class ArticleListView extends Component {
  state = {
    articles:[]
  }
  componentDidMount(){
    axios
    .get('http://127.0.0.1:8000/api/')
    .then(res=>{
      this.setState({
        articles:res.data
      });
    })
  }



    render() {
        return (
            <div>
                <Articles data={this.state.articles} />
            </div>
        )
    }
}
