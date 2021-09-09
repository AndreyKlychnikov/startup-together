import { IProject } from '@/interfaces';
import { ProjectState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { State } from '../state';


export const mutations = {
    setProjects(state: ProjectState, payload: IProject) {
        state.projects = payload;
    },
};

const {commit} = getStoreAccessors<ProjectState | any, State>('');

export const commitSetProjects = commit(mutations.setProjects);

