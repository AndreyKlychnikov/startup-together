import { ProjectState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { State } from '../state';

export const getters = {
    projects: (state: ProjectState) => state.projects,
};

const {read} = getStoreAccessors<ProjectState, State>('');

export const readProjects = read(getters.projects);
