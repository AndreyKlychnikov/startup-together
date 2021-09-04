import Vue from "vue";
import Router from "vue-router";

import RouterComponent from "./components/RouterComponent.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      component: () =>
        import(/* webpackChunkName: "start" */ "./views/Start.vue"),

      children: [
        {
          path: "login",
          // route level code-splitting
          // this generates a separate chunk (about.[hash].js) for this route
          // which is lazy-loaded when the route is visited.
          component: () =>
            import(/* webpackChunkName: "login" */ "./views/Login.vue"),
        },
        {
          path: "recover-password",
          component: () =>
            import(
              /* webpackChunkName: "recover-password" */ "./views/PasswordRecovery.vue"
            ),
        },
        {
          path: "reset-password",
          component: () =>
            import(
              /* webpackChunkName: "reset-password" */ "./views/ResetPassword.vue"
            ),
        },
        {
          path: "",
          component: ()=> import("./views/main/Main.vue"),
          redirect: "/explore",
          children: [
            {
              path: "explore",
              component: () => import("./views/main/explore/Explore.vue"),
            },
            {
              path: "ideas",
              component: () => import("./views/main/Ideas.vue"),
            },
            {
              path: "project/:id",
              component: ()=> import("./views/main/projects/Project.vue")
            },
            {
              path: "projects",
              component: ()=> import("./views/main/projects/Projects.vue")
            },
          ]
        },

        {
          path: "adminPage",
          component: () =>
            import(/* webpackChunkName: "main" */ "./views/adminPage/Main.vue"),
          children: [
            {
              path: "dashboard",
              component: () =>
                import(
                  /* webpackChunkName: "main-dashboard" */ "./views/adminPage/Dashboard.vue"
                ),
            },
            {
              path: "profile",
              component: RouterComponent,
              redirect: "profile/view",
              children: [
                {
                  path: "view",
                  component: () =>
                    import(
                      /* webpackChunkName: "main-profile" */ "./views/adminPage/profile/UserProfile.vue"
                    ),
                },
                {
                  path: "edit",
                  component: () =>
                    import(
                      /* webpackChunkName: "main-profile-edit" */ "./views/adminPage/profile/UserProfileEdit.vue"
                    ),
                },
                {
                  path: "password",
                  component: () =>
                    import(
                      /* webpackChunkName: "main-profile-password" */ "./views/adminPage/profile/UserProfileEditPassword.vue"
                    ),
                },
              ],
            },

            {
              path: "users",
              redirect: "users/all",
            },
            {
              path: "users/all",
              component: () =>
                import(
                  /* webpackChunkName: "main-adminPage-users" */ "./views/adminPage/admin/AdminUsers.vue"
                ),
            },
            {
              path: "users/edit/:id",
              name: "main-admin-users-edit",
              component: () =>
                import(
                  /* webpackChunkName: "main-admin-users-edit" */ "./views/adminPage/admin/EditUser.vue"
                ),
            },
            {
              path: "users/create",
              name: "main-admin-users-create",
              component: () =>
                import(
                  /* webpackChunkName: "main-admin-users-create" */ "./views/adminPage/admin/CreateUser.vue"
                ),
            },
          ],
        },
      ],
    },
    {
      path: "/*",
      redirect: "/",
    },
  ],
});
