import { api } from '@/api';
import router from '@/router';
import { getLocalToken, removeLocalToken, saveLocalToken } from '@/utils';
import { AxiosError } from 'axios';
import { getStoreAccessors } from 'typesafe-vuex';
import { ActionContext } from 'vuex';
import { State } from '../state';
import {
    commitSetProjects,
} from './mutations';
import { ProjectState } from './state';

type MainContext = ActionContext<ProjectState, State>;

export const actions = {
    async actionGetProjects(context: MainContext) {
        try {
            const response = await api.getProjects(context.rootState.main.token);
            if (response.data) {
                commitSetProjects(context, response.data);
            }
        } catch(err){

        }
    },
};

const { dispatch } = getStoreAccessors<ProjectState | any, State>('');

export const dispatchGetProjects = dispatch(actions.actionGetProjects);