import React  from 'react';

import { Route } from 'react-router-dom';

import ArticleListView from './ArticleListView';
import ArticleDetailView from './ArticleDetailView';

const BaseRouter = () => (
    <div>
        <Route exact path='/' component={ArticleListView} />
        <Route exact path='/:articleID' component={ArticleDetailView} />

    </div>

);
export  default BaseRouter;