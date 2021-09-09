import { mutations } from './mutations';
import { getters } from './getters';
import { actions } from './actions';
import { ProjectState } from './state';

const defaultState: ProjectState = {
    projects: null
};

export const exploreModule = {
  state: defaultState,
  mutations,
  actions,
  getters,
};
